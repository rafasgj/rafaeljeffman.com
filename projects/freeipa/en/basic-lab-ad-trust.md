---
layout: main
section: FreeIPA
tags:
  - FreeIPA
  - Windows Active Directory
  - trust
  - ansible-freeipa
  - Ansible
title: Creating a test lab for FreeIPA-AD trust
lang: en
copy: 2022
date: 2022-04-19
description: >
  Automate the creation of a trust bettwen FreeIPA and Windows
  Server Active Directory using Ansible and ansible-freeipa.
---

[FreeIPA] is an integrated Identity and Authentication solution for
Linux/UNIX networked environments. Microsoft's [Active Directory] (AD)
is a directory service for [Microsoft Windows] domain networks which
provides authentication and access control to directory objects.

In a mixed environment it makes sense to integrate both to provide an
integrated authentication solution for network users. It is possible to
integrate FreeIPA and Active Directory through a _trust_ between both
systems.

The goal of this document is to show the steps to configure a virtual
test lab using libvirt/KVM virtual machines to test FreeIPA/AD trust
setup and configuration.

The environment created will consist of a single FreeIPA server and a
single Windows Server with Active Directory, and neither domain is a
sub-domain of the other. There will be no clients or replication
involved. Different ways of setting up a trust between FreeIPA and AD
are not discussed here, only the simplest case. The Windows/Active
Directory domain is `ad.ipa.test`. The Linux/FreeIPA domain
`lin.ipa.test`. Each domain have its own authoritative DNS nameserver.

It is assumed that you have a good amount of disk space as, at least,
40GB are used, you should have some spare space, and I would not
recommend starting this with less that 50GB available. You'll also need
at least 16 GB of RAM, where a minimum of 7GB will be used for the
virtual machines. Expect much more if you need clients and replication.

Both a manual installation of the servers, and an automated one (at
least partially automated) will be discussed.


## Prerequisites


### Manual Installation

For the manual installation process you will need a working setup of
libvirt/KVM. The host machine will double as the _controller node_ for
the automated installation using [Ansible].

### Ansible Automation

For the automated installation, you will also need Ansible, and a few
of its collections:
   * [ansible-freeipa]
   * [linux-system-roles]
   * ansible.windows
   * community.windows
   * community.general

[ansible-freeipa] and [linux-system-roles] can be installed either as
packages or [Ansible Galaxy] collections. The other collections are
available with the Ansible package,  but must be individually installed
(e.g. through Galaxy) if using `ansible-core`.

