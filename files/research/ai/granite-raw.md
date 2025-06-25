To deploy FreeIPA using Ansible and the ansible-freeipa role, follow these steps. I assume you have a working Ansible environment with the required dependencies and a target server ready for FreeIPA installation. Here's a step-by-step guide:

1. **Install required packages:**

On your Ansible control node, install the necessary packages:

```bash
sudo apt update
sudo apt install ansible git
```

2. **Clone the ansible-freeipa repository:**

```bash
git clone https://github.com/freeipa/ansible-freeipa.git
cd ansible-freeipa
```

3. **Create an inventory file:**

Create an inventory file (e.g., `inventory.ini`) with your target FreeIPA server:

```ini
[freeipa]
<freeipa_server_ip>  ansible_user=<your_username>  ansible_ssh_private_key_file=<path_to_your_ssh_key>
```

Replace `<freeipa_server_ip>` with the IP address of your target server and `<your_username>` with an appropriate username that has sudo privileges.

4. **Choose a playbook:**

Ansible-freeipa provides several playbooks to simplify the deployment process. You can choose from:

- `site.yml`: For a simple single-server deployment.
- `multi-master.yml`: For a multi-master replication setup.
- `replica.yml`: For setting up a read-only replica.

For this example, let's use the `site.yml` playbook for a single-server deployment.

5. **Run the playbook:**

Execute the playbook using the following command:

```bash
ansible-playbook -i inventory.ini -v -K site.yml
```

- `-i inventory.ini`: Specifies the inventory file.
- `-v`: Enables verbose output for better visibility.
- `-K`: Prompts for the Ansible vault password if required.

6. **Configure FreeIPA:**

During the deployment, you'll be prompted to provide the following information:

- Domain name (e.g., example.com)
- Realm (e.g., EXAMPLE.COM)
- DNS forwarder (optional, can be left blank)
- Admin password

7. **Verify the deployment:**

Once the playbook finishes, you can verify the FreeIPA installation by connecting to the server using the `ipa` command-line tool:

```bash
ipa user-show <admin_username>
```

Replace `<admin_username>` with the admin username you chose during the deployment.

8. **Optional - Configure client machines:**

To join client machines to the FreeIPA domain, you can use the `client.yml` playbook:

```bash
ansible-playbook -i inventory.ini -v -K client.yml
```

This will prompt you for the client's hostname and other relevant details.

That's it! You have successfully deployed FreeIPA using Ansible and the ansible-freeipa role. For more detailed information, refer to the official ansible-freeipa documentation: https://github.com/freeipa/ansible-freeipa

