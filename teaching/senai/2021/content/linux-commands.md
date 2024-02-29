---
layout: main
section: Sistemas Operacionais de Código Aberto
tags:
  - linux
  - shell
  - script
title: Comandos úteis em _scripts shell_
copy: 2022
date: 2022-05-23
---

Estes são comandos úteis na criação de _scripts shell_.

## grep

Procura por uma string dentro de um arquivo.

## find

Procura arquivos em uma estrutura de diretórios, de forma recursiva.

## cut

O comando `cut` imprime partes de linhas de cada arquivo na saída padrão. Por exemplo, `cut -d "," -f 2,5-7` imprime os _campos_ 2, 5, 6 e 7 de um arquivo no formato CSV (_comma separated list_ - list separada por vírgulas).

## echo

O comando echo imprime um texto na tela, que pode conter caracteres especiais.

* `echo -n`
    : não insere uma nova linha ao final do texto.
* `echo -e`
    : habilita a interpretação de caracteres de comando, por exemplo `echo -e "Texto \033[31mvermelho \033[0m e branco."`

# cat e tac

Enviam os dados de um arquivo para a saída padrão. No caso do `tac`, envia os dados invertendo as linhas.

## head

Imprime as primeiras linhas de um arquivo.

## tail

Imprime as últimas linhas de um arquivo.

## tee

Copia os dados da entrada padrão para um arquivo, e os envia para a saída padrão. Por exemplo, `seq 1 100 | tee numeros.txt` irá exibir os números de 1 a 100 na tela e criar um arquivo, `numeros.txt`, contendo os mesmos números de 1 a 100.

## more (ou less)

Exibem o conteúdo de um arquivo, uma página de cada vez.

## mktemp

Cria um arquivo ou um diretório (`-d`) temporários. Por padrão os arquivos ou diretórios criados ficam armazenados no diretório `/tmp`.
