---
layout: main
section: Shell Script
tags:
  - linux
  - shell script
  - bash
title: Argumentos de linha de comando
copy: 2022
date: 2022-06-12
---

Quase todos os programas com interface por linha de comando oferecem uma série de parâmetros que permitem modificar o comportamento do programa. Esses argumentos podem ser opções selecionáveis ou parâmetros posicionais.

Por exemplo, o comando `ls` oferece opções como:
* `-1`: lista um arquivo por linha
* `-t`: ordena os arquivos pelo horário de criação
* `-S`: ordena os arquivos por tamanho
* `-a`: mostra todos os arquivos, inclindo os que começãm por `.`
* `-l`: usa um formato de listagem longa

As opções podem exigir que valores sejam fornecidos, como a opção `-w` do `ls`, que exige o número de colunas que terá a saída do comando (ex.: `ls -w 40`, onde a saída do `ls` terá, no máximo, 40 colunas).

Além das opções, podemos passar parâmetros posicionais. No caso do `ls` esses parâmetros são os padrões para selecionar arquivos, por exemplo, `ls a* c*`.

## Parâmetros Posicionais

Podemos acessar os parâmetros posicionais utilizando `$<NUM>`. O primeiro parâmetro posicional é o `${1}`, o segundo parâmero é o `${2}`, e assim por diante. Note que você pode acessar o parâmetro sem o uso de _chaves_, por exemplo `$3`, no entanto, ao não utilizar as chaves você só poderá acessar até o nono parâmetro posicional.

Podemos utilizar qualquer tipo de substituição permitido pelo _shell_ ao acessar os parâmetros posicionais. Por exemplo, um programa que aceita um parâmetro posicional que se não utilizado assume um valor padrão, utilizaria `${1:-DEFAULT}` para obter o valor do primeiro argumento.

O exemplo abaixo mostra um exemplo disso:

```sh
#!/bin/sh

echo "Olá, ${1:-Mundo}!"
```

Acho executar esse _script_ apenas com `script`, o resultado será `Olá, Mundo!`, se passarmos um argumento posicionar, por exemplo `script John`, o _script_ utilizará o valor passado (no exemplo, `Olá, John!`).

O número de parâmetros posicionais pode ser obtido utilizando `$#` e a lista de parâmetros pode ser obtida com `$@`.

O parâmetro `${0}`, representa o comando utilizado para executar o _script_. Se o _script_ for executado como `./script.sh param1`, o valor de `$0` será `./script.sh`, se for executado como `/home/usuario/bin/script.sh param1`, o valor será `/home/usuario/bin/script.sh`, se for executado como `bash script.sh`, o valor será `script.sh`. Em resumo, o valor de `${0}` mostra o caminho utilizado para a execução do _script_.

### Processando um parâmetro por vez

Quando temos uma lista de parâmetros posicionais de tamanho indeterminado, por exemplo, no caso de uso do _script_ ser `usage: script FILE...`, podemos processar os argumentos, enquanto eles existirem.

```sh
while [ -n "${1}" ]
do
    echo "${1}"
    shift 1
done
```

O comando `shift` remove elementos da lista de parâmetros posicionais.

Com o código abaixo, poderiamos processar pares de parâmetors em um _script_ do tipo `usage: script CHAVE VALOR ...`

```sh
# verifica se o número de parâmetros é par.
if [ $(($# % 2)) -ne 0 ]
then
    echo "É necessário um número par de parâmetros."
    exit 1
fi

while [ -n "${1}" ]
do
    echo "CHAVE: ${1}    VALOR: ${2}"
    shift 2
done
```

## Parâmetros como "Opções"

Todos os parâmetros de um _script shell_ são posicionais, porêm, podemos alterar o processamento desses parâmetors para tratar os parâmetros posicionais como _opções_.

O comando `getopts OPTSTRING VAR` pode ser utilizado para processar opções a partir dos parâmetros posicionais do script.

Quando executado, o `getopts` coloca o _nome_ da opção em `VAR`, e se ela recebe um argumento, o valor do argumento pode ser acessado com `${OPTARG}`.

A opções válidas são definidas em `OPTSTRING`, por exemplo `getopts "abc" OPT` aceita as opções `-a`, `-b` e `-c`, e irá atribuir a opção encontrada a variável `OPT`. Para que uma opção aceite um valor como argumento, utilizamos `:`, como em `getopts "a:bc" OPT`, que aceita as opções `-a ARG`, `-b` e `-c`.

A variável `OPTIND` é inicializada com `1`, e esse valor é incrementado a cada novo argumento analisado. Podemos mesclar opções e parâmetros posicionais, utilizando `shift` e `OPTIND`.

Veja um exemplo:

```sh
#!/bin/sh

while getopts "a:bc" OPT
do
    case "${OPT}" in
        a) echo "Argumento: ${OPTARG}" ;;
        b | c) echo "Flag: ${OPT}" ;;
    esac
done

shift $((OPTIND - 1))

echo "Parâmetros posicionais: ${@}"
```

> Experimente executar esse _script_ utilizando `dash t.sh -a AAA -b -c -b file file`.

## Exemplo de uso do `getopts`

Neste exemplo, são mostradas algumas técnicas de aplicação do `getopts` para o processamento de argumentos de linha de comando, incluindo o uso dos parâmetros como um _array_ de elementos, o que requer o uso de uma versão um pouco mais recente do _bash_.

O uso de _arrays_ não está disponível em alguns _shells_ POSIX, como o `dash`, que é o _shell_ padrão de algumas distribuições Linux, por exemplo, o Debian. Nesses casos, para o uso de _arrays_, é necessário instalar o _bash_ e forçar seu uso a partir da definição do interpretador do _script_ (`hashbang`/"`#!`").

[](/teaching/code/shellscript/getopts_example.sh){:class="download fa fa-download"}
```bash
#!/bin/bash

# Program: parameters.sh

usage() {
    cat<<EOF
usage: parameters.sh [-h] [-i VALOR] [-v|-vv|-vvv] POSICIONAL...

Opções:

    -i VALOR      Uma opção que aceita um valor como parâmetro.
    -v            Uma opção que aceita contagem de vezes que aparece.
    -h            Uma opção que pode ou não ser utilizado.

    POSICIONAL    Parâmetros posicionais.
EOF
}

VERBOSE=0
FLAG=0
unset VALUE

while getopts "hi:fv" OPT
do
    case "${OPT}" in
        h) usage && exit 0  ;;
        f) FLAG=1 ;;
        i) VALUE="${OPTARG}" ;;
        v) VERBOSE=$((VERBOSE + 1)) ;;
        *) echo "ERRO: Opção inválida: ${OPT}" && exit 1 ;;
    esac
done

# Usando um "array" com as opções posicionais.
POSICIONAIS=(${@:OPTIND})

echo "Número de parâmetros posicionais: ${#POSICIONAIS[@]}"
echo "Parâmetros: ${POSICIONAIS[@]}"
echo "Primeiro parâmetro: ${POSICIONAIS[0]}"

# usando as opções com ${1}
shift $((OPTIND - 1))
echo "Número de parâmetros posicionais: $#"
echo "Parâmetros: $*"
echo "Primeiro parâmetro: ${1}"

[ -z "${VALUE}" ] && echo "VALUE: (null)" || echo "VALUE: ${VALUE}"
echo "Número de 'v': ${VERBOSE}"
```
