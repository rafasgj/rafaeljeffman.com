---
title: Programação Dinâmica
subtitle: Complexidade de Algoritmos e Análise de Desempenho
layout: lecture
last_occurrence: 2023-10-30
copy: 2023
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2023-02-analise-algoritmos
---

## Programação Dinâmica

* Idéia básica: utilizar resultados parciais para melhorar o tempo de resposta do algoritmo.
    * Programação Dinâmica $\approx$ recursão + _memoization_
* Como desenvolver algoritmos recursivos?
    * SRTBOT
        * _Subproblem definition_ (Definição do subprboblema)
        * Relacionar soluções recursivas do supbropblema
        * _Topological Order_ (Ordenação Topológica)
        : chamadas dos subproblemas criam um DAG
        * _Base Case_ (caso base)
        * _Original problem_ (problema orgiinal)
        : Resolver o problema original
        * _Time analysis_ (análise da complexidade de tempo)
    * Exemplo: Merge Sort
        * Algoritmo de _divisão e conquista_.
        * Supbroblemas: **S(i, j) = array ordenado em A[i:j]**
        * Relação: **S(i,j) = merge(S(i,m), S(m, j))** $\quad\quad m = \lfloor\frac{i+j}{2}\rfloor$
        * _Topo. order_: aumentar $j-i$
        * _Base case_: **S(i, i) = []**
        * _Original prob._: **S(0, n)**
        * _Time_: $T(n) = 2T(\frac{n}{2})+O(n) = O(n\log{n})\quad\quad n = j - i$
    * Exemplo: Calcular o n-ésimo número de Fibonacci
        * Dado $n$, calcular $F_n = F_{n-1} + F_{n-2}$, sendo $F_1 = F_2 = 1$
        * Subproblemas: $F_{i}, 1 \le i \le n \quad\quad\Theta(n)$
        * Relação: $F(i) = F(i-1) + F(i-2)$
        * _Topo. order_: aumentar $i$, sendo $i = 1, 2, \dots, n$
        * Base: $F(1) = F(2) = 1
        * Original: F(n)
        * _Time_:
            * $T(n) = T(n-1) + T(n-2) + 1$
            : o _+1_ é das adições
            : Não pode usar o teorema master, mas... 
            * $T(n) \lt F_n \approx \varphi^n$
            : Como $\varphi \gt 1$, o algoritmo tem tempo exponencial.
* _Memoization_
    * Palavra criada pela ciência da computação.
    * Significa _lembrar e reutilizar resultados de subproblemas_.
    * Técnica:
        * manter um dicionário mapeando subproblemas a soluções
        * função recursiva retorna uma solução previamente armazenada, se existir, ou calcula uma nova, caso contrário.
    * Análise para o problema do número de Fibonacci: $O(n)$
* Estrutura dos algoritmos de progração dinâmica:

```python
memo = {}

def f(subproblem):
    if subproblem not in memo:
        if base_case:
            memo[subproblem] = base
        else:
            memo[subproblem] =recurse_subproblem
    return memo[subproblem]
```
* Exemplo de implementação de memoization em Python

    > **Nota:** Em geral não implementamos essa operação em Python e utilizamos a função `functools.cache` da biblioteca padrão da linguagem.

```python
def memoization(subproblem):
    def inner(*args):
        if tuple(args) not in memo:
            memo[tuple(args)] = subproblem(*args)
        return memo[tuple(args)]
    
    memo = {}
    return inner

@memoization
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

@memoization
def fat(n):
    if n <= 1:
        return 1
    return n * fat(n-1)
```

* Menor caminho em um DAG
    * Problema: Dado um _grafo acíclico direcionado_ (DAG) $G$ e um vértice $s$, calcular $\delta(s,v)\,\forall v \in V$. 
    * Subproblemas: $\delta(s,v)$ para cada $v \in V$ 
    * Relação: $\delta(s, v) = \min\\{\delta(s,u) + w(u,v)\,\|\, u \in {Adj}^{-}(v)\cup\\{\infty\\}\\}$
    * Topo. Order.: Ordenação topológica de G (DAG)
    * Base: $\delta(s,s) = 0$
    * Original: Conjunto de todos subproblemas
    * Tempo: $\Sigma_{v \in V} O(1 + \|{Adj}^{-}(v)\|)$ = O(\|V\| + \|E\|)

