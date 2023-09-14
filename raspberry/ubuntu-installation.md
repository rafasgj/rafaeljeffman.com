---
layout: main
section: Raspberry-Pi
tags:
  - raspberry-pi
  - installation
  - Ubuntu
title: Instalação do Ubuntu Server no Raspberry Pi 4
copy: "2022-2023"
date: 2023-02-17
---

> **_Nota_**: as instruções oficiais para a instalação do Ubuntu utilizam o Raspberry Pi Image Writer, que embora seja muito útil, pode não estar disponível ou exigir a instalação de um pograma extra. Aqui, é utilizado o `dd`, que está disponível em qualquer instalação Linux.

> **_Nota_**: Este processo foi testado com as versões 20.04 e 22.04 do Ubuntu.

A instalação do Ubuntu Server é um pouco mais fácil que a do Fedora, pois toda a configuração inicial pode ser realizada antes do primeiro _boot_ no Raspberry Pi, e não é necessário que o dispositivo seja ligado a um teclado e a um monitor, e, embora os passos aqui são executados manualmente, automatizar o processo de configuração do sistema é bem simples.

1. Em um computador, grave a [imagem](https://ubuntu.com/download/raspberry-pi) no micro-SD:
```nohl
$ zcat <image_file> | sudo dd status=progress of='/dev/disk/by-id/my-sd-card'
```

2. Monte a partição `system-boot` encontrada no cartão micro-SD.

3. Edite o arquivo `<system-boot>/network-config`, habilitando a rede WiFi. Se você estiver usando rede por cabo, procure pela seção `ethernets` e a entrada `eth0`. Após a instalação do sistema, a configuração de rede estará disponível no arquivo `/etc/netplan/50-cloud-init.yaml`.

    ```yaml
    wifis:
      wlan0:
        dhcp4: true
        optional: true
        access-points:
          my_cool_network_name:
          password: "1123581321"
```

   1. (Opcional) Caso for utilizar endereços IP estáticos, altere a linha `dhcp4: true` para:
```yaml
        addresses:
          - 192.168.15.250/24
        gateway4: 192.168.15.1
        nameservers:
          addresses:
            - 1.1.1.1
            - 8.8.8.8
```

4. Instale o cartão micro-SD no Raspberry Pi. Se você vai utilizar um monitor e um teclado, plugue-os ao Raspberry Pi _antes_ de ligar o dispositivo.

5. A configuração inicial é realizada pela ferramenta `cloud-init`. Se você plugou o Raspberry Pi em um monitor, espere até que algumas mensagens sobre configuração do SSH apareçam no terminal. Caso não esteja utilizando um monitor, a instalação no meu Raspberry Pi 4 com 8Gb de RAM, demorou um pouco menos de 5 minutos.

    Com a instalação terminada, você pode realizar o _login_ no dispositivo com o usuário `ubuntu`. A senha também é `ubuntu`, e a troca de senha será requisitada no primeiro login. Você pode precisar esperar uns minutos para que o usuário seja criado e habilitado. Utilize uma senha "forte", pois este usuário tem permissões de executar comandos com `sudo`.

6. Atualize o sistema (essa operação pode demorar bastante tempo):

    ```nohl
$ sudo apt-get update
$ sudo apt-get dist-upgrade
    ```
    > Nota: Por algum motivo que não procurei, precisei executar o `update` duas vezes, pois na primeira os repositórios não são atualizados, aparentemente, por um problema de certificado (data).

7. A partir desse ponto, seu sistema está pronto para uso. Embora o site oficial afirme que o sistema possa ser instalado em um cartão de 4GiB, o sistema que instalei ocupa um pouco mais de 4GiB, logo o uso de um cartão de memória maior ou a instalação em um disco externo USB é altamente recomendada.

8. Opcionais:

    * Configuração persistente do teclado:

    ```nohl
    $ sudo dpkg-reconfigure keyboard-configuration
```
