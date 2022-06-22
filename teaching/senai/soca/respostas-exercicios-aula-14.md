---
layout: main
section: Sistemas Operacionais de Código Aberto
tags:
  - SENAI
  - exercícios
  - respostas
title: Respostas aos exercícios da aula 14
copy: 2022
date: 2022-06-22
---

## Exercício 1

> Em uma Pet Shop, os animais são separados por turnos para os banhos, de forma que os animais maiores não se misturem com os animais menores.
Crie um script que receba como entrada o peso do animal e imprima o horário que o animal pode ter o banho agendado:
* Até 8Kg: 8:30 - 10:00h
* Até 14Kg: 10:30 - 14:00h
* Ate 20Kg: 14:30h - 16:00h
* Acima de 20Kg: 16:30h - 18:00h

Neste exercício é necessário obter como entrada o peso do animal. Esta entrada pode ser feita com o comando `read`, ou utilizando um parâmetro de linha de comando (`${1}`).

De posse do peso do cachorro, podemos utiliza `if` para imprimir o horário de atendimento:
```bash
if [ $peso -lt 8 ]
then
  echo "8:30h - 10:00h"
  exit
fi

if [ $peso -lt 14 ]
then
  echo "10:30h - 14:00h"
  exit
fi

# e assim por diante.
```


## Exercício 2

> Crie um script que simule o login do usuário, perguntando seu nome de usuário e senha. Caso a senha seja válida, o programa escreve “ACESSO LIBERADO” e termina sem erro, caso a senha seja inválida, o programa permite que o usuário tente novamente, até um máximo de 3 tentativas.
Caso a senha correta não seja utilizada, o programa termina com a mensagem “ACESSO NEGADO”, e retorna um código de erro.


No segundo exercício precisamos de um _loop_ permitindo 3 tentativas, e loop exterior para permitir que o usuário tente novamente após um tempo.

```bash
#!/bin/sh

EX_USER="usuario"
EX_PASSWORD="password"

while true
do
  for _ in $(seq 3)
  do
    read -p "login:" USER
    read -p "senha:" -s PASSWORD
    if [ "${USER}" == "${EX_USER}" ] && [ "${PASSWORD}" == "${EX_PASSWORD}" ]
    then
      echo "ACESSO LIBERADO"
      exit
    else
      echo "ACESSO NEGADO"
      echo
    fi
  done
  sleep 15
done
```


## Exercício 3

>Crie um script que imprima na tela o hostname e o endereço IP da máquina:
```
minha.maquina: 192.168.10.123
```

Para esse exercício você pode utilizar os comandos `grep` ou `cut` associados ao comando `ip` para obter o endereço IP da máquina, ou utilizar apenas o comando `hostname`, tanto para obter o nome da máquina quanto o endereço IP.
