---
title: Running containers the macOS way
subtitle:
layout: main
section: containers
sections: []
tags:
  - macos
  - containeres
lang: pt
copy: 2025
date: 2025-06-14
abstract:
  On 2025-06-10, Apple has unveiled the first public version of
  [container](https://github.com/apple/container) and
  [containerization](https://github.com/apple/containerization), a set
  of tools that allow applications to use Linux containers on macOS,
  based on Apple's lightweight virtual machine framework. The goal here
  is to grasp the basics f these tools and evaluate how they compare to
  [podman](https://podman.io) and [docker](https://docker.io)
---

Containers are lightweight, fully function and portable environments
for OS or application level virtualization. It has been widely adopted
on cloud computing environments, and have become an ubiquitous way of
deploying software.

On the Linux World, the most used tools to manage containers are
[podman](https://podman.io) and [docker](https://docker.io), at least
at the time of this writing. And both use nearly the same interfaces,
as _podman_ was built as a drop-in replacement for _docker_, without the
need to run daemons with superuser privileges. Also, on the Linux World,
the Linux Kernel provides a subsystem that provides the means to run the
containers, which are itself, Linux environments.

Under macOS (and Windows), it is not expected that containers run without
some additional work, as the operating system kernel does not provide the
same tooling to run Linux containers, so, a virtual machine, running a
Linux kernel, is used to actually execute the containers. This virtual
machine environment is somewhat transparent for the user managing
containers, and it is mostly visible when something goes wrong, or some
more invoved configuration is required.

Apple's macOS, for some time now, has a framework that allows the
management of lightweight virtual machines capable of running macOS and
Linux operating systems, since macOS 11.0, and based on this framework
it has released [container](https://github.com/apple/container) and
[containerization](https://github.com/apple/containerization), a set
of tools to manage OCI containers and use them in macOS applications.

The **container** tool is similar to _podman_ and _docker_ and it is
capable of building and running Linux containers. The **containerization**
package allows applications to use Linux containers. Here, I'll focus on
the **container** tool, and its similarities and differences to _podman_.
The final goal is to try to run [FreeIPA](https://freeipa.org) using
**container**, in a way that it would enable the execution of the FreeIPA
Workshop.

> **Huge spoiler**: I could not run FreeIPA using **container**. It might be
possible, but I'd need a lot of free time to dig into the used frameworks.

## Using **container**

There are detailed instructions and tutorials on the **container**
repository, so we'll take some shortcuts here, and you are advised to
read the official documentation to get detailed information.

The first thing to understand is that, as with _podman_, **container**
runs the Linux container inside a Linux Virtual Machine. This is needed
as a Linux kernel is required. The difference here is that _podman_ runs
a _heavy weight virtual machine_ (my wording) with `qemu` and run all of
the containers under that virtual machine. The approach for **container**
is slightly different, it uses a lightweight virtual machine for each
container.

The first thing to do is to install and run the container subsystem with:

```
$ container subsystem start
```

If it is the first time you are running **container**, accept the
suggested kernel option and wait for the command to finish. After it is
executed, the container subsystem is ready to run.

Test that containers can be executed with:

```
$ container run quay.io/podman/hello
```

This will download and execute _podman_'s Hello World container, using
a _aarch64/arm64_ image.

![vhs: running container](/images/vhs/apple_container.gif){:style="max-width:90%;margin: 0 auto"}

Apple's **container** is only available for Apple Silicon machines
(ARM 64-bits), and it does support _x86_64_ containers through Rosetta 2,
but remember that Rosetta 2 is scheduled to be phased of, so start
planning on always use _arm64/aarch64_ containers.

## Limitations on **container**

Apple's **container** is in its early stages of development
(version 0.1.0) and currently poses many limitations on container
configuration. One must also remember that it is not meant to be
a _podman_ or _docker_ replacement (at least not currently).

One of the first things I missed was the flexibility to define a
virtual network to run multiple containers, defining the hostnames and
IP addresses. There is a DNS domain option, but it is not as powerful
and the network definition on _podman_, or even on a compose file.

Speaking of composes, there is still no _docker compose_ equivalent,
or any other orchestration tool.

## Wrap up

For a first release, **container** is a very interesting tool, that
is full of possibilities, but still very far from its much more mature
contenders.

It make it easy to build and run Linux containers in a (almost) native
way on macOS, and one can imagine we might have some macOS containers
in the future (as the Virtualization subsystem can run macOS VMs).

For now, I'll keep an eye on it, and maybe contribute to the project,
but I'll stick with _podman_ for now, as it is not as fast, but is
much more flexible and allows container orchestration.
