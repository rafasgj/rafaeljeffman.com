---
section: Paradigmas de Programação
title: Exercícios de Revisão
subtitle:
layout: lecture
last_occurrence: 2024-07-02
copy: 2024
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2024/paradigmas
---

## Questão 1

Uma lista pode ser dividida em duas partes: o primeiro elemento (a cabeça da lista) e os demais
elementos (sua cauda). Por exemplo, em uma lista de inteiros `[1, 2, 3, 4]`, a cabeça dessa
lista é o valor inteiro 1, enquanto sua cauda é a lista de inteiros `[2, 3, 4]`. Uma lista vazia é
representada por `[]`.
O código a seguir define duas funções descritas em uma linguagem de programação funcional que
manipulam listas de inteiros. A função enade recebe uma lista de inteiros e produz uma nova lista de
inteiros. A função auxiliar é chamada pela função enade e possui dois parâmetros: um número
inteiro e uma lista de inteiros. Essa função produz uma lista de inteiros.

```haskell
enade :: [Int] -> [Int]
enade [] = []
enade (cabeca:cauda) = auxiliar cabeca (enade cauda)
auxiliar :: Int -> [Int] -> [Int]
auxiliar x [] = [x]
auxiliar x (cabeca:cauda)
| (x `mod` 2 == 0) = x:cabeca:cauda
| otherwise = cabeca:auxiliar x cauda
```

Considerando o código apresentado, é correto afirmar que se a função enade for executada recebendo
como parâmetro de entrada a lista `[1, 2, 3, 4, 5, 6, 7, 8]`, o resultado será

* [].
* [2, 4, 6, 8].
* [1, 2, 3, 4, 5, 6, 7, 8].
* [2, 4, 6, 8, 1, 3, 5, 7].
* [2, 4, 6, 8, 7, 5, 3, 1].
{:class="lettered"}

## Questão 2

_Memory leak_, ou vazamento de memória, é um problema que ocorre em sistemas computacionais
quando uma parte da memória, alocada para uma determinada operação, não é liberada quando se
torna desnecessária. Na linguagem `C`, esse tipo de problema é quase sempre relacionado ao uso
incorreto das funções `malloc()` e `free()`. Esse erro de programação pode levar a falhas no
sistema se a memória for completamente consumida.

A partir dessas informações, assinale a opção que apresenta um caminho de execução onde pode
ocorrer _memory leak_.

* ```c
void f(){
    void *s;
    s = malloc(50);
    free(s);
}
```
* ```c
int f(){
    float *a;
    return 0;
}
```
* ```c
int f(char *data){
    void *s;
    s = malloc(50);
    int size = strlen(data);
    if (size > 50) {
        return(-1);
    }
    free(s);
    return 0;
}
```
* ```c
int *f(int n){
    int *num = malloc(sizeof(int)*n);
    return num;
}
int main(void){
    int *num;
    num = f(10);
    free(num);
    return 0;
}
```
* ```c
void f(int n){
    char *m = malloc(10);
    char *n = malloc(10);
    free(m);
    m = n;
    free(m);
    free(n);
}
```
{:class="lettered"}

## Questão 3

Observe o código abaixo escrito na linguagem C.

```nohl
1 #include <stdio.h>
2 #define TAM 10
3 int funcaol(int vetor[], int v){
4     int i;
5     for (i = 0; i < TAM; i++){
6         if (vetor[i] == v)
7             return i;
8     }
9     return -1;
10 }
11
12 int funcao2(int vetor[], int v, int i, int f){
13     int m = (i + f) / 2;
14     if (v == vetor[m])
15         return m;
16     if (i >= f)
17         return -1;
18     if (v > vetor[m])
19         return funcao2(vetor, v, m+l, f);
20     else
21         return funcao2(vetor, v, i, m-1);
22 }
23
24 int main(){
25     int vetor[TAM] = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
26     printf(“%d - %d”, funcao1(vetor, 15), funcao2(vetor, 15, 0, TAM-1));
27     return 0;
28 }
```

A respeito das funções implementadas, avalie as afirmações a seguir.

1. O resultado da impressão na linha 26 é: 7 - 7.
2. A função funcao1, no pior caso, é uma estratégia mais rápida do que a funcao2.
3. A função funcao2 implementa uma estratégia iterativa na concepção do algoritmo.

Sabendo que apenas uma das alternativas é verdadeira, indique quais das alternativas é verdadeira e rescreva as alternativas erradas de forma a corrigi-las.

## Questão 4

Dado o seguinte código Haskell:

```haskel
______ :: [a] -> [a] -> [a]
______ [] l = l 
______ (h:t) l = h : (______ t l)
```

Qual seria um bom nome para esta função que descreve o que ela faz?

## Questão 5

Com relação a imutabilidade dos dados em Haskell, qual a(s) vantagem(ns) em ter essa característica em relação à mutabilidade e efeitos colaterais das atribuições de valores em linguagens imperativas?

## Questão 6

A linguagem PROLOG pertence ao paradigma da programação lógica, no qual a lógica proposicional e
algorítmica pode ser expressa na forma de descritores de fatos e regras de produção de respostas. No contexto
da árvore genealógica de uma família, analise a seguinte base de fatos descrita em linguagem Prolog.

```prolog
paide(ana,francisco).
paide(maria,francisco).
paide(luiz,francisco).
maede(jose,maria).
maede(angelica,ana).
paide(luiza,luiz).
paide(joaquim,luiz).
homem(francisco).
homem(jose).
homem(luiz).
homem(joaquim).
mulher(ana).
mulher(maria).
mulher(angelica).
mulher(luiza)
```

Podemos definir uma regra lógica de produção para identificar se uma pessoa é avô de outra com a regra:

```prolog
avode(avo, neto) :- paide(X, avo), paide(neto, X).
avode(avo, neto) :- paide(X, avo), maede(neto, X).
```

Escreva uma regra lógica de produção verificar se duas pessoas são irmãs.
