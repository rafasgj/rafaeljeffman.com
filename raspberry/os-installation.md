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
date: 2022-02-14
---

> **Nota**: Tanto a [documentação oficial do Raspberry Pi](https://www.raspberrypi.com/software/), quanto a do Sistema Operacional que você escolheu continua sendo a melhor fonte de informação sobre a instalção do sistema, tente, antes de seguir qualquer coisa dita aqui, utilizar os documentos oficiais.

Instalar um sistema no Raspberry Pi não é difícil, no entanto, algumas operações nem sempre são claras, ou as ferramentas utilizadas não estão disponíveis, ou o sistema que você deseja não é oficialmente suportado.

O objetivo desta página é reunir o mínimo possível de informação que auxilie na instalação de sistemas operacionais no Raspberry Pi 4. Os sistemas escolhidos foram os que eu utilizei, ou utilizo, para testes. Em alguns casos, as instruções servirão para outras versões do Raspberry Pi (além do Raspberry Pi 4, eu também uso algumas versões do 1 e o ZeroW).

<div class="tag-list">Sistemas testados:</div>

* [Ubuntu Server 20.04](#ubuntu-server-2004)
<!-- * [Fedora 35](#fedora-35) -->

## Ubuntu Server 20.04

> **_Problema_**: as instruções oficiais utilizam o Raspberry Pi Image Writer, que embora seja muito útil, pode não estar disponíve ou exigir a instalação de um pograma extar. Aqui, é utilizado o `dd`, que está disponível em qualquer instalação Linux.

1. Em um computador, grave a [imagem](https://ubuntu.com/download/raspberry-pi) no SD:
   ```sh
   zcat | sudo dd status=progress of='/dev/disk/by-id/my-sd-card'
   ```

2. Monte a partição `system-boot` encontrada no cartão SD.

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
        - 192.168.15.23/24
      gateway4: 192.168.15.1
      nameservers:
        addresses:
          - 1.1.1.1
          - 8.8.8.8
      ```

   2. Após a instalação do sistema, a configuração de rede estará disponível no arquivo `/etc/netplan/50-cloud-init.yaml`.

4. Instale o cartão SD no Raspberry Pi. Se você vai utilizar um monitor e um teclado, plugue-os ao Raspberry Pi _antes_ de ligar o dispositivo.

5. A configuração inicial é realizada pela ferramenta `cloud-init`. Se você plugou o Raspberry Pi em um monitor, espere até que algumas mensagens sobre configuração do SSH apareçam no terminal. Caso não esteja utilizando um monitor, a instalação no meu Raspberry Pi 4 com 8Gb de RAM, demorou um pouco menos de 5 minutos.

   Com a instalação terminada, você pode realizar o _login_ no dispositivo com o usuário `ubuntu`. A senha também é `ubuntu`, e a troca de senha será requisitada no primeiro login. Utilize uma senha "forte", pois este usuário tem permissões de executar comandos com `sudo`.

6. Atualize o sistema (essa operação pode demorar bastante tempo):
   ```sh
   sudo apt-get update
   sudo apt-get dist-upgrade
   ```
   > Nota: Por algum motivo que não procurei, precisei executar o `update` duas vezes, pois na primeira os repositórios não são atualizados, aparentemente, por um problema de certificado (data).

7. A partir desse ponto, seu sistema está pronto para uso. Embora o site oficial afirme que o sistema possa ser instalado em um cartão de 4GiB, o sistema que instalei ocupa um pouco mais de 4GiB, logo o uso de um cartão de memória maior ou a instalação em um disco externo USB é altamente recomendada.

8. Opcionais:
   * Configuração persistente do teclado: `sudo dpkg-reconfigure keyboard-configuration`
