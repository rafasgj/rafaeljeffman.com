---
title: T1 - Algoritmos de Pesquisa
section: Inteligência Artificial
layout: lecture
last_occurrence: "2024-1"
copy: 2024
institution:
  name: Universidade Lasalle Canoas
  link: index.html
---

## Objetivo

Comparar os algoritmos de busca em espaços de resposta, aplicados na busca pelo melhor caminho em um mapa bi-dimensional.

## Pré-requisitos

* Todos os alunos necessitarão de contas no site [Github](https://github.com).
* Para o desenvolvimento, será necessário que os alunos tenham acesso a uma versão do ambiente de execução da linguagem de programação Python e o sistema de controle de versão Github.

## Tarefas

1. Criar um _fork_ do projeto [`ia-2024-t1`](https://github.com/exercicios-programacao/ia-2024-t1).
2. Implementar os algoritmos de busca vistos em aula:
    * Busca em profundidade
    * Busca em largura
3. Implementar os algoritmos de busca com heurísticas vistos em aula:
    * _Branch and Bound_
    * _A\*_
4. Implementar o algoritmo de Dijkstra para busca do caminho mais curto em um grafo.
5. As funções de entrada dos algoritmos devem ser implementadas no arquvivo `src/busca.py`:
    * Os parametros das funções são:
        * graph: Uma descrição do grafo (que pode ser definida pelo aluno)
        * start: um inteiro representando um nó do grafo
        * goal: um inteiro representando um nó do grafo
    * O retorno das funções deve ser uma tupla contendo, pela ordem:
        * inteiro com o número de nós do grafo analizados.
        * _float_ com o comprimento do caminho encontrado.
        * lista de inteiros representando o caminho de `start` a `goal`
    * As assinaturas das funções devem ser:
        ```python
        def dfs(graph, start: int, goal: int) -> (int, float, [int]):
            """Busca em graph, um caminho entre start e goal usando busca em profundidade."""

        def bfs(graph, start: int, goal: int) -> (int, float, [int]):
            """Busca em graph, um caminho entre start e goal usando busca em largura."""

        def branch_and_bound(graph, start: int, goal: int) -> (int, float, [int]):
            """Busca em graph, um caminho entre start e goal usando Branch and Bound."""

        def a_star(graph, start: int, goal: int) -> (int, float, [int]):
            """Busca em graph, um caminho entre start e goal usando A*."""

        def dijkstra(graph, start: int, goal: int) -> (int, float, [int]):
            """Busca em graph, um caminho entre start e goal usando Dijkstra."""
```

6. Implementar uma função para a leitura de um grafo com a seguinte interface
    ```python
    def read_graph(filename: string) -> Graph
        """Le a estrutura do grafo a partir de um arquivo."""
```
    * A estrutura do grafo pode ser definida como desejado (recomenda-se listas de adjacências)
7. O formato do arquivo a ser lido é: 
```
    <número de nós no grafo>
    <nó> <latitude> <longitude>  # repete para cada nó do grafo
    <número de arestas no grafo>
    <nó> <nó> <custo_da_aresta> # repete para cada aresta do grafo
```

8. Serão fornecidos testes automatizados para a avaliação do trabalho. Os testes podem ser executadosu utilizando o utilitário `behave` ou o utilitário `tox`, que podem ser instalados em um ambiente virtual do Python.

## Entrega do trabalho

Um único aluno do grupo de alunos que trabalhou na execução do trabalho deverá criar um _pull request_ contra o repositório original do trabalho. O título do _pull request_ é livre, porém o corpo deve conter os **nomes completos** de todos os alunos do grupo.

Uma vez criado o _pull request_ ele pode ser atualizado a qualquer momento, até a data limite de entrega.

Na data limite, o _pull request_ receberá um _label_ de `AVALIADO`, um comentário com o resultado da avaliação, será fechado, e não poderá mais ser alterado.

No `LEX`, **todos** os alunos do grupo devem inserir, até a data limite, o link para o _pull request_ de entrega do trabalho.

A data máxima de entrega é dia **04 de maio de 2024**.

## Observações

* Não é permitida a alteração de qualquer arquivo fora do diretório `src`.
* Não é permitida a utilização de qualquer biblioteca externa.
* O trabalho pode ser realizado em grupos de até quatro alunos.
* Será fornecida uma função para calcular a distância entre duas coordenadas em uma esfera (latitude, longitude).
* Todo código fornecido em aula pode ser utilizado no trabalho.
* Em caso de plágio, a nota atribuída ao trabalho será 0 (zero).
