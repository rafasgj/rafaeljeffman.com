---
title: "Utilizando MongoDB com o Podman"
layout: main
section: Bancos de Dados
tags:
  - MongoDB
  - NoSQL
  - container
  - desenvolvimento
  - bancos de dados
  - big data
copy: 2023
date: 2023-09-21
abstract: |-
    MongoDB é um dos bancos de dados orientados a documentos mais
    utilizados no mercado. No entanto, como possui uma licença
    proprietária (desde 2018), as distribuições Linux removeram o
    banco de dados de sua lista de pacotes, porém, é possível
    utilizar o MongoDB a partir de imagens de _container_, como
    demonstrado aqui, em um exemplo que utiliza a importação de
    dados a partir de arquivos CSV como demontração do ambiente.
---

O MongoDB utiliza uma licença proprietária (SSPL), ou seja, uma licença que não é livre e não é compatível com licenças _open source_ comuns com GPL, Apache ou BSD, e, por esse motivos, foi removido das distribuições Linux. Como alternativa, para poder desenvolver utilizando o MongoDB de forma relativamente fácil e repetível, podemos utilizar um _container_ baseado no Docker ou Podman.

Aqui, utilizarei o [`podman`](https://podman.org), pois assim é possível utilizar um usuário sem privilégios. Para usar o `docker` talvez seja necessário, apenas, trocar o comando `podman` por `docker`, uma vez que a ideia do Podman é que ele seja um substituto direto do Docker.

Como a ideia é preparar um ambiente que permita o desenvolvimento utilizando MongoDB, será criado um projeto de importação de dados a partir de um arquivo CSV.

Crie um diretório para o projeto:

```nohl
$ mkdir mongo_test
$ cd mongo_test
```

Quando utilizamos um _container_, ao encerrá-lo os dados do _container_ são perdidos, e, para esse projeto, é interessante que possamos acessar os dados criados mesmo após a exclusão do _container_. Para isso, crie um diretório para armazenar os dados:

```nohl
$ mkdir data
```

Crie um arquivo CSV com os dados a serem importados, por exemplo o arquivo `${PWD}/import/users.csv`:

```nohl
id,first_name,last_name,email,gender
1,Annamarie,Sexten,asexten0@admin.ch,Genderqueer
2,Bartholomew,Summerson,bsummerson1@sina.com.cn,Male
3,Lalo,Dumbelton,ldumbelton2@friendfeed.com,Male
4,Clayborne,Tincknell,ctincknell3@google.fr,Male
5,Paula,Oley,poley4@soundcloud.com,Female
6,Alexandr,Burkert,aburkert5@com.com,Genderfluid
7,Temple,Breens,tbreens6@technorati.com,Male
8,Vance,Gallifont,vgallifont7@theguardian.com,Male
9,Koenraad,Weavill,kweavill8@foxnews.com,Male
```

Para inicializar o _container_, utilize:

```nohl
$ podman run --name mongo-container \
    --volume "${PWD}/data:/data/db:Z" \
    -dt \
    docker.io/library/mongo:latest
```

Ao executarmos o comando `run` do podman, um _container_ será criado com o nome fornecido em `--name`, utilizando a imagem especificada (`docker.io/library/mongo:lates` no exemplo). O uso do argumento `-d` em conjunto com o argumento `-t` permite que o _container_ continue executando em _background_ após a sua criação e inicialização. Sem isso, o _container_ irá encerrar e parar a execução.  

O parâmetro `--volume` é muito importante pois permite utilizar a mesma base de dados caso o _container_ precise ser recriado novamente. Para apagar a base de dados, basta apagar o diretório `data`, recriá-lo, e executar os passos de importação dos dados novamente.

Para importar os dados, utilize:

```nohl
$ podman exec -i mongo-container \
    mongoimport \
        --db=Company \
        --collection=Users \
        --drop \
        --mode=insert \
        --type=csv \
        --headerline < "${PWD}/import/users.csv"
```

O argumento `-i` permite que o `podman` redirecione os dados recebidos via `stdin` para o comando sendo executado no _container_. Os dados estão sendo lidos do arquivo criado anteriormente. No lado do `mongoimport`, os parâmetros são:
* --db=Company
: Utiliza a base de dados `Users`
* --collection=Users
: Utiliza a coleção `Users`
* --drop
: Apaga a coleção caso ela exista
* --mode=insert
: Insere os documentos na base
* --type=csv
: Define o formato dos dados a serem importados (por exemplo, `csv` ou `json`)
* --headerline
: Trata a primeira linha dos dados como a descrição dos campos.

> Note que, nesse exemplo, o arquivo contém a lista de campos na primeira linha. Caso o arquivo CSV não tenha a definição dos campos, utilize o parâmetro `--fields`, passando o nome dos campos, por exemplo `--fields id,first_name,last_name,email,gender`.

Com os dados disponíveis, podemos utilizar o `mongosh` para manipulá-los:

```nohl
$ podman exec -it \
    mongo-container \
    mongosh
```

Podemos também consultá-los com uma única linha de comando:

```nohl
$ podman exec -i mongo-container \
    mongosh Company <<< 'db.Users.find({gender:{$ne: "Male"}})'
```

Nesse caso, passamos o _endereço_ do banco de dados (no exemplo utilizado `Company` em `localhost`), e utilizamos o redirecionamento de texto (`<<<`) para executar uma consulta na coleção `Users`.

Para esse exemplo a saída seria:

```yaml
Company> [
  {
    _id: ObjectId("650cfe6b52dd9225bf9f635b"),
    id: 1,
    first_name: 'Annamarie',
    last_name: 'Sexten',
    email: 'asexten0@admin.ch',
    gender: 'Genderqueer'
  },
  {
    _id: ObjectId("650cfe6b52dd9225bf9f6362"),
    id: 6,
    first_name: 'Alexandr',
    last_name: 'Burkert',
    email: 'aburkert5@com.com',
    gender: 'Genderfluid'
  },
  {
    _id: ObjectId("650cfe6b52dd9225bf9f6363"),
    id: 5,
    first_name: 'Paula',
    last_name: 'Oley',
    email: 'poley4@soundcloud.com',
    gender: 'Female'
  }
]
```

Apesar da ausência dos pacotes do MongoDB nas atuais distribuições Linux, utilizá-lo de forma local continua sendo bastante simples com o uso de `containers`, com a vantagem que fica muito mais fácil de recriar o ambiente de desenvolvimento num ambiente de testes, o recriar um ambiente semelhante ao de produção para o desenvolvimento.

## Recursos Extras

* [Running MongoDB with Podman](https://mehmetozanguven.com/run-mongodb-with-podman/)
* [MongoDB Shell](https://www.mongodb.com/docs/mongodb-shell/)(mongosh)
* [mongoimport](https://www.mongodb.com/docs/database-tools/mongoimport/)
* [MongoDB Tutorial](https://www.w3schools.com/mongodb/) (W3Schools)
* [MongoDB Manual](https://www.mongodb.com/docs/manual/)
* [Import a CSV File into MongoDB with mongoimport](https://database.guide/import-a-csv-file-into-mongodb-with-mongoimport/)
* [podman-exec](https://docs.podman.io/en/latest/markdown/podman-exec.1.html)
* [mongo](https://hub.docker.com/_/mongo/) (Imagem oficial Docker)
