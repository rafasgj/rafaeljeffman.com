---
title: FreeIPA and External Identity Providers
subtitle: 
layout: main
section: FreeIPA
sections: []
tags:
  - freeipa
  - external idp
  - user identity
lang: en
copy: 2024
date: 2024-01-28
abstract:
---
## FreeIPA, identities and identity providers

[FreeIPA] provides an integrated identity management solution for POSIX-alike environments, and this environment influenced the way users and groups are represented and implemented. The POSIX model is based on applications usually interfacing inside a shell session, initiated by the users represented by the POSIX identity.

With the move to web and mobile oriented user interfaces, the POSIX user consumption patter have become less prominent, and POSIX identities may be relegated to be a support mechanims for running isolated applications. 

Usage shift does not mean that one model superseeded the other. The same users need to access both operating sysetm-level applications and be able to authenticate as application-lever identities. This is tipycall achieved by forming a single sign-on environment where a user would authenticate once and then the fact of authentication is consumed by other services for a certain amount of time, regardless of how the applications that represent these services are operating.

Currently, FreeIPA suuports using external identity providers (_external IdP_) to perform identity verification and ask for an access grant to itself. Authentication and authorization of the identity is delegated to the external IdP and the user information in FreeIPA is used as an anchor to map external IdP identity to a system-level user identity.

You can get a lot more details on the design and implementation on the [FreeIPA external IdP design document]{:target="\_blank"}.


## Using Github as an Identity Provider for FreeIPA

Before configuring your FreeIPA deployment to use Github as an application provider, you need to register a new OAuth appliction within Github. It will provide some attributes you'll need to configure FreeIPA, and will also allow your users to know what they are sharing with you.

This is a step-by-step procedure to register your application with Github:

