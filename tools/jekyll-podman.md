---
title: Criando sites estáticos com Jekyll e Podman
layout: main
section: Ferramentas
tags:
  - podman
  - jekyll
  - documentação
  - containers
lang: pt
copy: 2024
date: 2024-01-02
abstract: |-
    Ao desenvolver um _site_ estático com o
    [Jekyll](https://jeyllrb.com){:target="\_blank}, um dos
    principais problemas é recriar o ambiente de desenvolvimento
    para testar o site localmente, devido a diferenças de versões
    do [Ruby](https://ruby-lang.org/en){:target="\_blank"}, _gems_
    instaladas, bibliotecas e ambientes de desenvolvimento
    disponíveis. Uma boa alternativa é utilizar _containers_ para
    criar um ambiente semelhante ao do
    [GitHub Pages](https://pages.github.com){:target="\_blank"}
    que permite testar as alterações localmente,
    antes de publicar a página. Neste documento é descrita uma
    forma de facilitar esse processo, de forma que seja repetível,
    mesmo em diferentes ambientes de desenvolvimento, utilizando
    o [podman](https://podman.io){:target="\_blank"} para
    executar os _containers_.
---

Um dos principais problemas ao desenvolver páginas para o
[GitHub Pages](https://pages.github.com){:target="\_blank"}, utilizando
o [Jekyll](https://jekyllrb.com){:target="\_blank"}, é testar as
alterações nas paginas, antes de publicá-las, uma vez que, até hoje, não
existe uma área de "espera" (_staging area_), onde é possível visualizar
as páginas sem publicá-las. Uma solução para esse prbolema é executar um
_container_ com [podman](https://podman.io){:target="\_blank"}, criando,
na máquina de desenvolvimento, um ambiente semelhante ao oferecido pelo
GitHub.

O Jekyll é um sistema de geração de _sites_ estáticos, com suporte a
_blog_, implementado em [Ruby](https://ruby-lang.org/en){:target="\_blank"},
e que permite uma série de customizações com relação a _plugins_ para
modificar o comportamento ou a forma como as páginas são geradas. Os
_plugins_ são _gems_ Ruby, e alguns destes plugins requerem ferramentas
de desenvolvimento local (como o _toolchain_ GCC) para a sua compilação
e instalação.

A diferença de versões de Ruby, ferramentas de desenvolvimento, ou
_gems_ instaladas na máquina de desenvolvimento, dificultam a criação
do ambiente para gerar e testar, localmente, as páginas editadas, apesar
da ferramenta _bundle_, a qual já facilita muito esse processo.

## Utilizando _containers_

Uma forma de obter um ambiente estável e reproduzível, mesmo em
plataformas diferentes, é o uso de _containers_, popularizados a partir
do [Docker](https://docker.com){:target="\_blank"}.

_Containers_ fornecem uma forma de criar um ambiente isolado sobre o
sistema operacional, isolando as camadas de software necessária para um
ambiente específico. Esse isolamento de _container_, permite limitar o
uso de CPU, armazenamento, e memória, além de isolar todo o _stack_ de
software utilizado do sistema hospedeiro.

Definimos o ambiente do _container_ a partir de um arquivo
(**Dockerfile**), onde descrevemos todos os recursos de hardware e
software que serão utilizados. É a partir deste arquivo de descrição
que será criada uma imagem para o _container_.

Toda imagem é, normalmente, criada a partir de uma imagem pré-existente.
Selecionamos a imagem base a partir da diretiva `FROM`. Para criar uma
imagem que nos permita simular o ambiente do GitHub Pages, executando o
Jekyll, utilizamos uma imagem oficial da liguagem de programação
[Ruby](https://ruby-lang.org/en){:target="\_blank"}.

```Dockerfile
FROM ruby:alpine
```

Precisaremos de um _toolchain GCC_ para compilar alguns módulos (_gem_)
que não são 100% Ruby, e para isso, executamos o comando `apk`, que é o
gerenciador de pacotes do [Alpine Linux](https://alpinelinux.org){:target="\_blank"},
utilizando a diretiva `RUN`.

```Dockerfile
RUN apk add --no-cache make gcc g++ libc-dev openssl-dev
```

Ao executar o _container_ precisamos instalar as _gems_ utilizadas pelo
_site_, e iniciar o servidor do Jekyll. Como esse processo envolve dois
programas em execução, definimos o `ENTRYPOINT` como:

```Dockerfile
ENTRYPOINT ["/bin/sh", "-c", \
    "bundle install && \
     bundle exec jekyll server --trace --host 0.0.0.0" \
]
```

O servidor do Jekyll executa na porta 4000 (TCP), então temos que expor
essa porta do _container_:

```Dockerfile
EXPOSE 4000
```

Ainda precisamos nos preocupar com um ponto muito importante: como o
Jekyll irá acessar o codígo fonte (_Markdown_) do site?

Para isso configuramos um `VOLUME`, que permitirá que um diretório no
_host_ seja compartilhado com o _container_:

```
VOLUME ["/srv/jekyll"]
```

O mapeamento do diretório compartilhado será feito na chamada de
execução do _container_.

Um último problema a ser solucionado é que uma vez criada a imagem,
todas as alterações da imagem feitas pelo `bundle install` são perdidas, 
quando o container termina a execução, e a instalação do _bundle_ deve
ser refeita sempre que o container inicializar, incluindo acessar os
repositórios remotos de código para as _gems_.

Para evitar isso, podemos configuar a imagem para utilizar um diretório
específico para armazenar as _gems_ e todos os plugins utilizados pelo
Jekyll, e associar esse diretório com um diretório do _host_, criando um
_cache_ para os arquivos.

Essa configuração envolve uma série de variáveis de ambiente, que são
definidas com a diretiva `ENV`. 

Abaixo encontra-se o arquivo `Dockerfile` completo para a criação do
_container_:

[](https://raw.githubusercontent.com/rafasgj/rafaeljeffman.com/master/_utils/Dockerfile){:class="download fa-solid fa-download"}
{% raw %}
```Dockerfile
FROM ruby:alpine

RUN apk add --no-cache make gcc g++ libc-dev openssl-dev

VOLUME ["/srv/jekyll"]

EXPOSE 4000

ENV GEM_HOME="/usr/local/bundle"
ENV BUNDLE_PATH=/usr/local/bundle \
    BUNDLE_SILENCE_ROOT_WARNING=1 \
    BUNDLE_APP_CONFIG=/usr/local/bundle
ENV PATH=/usr/local/bundle/bin:/usr/local/bundle/gems/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

RUN mkdir -p "/usr/local/bundle"

WORKDIR "/srv/jekyll"
ENTRYPOINT ["/bin/sh", "-c", \
    "bundle install && \
     bundle exec jekyll server --trace --host 0.0.0.0" \
]
```
{% endraw %}

Agora podemos criar a imagem para o container, e associar a ela um `TAG`
(\_my\_user\_name/site\_server\_):

{% raw %}
```sh
podman build -t "my_user_name/site_server" /path/to/Dockerfile/directory
```
{% endraw %}

Uma vez que a imagem é criada, podemos inicir um _container_, definindo
o diretório com os arquivos fontes do _site_, e o diretório que será
utilizado como _cache_ (lembre-se de criar o diretório antes, caso ele
não exista):

{% raw %}
```sh
podman run \
    --volume "/path/to/website:/srv/jekyll:Z" \
    --volume "/path/to/website/.vendor/bundle:/usr/local/bundle:Z" \
    -p 4000:4000 \
    "my_user_name/site_server"
```
{% endraw %}

Agora, com o _container_ executando, é possivel acessar o _site_ gerado
pelo Jekyll no endereço [http://localhost:4000](http://localhost:4000).

## Configurando os plugins

Agora que temos um ambiente reproduzível, precisamos configurar os
_plugins_ de forma a simular o ambiente do GitHub Pages.

As versões utilizadas pelo GitHub [são públicas](https://pages.github.com/versions/)
e basta que as versões definidas no `Gemfile` limitem as versões das
_gems_ a essas versões disponíveis no Github.

Abaixo, está a contfiguração utilizada nesse _site_, na data que esse
_post_ foi escrito:

[](https://raw.githubusercontent.com/rafasgj/rafaeljeffman.com/master/Gemfile){:class="download fa-solid fa-download"}
{% raw %}
```ruby
source "https://rubygems.org"
gem "jekyll", "~> 3.9.3"
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
end

gem "kramdown", "~> 2.3.2"
gem "kramdown-parser-gfm"
gem "webrick", "~> 1.7"
gem "ffi", "~> 1.15.5"
```
{% endraw %}

## Conclusão

Manter uma configuração para utilizar o Jekyll em diferentes ambientes
e diferentes sistemas operacionais pode ser muito trabalhoso,
principalmente por causa das versões e dependências da linguagem Ruby e
das _gems_ utilizadas pelo Jekyll.

Utilizando _containers_, podemos criar um ambiente que pode ser
reproduzido com certa facilidade, mesmo em sistemas operacionais
diferentes, e mantendo a compatibilidade com o GitHub Pages, de forma a
permitir a visualização das páginas editadas antes da sua publicação.

## Bônus: utilizando um _script_ para iniciar o Jekyll

Na elaboração deste _site_, eu utilizo um _script_ que me permite criar
a imagem do _container_ apenas se necessário, e iniciar o container sem
me preocupar com a configuração necessária na linha de comando,
permitindo que o processo seja apenas copiar o repositório e executar o
_script_.

Abaixo você encontra esse _script_, que foi testado apenas no Linux,
mas deve funcionar em qualquer _shell_ razoavelmente compatível com o
Bash (como o `zsh` do macOS).

Para executar o _script_, basta que ele esteja no mesmo diretório do
_Dockerfile_.

[](https://raw.githubusercontent.com/rafasgj/rafaeljeffman.com/master/_utils/localserver.sh){:class="download fa-solid fa-download"}
{% raw %}
```bash
#!/bin/sh

SCRIPTDIR="$(realpath $(dirname "$0"))"
TOPDIR="$(dirname "${SCRIPTDIR}")"

TAG="$(whoami)/site_server"

[ -d "${TOPDIR}/.vendor/bundle" ] || mkdir -p "${TOPDIR}/.vendor/bundle"


existing=$(podman images -f reference="localhost/${TAG}" --format "{{ .Repository }}")

[ -z "${existing}" ] && podman build -t "${TAG}" "${SCRIPTDIR}"

podman run \
    --volume "${TOPDIR}:/srv/jekyll:Z" \
    --volume "${TOPDIR}/.vendor/bundle:/usr/local/bundle:Z" \
    -p 4000:4000 \
    "${TAG}"
```
{% endraw %}
