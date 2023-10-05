---
layout: main
section: Raspberry-Pi
tags:
  - raspberry-pi
  - installation
title: Instalação do Rasberry Pi OS no Raspberry Pi 4
copy: "2022-2023"
date: 2023-09-13
---

O [Raspberry Pi OS](https://www.raspberrypi.com/software/), antigamente conhecido como "Raspbian" é o sistema operacional "oficial" do Raspberry Pi. É, no momento, o que oferece melhor suporte ao dispositivo. Existem várias formas de instalação, porém eu prefiro a forma manual.

1. Após baixar a [imagem desejada](https://www.raspberrypi.com/software/operating-systems/) (utilizei o Raspberry Pi OS Lite, da versão para todos os modelos), grave a imagem em um cartão SD:
```nohl
# xzcat <image_file> | sudo dd status=progress of='/dev/disk/by-id/my-sd-card'
```

2. Instale o cartão micro-SD no Raspberry Pi. Ligue um teclado e um monitor ao dispositivo e inicialize-o. A finalização da configuração deve ser feita diretamente no Raspberry Pi.
    > Não esqueça de criar um usuário, que será o administrador do sistema, durante a instalação.

3. Após a configuração inicial, configure o WiFi, que utiliza o `wpa_supplicant`. Minha rede (como diversas outras) utiliza WPA-PSK (WPA2) para autenticação e foi necessário adicionar a seguinte configuração ao arquivo `/etc/wpa_supplicant/wpa_supplicant.conf`:
```nohl
    network={
        ssid="MyNetworkSSID"
        scan_ssid=1
        key_mgmt=WPA-PSK
        psk="my_secret_password"
    }
```

4. Com a rede configurada foi possível atualizar os pacotes do sistema:
```nohl
$ sudo apt-get update
$ sudo apt-get dist-upgrade
```

5. A qualquer momento você pode alterar diversas configurações do dispositivo, utilizando o comando `sudo raspi-config`, incluindo quantidade de memória da GPU, overclock, protocolos de comunicação do GPIO (ex. I2C, SPI e UART), entre diversas outras configurações.
    > Eu não gosto muito da interface do `raspi-config`, no entanto é bom encontrar toda a configuração centralizada em um único programa.

6. Caso você tenha esquecido e precise refazer a configuração persistente do teclado, você pode utilizar:
```nohl
$ sudo dpkg-reconfigure keyboard-configuration
```

Uma das vantagens de utilizar a versão _lite_ do Raspberry Pi OS, é que ocupa relativamente pouco espaço no cartão de memória. Com um cartão de 8GB, o sistema inteiro ocupa 1.6GB, deixando 5.2GB disponíveis para uso.