* Bowling (_toy problem_)
    * Dados $n$ pinos, $\{0, 1, \dots, n-1\}$, posicionados linearmente, sendo o valor do pino $i$ definido por $v_i$.
    * Ao jogar uma bola nos pinos, se você acertar o pino $i$, você ganha $v_i$ pontos.
    * Se acertar no meio dos pinos $i$ e $i+1$, você recebe $v_{i} \times v_{i+1}$
    * Objetivo é maximizar o _score_
    * Ex.: Dado o cojunto de pinos $\{-3, 1, 1, 9, 9, 2, -5, -5\}$, a combinação que maximiza o _score_ é $\\{1, 1, (9, 9), 2, (-5, -5)\\}$
    * problem input is a sequence of numbers
    * General tool for subproblem design
        * if your input is a sequence, good some problems:
            * prefixes (x[:i]) $\Theta(n)$
            * sufixes (x[i:])  $\Theta(n)$
            * substrings (X[i:j])  $\Theta(n^2)$
    * SRTBOT for bowling
        * Subproblem: B[i] is the max score possible starting with {i, i+1, \dots, n-1}
        * Relate: B(i) = max { B(i+1), B(i+1) + v_i, B(i+2) + v_i \times v_{i+1}
        * Topo. Ord.: decreasing i order (for i in n..0)
        * Base: B(n) = 0
        * Original: B(0)
        * Time: \Theta(1) * \Theta(i) = \Theta(n)

* Bottom Up DP (iterative algorithm):
    * B(n) = 0
    for i = n..0
        B[i] = max{...}
    return B[0]

## Algoritmo A*

* Objetivo: Achar um caminho entro os pontos $S$ e $G$ em um mapa.
* Busca em largura (Breadth First Search)
    * Busca exaustiva.
    * Resultado ótimo.
* Algoritmo de Dijkstra para o menor caminho em um grafo a partir de uma única origem
    * Resultado ótimo.
    * _Saida mais cedo_.
* Busca Gulosa (Best First Search)
    * Heurísticas
        * Método para resolver um problema sem garantia de encontrar a melhor solução.
    * Distância Euclidiana: $D_{e}(a, b) = \sqrt{\sum_{i=1}^{n}(b_i - a_i)^2}$
    * Distância de Manhattan (Táxi): $D_{m}(a, b) = \sum_{i=1}^{n}\|b_i - a_i\| $
    * Heurística Admissível: $H(x, g) \leq D(x, g)$
    * Resultado mais rápido, porém pode não encontrar o resultado ótimo.
* Algoritmo $A^{\*}$
    * Heuristica consistente: $\| H(x, g) - H(y, g) \| \leq D(x, y)$
    * Levando em consideração, na heurística o caminho percorido, é possível chegar ao melhor resultado.


```python
frontier = PriorityQueue()
frontier.put(start, 0)
came_from = dict()
cost_so_far = dict()
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


## Questões

1. **Projeto**: Implementar o algoritmo $A^\*$ para encontrar o caminho entre dois pontos em um mapa, levando em consideraçãoo custo de locomoção nesse mapa. O mapa é um _grid_ definido como uma série de valores inteiros. Se o valor for positivo ou igual a zero, representa o custo (esforço) de passar pelo terreno. Se o valor for negativo (_-1_), significa que é impossível passar pelo terreno.
2. Crie uma interface e representação da resposta interessante para a utilização do sistema implementado no **item 1**.

## Recursos para essa aula

### Recursos Online

* [Best First Search](https://en.wikipedia.org/wiki/Best-first_search) (Wikipedia)
* [A\* Algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm) (Wikipedia) 
* [Introduction to the A* Algorithm](https://www.redblobgames.com/pathfinding/a-star/introduction.html) (Red Blob Games)

