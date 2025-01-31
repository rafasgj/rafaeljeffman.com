---
title: IPA-AD trust local tests using ipalab-config
subtitle:
layout: main
section: ipalab-config
sections: []
tags:
  - ipalab-config
  - freeipa
  - windows active directory
  - development
lang: en
copy: 2025
date: 2025-01-31
abstract: >-
    Setting up an environment for local tests of FreeIPA trusts
    against Microsoft Active Directory requires [some good amount
    of work](/projects/freeipa/en/basic-lab-ad-trust), and require
    above average hardware resources, as you'll need a VM with a
    good amount of memory available and a good CPU. Here, we'll
    use [ipalab-config](https://pypi.org/p/ipalab-config) to
    simulate this environment using containers for FreeIPA and
    Samba AD DC, which will enable a fast environment that allow,
    many cases to be tested.
---

One important use-case of FreeIPA is to integrate to environments
that use Microsoft's Active Directory (AD), this is done by setting
a trust against the AD domain, and managing AD users access to IPA
resources through idviews and idoverrides. To enable the creation of
this trust, one needs a FreeIPA server with AD trust support, and an
Active Directory host.

As of today, the only way to run a Windows Server node in a Linux
host, is to use a virtual machine, and it requires, at least, 6Gb
of RAM, and a good processor so that the VM is usable for development.
FreeIPA is also only supported if deployed in a virtual machine, or bare
metal.

The goal here is to simulate this environment using lightweight,
rootless, containers, so that a trust between IPA and AD can be created
and most (if not all) operations between the trusts can be tested.

By using [ipalab-config](https://pypi.org/p/ipalab-config) to produce
the environment, if you have the configuration file ready, it takes
about 10 minutes to have the environment running.


## Requirements

The software required to run this environment is:

* [ipalab-config](https://pypi.org/p/ipalab-config) (at least, version 0.10.1)
* [podman-compose](https://github.com/containers/podman-compose)
* [podman](https://podman.io)
* [Ansible](https://ansible.com)

Before starting the environment, install the requirements with:

```nohl
$ python3 -m venv /tmp/ipalab
$ source /tmp/ipalab/bin/activate
$ pip install "ipalab-config>=0.10.1" "podman-compose>=1.3.0"
```

Note that the minimum version for `ipalab-config` is `0.10.1`, and this
experiment will not work with previous versions.

If you don't have `podman` and `ansible` installed, you can install them
in the same virtual environment:

```nohl
$ pip install podman ansible-core
```

## Creating the Environment

The configuration file for `ipalab-config` for the IPA-AD environment is:

[](https://github.com/rjeffman/ipalab-config/blob/main/examples/external_addc.yml){:class="download fa-solid fa-download" target="\_blank"}
```yaml
---
lab_name: ipa-ad-trust
subnet: "192.168.13.0/24"
external:
  hosts:
  - name: addc
    hostname: dc.ad.ipa.test
    role: addc
    ip_address: 192.168.13.250
    vars:
      forwarder: 192.168.13.100
ipa_deployments:
  - name: ipa
    domain: linux.ipa.test
    admin_password: SomeADMINpassword
    dm_password: SomeDMpassword
    cluster:
      servers:
        - name: server
          ip_address: 192.168.13.100
          capabilities: ["DNS", "AD"]
          vars:
            ipaserver_netbios_name: IPA
            ipaserver_idstart: 60000
            ipaserver_idmax: 62000
            ipaserver_rid_base: 63000
            ipaserver_secondary_rid_base: 70000
```

This configuration will create container composed of two nodes,
one node external to the IPA realm, the `addc` node, where we'll
install Samda AD DC. The other node will be the IPA server.

Given this configuration file (`external-addc.yml`), execute:

```nohl
$ ipalab-config external-addc.yml
```

A directory `ipa-ad-trust` will be crated, and inside you'll find:

* compose.yml
    : A compose file with the containers and network configuration
* inventory.yml
    : An Ansible inventory file with the container nodes and its variables
* containerfiles
    : A collection of containerfiles that can be used to experiment with
      different configurations/operating systems
* playbooks
    : A collection of Ansible playbooks
* hosts
    : A patch to append to /etc/hosts to access the nodes from the host
* requirements.yml
    : A list of Ansible collections that can be used to install the required
      collections with `ansible-galaxy collection install -r requirements.yml`

To start the containers, change to the `ipa-ad-trust` directory and run
`podman-compose`

```nohl
$ cd ipa-ad-trust
$ podman-compose up -d --build
```

### Deploying Samba AD DC

This configuration provides a playbook that allows fast deployment of
Samba AD DC using an Ansible playbook.

To run Ansible playbooks in containers running with Podman, the collection
`containers.podman` must be available, and can be installed from Ansible
Galaxy (use only if you did not install with `requirements.yml`):

```nohl
$ ansible-galaxy collection install containers.podman
```

Now run the playbook:

```nohl
$ ansible-playbook -i inventory.yml playbooks/deploy_addc.yml
```

After this steps, the container `addc` contains a working deployment of
Samba AD DC, with the required DNS entries and the DNS forwarder enabling
a two-way trust to be set on the IPA side.


### Deploying FreeIPA

You can deploy FreeIPA in the `server` using
[ansible-freeipa](https://github.com/freeipa/ansible-freeipa), which is
listed in the `requirements.yml` file, or can be installed with:

```nohl
$ ansible-galaxy collection install freeipa.ansible_freeipa
```

With the collection installed, deploy the FreeIPA server with:

```nohl
$ ansible-playbook -i inventory.yaml playbooks/install-cluster.yml
```

> Note: It is possible to install `ansible-freeipa` as an RPM in Fedora,
CentOS, RHEL and similar Linux distributions. Up to version 1.14.z, on
most of the platforms, the RPM package does not install the collection,
but the modules and roles. In this case, the provided playbook will not
work without adaptation. It is preferable, at this time, to use the
Galaxy collection.

### Configuring the Trust

Before creating the trust, the `server` host must be able to resolve
some DNS records from `addc`. To allow this, add a DNS forward zone
with a forwarder to the AD DC node.

As the commands will be executed in the server node, start a shell:

```nohl
$ podman exec -it server bash
```

```nohl
$ ipa dnsforwardzone-add ad.ipa.test. --forwarder 192.168.13.250
```

With the forwarder zone in place, you can create the trust wit;h

```nohl
$ ipa trust-add ad.ipa.test --admin=Administrator --password <<< Secret123
```

After this commands, you can start using the IPA-AD trust.

### Cleaning Up

After the tests are finished, the environment can be removed with:

```nohl
$ podman-compose down
```

## What have we done?

Let's dissect the environment description.

The `ipalab-config` file can be divided in three sections, the global
variables, the IPA deployments, and the external hosts. Most of global
variables are optional, but `subnet` is useful when defining specific
IP addresses for the host (unless you remember that the default `subnet`
CIDR is `192.168.159.0/24`).

The `lab_name` is mostly useful as documentation, but it also defines
the name of the output directory and the name of the `pod` created to
contain the containers. Having different `lab_name` allows the creation
of different environments on the same host.

```yaml
lab_name: ipa-ad-trust
subnet: "192.168.13.0/24"
```

### The external AD DC host

An external host will have a `role`, and it means that a default
configuration for the host (containerfile, Ansible playbooks) will be
create by `ipalab-config`:

```yaml
external:
  hosts:
  - name: addc
    hostname: dc.ad.ipa.test
    ip_address: 192.168.13.250
    role: addc
    vars:
      forwarder: 192.168.13.100
```

In this case, we have a host that has a specific address defined and
hostname, which are required if we use the provided playbook to deploy
Samba AD DC. The `vars` section on the host is directly passed to the
Ansible inventory file.

The external hosts created by `ipalab-config` use, when possible, the
same base image which need to be configured with packages and an entry
point command. In the case of the `addc` role, the configuration that
is generated for the container image is:

```yaml
image: localhost/samba-addc
build:
  context: containerfiles
  dockerfile: external-nodes
  args:
    packages: systemd
command: /usr/sbin/init
```

The only package added to the image is `systemd`, and the entry point
(`command`) is set to use systemd on the start of the container. The
actual package installation for Samba AD DC is done through the
provided Ansible playbook, found in `playbooks/deploy_addc.yml`. An
advantage of this method is to allow easy deployment and configuration
through Ansible variables (on the `vars` section), on through any other
means to modify the running image.


## The IPA cluster and Rootless Container Limitation

For this simple experiment, the IPA cluster is composed by a single
server, with "DNS" and "AD" (trust) roles.

```yaml
ipa_deployments:
  - name: ipa
    domain: linux.ipa.test
    admin_password: SomeADMINpassword
    dm_password: SomeDMpassword
    cluster:
      servers:
        - name: server
          ip_address: 192.168.13.100
          capabilities: ["DNS", "AD"]
          vars:
            ipaserver_netbios_name: IPA
            ipaserver_idstart: 60000
            ipaserver_idmax: 62000
            ipaserver_rid_base: 63000
            ipaserver_secondary_rid_base: 70000
```

There's not much interesting things about the `server` node, other than
the defined IP address (which is used as forwarder for Samba AD DC).

For this deployment, one should  note the use of some `ansible-freeipa`
variables to define the `idrange` of the server. This is required so that
when creating the trust there is some room in the `subuid/subgid` space
for the trust objects.

This limitation is caused by running the environment in a rootless
container, which limits the number of available subuid/subguid. Note that
this limitation also affects the Samba AD DC node, and some configuration
is also provided by `ipalab-config` to manage this limits.


## Wrap Up

The idea behind [ipalab-config](https://pypi.org/p/ipalab-config) is to
allow the easy and fast creation of complex environments to run FreeIPA
tests, and here, the tool was used to create an environment with two nodes,
one FreeIPA server and one Samba AD DC, so that trust operations can be
performed. Extending the environment to include IPA and AD DC clients
would not be difficult (and automation for IPA clients would already be
provided).

The usage of automation tools (Ansible) and rootless containers (Podman)
reduce issues like hardware requirements, deployment time, and allow for
easy recreation of the same environment, or with variations of it with
small changes in the configuration.
