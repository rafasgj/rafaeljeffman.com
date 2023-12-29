---
title: Grafos - Parte 1
subtitle: Complexidade de Algoritmos e Análise de Desempenho
layout: lecture
last_occurrence: 2023-10-02
copy: 2023
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2023/analise-algoritmos
  link: /teaching/lasalle/2023/analise-algoritmos
---

## Grafos

1. Aplicações de Grafos:
    * Redes de computadores e dados
    * Redes sociais
    * Redes de logística
    * Compiladores
    * Puzzles e Jogos
    * _meshes_
    * Circuitos
    * Estruturas moleculares
    * $\dots$
2. Definição e características de Grafos
    * Um grafo ($G$) pode ser representado por um conjunto de vértices ($V$) e arestas ($E$)
    : $\to G = (V, E)$, onde $E \subseteq V \times V$
    * Um grafo pode ser:
        : $\to $ **direcionado**: onde uma aresta ($v_i$, $v_j$) não é igual a uma aresta ($v_j$, $v_i$)
        : $\to$ **não-direcionado**: onde as arestas representam qualquer uma das direções.
        : $\to$ **cíclico**: que possui ciclos em pelo menos um de seus caminhos possíveis
        : $\to$ **acíclico**: que não possuí ciclos
    * Assumiremos, nesta aula, que todo grafo é um grafo simples
    : $\to$ não tem auto-arestas (uma aresta que sai e volta para o mesmo nó)
    : $\to$ toda aresta é distinta, ou seja, só existe uma aresta $(v, w)$
    : $\to\|E\| = O(\|V\|^{2})$
        : Algoritmos cuja complexidade está baseada nas arestas podem ser vistos como $O(\|V\|^2)$, no entanto, em muitos casos práticos os grafos são esparsos, onde $E \ll \|V\|^2$.
    * Existe uma relação polinomial entre o número de aresta se vértices, logo $\log \|E\| = \Theta(\log \|V\|)$
    * Um grafo **conectado** é um grafo onde existe, pelo menos, um caminho entre quaisquer dois vértices do grafo, e $\|E\| \ge \|V\| - 1$.
3. Grafo como tipo abstrato de dados
    * Operações
        * `adjacent(G, u, v): bool`
        : existe uma aresta ligando $u$ a $v$?
        * `neighbors(G, u): set`
            : lista todos os vértices $v$ para os quais exista uma aresta $(u, v)$
        * `add_vertex(G, u)`
            : adiciona um vértice $u$ ao conjunto de vértices do grafo $G$
        * `remove_vertex(G, u)`
            : remove o vértice $u$ do conjunto de vértices do grafo $G$
        * `add_edge(G, u, v)`
            : adiciona uma aresta $(u, v)$ ao conjunto de arestas do grafo $G$
        * `remove_edge(G, u, v)`
            : remove a aresta $(u, v)$ do conjunto de arestas do grafo $G$

4. _Vizinhança_
    * O conjunto de nós vizinhos de saída é dado por $\text{Adj}^{+}(u) = \\{v \in V \| (u, v) \in E\\}$, para $u \in V$
    * O conjunto de nós vizinhos de entrada é dado por $\text{Adj}^{-}(u) = \\{v \in V \| (v, u) \in E\\}$, para $u \in V$
    * O **grau de saída** de um vértice $u \in V$ é $\deg^{+}(u) = \|\text{Adj}^{+}(u)\|$
    * O **grau de entrada** de um vértice $u \in V$ é $\deg^{-}(u) = \|\text{Adj}^{-}(u)\|$
    * Para grafos não-direcionados $\text{Adj}^{+}(u) = \text{Adj}^{-}(u)$ e $\deg^{+}(u) = \deg^{-}(u)$
    * Quando o sobrescrito não é utilizado, estamos nos referenciando aos vizinhos de saída: $\text{Adj}(u) = \text{Adj}^{+}(u)$ e $\deg(u) = \deg^{+}(u)$

5. Representação de Grafos
    * O objetivo é otimizar:
        * espaço de armazenamento
        * funções `adjacent` e `neighbors`
    * Lista de adjacências
        * Lista de arestas para um vértice $v \in G$.
        * O custo de armazenamento é $\Theta(\|V\| + \|E\|)$.
        * É uma representação _esparsa_, pois representa apenas as arestas necessárias, em grafos esparsos.
        * Exemplo de grafos esparsos: grafo planar ($\|E\| \le 3\|V\|-6$, para $\|V\| \ge 3$), árvores, lista encadeada.
    * Matrix de adjacências
        * Matriz $V\timesV$ com cada célula $(i, j)$ representando uma aresta entre os vértices $i$ e $j$.
        * O custo de armazenamento é $\Theta(\|V\|^2)$.
        * É uma representação _densa_, pois representa grafos densamente conectados.
        * Exemplo de grafos densos: grafo completo.

