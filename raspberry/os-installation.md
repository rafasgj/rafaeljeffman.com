---
layout: main
section: Raspberry-Pi
tags:
  - raspberry-pi
  - installation
  - Fedora
  - Ubuntu
title: Instalação de um Sistema Operacional no Raspberry Pi 4
copy: 2022
date: 2023-01-31
---

> **Nota**: Tanto a [documentação oficial do Raspberry Pi](https://www.raspberrypi.com/software/), quanto a do Sistema Operacional que você escolheu continua sendo a melhor fonte de informação sobre a instalção do sistema, tente, antes de seguir qualquer coisa dita aqui, utilizar os documentos oficiais.

Instalar um sistema no Raspberry Pi não é difícil, no entanto, algumas operações nem sempre são claras, ou as ferramentas utilizadas não estão disponíveis, ou o sistema que você deseja não é oficialmente suportado.

O objetivo desta página é reunir o mínimo possível de informação que auxilie na instalação de sistemas operacionais no Raspberry Pi 4. Os sistemas escolhidos foram os que eu utilizei, ou utilizo, para testes. Em alguns casos, as instruções servirão para outras versões do Raspberry Pi (além do Raspberry Pi 4, eu também uso algumas versões do 1 e o ZeroW).

A partir do Raspberry Pi 4, é possível inicializar o sistema a partir de um disco externo (USB), como meus objetivos são testes rápidos ou usar o Rasberry Pi com "o menor _footprint_ físico possível", eu faço todas as instalações utilizando um cartão de memória micro-SD.

O uso de um micro-SD como disco de sistema deixa o sistema um pouco mais lento (Raspberry Pi 4) e é uma questão de tempo para que o sistema do arquivo do cartão seja corrompido e ele precise ser recuperado ou reconstruído. Leve isso em consideração ao planejar o uso do Raspberry Pi, incluindo a necessidade de _backup_ de dados, replicação e restauração do sistema.

Outro fato importante para ser levado em consideração é o suporte de hardware que cada distribuiçao oferece. Hoje, o Raspberry Pi OS (baseado no Debian) provê o melhor suporte de hardware, incluindo aceleração gráfica e decodificação de vídeo. Se você vai utilizar com um desktop normal, talvez a melhor opção seja utilizar o Raspberry Pi OS, mas como isso não é o meu caso, eu o utilizo apenas nas versões antigas do Raspberry Pi (1 A, B e B+, 32-bits), que não são suportadas por outras distribuições.

<div class="tag-list">Sistemas testados:</div>

* [Fedora](#fedora)
* [Ubuntu Server](#ubuntu-server)

## Fedora

Há diversas versões do Fedora compatíveis com o Raspberry Pi 4 e os passos aqui descritos foram testados com a versão "_Minimal_" do Fedora 35 e 36.

Embora eu prefire utilizar o Fedora no Raspberry que outras distribuições, a instalação tem uma desvantagem que é a necessidade de um teclado e monitor para configurar a instalação no primeiro _boot_. Ainda não achei uma forma de fazer isso de forma automatizada.

1. Em um computador, grave a [imagem escolhida](https://alt.fedoraproject.org/alt/) no micro-SD:

    ```sh
xzcat <image_file> | sudo dd status=progress of='/dev/disk/by-id/my-sd-card'
    ```

2. Instale o cartão micro-SD no Raspberry Pi. Ligue um teclado e um monitor ao dispositivo e inicialize-o. A finalização da configuração deve ser feita diretamente no Raspberry Pi.

3. No primeiro _boot_, será exibido um menu com opções para configuração do dispositivo, e você deve configurá-lo com suas preferências.

    * Configure a língua que você deseja utilizar (pode ser feito mais parte, junto com o _passo 4.1_, uma vez que a configuração inicial não lhe permite alterar o mapa de teclado).

    * Configure a sua _time zone_.

        * Um servidor NTP vem pré-configurado, e eu recomendo o uso de um, no entanto, pode ser que você precise trocar a _timezone_.

    * Configure a rede **apenas** se você for utilizar rede cabeada, não configure se você for utilizar o WiFi.

        * Mesmo se você não for utilizar rede cabeada, você pode configurar o _hostname_ nesse ponto.

    * A senha de _root_ não precisa ser configurada e/ou usuários não precisam ser criados. Como o meu objetivo é gerenciar os usuários com o [FreeIPA](/projects/freeipa), eu configurei uma senha para o _root_, mas não criei novos usuários, se você for utilizar o dispositivo como um _desktop_, eu recomendo fazer exatamente o contrário.

4. Após a configuração, faça _login_ com um usuário que lhe permita alterar configurações da máquina (_root_ ou _sudoer_).

    1. (Opcional) Nesse ponto eu gosto de configurar o teclado:
    ```sh
localectl set-keymap us-dvorak-alt-intl
    ```

5. (Opcional) Configure o WiFi:

    ```sh
nmcli device wifi list
nmcli device wifi connect <SSID> --ask
    ```

    1. (Optional) To setup a static IP:

    ```sh
nmcli connection modify <SSID> ipv4.method "manual" ipv4.addresses "192.168.15.250/24" ipv4.gateway "192.168.15.1" ipv4.dns "1.1.1.1,8.8.8.8"
    ```

6. Aumente o tamanho da partição de dados e do sistema de arquivos para ocupar todo o espaço disponível no cartão micro-SD:

    ```sh
growpart /dev/mmcblk0 3
resize2fs /dev/mmcblk0p3
    ```

7. Atualize o sistema (esse passo pode demorar vários minutos):

    ```sh
dnf update -y
    ```

A instalação do Fedora 35 exigiu um cartão micro-SD de 8Gb, e após a instalação da versão _Minimal_, devido ao particionamento utilizado por padrão, a partição disponível para uso ("**/**") ficou com um tamanho de _5.7GB_, com _3.7GB_ disponíveis.


## Ubuntu Server

> **_Nota_**: as instruções oficiais para a instalação do Ubuntu utilizam o Raspberry Pi Image Writer, que embora seja muito útil, pode não estar disponível ou exigir a instalação de um pograma extra. Aqui, é utilizado o `dd`, que está disponível em qualquer instalação Linux.

> **_Nota_**: Este processo foi testado com as versões 20.04 e 22.04 do Ubuntu.

A instalação do Ubuntu Server é um pouco mais fácil que a do Fedora, pois toda a configuração inicial pode ser realizada antes do primeiro _boot_ no Raspberry Pi, e não é necessário que o dispositivo seja ligado a um teclado e a um monitor, e, embora os passos aqui são executados manualmente, automatizar o processo de configuração do sistema é bem simples.

1. Em um computador, grave a [imagem](https://ubuntu.com/download/raspberry-pi) no micro-SD:

    ```sh
zcat <image_file> | sudo dd status=progress of='/dev/disk/by-id/my-sd-card'
    ```

2. Monte a partição `system-boot` encontrada no cartão micro-SD.

3. Edite o arquivo `<system-boot>/network-config`, habilitando a rede WiFi.

    ```yaml
    wifis:
      wlan0:
        dhcp4: true
        optional: true
        access-points:
          <my_cool_network_name>:
            password: "1123581321"
    ```

   Se você estiver usando rede por cabo, procure pela seção `ethernets` e a entrada `eth0`.

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
    2. Após a instalação do sistema, a configuração de rede estará disponível no arquivo `/etc/netplan/50-cloud-init.yaml`.

4. Instale o cartão micro-SD no Raspberry Pi. Se você vai utilizar um monitor e um teclado, plugue-os ao Raspberry Pi _antes_ de ligar o dispositivo.

5. A configuração inicial é realizada pela ferramenta `cloud-init`. Se você plugou o Raspberry Pi em um monitor, espere até que algumas mensagens sobre configuração do SSH apareçam no terminal. Caso não esteja utilizando um monitor, a instalação no meu Raspberry Pi 4 com 8Gb de RAM, demorou um pouco menos de 5 minutos.

    Com a instalação terminada, você pode realizar o _login_ no dispositivo com o usuário `ubuntu`. A senha também é `ubuntu`, e a troca de senha será requisitada no primeiro login. Você pode precisar esperar uns minutos para que o usuário seja criado e habilitado. Utilize uma senha "forte", pois este usuário tem permissões de executar comandos com `sudo`.

6. Atualize o sistema (essa operação pode demorar bastante tempo):

    ```sh
sudo apt-get update
sudo apt-get dist-upgrade
    ```
    > Nota: Por algum motivo que não procurei, precisei executar o `update` duas vezes, pois na primeira os repositórios não são atualizados, aparentemente, por um problema de certificado (data).

7. A partir desse ponto, seu sistema está pronto para uso. Embora o site oficial afirme que o sistema possa ser instalado em um cartão de 4GiB, o sistema que instalei ocupa um pouco mais de 4GiB, logo o uso de um cartão de memória maior ou a instalação em um disco externo USB é altamente recomendada.

8. Opcionais:

    * Configuração persistente do teclado:

        ```sh
sudo dpkg-reconfigure keyboard-configuration`
        ```
