---
title: Running AI prompts on macOS with Ramalama
subtitle:
layout: main
section: Artificial Intelligence
sections:
  - Artificial Intelligence
tags:
  - containers
  - macos
  - artificial intelligence
  - llm
lang: en
copy: 2025
date: 2025-07-03
abstract: |-
    [RamaLama](https://ramalama.ai) is an open-source tool that
    simplifies the usage of artificial intelligence models for
    inference by using the same approach used for containers, and
    simplifies machine setup by running the prompt server or CLI
    inside a container. It detects hardware support for optimizing
    inference execution and handles dependencies and configuration.
    As it uses Linux containers, it's usage under macOS requires
    some tuning to get the best performance of the available hardware,
    specially if running under Apple Silicon. Here I show the
    required configuration to take advantage of the M-series GPU
    when running a prompt with Ramalama.
---

[RamaLama](https://ramalama.ai) simplifies a lot the system setup for
running LLM models by abstracting the management of libraries and
dependencies. It even allows you to take advantage of hardware acceleration
for running the models, even on macOS systems running on Apple Silicon
(M-series).

As RamaLama uses Linux containers, it requires a Linux kernel, what is
provided, under macOS (and Microsoft Windows) by a _"hidden"_ virtual machine.
This same workaround is used by [Podman](https://podman.io) and
[Docker](https://docker.io), and is done in a quasi-transparent way,
as one still have to create and start the virtual machine that will
run the actual containers.

With `podman` you can use:

```nohl
$ podman machine init
$ podman machine start
```

If you execute these commands, you'll have a Linux virtual machine
running, configured with 4 CPUs, 100GiB of storage and 2GiB (2048MiB) of
memory. The configuration can check the machine data with:

>
```nohl
$ podman machine list
NAME                     VM TYPE     CREATED         LAST UP            CPUS        MEMORY      DISK SIZE
podman-machine-default*  applehv     24 minutes ago  18 minutes ago     4           2GiB        100GiB
```

Test your podman configuration:

```nohl
$ podman run --rm quay.io/podman/hello
```

Now you can use [Homebrew](https://brew.sh) to install RamaLama:

```
# brew install ramalama
```

Trying to run RamaLama with this machine will give you a warning,
and ask if you want to continue:

```
$ ramalama list
Warning! Your VM podman-machine-default is
using applehv, which does not support GPU.
Only the provider libkrun has GPU support.
See `man ramalama-macos` for more information.
Do you want to proceed without GPU? (yes/no):
```

You can check the the virtual machine does not have direct access
to the GPU with

```
$ podman machine ssh
(...)

core@localhost:~$ ls /dev/dri
ls: cannot access '/dev/dri': No such file or directory
```

## Setting up the podman machine

To setup a podman machine that can take advantage of the M-series GPU,
you'll need to create a custom machine, that will use
[libkrun](https://github.com/containers/libkrun) instead of `applehv`.

Before the machine can be created, `krunkit` needs to be available on
the host, and I suggest you install it through [Homebrew](https://brew.sh)

```
$ brew tap slp/krunkit
$ brew install krunkit
```

Now create a new podman machine, using the `libkrun` provider:

```
$ export CONTAINERS_MACHINE_PROVIDER="libkrun"
$ podman machine init
$ podman machine start
```

Note that you have to `export` the `CONTAINERS_MACHINE_PROVIDER` variable,
as any other podman command will require it to select the proper machine.
(Otherwise, it will try to use the default value, which is `applehv`, and
will try to access the `podman-machine-default`).

Check the machine type:

>
```nohl
$ podman machine list
NAME        VM TYPE     CREATED         LAST UP            CPUS        MEMORY      DISK SIZE
ramalama    libkrun     22 minutes ago  Currently running  4           2GiB        100GiB
```

And check direct access to the GPU:

```nohl
$ podman machine ssh ramalama ls /dev/dri
by-path
card0
renderD128
```

Now we can take advantage of the Apple Silicon GPU when running RamaLama.

## Running ramalama

With the environment properly configured, retrieve one of the available
models. You can see a list of available models (accessible through their
short names) with:

```nohl
$ ramalama info
```

The first time you run ramalama with a model, it will download a container
image, and it can take a while, but no visual feedback is provided, so,
for the downloading the first model, I suggest using the `--debug` option:

```nohl
$ ramalama --debug pull gemma3
```

After downloading the model, you can start it and run a CLI prompt with:

```nohl
$ ramalama run gemma3
```

Or you can start it as a server that can be accessed through any browser:

```nohl
$ ramalama run gemma3
```

With this configuration, any RamaLama tool can be used, such as the
nice way it provides to
[improve model response with RAG](/research/ai/fortune-telling-hallucination-llm).

## Wrap Up

Running containers and tools that use containers on macOS has improved
a lot in the last few years (2?).

As Linux containers are somehow "alien software" for the operating system,
some work may be required specially when some dedicated hardware support is
need, as is the case of making the GPU available for AI inference.

There's still some (lots of!) room for improvement on the user experience
side of running software in containers on a Mac, but it looks like the gap
on some basic or not-so-basic workloads is not that big anymore, even when
compared to running native containers in Linux.

### Common issues

This are some issues that you may hit:

* If podman can't run a container, check if the podman machine was created
and started.

* If RamaLama can't start due to podman being unable to access the podman
machine, check if the machine is running, and check if you don't have
another machine running (e.g. the `podman-default-machine`). RamaLama does
not seem to be smart enough to select the machine based on
`CONTAINERS_MACHINE_PROVIDER`, and it may get the default machine. Try
stopping the `podman-default-machine` and run RamaLama again. As a last
resort, remove the `podman-default-machine` (it can be recreated at any time).

* If things start to get too slow, without without any visual feedback,
stop execution (CTLR+C) and restart with `--debug`. Most operations restart
from where it stopped (specially those involving downloads), and debug may
calm down your anxiety. (It helped with mine.)

## References

1. [RamaLama](https://ramalama.ai)
2. [Podman](https://podman.io)

