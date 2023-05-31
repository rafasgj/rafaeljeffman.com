---
layout: main
section: FreeIPA
tags:
  - FreeIPA
  - ansible-freeipa
  - Ansible
  - deployment
  - cluster
title: Deploying a FreeIPA cluster with ansible-freeipa
lang: en
copy: 2022
date: 2022-04-24
description: >
  Automate a FreeIPA cluster deployment with Ansible and ansible-freeipa.
---

[FreeIPA](https://freeipa.org) is a solution that allows, among other things, centralized authentication, authorization and account information. A mimimun FreeIPA environment would consist of a main server (responsible for CA revewal), a replica server (as you want to have some resilience on your auth environment), and one client (actually a bunch of clients).

Although planning a FreeIPA environment is the hard part, deploying it may be slightly easier, and can be automated with Ansible, using [ansible-freeipa](https://github.com/freeipa/ansible-freeipa).

The goal of this document is to show how FreeIPA deployment can be automated with ansible-freeipa. It assumes you have a controller node and more than one target nodes. All nodes should have network configured, static hostnames, and have hostnames resolvable, either though DNS or other means (e.g.: `/etc/hosts`). As packages will be installed, the target nodes should be able to connect to a `dnf` repository.


## Environment setup

Deploying a FreeIPA cluster with Ansible using ansible-freeipa requires either the use of the [ansible-freeipa repository](https://github.com/freeipa/ansible-freeipa), or the installation of the ansible-freeipa RPM package, or using a collection.

> RPM packages are available for Fedora, CentOS and Red Hat Enterprise Linux, and they differ a little from the collections as the roles and modules are not provided in a collection, so, instead of `freeipa.ansible_freeipa.ipaserver`, one would simply use `ipaserver`.

> For Ansible Automation Platform subscribers, `ansible-freeipa` is available through `Automation Hub'.

Of course you must have Ansible installed on your controller machine. You may use a Python virtual environment:

```
python -m venv /tmp/freeipa
. /tmp/freeipa/bin/activate
pip install ansible-core
```

[Ansible Galaxy](https://galaxy.ansible.com) [ansible-freeipa collection](https://galaxy.ansible.com/freeipa/ansible_freeipa) will be used, and it has to be installed before use:

```
ansible-galaxy collection install freeipa.ansible_freeipa
```

In the examples, some variables available only on version 1.9.0 of ansible-freeipa collection will be used. Make sure you have at least version 1.9.0 installed.


## Deploying the FreeIPA server

With the collection installed, the first FreeIPA server can be deployed using the playbook `install-server.yaml`:

```yaml
- name: Deploy an IPA server
  hosts: ipaserver
  become: true

  roles:
    - freeipa.ansible_freeipa.ipaserver:
      state: present
```

Altough some features can be added to an IPA server after it is installed (e.g.: KRA and DNS), adding new components is not suppported by ansible-freeipa, and you have to plan before installing the server.

In this example, the server deployed should have all the required components to be used as a testing host for ansible-freeipa, which means we need to have DNS, KRA and AD Trust components.

The configuration is done through role variables, which can be set in an inventory file:

{% raw %}
```yaml
all:
   children:
    ipacluster:
      hosts:
        ipaserver:
        ipareplicas:
        ipaclients:
      vars:
          ipadm_password: "{{ ipa_dm_password }}"
          ipaadmin_password: "{{ ipa_admin_password }}"
          ipaserver_domain: ipa.test
          ipaserver_realm: IPA.TEST
    ipaserver:
      hosts:
        server.ipa.test:
          ansible_user: root
      vars:
        # KRA
        ipaserver_setup_kra: true
        # DNS
        ipaserver_setup_dns: true
        ipaserver_forwarders: 1.1.1.1
        ipaserver_auto_reverse: true
        ipaserver_allow_zone_overlap: true
        # this is required for AD trust
        ipaserver_no_dnssec_validation: true
        # trust vars
        ipaserver_setup_adtrust: false
        # disable 'allow all' HBAC rule
        ipaserver_no_hbac_allow: true
```
{% endraw %}

The AD Trust and KRA setup are pretty simple and straightforward for ansible-freeipa tests. DNS is also somewhat simple. We need to set `no_dnssec_validation`, as it is required to setup a trust with Microsoft Ad, and adding a DNS forwarder allows us to keep external name resolution in an easy way. The `ipaserver_no_hbac_allow` is used as it is a recommended setting.

For more information on the `ipaserver` role options, [see the offical documentation](https://github.com/freeipa/ansible-freeipa/tree/master/roles/ipaserver).

Note that the _domain_ and _realm_ are set as variables for the cluster, as the same values will be used by _replicas_ and _clients_. The Directory Manager password (`ipadm_password`) and the Administrator (user `admin`, `ipaadmin_password`), are also set for the whole cluster.

> Note: As it is not in the scope of this document to describe the ways you have to provide a password for an Ansible playbook, a _placeholder_ will be used in the place of the passwords. ansbile-freeipa uses `SomeDMpassword` and `SomeADMINpassword` for testing purposes, and they are useally stored directly on the playbooks, but this behavior should be avoided, specially if you plan to share playbooks.

After deploying the server, some backup files are created with the private and public keys for the CA and KRA on the `ansible_user` directory. These files should be securely stored and backed up, what can be accomplished with a playbook:

```yaml
- name: Backup IPA server certificates
  hosts: ipaserver
  become: false
  gather_facts: false

  vars:
    target_dir: "{{ ipaserver_realm }}-certs"

  tasks:
  - name: Ensure backup directory exists locally
    ansible.builtin.file:
      path: "{{ target_dir }}"
      state: directory
    delegate_to: localhost

  - name: Retrieve IPA server master certificates
    ansible.builtin.fetch:
      src: "{{ item }}"
      dest: "{{ target_dir }}/"
      flat: true
    with_items:
      - cacert.p12
      - ca-agent.p12
      - kracert.p12
    become: true
```

Once the server is deployed, we can start deploying replicas and clients.


## Adding IPA replicas

Adding a replica to an IPA realm adds redundancy to your network, and allow clients to authenticate, resolve DNS, or access KRA data (vaults), even in the face o a complete meltdown of the initial server. If your server is also high on load, this might give it some relief.

A replica is also required in the case of upgrading the server. Even if upgrading a running server may be possible, it is not recommended, and upgrading servers involve decommissioning it, installing the new version, and waiting for replication.

The playbook to deploy a replica with ansible-freeipa is similar to the server deployment:

```yaml
- name: Deploy the IPA replicas
  hosts: ipareplicas
  become: true

  roles:
    - freeipa.ansible_freeipa.ipareplica:
      state: present
```

The changes occur in the variables configured in the inventory file:

{% raw %}
```yaml
all:
  children:
    ipacluster:
      hosts:
        ipaserver:
        ipareplicas:
        ipaclients:
      vars:
          ipadm_password: "{{ ipa_dm_password }}"
          ipaadmin_password: "{{ ipa_admin_password }}"
          ipaserver_domain: ipa.test
          ipaserver_realm: IPA.TEST
    ipareplicas:
      hosts:
        rep-01.fed.ipa.test:
          ansible_user: root
          # CA backup
          ipareplica_setup_ca: true
          # KRA backup
          ipareplica_setup_kra: true
          # DNS backup
          ipareplica_setup_dns: true
          ipareplica_no_dnssec_validation: true
          ipareplica_no_forwarders: true
          # Trust backup
          ipareplica_setup_trust: true
      vars:
        # Update DNS address
        ipasssd_enable_dns_updates: true
        # Automatically handle DNS nameservers (v1.9.0+)
        ipaclient_configure_dns_resolver: true
        ipaclient_dns_servers:
          # server.fed.ipa.test IPv4 address
          - 192.168.122.30
          # rep-01.fed.ipa.test IPv4 address
          - 192.168.122.31
```
{% endraw %}

After the initial IPA server is deployed, any number of replicas can be added to the realm (in an already existing environment, it is recommended that replicas are added one by one, and enough time for replication to finish is given), and each replica can have a different configuration.

Since each replica can have its own set of services, the configuration is done per host, and in this case, a similar configuration to the initial server is used. The main difference is that no forwarder is configured for DNS.

Although similar, a replica installation is different than the initial server. A replica is installed first as a client, then it is promoted to a replica. This means that the same configuration available for the `ipaclient` role is also availabel for the replica.

On ansible-freeipa prior to 1.9.0 one would have to configure the DNS resolution of the target node, specially if the only DNS server was the IPA server. This would involve a few tasks, depending on the network configuration.

Starting with version 1.9.0, the ansible-freeipa's `ipaclient` role allows one to configure the host DNS resolver to use a specific set of nameservers by setting the variables `ipaclient_configure_dns_resolver` and `ipaclient_dns_servers`. This will work with `systemd-resolved`, `NetworkManager` or plain `/etc/resolv.conf`.

Acconding to the oficial documentation, `ipaclient_all_ip_addresses` "defines if DNS A/AAAA records for each IP address on the client will be created", and, if the target node has a single IP this has the effect of adding the host IP to the embedded DNS database, and this is needed to finish `ipareplica` deployment, as it will allow replication to take place, finishing replica setup. 

For more information on the `ipareplica` role options, [see the offical documentation](https://github.com/freeipa/ansible-freeipa/tree/master/roles/ipareplica).

Now that our network has some redundancy, we can add some clients to it.


## Adding IPA clients

As it should be expected, by now, the playbook to deploy an IPA client is not much different from the playbooks used to deploy servers and replicas.

```yaml
- name: Deploy the IPA clients
  hosts: ipaclients
  become: true

  roles:
    - freeipa.ansible_freeipa.ipaclient:
      state: present
```

The options, on this case, will configure the environment users will see when they log into the client hosts. And although there might have some different configurations for each client, it is not uncommon that the configuration is shared between all client hosts:

{% raw %}
```yaml
all:
  children:
    ipacluster:
      hosts:
        ipaserver:
        ipareplicas:
        ipaclients:
      vars:
          ipadm_password: "{{ ipa_dm_password }}"
          ipaadmin_password: "{{ ipa_admin_password }}"
          ipaserver_domain: ipa.test
          ipaserver_realm: IPA.TEST
    ipaclients:
      hosts:
        cli-01.fed.ipa.test:
          ansible_user: root
      vars:
        # Client options
        ipaclient_mkhomedir: true
        # Update DNS address
        ipasssd_enable_dns_updates: true
        # Automatically handle DNS nameservers (v1.9.0+)
        ipaclient_configure_dns_resolver: true
        ipaclient_dns_servers:
          # server.fed.ipa.test IPv4 address
          - 192.168.122.30
          # rep-01.fed.ipa.test IPv4 address
          - 192.168.122.31
```
{% endraw %}

In this case the only specific setting for the client hosts is to allow the creation of the user home directory upon first login (as NFS shares are not used for user home directories).

With the clients deployed, we have the whole IPA cluster up and running, and now we can manage its configuration.


## Add users, groups and rules to access the clients

As the first server was installed with `ipaserver_no_hbac_allow: true`, access to all clients by IPA users is disabled by default. Using ansible-freipa plugins allow us to add users and HBAC rules for these users to allow them to log into the client host.

```yaml
---
- name: Configure users and host access
  hosts: ipaserver
  become: false
  gather_facts: false

  tasks:
  - name: Add a testing user
    ipauser:
      ipaadmin_password: "{{ ipa_admin_password }}"
      name: jdoe
      first: John
      last: Doe
      password: SomeJOHN

  - name: Ensure HBAC login services exist
    ipahbacsvc:
      ipaadmin_password: "{{ ipa_admin_password }}"
      name: "{{ item }}"
      state: present
    loop:
      - sshd
      - login

  - name: Allow user login on client hosts
    ipahbacrule:
      ipaadmin_password: "{{ ipa_admin_password }}"
      name: "User Login"
      usercategory: "all"
      hbacsvc:
        - "sshd"
        - "login"
      host: "{{ groups['ipaclients'] }}"
```

Note that importing a large number of users or rules will have an impact on the environment due to load in the server where the playbook runs (in this case `ipaserver`, the first server) and due to replication. One alternative is to use a hidden replica for bigger changes.

To test the final configuration, issue `ssh jdoe@cli-01.fed.ipa.test` and use the password `SomeJOHN` to log into the computing node.

## Wrap up

Installing an IPA cluster with ansible-freeipa is somewhat easy, but this should not encourage one to not think thoroughly on the environment being created. It only allows you to achieve what you pretend in an easier, automated and reproducible way.

Some important topics were not covered here for the provided playbooks to be used in production, like securing passwords, the domain names, or IPA addresses. These should all be well defined, specially since the domain cannot be changed once the realm is up.

Another interesting point not covered here is the deployment of hidden replicas, which are useful for backing up the configuration, or performing mass or lengty operations without disrupting the environment for clients.

What has been shown here is that using ansible-freeipa, specially in the later versions, can ease the setup and allow for fast experiences with an environment. For example, with a set of three virtual machines with network and domain names already setup, it is possible to bring up a cluster in about 20 minutes (most of the time is spent on downloading packages, so a local package repository or pre-downloaded packages will speed up). This is fast enough to make some experiments with the desired environment.

----

## Putting it all toghether

To deploy the whole cluster with a single execution you can merge the playbooks and the inventory files, allowing the cluster deployment in a single execution, for example:

```
ansible-playbook -i inventory.yaml install-freeipa-cluster.yml
```

Find below the code and the download option for these files.

[](/files/freeipa/install-freeipa-cluster.yml){:class="download fa-solid fa-download" download="install-freeipa-cluster.md"}
```yaml
---
- name: Install IPA server
  hosts: ipaserver
  become: true
  gather_facts: true

  roles:
  - role: freeipa.ansible_freeipa.ipaserver
    state: present

- name: Backup IPA server certificates
  hosts: ipaserver
  become: false
  gather_facts: false

  vars:
    target_dir: "{{ ipaserver_realm }}-certs"

  tasks:
  - name: Ensure backup directory exists locally
    ansible.builtin.file:
      path: "{{ target_dir }}"
      state: directory
    delegate_to: localhost

  - name: Retrieve IPA server master certificates
    ansible.builtin.fetch:
      src: "{{ item }}"
      dest: "{{ target_dir }}/"
      flat: true
    with_items:
      - cacert.p12
      - ca-agent.p12
      - kracert.p12
    become: true

- name: Install IPA replicas
  hosts: ipareplicas
  become: true
  gather_facts: true

  roles:
  - role: freeipa.ansible_freeipa.ipareplica
    state: present

- name: Install IPA clients
  hosts: ipaclients
  become: true
  gather_facts: true

  roles:
  - role: freeipa.ansible_freeipa.ipaclient
    state: present
```

[](/files/freeipa/cluster-inventory.yaml){:class="download fa-solid fa-download" download="cluster-inventory.yaml"}
{% raw %}
```yaml
---
all:
  children:
    # define cluster
    ipacluster:
      children:
        ipaserver:
        ipareplicas:
        ipaclients:
      vars:
        ipaserver_domain: fed.ipa.test
        ipaserver_realm: FED.IPA.TEST
        ipadm_password: "{{ ipa_dm_password }}"
        ipaadmin_password: "{{ ipa_admin_password }}"
    # IPA First Server (CA Renewal)
    ipaserver:
      hosts:
        server.fed.ipa.test:
          ansible_user: root
      vars:
        # KRA
        ipaserver_setup_kra: true
        # DNS
        ipaserver_setup_dns: true
        ipaserver_forwarders: 1.1.1.1
        ipaserver_auto_reverse: true
        ipaserver_allow_zone_overlap: true
        # this is required for AD trust
        ipaserver_no_dnssec_validation: true
        # trust vars
        ipaserver_setup_adtrust: true
        # disable 'allow all' HBAC rule
        ipaserver_no_hbac_allow: true
        # other vars
    # IPA Replica Servers
    ipareplicas:
      hosts:
        rep-01.fed.ipa.test:
          ansible_user: root
          # CA backup
          ipareplica_setup_ca: true
          # KRA backup
          ipareplica_setup_kra: true
          # DNS backup
          ipareplica_setup_dns: true
          ipareplica_no_dnssec_validation: true
          ipareplica_no_forwarders: true
          # Trust backup
          ipareplica_setup_trust: true
      vars:
        # Update DNS address
        ipasssd_enable_dns_updates: true
        # Automatically handle DNS nameservers (v1.9.0+)
        ipaclient_configure_dns_resolver: true
        ipaclient_dns_servers:
          # server.fed.ipa.test IPv4 address
          - 192.168.122.30
          # rep-01.fed.ipa.test IPv4 address
          - 192.168.122.31
    # IPA Client hosts
    ipaclients:
      hosts:
        cli-01.fed.ipa.test:
          ansible_user: root
      vars:
        # Client options
        ipaclient_mkhomedir: true
        # Update DNS address
        ipasssd_enable_dns_updates: true
        # Automatically handle DNS nameservers (v1.9.0+)
        ipaclient_configure_dns_resolver: true
        ipaclient_dns_servers:
          # server.fed.ipa.test IPv4 address
          - 192.168.122.30
          # rep-01.fed.ipa.test IPv4 address
          - 192.168.122.31
```
{% endraw %}
