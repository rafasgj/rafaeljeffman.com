---
section: Compiladores
title: Criação de uma gramática livre de contexto para uma linguagem
subtitle:
layout: lecture
last_occurrence: "2024-1"
copy: 2024
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2024/compiladores
---

## Objetivo

Praticar a especificação de uma linguagem de programação utilizando a notação _Bacuks-Naur Form_ (BNF).

## Instruções

Escrever uma gramática, utilizando a notação BNF, capaz de gerar os programas exemplo apresentandos aqui. Os programas utilizam uma versão simplificada da linguagem **LOGO**.

### Exemplo 1 - Hello World

```
hello = "Hello World\n"
PRINT :hello
```

### Exemplo 2 - Calcula a área e a circunferência do círculo

```
pi = 3.141592
PRINT "Ray: "
TYPEIN ray
PRINT "Circunference: " 2*:pi*:ray "\n"
PRINT "Area: " :pi*:ray^2 "\n"
```

### Exmple 3 - _Guess Game_

```
chances = 0
secret = RANDOM + 1
guess = -1

PRINT "Guess a number between 1 and 10\n"
while :guess <> :secret and :chances < 3
    chances += 1
    PRINT "Try #" :chances ". What is you guess? "
    TYPEIN guess
    if :guess > :secret then
      PRINT "The number is smaller.\n"
   end
   if :guess < :secret then
      PRINT "The number is higher.\n"
   end
end

if :guess == :secret then
   PRINT "You win\n"
else
   PRINT "Sorry... try again.\n"
end

PRINT "The number was " :secret "\n"
```

## Entrega do trabalho

Colar a gramática resultante, utilizando a notação BNF, no campo de resposta do LEX.

A data máxima de entrega é dia **13 de julho de 2024**.

## Referências

* [Backus-Naur Form](https://pt.wikipedia.org/wiki/Formalismo_de_Backus-Naur)
