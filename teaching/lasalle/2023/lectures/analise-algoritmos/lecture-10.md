---
title: Grafos - Parte 2
section: Complexidade de Algoritmos e Análise de Desempenho
layout: lecture
last_occurrence: 
copy: 2023
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2023/analise-algoritmos
  link: /teaching/lasalle/2023/analise-algoritmos
---

## Grafos

* [Revisão de Grafos](lecture-09)
* Grafos ponderados
  : São grafos onde um valor (peso) é associado as arestas.
* Extensão do Grafo como ADT:
    * Para para grafos com arestas valoradas:
        * `add_edge(G, u, v, z)`
        : adiciona uma aresta $(u, v)$ com o valor $z$ ao conjunto de arestas do grafo $G$
        * `get_edge_value(G, u, v): value`
            : retorna o valor associado a aresta $(u, v)$ do grafo $G$, ou $+\infty$ se a aresta não existe.
        * `set_edge_value(G, u, v, z)`
            : define o valor associado a aresta $u$ do grafo $G$ como sendo $z$
    * Para grafos com vértices valorados
        * `get_vertex_value(G, u): value`
            : retorna o valor associado ao vértice $u$ do grafo $G$
        * `set_vertex_value(G, u, z)`
                : define o valor associado ao vértice $u$ do grafo $G$ como sendo $z$

## _Minimum Spanning Trees_
* Importante em sistemas distribuídos.
* Usado nos protocolos de rede baseados no [STP](https://en.wikipedia.org/wiki/Spanning_Tree_Protocol).
* Definição:
    : **Entrada** $\rightarrow$ dado um grafo $G=(V,E)$ e uma relação $w: E\rightarrow\mathbb{R}$
    : **Saída** $\rightarrow$ Uma árvore $T$, conectando todos os vértices, cujo custo total de conexão é o mínimo possível $w(T) = \sum_{(u,v) \in T} w((u,v))$
* Algoritmo de Prim:
    1. Inicialização: A árvore $T$ tem um vértice $u$, escolido arbitrariamente de $G$.
    2. Base: Se $V_T = V_G$, termine.
    3. Recursão: Escolha a aresta $(u,v)$ tal que $u \in T$ e $v \in G$ e $w((u,v)) \le w((t, z)), \; \forall (t, z) \in E,(t,z) \ne (u, v)$
* Implementação:
    1. Associe cada vértice do grafo com um custo $C[v]$ que representa o menor custo de conexão a $v$ utilizando a aresta $(u, v)$. Inicialize $C[v] = (+\infty, \varnothing)$, e $C[u] = (0, \varnothing)$, onde $u$ é o vértice escolhid para iniciar a MST 
    2. Inicialize uma floresta vazia $F$ e um conjunto de vértices $Q$ contendo todos os vértices.
    3. Ache o vértice $u$ de $Q$ que tem o menor valor de $C[u]$, e remova-o de Q e o adicione a F.
    4. Para todos os vértices $v$ que exista uma aresta $(u, v)$, se $v \in Q$ e $w(u,v) \lt C[v]$, então ajuste $C[v] = (w((u,v))), u)$
    5. Se ainda existem vértices em $Q$, retorne a $2$.
* Análise do algoritmo de Prim
    * Utilizando uma matriz de adjacências: $O(\|V\|^2)$
    * Utilizando um _heap binário_ e lista de adjacências: $O(\|E\|\log\|V\|)$
    * Utilizando um _heap de Fibonacci_ e lista de adjacências: $O(\|E\| + \|V\|\log\|V\|)$
* O algoritmo para obter uma MST é um _algoritmo guloso_ (_greedy algorithm_).


## Função de custo

* A função de custo em um grafo ponderado é uma função $w: E\rightarrow\mathbb{R}$ que define o custo associado às arestas do grafo.
* Uma função de custo é qualquer algoritmo que atribua um valor $v \in \mathbb{R}$ a uma aresta $(u, v)$.
* Exemplos de funções de custo:
    * Distância Euclidiana
    * Distância de Manhattan
    * Tempo esperado para percorrer $(u,v)$
    * Relação entre a distância, tempo e custo de abastecimento entre dois pontos.


## Problema do Menor Caminho

* Um caminho é um conjunto de vértices $\{v_1, v_2, \dots, v_k\}$.
* O tamanho de um caminho é dado por $\delta(p) = \sum_{i=1}^{k-1}w(v_i,v_{i+1})$
* Objetivo é encontrar
    * O menor caminho entre dois vértices
    * O menor caminho entre um vértice e todos os outros
    * O menor caminho entre todos os pares de vértices
* Para isso, é necessário existir um menor caminho entre dois nós $u$ e $v$
    * Se não existir um caminho entre $u$ e $v$, não existe um caminho, e, normalmente, dizemos que $\delta_{(u,v)} = +\infty$
    * Se existir um ciclo com $\delta \lt 0$ em algum caminho entre $u$ e $v$, não exisitirá um menor caminho entre $u$ e $v$


## Algoritmo de Floyd-Warshall

* Encontra o menor caminho entre todos os pares de vértices em um grafo ponderado direcionado.
* As arestas podem ter pesos positivos ou negativos.
* Não podem existir ciclos negativos.
* Simples de implementar utilizando uma matriz de adjacências.
* [Pseudocódigo](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm#Pseudocode){:target="\_blank"}
    ```nohl
    for i from 1 to |V|
        for j from 1 to |V|
            dist[i][j] = get_edge_cost(G, i, j)
    for k from 1 to |V|
        for i from 1 to |V|
            for j from 1 to |V|
                if dist[i][j] > dist[i][k] + dist[k][j] 
                    dist[i][j] ← dist[i][k] + dist[k][j]
                end if
    ```
* Complexidade de tempo: $O(|V|^3)$
* O algoritmo pode ser modificado adicionando-se uma matriz que armazena o vértice anterior do caminho, obtendo assim, além do menor custo, qual o caminho percorrido.


## Algoritmo de Dijkstra

* Encontra o menor caminho entre um nó no grafo e todos os outros vértices (_single source shortest path_)
* As arestas devem ter pesos positivos
* [Pseudocódigo](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Pseudocode){:target="\_blank"}
    ```
    function Dijkstra(Graph, source):
        for each vertex v in Graph.Vertices:
            dist[v] ← INFINITY
            prev[v] ← UNDEFINED
            add v to Q
        dist[source] ← 0
        while Q is not empty:
            u ← vertex in Q with min dist[u]
            remove u from Q
            for each neighbor v of u still in Q:
                alt ← dist[u] + Graph.Edges(u, v)
                if alt < dist[v]:
                    dist[v] ← alt
                    prev[v] ← u
        return dist[], prev[]
    ```
* Análise do algoritmo de Dijkstra
    * Utilizando um _heap binário_: $\Theta(\,(\|E\| + \|V\|)\,\log\|V\|)$
    * Utilizando um _heap de Fibonacci_: $\Theta(\|E\| + \|V\|\log\|V\|)$
* Para encontrar a menor distância entre dois nós basta encerrar o algoritmo quando $u$ for o destino desejado.


## Recursos para essa aula

* [Primeira parte do estudo de Grafos](lecture-09)
* [Floyd-Warshall Algorithm](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm){:target="\_blank"}
* [Dijkstra's Shortest Path Algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm){:target="\_blank"}
