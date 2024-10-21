---
title: Raspberry Pi Fully Headless Installation
subtitle: 
layout: main
section: Raspberry-Pi
sections: []
tags: []
lang: en
copy: 2024
date: 2024-10-21
abstract:
    The Raspberry Pi is a nice small device to have hanging around for
    some IoT or low computing server tasks. For these usage having to
    use a keyboard and monitor to setup the device is a hassle, and
    since it will be used without interactive devices, it seems somewhat
    counterintuitive. The goal here is to be able to deploy a working
    device to provide some service, without anything other than a
    network attached to the Raspberry Pi.
---

I've had a bunch of Raspberry Pi devices laying around for some time, and I wanted to put some to work, but I'm too lazy to burn the image to an SD card, attach the raspberry to the only easily accessible display at home (a 55" TV), setup a keyboard on it, turn it on, configure it and deploy, just for the SD card to die in some _not so much_ misterious ways and have to do everything again. Sure, using a better storage (SSD or HDD) could help, but then it adds firmware updates, finding bigger cases, and what not.

I also have a hard time with Internet Ads. I used a bunch of ad blockers over the years, but I have to configure them on all the machines, and that leaves the devices unconfigured (or they are even worse to configure), and that brings us back to the original real issue: I'm lazy.

Having decided that I would block as much ads as possible, with the least amount of work, I decided it was really time to put some Raspberry Pi to work. There are at least two great alternatives to block ads for the whole network by controlling DNS queries. [Pi-Hole](https://pi-hole.net) and [AdGuard Home](https://adguard.com/en/adguard-home/overview.html) allow you to setup a DNS cache on your network that will block queries for known Ad (and phising) sites. The great thing is that you configure either of them once, and all the devices get the same level of protection. Also, both can be executed in a Raspberry Pi. I'd also like to have access to my machines through their names (there's a reason [I choose names for them](https://starwars.fandom.com/wiki/List_of_planets)), and having a proper DNS nameserver would be nice.

As one can imagine, this devices should run alone, hidden from everyone else eyes (or so it is as requested by my significant other). There should not be a big monitor and keyboard right next to the front door.

So there's it is. I have a goal. And having work with automation and deployment for so many years, I didn't want to do the "honey, I have to use the TV screen to setup this console based thingy" anymore. There has to be a way to setup the Pi without ever plugging a monitor to it.

And there is, but there are some things to look for. 

## The OS selection

There is a ton of operating systems that one can use on the Raspberry Pi. There's the official [Raspberry Pi OS](), which shows great support for the hardware, support all known version of de device, and is based on Debian (which is not my go to option). There's is [Fedora](https://fedoraproject.org) with several flavors include the very nice immutable version [designed for IoT workflows](https://fedoraproject.org/iot) (and that is my go to version), but only support the 64-bit boards (_aarch64_). And there are some other fun to play with operatings systems, like [NetBSD](https://wiki.netbsd.org/ports/evbarm/raspberry_pi/) or [Risc OS](https://www.riscosopen.org/content/downloads/raspberry-pi).

As I imagined that even my small network would put some load into this small devices to resolve DNS names (and that I'd like some other services to run on it), I decided to go with some Raspberry Pi 4 with 4Gb of RAM. That would allow me to use the [Fedora IOT](https://fedoraproject.org/iot/), which I was willing to play with for some time.

So we are set, at least for what will be used.


## Pre-boot configuration

When deploying a headless device there are some configuration that should be done before it is turned on for the first time. For example, conecting to a network, allowing remote access, and properly starting up. With the regular [Fedora](https://alt.fedoraproject.org/alt) distribution, this is accomplished, mostly during the first boot, where a set of menu questions are asked and the system is configured based on what you answer.

For the IOT version of Fedora, [the deployment to a physical device](https://docs.fedoraproject.org/en-US/iot/physical-device-setup) can be tweaked to provide some configuration to be available since the first boot. For example, WiFi network for Raspberry Pi is available in the base image, so seting up the network to use allows you to connect to it, even if a cable connection is not to be used (or even available), and it is great that a SSH key can be available since the first boot, so any later configuration can be done through SSH.

To write the OS image to the SD card, we'll use `arm-image-installer`:

```sh
arm-image-installer -y \
   --image="/path/to/Fedora/IoT/image.xz" \
   --media="/dev/sda" \
   --addkey="${HOME}/.ssh/mykey.pub" \
   --norootpass \
   --resizefs \
   --target="rpi4"
```

Upon first boot, Fedora IOT will resize the root partition and deploy the system using [ostree](https://ostreedev.github.io/ostree/). The good thing is that you can use `ostree` tools to configure the device, the bad thing is that you have to learn to use `ostree`. You can also use [Zezere]() to configure the device, but that includes using third party services (third-party for my network, as it's a [Fedora service](https://provision.fedoraproject.org/)). I may do any of this some time, but now, let's just hack into it...

No matter how the operating system is expected to operate, the machine will only run code that is in memory, and code will be loaded from de auxiliary storage to the memory, so whatever will be executed, is somehow on the card that was written. This will allow us to hack some changes before the first boot.

Before plugging the card into the Raspberry Pi, let's mount it on our development machine and look at what's there.

If you examine the SD card that was writen by `arm-image-installer`, you'll see that there's a boot partition (1) and a data partition (3). The boot partition is pretty standard for all Raspberry Pi Oses, it contains, for example, the `config.txt` file. The data partition, contain a directory `/ostree/deploy/fedora-iot` where the data to be deployed to the device is located.

As `ostree` has a special way of dealing with `/etc` will use this to modify the configuration before first boot.

First, let's find where data should be written:

```sh
deployroot=$(dirname "$(realpath "$(find "${1}/ostree/deploy/fedora-iot/" -name "etc" ! -path "*/usr/*")")")
```

To set the hostname, for example, we can:

```sh
echo "${hostname}" > "${deployroot}/etc/hostname"
```

To set a keymap (if you ever want to plug the device into a monitor and keyboard):

```sh
echo "KEYMAP=${keymap}" > "${deployroot}/etc/vconsole.conf"
```

And what helped me the most was to be able to deploy a configuration to enable WiFi since the first boot:

```sh
cp wifi01.nmconnection "${deployroot}/etc/NetworkManager/system-connections/wifi01.nmconnection"
```

And you can set the `wifi01.nmconnection` to something like:

```toml
[connection]
id=wifi01
type=wifi
permissions=
autoconnect=true

[wifi]
mac-address-blacklist=
mode=infrastructure
ssid=<YourWiFiSSID>

[wifi-security]
auth-alg=open
key-mgmt=wpa-psk
psk=<YourUberSecurePassword>

[ipv4]
dns-search=
method=auto

[ipv6]
addr-gen-mode=stable-privacy
dns-search=
method=auto

[proxy]
```

With these steps you can now unmount the SD card, install it on the Raspberry Pi, and turn it on.

If everything went fine, it will boot, configure, possibly reboot, and be ready to be used. It takes up to 20 minutes for the whole process to finish.

Once it's up you can access the device remotely and start playing with it:

```sh
ssh -i "${HOME}/.ssh/mykey" root@${hostname}
```

We have a Raspberry Pi deployed without a monitor and a keyboard. Life's good.


## Replicating and customizing the process

So, it all started with the idea that I have a DNS nameserver on my network, and as we all know if you have one you have none, so I need some redundancy. That is, I need a second machine deployed. Also, we all know how unreliable SD cards are, so even if we have two machines running nameservers, there will be the case that one fails to restart due to a corrupted card.

We need a way to reproduce the steps to deploy the machine, with different hostnames, may be a different configuration, even a different OS, or a different Pi version.

So, what if we could configure the device using a configuration file and runing a script over it?

```yaml`
ssh-key: "ssh-keys/netdevice.pub"
keymap: "us-dvorak-alt-intl"
hostname: "myhost"
domain: "example.com"
timezone: "Americas/Sao_Paulo"
network:
  wifi:
    ssid: "my_network_ssid"
    password: "SomeClearTextPassword"
    hidden: false
```

That's where the problem starts, as Fedora IoT has a much different way of configuring the device than Raspberry Pi OS. Fedora IoT uses OSTree, Raspberry Pi OS relies on the `raspi-config` tool.

Raspberry Pi OS relies on some configuration being available on the `boot` partition:
* A `custom.toml` file where most of the configuration is to be set:

```toml
config_version = 1
[system]
hostname = "${hostname}"
[user]
name = "${USERNAME}"
password = "${USERPASS}"
password_encrypted = false
[ssh]
enabled = true
password_authentication = true
autorized_keys = ["$(cat "${ssh_key}")"]
[wlan]
ssid="${wifi_ssid}"
password="${wifi_password}"
password_encrypted = false
hidden=${wifi_hidden}
country = ""
[locale]
# keymap is not working as needed
# keymap="us"
timezone = "${timezone}"
```

After using that you realize that some of the configuration does not work, like the `keymap` and `user` settings, or using an encrypted WiFi password. You then add a `userconf.txt` file with the user name and an encrypted password, so that the first user is not `pi` with `raspberry` as password (and sudo powers). Finally, to enable `ssh` after the initial configuration, you'll need an empty `ssh` file in the same boot partition. 

To deal with the differences and allow a similar interface for both systems, [burn\_iot](https://github.com/rjeffman/burn_iot) was born.

Creating some pre-configuration, and allowing to setup both the network (cable or WiFi) and a user that can be used to SSH into the device and configure it, enables the deployment of the Raspbery Pi without the need of pluging it into a monitor and a keyboard.

With a script like that, it was also possible to deploy a [NetBSD](https://wiki.netbsd.org/ports/evbarm/raspberry_pi/) system to a Raspberry Pi Model 1B! But in this case, I had no support for the NetBSD filesystem (FFS) so the final configuration still requires the use of a montior and keyboard. 

After the first boot, with the machine acessible through the network, other tools can be used to configure the device, like `Ansible`.

## Wrap Up

And that's it. There's now a [nice script](https://github.com/rjeffman/burn_iot) that I can use to setup a bunch of Raspberry Pi from my workstation, with no interaction with the OS to set it up (kinda, and I'm talking to you NetBSD).

And the ad blocking and DNS stuff? They are here, working, and I'm much happier. I'm also sorry, as this text is already too long, and it's a story for another day, 


## References

* [Raspberry Pi Documentation - config.txt](https://www.raspberrypi.com/documentation/computers/config_txt.html)
* [Fedora Internet of Things - Setting up a Physical Device](https://docs.fedoraproject.org/en-US/iot/physical-device-setup/)
* [Setting up Fedora IoT on Raspberry Pi and rootless Podman containers](https://fedoramagazine.org/setting-up-fedora-iot-on-raspberry-pi-and-rootless-podman-containers)
