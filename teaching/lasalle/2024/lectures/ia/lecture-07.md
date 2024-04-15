---
section: Inteligência Artificial
title: Pseudo-código para os algoritmos de busca.
subtitle:
layout: lecture
last_occurrence: 2024-04-15
copy: 2024
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2024/ia
---

## Busca em Profundidade

Para este algoritmo:

* `Grafo` é uma classe que representa um grafo
* `Stack` é uma estrutura de pilha
    * Em Python podemos utilizar listas e os métodos `append` e `pop`
* `start` e `goal` são "nomes" de vértices
* `visited(vertice)` retorna `True` se o vértice já foi visitado.
* `set_visited(vertice)` marca o vértice como visitado.
    * Em Python, a lista de vértices visitados pode ser facilmente e eficientemente implementada com um `set` (ou `dict` se a lista guardar mais informações).
* `processa_caminho(v)` até o vértice `v`.
    * Para o DFS basta marcar `from` como _anterior_ de `v.

```python
def DFS(Grafo, start, goal):
    assert(start in Grafo.vertices)
    assert(goal in Grafo.vertices)
    S = Stack()
    S.push(start)
    while not S.is_empty():
        v = S.pop()
        if goal == v:
            return  # encontrou o caminho
        if not visited(v):
            # processa o caminho "até v"
            processa_caminho(v)
            set_visited(v)
            for u in Grafo.neighbors(v):
                S.push(u)
```

## Busca em Largura

* `Grafo` é uma classe que representa um grafo
* `Queue` é uma estrutura de fila
    * Em Python podemos utilizar a classe `queue.deque` e os métodos `appendleft` e `pop`.
* `start` e `goal` são "nomes" de vértices
* `visited(vertice)` retorna `True` se o vértice já foi visitado.
* `set_visited(vertice)` marca o vértice como visitado.
    * Em Python, a lista de vértices visitados pode ser facilmente e eficientemente implementada com um `set` (ou `dict` se a lista guardar mais informações).
* `processa_caminho(v)` processa o caminho até o vértice `v`. 
    * Para o BFS basta marcar `from` como _anterior_ de `v`.

```python
def BFS(Grafo, start, goal):
    assert(start in Grafo.vertices)
    assert(goal in Grafo.vertices)
    Q = Queue()
    Q.enqueue(start)
    while not Q.is_empty():
        v = Q.dequeue()
        if goal == v:
            return  # encontrou o caminho
        if not visited(v):
            # processa o caminho até v
            processa_caminho(v)
            set_visited(v)
            for u in Grafo.neighbors(v):
                Q.enqueue(u)
```

## Branch and Bound

O algoritmo _Branch and Bound_ leva em consideração o caminho até o momento e se este caminho não pode levar a um resultado melhor, não segue criando divisões a partir daquele vértice.

``` python
def branch_and_bound(Grafo, start, goal):
    assert(start in Grafo.vertices)
    assert(goal in Grafo.vertices)
    best_so_far = (None, +INF)
    Q = Queue()
    Q.enqueue(start)
    while not Q.is_empty():
        v = Q.dequeue()
        if goal == v:
            # 'candidate' é o comprimento atual do caminho
            new_path, candidate = processa_caminho(v)
            path, limit = best_so_far
            if candidate < limit:
                best_so_far = (new_path, candidate)
        else:
            ajusta_caminho(start, v)
            for u in Grafo.neighbors(v):
                # Só adiciona caminhos que podem ser melhores
                if caminho_ate_aqui(start, u) < best_so_far:
                    Q.enqueue(u)
```

## A<sup>\*</sup>

Para o algoritmo $A^\*$, será necessária a criação de uma heurística admissível, ou, melhor ainda, uma heurística consistente.

Sobre o algoritmo $A^\*$:

* Objetivo: Achar um caminho entro os pontos $S$ e $G$ em um mapa.
* Heurísticas
    * Método para resolver um problema sem garantia de encontrar a melhor solução.
* Exemplos de heurísticas para a distância em mapas 2D:
    * Distância Euclidiana: $D_{e}(a, b) = \sqrt{\sum_{i=1}^{n}(b_i - a_i)^2}$
    * Distância de Manhattan (Táxi): $D_{m}(a, b) = \sum_{i=1}^{n}\|b_i - a_i\| $
* Heurística Admissível: $H(x, g) \leq D(x, g)$
    * Resultado mais rápido, porém pode não encontrar o resultado ótimo.
* Heuristica consistente: $\| H(x, g) - H(y, g) \| \leq D(x, y)$
    * Levando em consideração, na heurística, o caminho percorido, é possível chegar ao melhor resultado (quando utilizamos uma heurística consistente).


```python
frontier = PriorityQueue()
frontier.put(start, 0)
came_from = {}
cost_so_far = {}
came_from[start] = None
cost_so_far[start] = 0

def heuristic(a, b):
   """Manhattan distance on a square grid."""
   return abs(a.x - b.x) + abs(a.y - b.y)

while not frontier.empty():
   current = frontier.get()

   if current == goal:
      break
   
   for next in graph.neighbors(current):
      new_cost = cost_so_far[current] + graph.cost(current, next)
      if next not in cost_so_far or new_cost < cost_so_far[next]:
         cost_so_far[next] = new_cost
         priority = new_cost + heuristic(goal, next)
         frontier.put(next, priority)
         came_from[next] = current
```

## Algoritmo de Dijkstra

O pseudocódigo para a implementação do [algoritmo de Dijkstra](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm):

```python

function Dijkstra(Graph, source, goal):
    for each vertex v in Graph.Vertices:
        dist[v] = INFINITY
        prev[v] = UNDEFINED
        add v to Q
    dist[source] = 0
   
    while Q is not empty:
        u = vertex in Q with min dist[u]
        remove u from Q
       
        for each neighbor v of u still in Q:
            alt = dist[u] + Graph.edge(u, v)
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    return dist[], prev[]
```

Para uma implementação eficiente do algoritmo, deve ser utilizada uma fila de prioridades (_priority queue_), que pode ser implementada como um _heap_ mínimo.

## Recursos para essa aula

### Links

* [O que é uma heurística?](https://www.allaboutai.com/pt-br/glossario-inteligencia-artificial/heuristica-consistente/)
* [O que é heurística? Definição, Funcionamento e Exemplos](https://finalverse.com.br/o-que-e-heuristica-definicao-funcionamento-e-exemplos/)
* [Heurística Admissível](https://en.wikipedia.org/wiki/Admissible_heuristic) (Wikipedia, Inglês)
* [Heurística Consistente](https://en.wikipedia.org/wiki/Consistent_heuristic) (Wikipedia, Inglês)

