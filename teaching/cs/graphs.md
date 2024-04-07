---
title: Grafos
subtitle: Conceitos
layout: main
section: Estruturas de Dados
sections:
  - Estruturas de Dados
tags:
  - estruturas de dados
  - grafos
lang: pt
copy: 2024
date: 2024-02-19
abstract:
extra_styles:
  - lecture
  - tikzimage
---
<!--
> Este artigo é um de uma série contendo:
>  * [Grafos: Conceitos](graphs)
>  * [Grafos: Representação e Algoritmos](graph-algorithms)
>  * [Grafos: Tipo Abstrato de Dados](graph-adt)
>  * [Grafos: Problema do menor caminho](graph-shortest-path)
-->

Um **grafo não-direcionado**, ou simplesmente **grafo** é um conjunto de pontos com linhas conectandos alguns desses pontos. Os pontós são chamados de **nós** ou **vértices** e as linhas são chamadas **arestas**.

![Grafo](/images/graph_star.svg)

O número de arestas de um nó específico é o **grau** do nó. Cada dois nós só podem ter uma aresta ligando-os. Na figura anterior, todos os nós tem grau 2.

Ao representar um grafo, utilizamos um conjunto com um par $\{i,j\}$ para reperesentar uma aresta que liga os nós $i$ e $j$. No caso do grafo _não-direcionado_, a ordem de $i$ e $j$ não importa, e os pares $\(i,j\)$ e $\(j,i\)$ representam a mesma aresta.

No caso do **grafo direcionado**, representamos cada aresta com uma tupla $\(i, j\)$ para representar uma aresta que sai do nó $i$ e chega ao nó $j$. No caso dos _grafos direcionados_, os pares $\(i,j\)$ e $\(j,i\)$ representam arestas diferentes. Em grafos direcionados o _grau_ de um nó é divido em **grau de entrada**, que é o número de arestas que chega no nó, e **grau de saída**, que é o número de arestas que inicia no nó.

![Caminho](/images/directed_graph.svg)

Formalmente, um grafo é composto por dois conjuntos $G = (V, E)$, onde $V$ é o conjunto de vértices e $E$ é o conjunto de arestas do grafo. Por exemplo, podemos descrever o grafo apresentado anteriormente como:

$$
G = (\{1,2,3,4,5\},\; \{(1,3), (2,4), (3,5), (4,1), (5,2)\})
$$

Um **subgrafo** de um grafo $G$ é um grafo formado com um subconjunto de vértices e arestas de G. O subconjunto de vértices deve incluir todos os vértices que estão relacionados as arestas do subconjunto de arestas, porém pode incluir vértices adicionais. Um **subgrafo induzido** é um subgrafo formado por um subconjunto de vértices e todas as arestas que conectam esses vértices.

![Subgrafo](/images/subgraph.svg)

Um **caminho** é uma sequência de _arestas_ que unem uma sequência de _vértices_. Um **caminho aberto** é um caminho onde o primeiro e o último vértices são diferentes, um **caminho fechado** é um caminho que começa e termina no mesmo vértice. Um **caminho simples** é um caminho onde não ocorrem repetições de vértices ou arestas.

![Caminho](/images/graph_path.svg)


Um **ciclo** ocorre quando é possível criar uma _caminho fechado_ em um grafo.
    
![Caminho](/images/graph_cicle.svg)

Um **grafo conexo** ou **grafo conectado** é um grafo onde é possível atingir qualquer vértice de um grafo a partir de um vértice qualquer deste grafo. Um **grafo fracamente conectado** é um grafo direcionado onde a substituição das arestas por arestas não direcionadas forma um grafo conectado. Um **grafo fortemente conectado** é um grafo conexo direcionado (existem arestas para ambos os lados em todos os pares de vértices).

![Grafo](/images/square_cross_graph.svg)

Um **grafo rotulado** é um grafo cujos vértices e/ou arestas possuem rótulos. Em alguns casos, chamamos um _grafo rotulado_ de **grafo ponderado**, quando os rótulos das arestas representam um _custo_ para aquela aresta.

![Caminho](/images/labeled_graph.svg)

Uma **auto-aresta** é uma aresta que tem nas suas duas pontas o mesmo vértice. Um grafo contendo uma _auto-aresta_ não é mais um grafo simples, e é tratado como um **multigrafo**.

![Caminho](/images/auto_loop.svg){:style="min-height: 130px !important; max-height: 130px !important;"}

<!-- arvores -->

