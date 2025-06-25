---
layout: main
section: Raspberry-Pi
tags:
  - raspberry-pi
  - installation
  - Fedora
title: Instalação do Fedora no Raspberry Pi 4
copy: "2022-2023"
date: 2023-09-27
---

> **Nota**: Tanto a [documentação oficial do Raspberry Pi](https://www.raspberrypi.com/software/), quanto a do Sistema Operacional que você escolheu continua sendo a melhor fonte de informação sobre a instalação do sistema, tente, antes de seguir qualquer coisa dita aqui, utilizar os documentos oficiais.

Desde o Fedora 37, o Raspberry Pi é uma plataforma oficialmente suportada, incluindo aceleração de hardware para vídeo.  Versões anteriores do Fedora, apesar de não oficialmente suportadas, também funcionavam com o Raspberry Pi 4. Os passos aqui descritos foram testados com a versão "_Minimal_" do Fedora da 35 até a 42, e com a versão "_Server_" do Fedora 38.

Embora eu prefira utilizar o Fedora no Raspberry que outras distribuições, a instalação tem uma desvantagem que é a necessidade de um teclado e monitor para configurar a instalação no primeiro _boot_. Até o momento não achei uma forma de fazer isso de forma automatizada.

Você irá precisar de uma imagem para a plataforma ARM `aarch64` para instalar o Fedora no Raspberry Pi 4. Você pode encontrar essas imagens na página de [Arquiteturas Alternativas](https://alt.fedoraproject.org/alt/), no [Fedora Workstation](https://fedoraproject.org/workstation/download/) ou no [Fedora Server](https://fedoraproject.org/server/download/). Recomendo que utilize uma imagem `Raw`.

1. Em um computador, grave a imagem escolhida no micro-SD:

    ```sh
$ xzcat <image_file> | sudo dd status=progress bs=1M of='/dev/disk/by-id/my-sd-card'
    ```

    É recomendado o uso de um cartão de 16GB para a imagem, e o mínimo é um cartão de 8GB. Para utilizar um cartão de 8GB é necessário o uso do parâmetro `bs=1M`. Não investiguei, mas a gravação sem esse parâmetro falha para cartões menores que 16GB.

2. Instale o cartão micro-SD no Raspberry Pi. Ligue um teclado e um monitor ao dispositivo e inicialize-o. A finalização da configuração deve ser feita diretamente no Raspberry Pi.

3. No primeiro _boot_, será exibido um menu com opções para configuração do dispositivo, e você deve configurá-lo com suas preferências.

    * Configure a língua que você deseja utilizar.

    * Configure a sua _time zone_.
    : Um servidor NTP vem pré-configurado, e eu recomendo o uso de um, no entanto, pode ser que você precise trocar a _timezone_.

    * Configure a rede **apenas** se você for utilizar rede cabeada, não configure se você for utilizar o WiFi.
    :  Mesmo se você não for utilizar rede cabeada, você pode configurar o _hostname_ nesse ponto.

    * A senha de _root_ não precisa ser configurada e/ou usuários não precisam ser criados.
    :  Como o meu objetivo é gerenciar os usuários com o [FreeIPA](/projects/freeipa), eu configurei uma senha para o _root_, mas não criei novos usuários, se você for utilizar o dispositivo como um _desktop_, eu recomendo fazer o oposto e criar um usuário com permissões de administrador.

4. Após a configuração, faça o _login_ com um usuário que lhe permita alterar configurações da máquina (_root_ ou o usuário com poder de administrador criado na instalação).

5. (Opcional) Nesse ponto eu gosto de configurar o teclado:
```nohl
# localectl set-keymap us-dvorak-alt-intl
```

6. (Opcional) Configure o WiFi:
```nohl
# nmcli device wifi list
# nmcli device wifi connect --ask <SSID>
```
    Caso o SSID seja ocultado pelo roteador, utilize:
```nohl
# nmcli device wifi connect --ask <SSID> \
    name <SSID> hidden yes
```
    > Pode ser necessário executar o comando de conexão para a rede oculta mais de uma vez.

7. (Opcional) Para configurar um IPv4 estático utilize:
```nohl
# nmcli connection modify <nome_da_conexão> \
    ipv4.method "manual" \
    ipv4.addresses "192.168.123.250/24" \
    ipv4.gateway "192.168.123.1" \
    ipv4.dns "8.8.8.8,1.1.1.1"
```

8. Aumente o tamanho da partição de dados e do sistema de arquivos para ocupar todo o espaço disponível no cartão micro-SD
    : Garanta que os utilitários necessários estão istalados:
```nohl
# dnf install -y cloud-utils-growpart
```
    : Para o Fedora Server:
```nohl
# growpart /dev/mmcblk0 3
# pvresize /dev/mmcblk0p3
# lvextend /dev/mapper/fedora-root \
    -l+100%FREE
# xfs_growfs /dev/mapper/fedora-root
```
    : Para o Fedora Minimal
```nohl
# growpart /dev/mmcblk0 3
# resize2fs /dev/mmcblk0p3
```
    > Utilize os comandos `fdisk -l` e `mount` para descobrir as partições e dispositivos corretos.

9. Atualize o sistema (esse passo pode demorar vários minutos):
```nohl
# dnf update -y
```

A instalação do Fedora ocupa em torno de 2.2GB (versão _Minimal_) e 3GB (versão _Server_) após a configuração e atualização. Outros 3GB são utilizados para partições do sistema. Com o cartão mínimo de 8GB, após a instalação e configuração, resta cerca de 2GB livres para uso.

