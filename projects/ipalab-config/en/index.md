---
title: ipalab-config
layout: section
lang: en
sections:
  - ipalab-config
---

[ipalab-config](https://github.com/rjeffman/ipalab-config) is a tool designed to simplify the creation of complex environments to test [FreeIPA](/projects/freeipa/en). From a single YAML configuration file, `ipalab-config` creates a compose and an inventory file that allows the creation of an environment with multiple nodes in a few minutes so that tests can be executed both in a workstation or in CI/CD environments like the ones provided by [Github](https://github.com) or [Azure](https://dev.azure.com).

Although FreeIPA does not officially support the use of containers, it is possible to run and test it within these environments.

Development is [done on Github](https://github.com/rjeffman/ipalab-config), and you cant install it using `pip` from [PyPi](https://pypi.org/project/ipalab-config)(it is suggested that Python's virtual environments are used).

Although not a direct dependency, you'll need [podman-compose](https://github.com/containers/podman-compose) to start the environment, and you'll probably will be using [Ansible](https://ansible.com) to deploy FreeIPA and other nodes.

Altough not used in this project, if you are interested in FreeIPA running on containers, check [freeipa-containers](https://github.com/freeipa/freeipa-container).
