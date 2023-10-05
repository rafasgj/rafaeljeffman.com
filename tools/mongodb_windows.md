---
title: "Utilizando MongoDB no Windows"
layout: main
section: Bancos de Dados
tags:
  - MongoDB
  - NoSQL
  - container
  - desenvolvimento
  - bancos de dados
  - big data
  - Windows
copy: 2023
date: 2023-09-24
abstract: |-
    Instruções de como fazer uma instalação simples do MongoDB,
    um dos bancos de dados orientados a documentos mais utilizados
    no mercado, para testes e desenvolvimento de aplicações no
    Windows, utilizando ferramentas de linha de comando.
---

O [MongoDB](https://mongodb.com){:target="\_blank"} é um dos principais bancos de dados orientados a documentos do mercado, e, apesar de 2018 utilizar uma licença proprietária, até o momento mantém uma versão _community_ que permite o seu uso para desenvolvimento sem custos.

Nesse artigo, mostro como instalar o MongoDB no Windows, e, para testar a instalação, realizar uma importação de dados CSV e executar uma consulta ao banco. Para os testes do procedimento foi utilizado o Windows 11, porém as instruções devem funcionar em qualquer versão a partir do Windows 8.

O primeiro passo é realizar o _download_ do [MongoDB Community Server](mongodb.com/try/download/community'). Foi utilizada a [versão 7.0.1 x86\_64](https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-7.0.1-signed.msi), mas você deve escolher a versão mais recente.

O MongoDB utiliza um sistema de instalação guiada, e você pode utilizar as configurações preestabelecidas, apenas lembre-se de usar a opção de instalação completa.

Após a instalação, o `Compass`, uma ferramenta gráfica para administração do MongoDB irá
iniciar, porém, não vamos utilizá-lo nesse momento. (Se a instalação do `Compass` falhar, você pode ignorar o erro, caso não vá utilizá-lo depois.)

Para verificar se o MongoDB está rodando, utilize o aplicativo `Services` (Serviços) e procure por "MongoDB Server". O _status_ deve ser `Running` (Executando).

O MongoDB não vem com as ferramentas de linha de comando instaladas. Você pode obter [diversas ferramentas de linha de comando](https://mongodb.com/try/download), aqui utilizaremos apenas o [MongoDB Shell](https://mongodb.com/try/download/shell) (foi utilizada a [versão 1.10.6](https://downloads.mongodb.com/compass/mongosh-1.10.6-x64.msi)) e o `mongoimport` que faz part do pacote [MongoDB Database Tools](https://mongodb.com/try/download/database-tools) (foi utilizada a [versão 100.8.0](https://fastdl.mongodb.org/tools/db/mongodb-database-tools-windows-x86_64-100.8.0.msi)).

Todas as ferramentas utilizam instalação guiada, e, ao instalar o `MongoDB Shell`, instale o programa para todos os usuários desmarcando a opção `Install just for you`.

A instalação do `MongoDB Shell` ajusta automaticamente o caminho de procura de ferramentas (`PATH`) dos _prompts_ de linha comando (`CMD` e `PowerShell`) para que o programa possa ser executado, porém as ferramentas do `Mongo Database Tools` não configuram essa variável de ambiente.

No prompt, Adicione o diretório das ferramentas ao `PATH` para poder executá-las:
```nohl
> SETX PATH "%PATH%;C:\Program Files\MongoDB\Tools\100\bin"
```

Ou, como administrador, para todos os usuários:
```nohl
> SETX /M PATH "%PATH%;C:\Program Files\MongoDB\Tools\100\bin"
```

Reinicie o _prompt`_ para que o novo `PATH` tenha efeito (não é preciso reiniciar o computador).

## Testando a importação de dados

Agora, testamos o MongoDB executando um processo de importação de dados. Crie um diretório para o projeto:

```nohl
> mkdir mongodb_test
> cd mondodb_test
```

Crie um aquivo texto `dados.csv` contendo os dados CSV:

```csv
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

Você pode usar o notepad para isso:
```nohl
> notepad data.csv
```

Com o arquivo de dados criado, podemos utilizar o `mongoimport` para importar os dados:

```nohl
> mongoimport \
        --db=Company \
        --collection=Users \
        --drop \
        --mode=insert \
        --type=csv \
        --headerline \
        --file="data.csv"
```

Os parâmetros do `mongoimport` utilizados para a importação dos dados são:
* `--db=Company`
: Utiliza a base de dados `Users`
* `--collection=Users`
: Utiliza a coleção `Users`
* `--drop`
: Apaga a coleção caso ela exista
* `--mode=insert`
: Insere os documentos na base
* `--type=csv`
: Define o formato dos dados a serem importados (por exemplo, `csv` ou `json`)
* `--headerline`
: Trata a primeira linha dos dados como a descrição dos campos.
* `--file="data.csv"`
: Define um arquivo contendo os dados para serem importados.

Para testar a importação dos dados, crie um arquivo `query.js` no mesmo diretório:
```javascript
db = connect("mongodb:Company")
printjson(db.Users.find({gender:{$ne:"Male"}}))
```

Teste a importação dos dados com o `mongosh`, executando o script criado:
```nohl
> mongosh --quiet query.js
```

A saída deverá ser:
```yaml
[
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

A instalação do MongoDB no Windows é relativamente simples, para quem gosta de desenvolver utilizando programas de linha de comando (quem não gosta?) é necessária a execução de alguns passos a mais (em relação ao [uso de um _container_](mongodb_fedora)) para que as ferramentas sejam corretamente instaladas.

