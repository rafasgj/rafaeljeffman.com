---
layout: main
section: Sistemas Operacionais de Código Aberto
tags:
  - linux
  - network
title: Configuração de Rede no Linux
copy: 2022
date: 2022-05-16
---

## Configurando um IP para uma interface de rede

### `nmcli`

As distribuições voltadas ao segmento _enterprise_, [Red Hat Enterprise Linux], [Ubuntu], [SuSE] e suas variações (Oracle Linux, CentOS, Alma Linux, Rocky Linux, etc), utilizam o programa `nmcli` para configurar as interfaces de rede. O `nmcli` também está disponível nas versões voltadas para comunidades, como [Fedora], [Debian] e [openSuSE].

Principais commandos do `nmcli`:

* `nmcli device status`

    Mostra o _status dos dispositivos de rede disponíveis.

* `nmcli device connect <ifname>`

    Conecta a interface _ifname_.

* `nmcli device reapply <ifname>`

    Aplica a configuração atual à inteface _ifname_.

* `nmcli device modify ([+|-]<setting>.<property> <value>)+`

    Altera uma propriedade da interface de rede, por exemplo:
    * `nmcli dev mod em1 ipv4.method manual ipv4.addr "192.168.1.2/24, 10.10.1.5/8"`
    * `nmcli dev mod em1 -ipv6.addr "abbe::cafe/56"``

* `nmcli connection show`

    Mostra todos os perfis de conexões disponíveis.

* `nmcli connection show <connection>`

    Mostra a configuração do perfil de conexão.

* `nmcli connection add`

    Adiciona um valor a uma propriedade da conexão.

* `nmcli connection modify`

    Altera o valor de uma propriedade da conexão

* `nmcli connectionedit <conncetion>`

    Inicia o _shell_ do `nmcli` para a edição de uma conexão. Utilize o comando `help` para ver os comandos disponíveis. Utilize o comando `save` para salvar as alterações. Utilize o comando `quit` para sair do _shell_.

* `nmcli connection delete <connection>`

    Exclui o perfil de conexão.

* `nmcli device wifi`

    Opções de configuração de redes WiFi.


As configurações são armazenadas em diferentes arquivos, que dependem dos plugins disponíveis para o Networ Manager. Para ver em quais arquivos as configurações estão sendo armazendasa, utilize o comando `nmcli -f NAME,DEVICE,FILENAME connection show`


### Ubuntu pré-22.04

As versões do Ubuntu anteriores à versão LTS 2022.04 utilizavam diversos meios para a configuração de rede. Na versão LTS 20.04, por exemplo, era utilizado o `netplan`.


### Debian

O [Debian] utiliza diversos formatos de configuração de rede, dependendo dos pacotes instalados no seu sistema e da forma como você o configurou para funcionar. Em diferentes versões do Debian, diferentes formatos de configuração estão disponíveis.

## Configurando a rota de uma interface de rede

## O comando `ip`

O comando `ip` é uma espécie de canivete suíco para configuração de interfaces de rede no Linux. Com ele podemos gerenciar _links_, endereços, rotas, tuneis, regras de roteamento, e executar diversas outras ações relacionadas às interfaces de rede e o protocolo IP.

* Para gerenciar os endereços IP: `ip addr {show | add | del} [dev <ifname>]`
* Para gerenciar as rotas: `ip route {show | add | del} [dev <ifname>] [<ROUTE>]`


## Depurar uma conexão de rede

### tcpdump

O [tcpdump] é um analisador de pacotes de rede que funciona em linha de comando.

Veja mais em [https://e-tinet.com/linux/tcpdump](https://e-tinet.com/linux/tcpdump)

### Wireshark

O [Wireshark] é um analisador de protocolos de rede, permitindo que você tenha uma visão em nível microscópico do que está acontecendo na sua rede.


## Configurando o _hostname_

Toda estação Linux possui um _nome_, que, idealmente, é único dentro de um _domínio_.

Quando acessamos um servidor, utilizando um _browser_, o primeiro campo da URL é o nome dessa máquina, junto ao seu domínio, chamamos esse nome de _FQDN - Fully Qualified Domain Name_. Por exemplo, uma máquina cujo nome é **www**, que está no domínio **google.com**, teria o FQDN **www.google.com**.

O comando `hostname` nos permite obter o hostname da máquina, seu domínio, seu FQDN, entre outras informações. Embora seja possível trocar o hostname utilizando esse comando, o ideal é que ele seja utilizado apenas para obter informações, e não alterar essas informações.

Para alterar o hostname da máquina (e o domínio) é melhor utilizar o comando `hostnamectl`.


## Referências

* **nmcli** - [página do projeto](https://developer-old.gnome.org/NetworkManager/stable/mcli.html)
* [**nmcli WiFi Tutorial**](https://fedingo.com/how-to-connect-to-wifi-using-nmcli/)

<!-- links -->
[Red Hat Enterprise Linux]: https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux
[Ubuntu]: https://ubuntu.com
[Debian]: https://debian.org
[wireshark]: https://www.wireshark.org
[tcpdump]: https://www.tcpdump.org
[SuSE]: https://www.suse.com
[openSuSE]: https://www.opensuse.org
[Fedora]: https://getfedora.org
