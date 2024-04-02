---
section: Paradigmas de Programação
title: Estruturas de Dados em C
subtitle:
layout: lecture
last_occurrence: 2024-01-02
copy: 2024
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2024/paradigmas
---

## _Arrays_ Dinâmicos

* Estrutura de Dados: [Vetor](https://pt.wikipedia.org/wiki/Arranjo_(computa%C3%A7%C3%A3o))
* [Implementação de um _array_ dinâmico para o armazenamento de números inteiros](https://github.com/rafasgj/paradigmas-t0/blob/main/src/intarray.c) ([_header file_](https://github.com/rafasgj/paradigmas-t0/blob/main/src/intarray.h))

## Filas

* Estrutura de Dados: [Fila](https://pt.wikipedia.org/wiki/FIFO)
* Estrutura do tipo _First In, First Out_
* Operações: _enqueue_, _dequeue_, _peek_, _is\_empty_
* Operações em listas duplas: _enqueue\_front_, _enqueue\_back_, _dequeue\_front_, _dequeue\_back_, _peek\_front_, _peek\_back_, _is_empty_


## Pilhas

* Estrutura de Dados: [Pilhas](https://pt.wikipedia.org/wiki/LIFO)
* Estrutura do tipo _Last In, First Out_
* Operações: _push_, _pop_, _peek_, _is\_empty_

## Listas Encadeadas

* Estrutura de Dados:
    * [Lista Encadeada](https://pt.wikipedia.org/wiki/Lista)
    * [Lista Duplamente Encadeada](https://pt.wikipedia.org/wiki/Lista_duplamente_ligada)
* Tem custo de inserção constante e acesso randômico linear.
* Em geral, a estrutura da lista é algo como:

```c
typedef struct list_node_int {
    int value;
    struct list_node_int *next;
} ListNodeInt;

typedef struct {
    ListNodeInt *head;
    ListNodeInt *tail;
    int size;
} ListaInt;
```

## Primeiro Trabalho

## Preparação para a próxima aula

* [Lógica Proposicional](https://pt.wikipedia.org/wiki/L%C3%B3gica_proposicional)
* [An Introduction to Prolog](https://link.springer.com/content/pdf/bbm:978-3-642-41464-0/1.pdf)
* [SWISH](https://swish.swi-prolog.org) - SWI-Prolog Shell on the Web
* [Facts, Rules and Queries](http://www.cs.trincoll.edu/~ram/cpsc352/notes/prolog/factsrules.html)

## Recursos para essa aula

### Bibliografia

* MIZRAHI, Victorine Viviane. **Treinamento em Linguagem C**. 2<sup>a</sup> Edição. Pearson Prentice Hall. São Paulo. 2008.
    * Contém implementação de uma lista encadeada no capítulo sobre ponteiros.
