---
title: Using podman on macOS
subtitle:
layout: main
section: macOS
sections: []
tags:
  - container
  - podman
  - macOS
  - development
lang: en
copy: 2025
date: 2025-02-15
abstract: |
    Containers are a nice way to deploy small services or to experiment
    with some software configuration in a lightweight environment.
    Currently I run my nameservers and local registry using containers,
    but my main use in to create ephemeral environments to run software
    that I want to test, learn, or don't want to install on my host
    machines. Containers are, usually, Linux devices, and run under Linux
    hosts, and in this article I'll show how to use them on a macOS host
    (similar instructions can be used under Windows hosts).
---

I write these pages in using Markdown, and host it on Github pages, I do so because Mrakdown is much easier to deal (content-wise) than HTML, and I can simple use these files with Github pages as it will translate these pages to HTML using Jekyll. The problem with this approach is that I need to run Jekyll on my host, if I want to make any change on the design of the pages, and for that I run the required environment using containers, both on Linux and macOS, which are the systems I user regularly (see [Creating static sites with Jekyll and Podman (PT_BR)](/tools/jekyll-podman)).

As containers are, oversimplifying, a Linux guest running on a Linux host, to use them under other operating systems requires some tooling, and both [Docker](https://docker.io){:target="\_blank"} and [Podman]{:target="\_blank"} provide the means so that we can run containers on either macOS or Windows. As I only use Windows if I have to (by choice, as it does not solve well the kind of OS problems I have), this article is about running containers on macOS, which is not my main operating system (currently), but is one I use very often. And due to many advantages I see in `podman` since its inception (specially the least required privilege approach), I'll use it as the container manager.

## Before you start

Before you start, you have to install `podman` to your machine. You should follow the instructions on https://podman.io/docs/installation.

You may find that [Podman Desktop](https://podman-desktop.io){:target="\_blank"} provides an interface that better suits your workflow, but I'd not suggest trying it before version 1.16.2, or using the [Homebrew](https://brew.sh){:target="\_blank"} version of `podman desktop`, as it struggled to setup the `podman machine` on several macOS versions.

I used to use only the `Homebrew` version of `podman`, and only lately (as of version 5.4.0) I started to use the official builds on macOS.

## Starting your first container

So, I'll assume that you installed the standard `podman` distribution (or the Homebrew one), and not the Podman Desktop bundle.

If you try to run Podman's _Hello World_, you'll try:

```nohl
$ podman run --rm hello
```

And instead of a nice ASCII-art drawing, all you have is an error message:

```nohl
Cannot connect to Podman. Please verify your connection to the Linux system using `podman system connection list`, or try `podman machine init` and `podman machine start` to manage a new Linux VM
Error: unable to connect to Podman socket: failed to connect: dial tcp 127.0.0.1:51509: connect: connection refused
```

Remember that we simplified a container to be `Linux-on-Linux`, but we just tried to run `Linux-on-Mac`, which does not unify (remember _Prolog_?).

To be able to run Linux containers on other operating systems than Linux `podman` (and `docker`) use the concept of a _podman machine_ that in connects to and actually run the containers on that machine and not on the actual host. The _podman machine_ is a Linux virtual machine that in managed by `podman` and is actually used to run the containers. The virtualization process is almost transparent, but does exist, and as will be seen later, impose some restrictions on the containers use.

So, to be able to run containers, we'll create a new podman machine. The machine can be created with the `podman machine init` command:

```nohl
$ podman machine init
````

This will create the `podman-default-machine`, with a default configuration. Let's inspect the characteristics of the machine:

{% raw %}
```nohl
$ podman machine inspect
[
     {
          "ConfigDir": {
               "Path": "/Users/rafael/.config/containers/podman/machine/applehv"
          },
          "ConnectionInfo": {
               "PodmanSocket": {
                    "Path": "/var/folders/y0/3tjjfj7n3sqfx2qy2bvvmwp80000gp/T/podman/podman-machine-default-api.sock"
               },
               "PodmanPipe": null
          },
          "Created": "2025-02-15T16:27:18.563644-03:00",
          "LastUp": "0001-01-01T00:00:00Z",
          "Name": "podman-machine-default",
          "Resources": {
               "CPUs": 4,
               "DiskSize": 100,
               "Memory": 2048,
               "USBs": []
          },
          "SSHConfig": {
               "IdentityPath": "/Users/rafael/.local/share/containers/podman/machine/machine",
               "Port": 52612,
               "RemoteUsername": "core"
          },
          "State": "stopped",
          "UserModeNetworking": true,
          "Rootful": false,
          "Rosetta": true
     }
]
```
{% endraw %}

Lot's of information that is not needed right now, so let's focus on what matters for this moment:

* `Name: podman-machine-default`: this is the machine name, and the default name. You can have more than one machine, if you use different names.
* `State: stopped`: this shows the state of the machine, and is currently not running.
* `Resources: DiskSize: 100`: this shows that the machine can use upon 100 GiB of disk space to store data, be it container data, container application data, or any other file that the machine needs to operate. For many applications, this is more than enough.
* `Resources: Memory: 2048`: this shows that the machine uses 2048 MiB of memory (2 GiB). This memory is shared between machine operation and all running containers. Unless you are using applications that have very little memory footprint, this will not be enough.

As most of the things I use containers require more than 2 GiB of run (for example, [FreeIPA test clusters](projects/ipalab-config/en/ipa-ad-testing)), and most of the fun stuff requires some good amount of memory, let's recreate the machine with a better configuration:

```nohl
$ podman machine rm podman-machine-default
(... remember to confirm machine removal ...)
$ podman machine init --memory 6144
```

Now that we have a machine with a better configuration, simply start the machine:

```nohl
$ podman machine start
```

This will start the machine in "rootless mode" and will only run rootless containers. You can change the behavior with the `podman machine set --rootful` command.

Now we can finally run our container:

```
$ podman run --rm hello
!... Hello Podman World ...!

         .--"--.
       / -     - \
      / (O)   (O) \
   ~~~| -=(,Y,)=- |
    .---. /`  \   |~~
 ~/  o  o \~~~~.----. ~~
  | =(X)= |~  / (O (O) \
   ~~~~~~~  ~| =(Y_)=-  |
  ~~~~    ~~~|   U      |~~
```

And we finally have our nice ASCII-art!


## Having fun with containers

Now let's try a more useful container:

```nohl
$ podman run -it --rm fedora:latest bash
```

This will start a container with the latest official container image of Fedora, and start a Bash shell on it. Let's get some information on the running environment:

```nohl
[container]# uname -sm
Linux aarch64
```

And we're running an ARM64 container!

In my case this is due to the machine being a M2 Mac (with 24 GB of RAM):

```
$ sysctl -n machdep.cpu.brand_string
Apple M2
$ uname -sm
Darwin arm64
$ bc <<< "$(sysctl -a | grep hw.memsize: | cut -d: -f2) /(2^30)"
24
```

Let's inspect some data on the _podman machine_:

```
$ podman machine ssh
[podman_vm]$ uname -sm
Linux aarch64
[podman_vm]$ head -n 4 /etc/os-release
NAME="Fedora Linux"
VERSION="41.20250117.3.0 (CoreOS)"
RELEASE_TYPE=stable
ID=fedora
```

The _podman machine_ is running a version of Fedora CoreOS, for aarch64, as it is running on an ARM64 machine, the Apple M2 processor, and, although there are many layers on this setup to run a "lightweight container", as we are not running Linux, it does not get much better than this.

## Wrap Up

Running containers on non-Linux operating systems have improved a lot in recent years. Even the sometimes considered "exotic" Apple Silicon is able to run the containers in a nearly transparent way, but you still have to realize that there is a virtual machine involved and with that some limitations.

On Apple hardware, using AppleHV to manage virtualization, there's a [long standing issue](https://github.com/containers/podman/issues/22343) that makes a lot of sense when you take into account that mounting a volume in the container means that you are sharing the host directory with the VM and then mounting the volume in the container.

I find that developing with containers on macOS is, currently, not only possible, but with much less issues than it used to be a few years ago. It is even possible now to run some [non-trivial environments](/projects/ipalab-config/en/ipa-ad-testing) in a somewhat easy way.

Maybe my next working machine could be a Mac? I don't know, but I know I would put as much memory on it I could buy. (Note: Don't ever buy the lowest RAM Apple machine, they are simply not worth it). Even if macOS seems to deal fine with memory and memory swap, you'll don't want to have you storage being used as memory, and I wouldn't recommend less than 24Gb as of 2025.