The playbooks are
[available in a Github repository](https://github.com/rjeffman/freeipa-ad-trust).

> **NOTE**: While I was creating this environment, in the Ansible
controller, _Linux System Roles_ was installed using Fedora packages,
the other collections were installed using [Ansible Galaxy], and the
_master_ branch of ansible-freeipa_ was used (either the Ansible Galaxy
or the RPM packages should work). I didn't care to fix the
playbooks so that they were readily usable in every situation. You may
need to adapt the playbooks for your own use (i.e. use fully qualified
collection names - FQCN - for roles/modules/actions).


## Installing and configuring the Windows AD server

You will need a VM running Windows Server and Active Directory to create
the trust. This section will guide you through the steps to install and
configure this VM.

> The AD installation procedure is the same as in
[XpertsTech](https://xpertstec.com/how-to-install-active-directory-in-server-2022),
they have screenshots there, which makes following the procedure easier.

1. Download Windows Server VHD Image (evaluation version, usable for
   180 days):

    > If you don't have a specific Windows Server version in mind, I suggest
    you use Windows Server 2019, as it is [officially supported by IPA], at
    the time of this writing (Windows Server 2022 should follow shortly).

    * [Windows Server 2022](https://www.microsoft.com/en-us/evalcenter/evaluate-windows-server-2022) - select VHD
    * [Windows Server 2019](https://www.microsoft.com/en-us/evalcenter/evaluate-windows-server-2019) - select VHD
    * [Windows Server 2016](https://www.microsoft.com/en-us/evalcenter/evaluate-windows-server-2016) - you'll have to select ISO and perform a "regular" installation, which is out of the scope of this document.

2. Convert the VHD image to QCOW2
    ```none
qemu-img convert -p -f vpc -O qcow2 <Windows Image>.vhd w2k22.qcow2
    ```
    > The Windows VHD image file will have different names depending on
    the version you selected. The resulting filename should easily
    identify the version being used, like _w2k22_ for Windows Server 2022,
    or _w2k19_ for Windows Server 2019, for example.

3. Create VM

    In this example, 1 virtual CPU and 4GB or RAM is used,
    what seems to make initial configuration much more slow, but will
    have little to no effect later. You may also use the `virt-manager`
    GUI to create the VM, importing the VM file.

    ```none
virt-install \
        --connect qemu:///system \
        --name "win2k22-ad" \
        --description "Windows Server 2022 AD" \
        --os-type "Windows" \
        --os-variant "win2k22" \
        --ram 4096 \
        --vcpus 1 \
        --disk path="win2k22.qcow2" \
        --virt-type kvm \
        --graphics spice \
        --import
    ```

    > The `os-type` will be `Windows`, the `os-variant` may be different
      depending on the Windows version used. You can use the value found
      in the "Short ID" field of the output of command
      `osinfo-query -s name -f short-id,name os family=winnt`. Also
      remember to change the `disk path`, if using another file as
      virtual storage.

4. Configure the Windows Server with the wizard, and log into it as
   `Administrator`.
> I used the password `SomeW1Npassword`, and I also changed the keyboard
  layout to Dvorak, which seems to finally work fine on Windows. I used
  the default value for any other setting.

5. Set an static IPv4 address:

    * On `Settings > Network & Internet > Change adapter Options`:
        * Double-click `Ethernet Instance 0`
        * Click `Properties`
        * Select `Internet Protocol Version 4 (TPC/IPv4)` and click
          `Properties`
            * Set the IP address (the values are the ones I used):
                * IP address: `192.168.122.252`
                * Subnet mask: `255.255.255.0`
                * Default Gateway: `192.168.122.1`
            * Set DNS server address:
                * Preferred DNS server: `1.1.1.1`
            * Click `Ok` to apply settings.

6. Change computer name.

    * In `Server Manager > Local Server`, click on the `Computer Name` value:
        * Click `Change...`
        * Set computer name to `server`
        * Click `More...`
            * Set `Primary DNS suffix of this computer` to `ad.ipa.test`
            * Click `Ok` to apply
        * Click `Ok` to apply

7. Reboot the VM.

8. If it is not running, start `Server Manager` and, in the
   `Quick Start` tab, choose `(2) Add roles and features`:

    * Before you Begin: Click `Next`
    * Installation Type: `Role-based or feature-based installation`
    * Select destination server: `server.ad.ipa.test`
    * Select server roles:
        * Choose `Active Directory Domain Services` and click
          `Add Features`
        * Choose `DNS Server` and click `Add Features`
        * Click `Next`
    * Features: click `Next`
    * AD DS: click `Next`
    * DNS Server: click `Next`
    * Confirmation: click `Install`

9. Back in the Server Manager Dashboard, click on the
   `Notifications Flag` (which should have a huge yellow warning icon
   now) and select `Promote this server to a domain controller`

    * Deployment Configuration:
        * Deployment operation: `Add a new forest`
        * Root domain name: `ad.ipa.test`
    * Domain controller options:
        * Provide DSRM password: `ad1Restore`
    * DNS Options: Do not set `Create DNS delegation`
    * Additional Options:
        * The NetBIOS domain name: `AD`
    * Advance (click `Next`) through _Paths_ and _Review Options_
    * Prerequisites Check: click `Install`

After the reboot (the wizard will prompt you to click a `Close` button,
but if you ignore it, it will restart anyway) you are done installing
Active Directory and can login into the `ad.ipa.test` domain with the
Administrator account (credentials: `Administrator`/`SomeW1Npassword`).


### Add a test user

This procedure will add user to AD, that will be used to test the trust
to FreeIPA.

* While in the `Server Manager` choose `Tools > Active Directory
  Administrative Center`
* Select `ad (local)`
* On the right panel (`Tasks`), select `ad (local) > New > user`
    * Fill in user information:
        * First name: `John`
        * Last name: `Doe`
        * User SamAccountName logon: `ad \ jdoe`
        * Password/Confirm Password: `SomeUS3Rpassword`
        * Set `Other password options > Password never expires`
    * Click `Ok`

> **Note**: If you don't want to set `Password never expires`, use a
  different password and login with `jdoe` user. Although the login
  will fail, it will be enough to change the password to a usable one.


### Testing Active Directory from a Linux machine

You may now test if you can acquire a Kerberos TGT from Windows AD in a
Linux machine. You may need to install `krb5-workstation` (Fedora
package name that contains `kinit`) for this test.

* Add `server.ad.ipa.test` IP address to `/etc/hosts` or configure
  `/ect/resolv.conf` to use `server.ad.ipa.test` as a nameserver.

* Add to `/etc/krb5.conf` in the `[realms]` section:

   ```none
AD.IPA.TEST = {
        kdc = server.ad.ipa.test
        admin_server = server.ad.ipa.test
}
   ```

* Test login with `kinit jdoe@AD.IPA.TEST`.

Once this test works, the Windows AD part is (nearly) ready.


## Installing and configuring the FreeIPA server

Now, setup a FreeIPA server using a Linux VM.

> **NOTE**: All settings not managed by FreeIPA are based on the ones I
  set for a Fedora 35 cloud image, as downloaded on 2022-04-04. You may
  have to adapt those to the distribution chosen.

> **NOTE 2**: A FreeIPA server requires the host to have a fixed DNS and
  a fully qualified domain name as hostname. Here, I'll use a static IP
  address, but the same effect is possible with DHCP and fixed IP
  attribution to the server.

1. Set hostname:

    ```none
$ hostnamectl set-hosname server.lin.ipa.test
    ```

2. Set a fixed IP address:

    ```none
# nmcli connection modify "Wired connection 1" \
        ipv4.method manual \
        ipv4.address 192.168.122.251/24 \
        ipv4.gateway 192.168.122.1 \
        ipv4.dns 1.1.1.1
# nmcli dev reapply eth0
    ```

3. Update image and reboot (Optional)

    ```none
# dnf -y update && reboot
    ```

4. Install FreeIPA packages

    ```none
# dnf install -y \
        ipa-server \
        ipa-server-dns \
        ipa-server-trust-ad \
        python3-libselinux \
        firewalld
    ```

5. Install FreeIPA with integrated DNS and AD trust (note that it is
   important to disable DNSSEC validation)

    ```none
# ipa-server-install \
    -U \
    --ds-password SomeDMpassword \
    --admin-password SomeADMINpassword \
    --domain lin.ipa.test \
    --realm LIN.IPA.TEST \
    --hostname server.lin.ipa.test \
    --mkhomedir \
    --no-ntp \
    --setup-kra \
    --setup-adtrust \
    --setup-dns \
    --no-dnssec-validation \
    --no-forwarders    
    ```

After these steps you'll have FreeIPA installed, and you can test your installation with:

```none
# kinit admin
Password for admin@LIN.IPA.TEST:
```


### Add Forward Zone to Windows AD

Before creating the trust there is one last configuration to do on the
Windows side. Start PowerShell and execute the command:

```none
dnscmd 127.0.0.1 /ZoneAdd lin.ipa.test /Forwarder 192.168.122.251
```

This will set a DNS forwarder zone on Windows DNS for the FreeIPA
domain. You can test it in PowerShell using:

```none
PS C:> nslookup
> set type=srv
> _ldap._tcp.ad.ipa.test
(you should see the Windows answer here)
> _ldap._tcp.lin.ipa.test
(you should see the Linux answer here)
> quit
```

There might be some IPv6 warnings or errors, for this exercise you can
safely ignore those errors. There should not be any `NXDOMAIN` errors.


### Creating a trust to AD

Now, we configure the FreeIPA integrated DNS nameserver so we are able
to find the Windows AD server, and then create the trust between FreeIPA
and Windows AD.

1. Add the Windows AD server IP as a DNS forwarder (you'll need a valid
   Kerberos TGT for user `admin`)
    ```none
$ ipa dnsconfig-mod --forwarder=192.168.122.252 --forward-policy=only
    ```
    This will set a global forwarder to the Windows AD server. You can
    test it with `nslookup`:
    ```none
# nslookup
> set type=srv
> _ldap._tcp.ad.ipa.test
(you should see the Windows answer here)
> _ldap._tcp.lin.ipa.test
(you should see the Linux answer here)
    ```

2. Configure IPA server for cross-forest trust
    ```none
# ipa-adtrust-install \
        -U \
        --netbios-name=LIN \
        --admin-password SomeADMINpassword \
        --add-sids
    ```

3. Establish IPA-AD trust (use Windows AD Administrator password:
   SomeW1Npassword)
    ```none
# ipa trust-add --type=ad ad.ipa.test --admin Administrator --password
Active Directory domain administrator's password:
    ```

With the trust configured, you can [test the trust](#testing-the-setup).


## Automating with Ansible

Now that we know all the steps to have a working FreeIPA-Windows AD
trust,a good part of this procedure be automated with Ansible. The best
part is that this makes for a reproducible environment, and it (usually)
runs much faster than the manual installation, specially on the Windows
side.

> All the steps that were turned into an Ansible playbooks _run
correctly on my machine_, YMMV. If you encounter an issue, open a
[Github issue](https://github.com/rafasgj/rafaeljeffman.com/issues/new),
and I'll try to fix it. Good Luck.

> You might want to
[download the playbooks used](https://github.com/rjeffman/freeipa-ad-trust).

Before you start, this steps assume you have the following installed on
your host machine:

* _WinRM_: install package `python3-winrm` (Fedora) or `pywinrm` (pip)
* _Ansible Collections_: The following collections must be installed:
    * ansible.windows
    * community.windows
    * community.general
    * freeipa.ansible_freeipa (I'll use the [git repository])

The host machine will double as Ansible controller node.


### The inventory file

To execute all the playbooks, an inventory file is required. It is also
used to define several variables that can be customized.

This was the inventory used to test this procedure. For production use,
you should not have your passwords in clear text in your inventory, this
is for demonstration purpose only:

[](https://github.com/rjeffman/freeipa-ad-trust/blob/main/inventory.yaml){:class="download fa-solid fa-download"}
{% raw %}
```yaml
# inventory.yaml
---
all:
  children:
    winserver:
      hosts:
        server.ad.ipa.test:
          ansible_connection: winrm
          ansible_winrm_server_cert_validation: ignore
          ansible_user: "Administrator"
          ansible_password: "{{ winserver_admin_password }}"
    ipaserver:
      hosts:
        server.lin.ipa.test:
          ansible_user: root
      vars:
        # DNS configuration
        ipaserver_setup_dns: true
        ipaserver_no_forwarders: true
        # trust configuration
        ipaserver_setup_adtrust: true
        # disable 'allow all' HBAC rule
        # ipaserver_no_hbac_allow: false
  vars:
    # passwords
    ipaadmin_password: SomeADMINpassword
    ipadm_password: SomeDMpassword
    # server/realm
    ipaserver_domain: lin.ipa.test
    ipaserver_realm: LIN.IPA.TEST
    ipaserver_netbios_name: IPA
    # client configuration
    ipaclient_mkhomedir: true
    ipaclient_no_ntp: true
    # hostnames
    ipaserver_hostname: server.lin.ipa.test
    winserver_hostname: server.ad.ipa.test
    # IP address
    ipaserver_ip: 192.168.122.251
    winserver_ip: 192.168.122.252
    # Windows vars
    winserver_admin_password: SomeW1Npassword
    winserver_dsrm_password: ad1Restore
    winserver_domain: ad.ipa.test
    winserver_realm: AD.IPA.TEST
    winserver_netbios_name: AD
    # timezones (the timezones must match)
    ipaserver_timezone: "Etc/UTC"
    winserver_timezone: "UTC"  # available timezones: `tzutil.exe /l`
```
{% endraw %}

One important item in this inventory is the Time Zones settings, as
Windows and Linux use different values to refer to the same time zone,
and the time zones must match.


### Windows installation and Configuration

The first steps of the
[Windows installation procedure](#installing-and-configuring-the-windows-ad-server)
were not automated, so you still have to manually execute steps `1`
through `5` (that is install Windows until you can login Administrator,
and setup its network connection).

After the Windows installation, you need to configure it so that Ansible
can connect to it using [WinRM connector]. [Red Hat] has provided a
[nice document] with instructions and details on automating Microsoft
Windows tasks with Ansible (you should read it and follow some links).

Download and execute the PowerShell script that will configure the
system for you:

```
> wget
        -Uri https://raw.githubusercontent.com/ansible/ansible/devel/examples/scripts/ConfigureRemotingForAnsible.ps1
        -OutFile configure_ansible.ps1
> .\configure_ansible.ps1
```

Now you can get back to your Ansible controller (host machine), and test
if the Windows machine is responding to Ansible:

```none
$ ansible winserver -i inventory.yaml -m ansible.windows.win_ping
```

The playbook below will configure the Windows server, deploy and
configure Active Directory and DNS, and prepare everything needed to
create the trust with FreeIPA. The Windows VM will reboot twice.

[](https://github.com/rjeffman/freeipa-ad-trust/blob/main/01-windows-ad-setup.yml){:class="download fa-solid fa-download"}
{% raw %}
```yaml
# windows-ad-setup.yml
---
- name: Deploy Windows Server AD
  hosts: winserver
  become: false

  tasks:
  - name: Ensure AD timezone matches IPA timezone.
    community.windows.win_timezone:
      timezone: "{{ winserver_timezone }}"

  - name: Change the Window hostname
    ansible.windows.win_hostname:
      name: "server"
    register: hostname

  - name: Reboot server
    ansible.windows.win_reboot:
      msg: "Reboot after name and timezone changes."
      pre_reboot_delay: 15
    when: hostname.reboot_required or hostname.reboot_required

  - name: Install AD feature
    ansible.windows.win_feature:
      name: AD-Domain-Services
      include_management_tools: true
      include_sub_features: true
      state: present

  - name: Install DNS feature and configure first AD Domain
    ansible.windows.win_domain:
      dns_domain_name: "{{ winserver_domain }}"
      safe_mode_password: "{{ winserver_dsrm_password }}"
      install_dns: true
      domain_netbios_name: "{{ winserver_netbios_name }}"
    register: status

  - name: Reboot server
    win_reboot:
      msg: "Reboot after AD Domain installation."
      pre_reboot_delay: 15
    when: status.changed

  - name: Add IPA DNS forward zone
    ansible.windows.win_command: |
      dnscmd 127.0.0.1 /ZoneAdd {{ ipaserver_domain }} /Forwarder {{ ipaserver_ip }}
    register: result
    failed_when:
      result.failed and "DNS_ERROR_FORWARDER_ALREADY_EXISTS" not in result.stdout

  - name: Add jdoe test user.
    community.windows.win_domain_user:
      # 'name' will be the user SAM account name and identity.
      name: jdoe
      upn: "jdoe@{{ winserver_domain }}"
      firstname: John
      surname: Doe
      enabled: true
      password_expired: false
      password: SomeUS3Rpassword
      update_password: on_create
```
{% endraw %}

Execute it with:

 ```none
$ ansible-playbook -i inventory.yaml windows-ad-setup.yml
 ```


### FreeIPA installation and configuration

The installation of FreeIPA requires a supported Linux distribution
(here I used a Fedora 35 cloud image) and can be easily achieved with
[ansible-freeipa]. This playbook will perform all the configuration,
but creating the trust.

[](https://github.com/rjeffman/freeipa-ad-trust/blob/main/02-ipa-setup.yml){:class="download fa-solid fa-download"}
{% raw %}
```yaml
# ipa-setup.yml
---
- name: Pre-checks to deploy IPA
  hosts: ipaserver
  become: true

  tasks:
  - name: Set FQDN for FreeIPA Server
    ansible.builtin.hostname:
      name: "{{ ipaserver_hostname }}"

  - name: Ensure IPA timezone matches AD timezone.
    community.general.timezone:
      name: "{{ ipaserver_timezone }}"
    become: true

# ---------------------
- name: Deploy IPA with support to AD.
  hosts: ipaserver
  become: true

  roles:
  - role: ipaserver
    state: present
    become: true

  # IPA configuration of trust to Windows AD
  tasks:
  - name: Add AD DNS forward zone
    ipadnsforwardzone:
      ipaadmin_password: SomeADMINpassword
      name: "{{ winserver_domain }}"
      forwarders:
      - ip_address: "{{ winserver_ip }}"
      forwardpolicy: "only"
```
{% endraw %}

Invoke the playbook with:

```none
$ ansible-playbook -i inventory.yaml ipa-setup.yml
```

After FreeIPA is deployed you can create the trust to AD, using
[ansible-freeipa]:

[](https://github.com/rjeffman/freeipa-ad-trust/blob/main/04-add-trust.yml){:class="download fa-solid fa-download"}
{% raw %}
```yaml
# add-trust.yml
---
- name: Playbook to create a trust to AD
  hosts: ipaserver
  become: false
  gather_facts: false

  tasks:
    - name: Ensure AD trust is present
      ipatrust:
        realm: {{ winserver_domain }}
        admin: Avdministrator
        password: {{ winserver_admin_password }}
        state: present
```
{% endraw %}

And now the FreeIPA-Windows AD trust is ready to be used.


## Testing the setup

To test the trust setup we'll allow AD users to login into the Linux
VM. On the FreeIPA side, you have to edit `/etc/krb5.conf`, add add the
two `auth_to_local` lines:

```none
[realms]
LIN.IPA.TEST = {
(...)
      auth_to_local = RULE:[1:$1@$0](^.*@AD.IPA.TEST)s/@AD.IPA.TEST/@ad.ipa.test/
      auth_to_local = DEFAULT
}
```

And restart `krb5kdc` and `ssd` services:
```none
# systemctl restart krb5kdc
# systemctl restart sssd
```

Now, AD users can login through SSH to the FreeIPA server using
`AD\<user name>` or _UPN username_, as in `ssh AD\\jdoe@ad.ipa.test`.

### Automating configuration with Ansible

This step can also be automated with the following playbook:

[](https://github.com/rjeffman/freeipa-ad-trust/blob/main/05-krb5-config.yml){:class="download fa-solid fa-download"}
{% raw %}
```yaml
# krb5-config.yml
---
- name: Configure Kerberos to allow for AD users login.
  hosts: "{{ target_host | default('ipaserver') }}"
  become: true
  gather_facts: false

  tasks:
  - name: Modify /etc/krb5.conf
    ansible.builtin.blockinfile:
      path: /etc/krb5.conf
      insertbefore: "kdc = {{ ipaserver_hostname }}:88"
      block: |
        auth_to_local = RULE:[1:$1@$0](^.*@AD_DOMAIN$)s/@AD_DOMAIN/@ad_domain/
        auth_to_local = DEFAULT

  - name: Restart Kerberos KDC
    ansible.builtin.systemd:
      name: krb5kdc
      state: restarted

  - name: Restart SSSD
    ansible.builtin.systemd:
      name: sssd
      state: restarted
```
{% endraw %}


##  Wrap up

A testing environment with a trust between FreeIPA and Widows Active
Directory was created and automated. It can be easily extended and
enhanced, and certainly needs to be secured, to be used in a production
environment.

Setting up a mixed environment that integrates [FreeIPA] and Active
Directory brings more flexibility to the network environment, and
enhance usability of both Linux and Windows domains for the users.

Automating the creation of such an environment can be achieved, and
brings a reproducible configuration, helping to reduce some of the
complexity.


<!-- links -->
[FreeIPA]: https://freeipa.org
[ansible]: https://ansible.com
[ansible-freeipa]: https://github.com/freeipa/ansible-freeipa
[git repository]: https://github.com/freeipa/ansible-freeipa
[linux-system-roles]: https://linux-system-roles.github.io
[libvirt]: https://libvirt.org
[kvm]: https://www.linux-kvm.org
[ansible galaxy]: https://galaxy.ansible.com
[nice document]: https://www.redhat.com/en/technologies/management/ansible/automate-microsoft-windows-with-ansible
[microsoft windows]: https://windowsserver.com
[active directory]: https://docs.microsoft.com/pt-br/windows-server/identity/identity-and-access
[red hat]: https://redhat.com
[WinRM connector]: https://docs.ansible.com/ansible/latest/user_guide/windows_winrm.html
[officially supported by IPA]: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/integrating_rhel_systems_directly_with_windows_active_directory/connecting-rhel-systems-directly-to-ad-using-sssd_integrating-rhel-systems-directly-with-active-directory#supported-windows-platforms-for-direct-integration_connecting-rhel-systems-directly-to-ad-using-sssd
<!-- [nice document]: https://www.redhat.com/pt-br/technologies/management/ansible/automate-microsoft-windows-with-ansible -->
