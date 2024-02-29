---
layout: main
section: Sistemas Operacionais de Código Aberto
tags:
  - linux
  - network
title: Configuração de servidor HTTPD no Linux
copy: 2022
date: 2022-05-23
---

## Instalação e Configuração

A maioria das distribuições conta com um pacote para instalação do Apache. Utilize o gerenciador de pacotes da sua distribuição para instalar a última versão.

* Fedora: `dnf install httpd`
* Debian: `apt install apache2`

> A configuração e os caminhos dos arquivos apresentados aqui são relativos ao _Debian_, podem existir pequenas diferenças entre as diferentes distribuições na localização dos arquivos, ou nos arquivos de configuração (dependentes da versão do servidor).

Ao instalar o pacote, você pode acessar o exemplo padrão que é intalado junto a partir de um _browser_ apontando-o para `http://localhost` ou utilizando o IP da máquina (VM). Além da instalação da página padrão, são instalados diversos módulos que podem ser ativados, se necessário.

> Note que você precisa utilizar HTTP, e não HTTPS, uma vez que os certificados de criptografia ainda não foram configurados.

O _site_ padrão pode ser encontrado no diretório `/var/www/html`. A localização deste site pode ser alterada modificando a diretiva `DocumentRoot`. No caso do Fedora, essa diretiva é encontrada no arquivo principal de configuração `/etc/apache2/apache2.conf` (`/etc/httpd/conf/httpd.conf`, no Fedora).

Lembre-se que ao alterar a configuração, servidor deve ser reiniciado, ou utilizando `systemctl restart apache2.service` (ou `httpd.service` no Fedora).

## Configurando VirtualHosts

A utilização de _virtual hosts_ permite que diversos _sites_ sejam configurados a partir da mesma instância do servidor HTTP.

A configuração básica de um _virtual host_ contem:

```
<VirtualHost *:80>
    DocumentRoot "/www/example1"
    ServerName www.example.com

    # Other directives here
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined

    # Configure DocumentRoot
    <Directory /www/example1>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>
```

Nesse exemplo temos:

* `<VirtualHost *:80>`

    * O asterisco `*` diz ao servidor que qualquer endereço IP pode conectar a esse _host_.

* `DocumentRoot "/www/example1"`

    * Define a raiz dos documentos do site. Todos os diretórios no caminho devem ter acesso de leitura para o usuário que executa o servidor, normalmente `httpd` ou `www-data`.

* `ServerName www.example.com`

    * Define o `ServerName` do `VirtualHost`.

* Diretiva `Directory`

    * Configura o acesso ao diretório de documentos do _virtual host_.

> Nota: A entrada do novo site deve estar no servidor DNS, caso você esteja testando localmente, adicione essa entrada no arquivo `/etc/hosts`. Deve haver uma entrada para cada novo `VirtualHost`.


## Configurando o módulo PHP

Para utilizar o módulo PHP, você deve ter tanto o PHP quanto o módulo PHP instalados:

* Debian: `apt install php libapache2-mod-php`
* Fedora: `dnf install php php-fpm`

Após a instalação dos pacotes o PHP já estará configurado para executar como um módulo do Apache.

Crie uma página no `DocumentRoot` com o nome `info.php`, e o seguinte conteúdo:

```
<?php phpinfo(); ?>
```

Aceesse o site pelo _browser_ utilizando `http://<endereco>/info.php`. Se a configuração estiver funcionando, você verá diversas informações sobre a instalação do PHP no seu servidor.

## Referências

1. [How To Install Apache on Debian 11](https://itslinuxfoss.com/how-install-apache-debian-11/)