6. Caminhos (_Paths_)
    * Um caminho é uma sequência de vértices $p = (v_1, v_2, \dots ,v_k)$, onde $(v_i, v_{i+1}) \in E \; \forall i \in \\{1, ..., k-1\\}$
    * $\ell(p)$ é o tamanho do caminho
    * $\delta(u, v)$ é o menor caminho entre $u$ e $v$
    * Level Set: $L_k = \\{v \in V \| \delta(s, v) = k\\}$, onde $s$ é o vertice de origem
    * Seja o menor caminho entre dois vértices $v_1 \longrightarrow v_k$ definido por $p = \\{v_1, v_2, \dots, v_{k-1}, v_k\\}$, o menor caminho entre os vértices $v_1$ e $v_i$, onde $i \in \\{2, \dots, k-1\\}$ também é conhecido.
    : ou seja, o menor caminho entre um vértice $u$ e $t$ é a união entre o menor caminho entre $u$ e $s$ e o menor caminho entre $s$ e $t$, bastando saber qual vértice é o anterior de cada vértice para armazenar tal caminho.

7. Problemas em Grafos:
    * Existe um caminho em $G$ entre os vértcies $s$ e $t$? (_Single pair reachability_)
    * Qual a menor distância entre $s$ e $t$ no grafo $G$? (_Single pair shortest path_)
    * Qual a menor distância entre $s$ e todos os vértices do grafo $G$? (_Single source shortest path_)

8. Algoritmos
    * Busca pelo menor caminho:
        * Caso base
        : $(i = 1): L_0 = \\{s\\}, \delta(s,s) = 0, P(s) = \varnothing$
        * Indução para calcular $L_i$
            * para cada vértice `u` em $L{i-1}$
                * para cada vértice $v \in \text{Adj}(u)$ que não está em $L_j$ para $j \lt i$
                    * adicione $v$ a $L_i$, defina $\delta(s, v) = i$, e $P(v) = u$
        *  Repetidamente calcule $L_i$ a partir de $L_j$ para $j \lt i$, incrementando $i$ até que $L_i$ seja o conjunto vazio.
        * Defina $\forall v \in V, \delta(s, v) = \infty$ se $\delta(s, v)$ não está definido.
    * Implementação
        : $L_0 \gets \\{s\\}$
        : $\delta(s, s) \gets 0$
        : $P(s) \gets \varnothing$
        : $i \gets 1$
        : $\text{while} \; L_{i-1} \ne \varnothing$
        : $\quad \forall u \in L_{i-1}i, \forall v \in \text{Adj}(u) \text{and} v \notin \cup^{i-1}\_{j}{L_j}$
        : $\quad\quad L_i \gets L_i \cup {v}$
        : $\quad\quad \delta(s, v) = i$
        : $\quad\quad P(v) = u$

    * Complexidade do algoritmo: $O(\|V\| + \|E\|)$

9. Buscas em Grafos
    * Busca em Largura (_Breadth First Search_)
        ```python
        from collections import deque as Queue
        def bfs(G, s):
            visited = set()
            queue = Queue()
            queue.append(s)
            while queue:
                u = queue.popleft()
                for v in neighbor(G, u):
                    if v not in visited:
                        queue.append(v)
                visited.add(u)
        ```
    * Busca em Profundidade (_Depth First Search_)
        ```python
        def dfs(G, s):
            visited = set()
            queue = list()
            queue.append(s)
            while queue:
                u = queue.pop()
                for v in neighbor(G, u):
                    if v not in visited:
                        q.append(v)
                visited.add(u)
        ```

## Questões

1. **Implementação** Implementar uma classe representando um grafo e suas operações.
2. Um grafo conectado é um grafo onde todos os vértices estão conectados. Dado um grafo $G$, como é possível verificar se um grafo é conectado ou não?
3. Um grafo acíclico é um grafo onde para qualquer caminho $\\{v_1, v_2, \dots, v_k\\}$, $v_i \ne v_j$ onde $i \ne j$ e  $i \in \\{1, \dots, k\\}, j \in \\{1, \dots, k\\}$. Como é possível encontrar um ciclo em um grafo?


## Recursos para essa aula

* [Conjuntos e Relações](/teaching/cs/basics/set-concepts)

### Recursos _online_

* [**Graph**](https://mathworld.wolfram.com/Graph.html){:target="\_blank"} Wolfram Mathwold. Wolfram Research.
* [Graph and its representations](https://www.geeksforgeeks.org/graph-and-its-representations/){:target="\_blank"} (Geeks for Geeks)
* [Graph (Abstract Data Type)](https://en.wikipedia.org/wiki/Graph_(abstract_data_type)){:target="\_blank"} (Wikipedia)
