---
title: Exercícios de Revisão
subtitle: Complexidade de Algoritmos e Análise de Desempenho
layout: lecture
last_occurrence: 2023-11-20
copy: 2023
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2023/analise-algoritmos
  link: /teaching/lasalle/2023/analise-algoritmos
---

## Questão 1

Julgue os itens a seguir, acerca de algoritmos para ordenação:

1. O algoritmo de ordenação por inserção tem complexidade $O(n\log{n})$.
2. Um algoritmo de ordenação é dito estável caso ele não altere a posição relativa de elementos de mesmo valor.
3. No algoritmo quicksort, a escolha do elemento pivô influencia o desempenho do algoritmo.
4. O bubble-sort e o algoritmo de ordenação por inserção fazem, em média, o mesmo número de comparações.

Qual(is) está(ão) correto(s)? O que tem de errado no(s) incorreto(s)?

## Questão 2

Considere o algoritmo que implementa o seguinte processo: uma coleção desordenada de elementos é dividida em duas metades e cada metade é utilizada como argumento para a reaplicação recursiva do procedimento. Os resultados das duas reaplicações são, então, combinados pela intercalação dos elementos de ambas, resultando em uma coleção ordenada. Qual é a complexidade desse algoritmo?

## Questão 3

No processo de pesquisa binária em um vetor ordenado, os números máximos de comparações necessárias para se determinar se um elemento faz parte de vetores com tamanhos 50, 1.000 e 300 são, respectivamente, iguais a <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u>, <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u> e <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u>.


## Questão 4

No famoso jogo da Torre de Hanoi, é dada uma torre com discos de raios diferentes, empilhados por tamanho decrescente em um dos três pinos dados, como ilustra a figura acima. O objetivo do jogo é transportar-se toda a torre para um dos outros pinos, de acordo com as seguintes regras: apenas um disco pode ser deslocado por vez, e, em todo instante, todos os discos precisam estar em um dos três pinos; além disso, em nenhum momento, um disco pode ser colocado sobre um disco de raio menor que o dele; é claro que o terceiro pino pode ser usado como local temporário para os discos.

Imaginando que se tenha uma situação em que a torre inicial tenha um conjunto de 5 discos, qual o número mínimo de movimentações de discos que deverão ser realizadas para se atingir o objetivo do jogo?


## Questão 5

A análise de complexidade provê critérios para a classificação de problemas com base na computabilidade de suas soluções, utilizando-se a máquina de Turing como modelo referencial e possibilitando o agrupamento de problemas em classes. Nesse
contexto, julgue os itens a seguir.

1. É possível demonstrar que $\text{P} \subseteq \text{NP}$ e $\text{NP} \subset \text{P}$.
2. É possível demonstrar que se $\text{P} \neq \text{NP}$, então $\text{P} \cap \text{NP-Completo} = \varnothing$.
3. Se um problema $Q$ é $\text{NP-difícil}$ e $Q \in \text{NP}$, então $Q$ é $\text{NP-completo}$.
4. O problema da satisfatibilidade de uma fórmula booleana $F$ (uma fórmula é satisfatível, se é verdadeira em algum modelo) foi provado ser $\text{NP-difícil}$ e $\text{NP-Completo}$.
5. Encontrar o caminho mais curto entre dois vértices dados em um grafo de $V$ vértices e $E$ arestas não é um problema da classe $\text{P}$.

A alternativa que lista apenas os itens corretos é:

* 1, 3 e 4
* 2, 3 e 4
* 3, 4 e 5
* 1, 2, 3 e 4
* 2, 3, 4 e 5
{:class="lettered"}

Corrija as afirmações incorretas.

## Questão 6

Um programador propôs um algoritmo não-recursivo para o percurso em preordem de uma árvore binária com as seguintes características:

* Cada nó da árvore binária é representado por um registro com três campos: chave, que armazena seu identificador; esq e dir, ponteiros para os filhos esquerdo e direito, respectivamente.
* O algoritmo deve ser invocado inicialmente tomando o ponteiro para o nó raiz da árvore binária como argumento.
* O algoritmo utiliza push() e pop() como funções auxiliares de empilhamento e desempilhamento de ponteiros para nós de árvore binária, respectivamente.

A seguir, está apresentado o algoritmo proposto, em que λ representa o ponteiro nulo.


```
Procedimento preordem (ptraiz : PtrNoArvBin)
    Var ptr : PtrNoArvBin;
    ptr := ptraiz;
    Enquanto (ptr ≠ λ) Faça
        escreva (ptr↑.chave);
        Se (ptr↑.dir ≠ λ) Então
            push(ptr↑.dir);
        Se (ptr↑.esq ≠ λ) Então
            push(ptr↑.esq);
        ptr := pop();
    Fim_Enquanto
Fim_Procedimento
```

Com base nessas informações e supondo que a raiz de uma árvore binária com n nós seja passada ao procedimento `preordem()`, julgue os itens seguintes.

1. O algoritmo visita cada nó da árvore binária exatamente uma vez ao longo do percurso.
2. O algoritmo só funcionará corretamente se o procedimento `pop()` for projetado de forma a retornar λ caso a pilha esteja vazia.
3. Empilhar e desempilhar ponteiros para nós da árvore são operações que podem ser implementadas com custo constante.
4. A complexidade do pior caso para o procedimento `preordem()` é $O(n)$.

Quais afirmações estão corretas? Corrija as afirmações incorretas.