1. Access [https://github.com/settings/applications/new](https://github.com/settings/applications/new)
2. Define your application name: `fosdem_demo`
3. Define the homepage URL to be `https://<freeipa_server>/ipa`. In my lab implamentation this would be `https://cs9.lin.ipa.test/ipa`
4. Set authorization callback URL to the same value as the homepage URL
5. Enable device workflow.

Once you register your OAuth application, a client ID wil be generated. This value must be copied and stored as it will be used later.

Generate a _client secret_, copy and store this value. Take care as you will not be able to see the secret again (altough you can generate a new one). 


## Using Identity Providers in FreeIPA

Now, on the FreeIPA server side, you must first add a new identity provider:

```bash
ipa idp-add github_idp \
    --provider github --secret \
    --client-id <the_cliend_id_from_github>
```

This will create an idp object stored in the FreeIPA LDAP database with the following configuration:

```nohighlight
[root@cs9 ~]# ipa idp-show github_idp
  Identity Provider reference name: github_idp
  Authorization URI: https://github.com/login/oauth/authorize
  Device authorization URI: https://github.com/login/device/code
  Token URI: https://github.com/login/oauth/access_token
  User info URI: https://api.github.com/user
  Client identifier: 481789d5cd3ca6b3f03f
  Scope: user
  External IdP user identifier attribute: login
```

Once the IdP object is setup, we can create or modify users to use the extenal entity to provide the identity. Users that will login using an external IdP must have the proper authentication type.

```bash
ipa user-add rafasgj \
    --first Rafael \
    --last Jeffman \
    --idp github_idp \
    --idp-user-id rafasgj \
    --user-auth-type idp
```

Note that the `idp` field is the name of the configured idp object, and `idp-user-id` is related to the `External idP user identifier attribute` as available in the identity provider.

The user identifier attribute should ensure that it identifies only that single user, but in the case of the Github provider it is set to `login` for convenient test purposes, as Github states that a user login is not unique and can be reused after a user account was deleted. In this case, a better suited attribute for use in production is `id`, and the issue is that is somewhat hidden from a user. One can use the following command to retrieve a user `id`:

```bash
curl --silent \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/users/<user_name> | jq .id
```

If you use user `test`, it should answer with `383316`.

To modify the Github IdP to use `id` instead of login, use

```bash
ipa idp-mod github_idp --idp-user-id id
```

Don't forget to modify the user(s) accordingly:

```bash
ipa user-mod rafasgj --idp-user-id 123456789
```

## Using the configured user

Once external IdP and the user has been configured, we can Anonymous PKINIT to obtain a ticket and store it in a cache file (e.g. `./fast.ccache`). Then we can enable FAST channel with the use of `-T` option for `kinit` tool.

```nohighlight
$ kinit -n -c ./fast.ccache
$ kinit -T ./fast.ccache rafasgj
Authenticate with PIN 05CF-40A4 at
https://github.com/login/device and press ENTER.:
```

Once this is executed, it will require the provided link to be opened and the pin to be entered

![Github PIN confirmation](/files/freeipa/github_idp_pin.png){:style="margin: auto 0"}

After obtaining the Kerberos TGT, a `klist -A` shows:

```nohighlight
Ticket cache: KCM:0
Default principal: rafasgj@LIN.IPA.TEST

Valid starting       Expires              Service principal
02/03/2024 03:25:32  02/04/2024 03:01:35  HTTP/cs9.lin.ipa.test@LIN.IPA.TEST
02/03/2024 03:24:47  02/04/2024 03:01:35  krbtgt/LIN.IPA.TEST@LIN.IPA.TEST
```

A similar process is used for SSH:

```nohighlight
[rjeffman@corellia ~]$ ssh rafasgj@cs9.lin.ipa.test
(rafasgj@cs9.lin.ipa.test) Authenticate with PIN EF85-C42E at
https://github.com/login/device and press ENTER.
[rafasgj@cs9 ~]$ 
```

And the same process can be used for local login:

```nohighlight
cs9 login: rafasgj
Authenticate with PIN F1FC-DA8C at
https://github.com/login/device and press ENTER.
Last login: Sat Feb 1 03:28:32 from 192.168.122.1
[rafasgj@cs9 ~]$ 
```

## Automating with ansible-freeipa

The [ansible-freeipa idp module](https://github.com/freeipa/ansible-freeipa/blob/master/README-idp.md) allows a custom creation of the configuration for an external IdP provider. Currently, it is recommended that one of the preset providers (Keycloak, Github, Google, Microsoft Identity, Okta) are used, and, if needed, modified.

As we want to replicate the previous setup, first, let's create the external IdP entry fr Github, but as it poses an issue with the default user identification attribute, we change it from `login` (which may not be unique) to `id` which is guaranteed to be unique over time:

[](/files/freeipa/01-setup-idp.yml){:class="download fa-solid fa-download"}
{% raw %}
```yaml
---
- name: Setup external IdP 
  hosts: ipaserver
  become: false
  gather_facts: false

  tasks:
  - name: Ensure an external provider for Github is available, using 'id' instead of 'login'
    ipaidp:
      ipaadmin_password: SomeADMINpassword
      name: github_idp
      provider: github
      client_id: 481789d5cd3ca6b3f03f
      secret: 979a1511df376e371c407760619148b82a2c4a6d
      idp_user_id: 'id'
```
{% endraw %}

The user configuration should be simple, but as we're not using the Github login anymore, we need to find out the Github user id. Thankfully, Github provides this information in an easyly accessible way (once you can parse JSON data):

[](/files/freeipa/02-configure-user-idp.yml){:class="download fa-solid fa-download"}
{% raw %}
```yaml
---
- name: Ensure a user can use Github as an external IdP
  hosts: ipaserver
  become: false
  gather_facts: false
  vars:
    github_login: rafasgj

  tasks:
  - name: Retrieve Gitbhub user id
    ansible.builtin.uri:
      url: "https://api.github.com/users/{{ github_login }}"
      method: GET
      headers:
        Accept: "application/vnd.github.v3+json"
    register: user_data

  - name: Ensure user exists with IdP configuration
    ipauser:
      ipaadmin_password: SomeADMINpassword
      name: rafasgj
      first: Rafael
      last: Jeffman
      userauthtype: idp
      idp: github_idp
      idp_user_id: "{{ user_data.json.id }}"
```
{% endraw %}

And that's all that is required to replicate the external IdP and user configuration and the user can now log into FreeIPA hosts.

## Wrap Up

Some recomendations can be found on FreeIPA official documentation, some that you should not forget are:
* Administrators must thoroughly check all URLs they add when creating the IdP server
* Users must check that the presented device authorization URL is correct and that the authentication happens over  asecure channel (usually https) with valid certificates.

Automating the few steps to configure the use of external IdP may sound as overkill, but, given the recomendations shown before, ensuring that the configuration is reproducible will aid to security and all the details were polished.

## References

1. [FreeIPA external IdP design document]
2. [FreeIPA IdP API]
3. [ansible-freeipa idp module](https://github.com/freeipa/ansible-freeipa/blob/master/README-idp.md)
4. [ansible-freeipa user module](https://github.com/freeipa/ansible-freeipa/blob/master/README-user.md)
5. [Github - Creating an OAuth application](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app)

<!-- links -->
[FreeIPA]: https://freeipa.org
[ansible]: https://ansible.com
[ansible-freeipa]: https://github.com/freeipa/ansible-freeipa
[red hat]: https://redhat.com
[ansible galaxy]: https://galaxy.ansible.com
[github]: https://github.com
[keycloak]: #
[FreeIPA external IdP design document]: https://freeipa.readthedocs.io/en/latest/designs/external-idp/external-idp.html
[FreeIPA IdP API]:https://freeipa.readthedocs.io/en/latest/designs/external-idp/idp-api.html
<!-- [nice document]: https://www.redhat.com/pt-br/technologies/management/ansible/automate-microsoft-windows-with-ansible -->
