---
title: Heaps e Heapsort
subtitle: Complexidade de Algoritmos e Análise de Desempenho
layout: lecture
last_occurrence: 2023-09-25
copy: 2023
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2023-02-analise-algoritmos
---

## Assunto

1. _Heaps_
    * Um _heap_ é uma estrutura em árvore que satisfaz uma **propriedade do _heap_**.
    * Um **maxheap** é um _heap_ cuja propriedade a ser satisfeita é
    : dado um nó C qualquer, o a chave do nó P, que é pai de C é **maior** que a chave de C.
    * Um **minheap** é um _heap_ cuja propriedade a ser satisfeita é
    : dado um nó C qualquer, o a chave do nó P, que é pai de C é **menor** que a chave de C.
    * _Heaps_ são a forma mais eficiente de implementação de _filas de prioridade_.
    * Uma implementação bastante comum é a de _heap binários_, que formam árvores binárias quase completas.
    * Operações:
        * `find_min`/`find_max`: $O(1)$
        * `insert`/`push`: $O(\log{n})$ (_heap_ binário) ou $\Theta(1)$ (amortizado, para outras implementações)
        * `delete_min`/`delete_max`/`pop`: $O(\log{n})$
        * `increse_key`/`decrease_key`: $O(\log{n})$ (_heap_ binário) ou $\Theta(1)$ (Fibonacci _heap_, Brodal _queue_)
        * `meld` (junção de dois _heaps_): $O(n)$ (_heap_ binário), $O(\log{n})$ (Binomial) ou $\Theta(1)$ (outras implementações)
    * Em geral todas implementações de _heaps_ que não sejam _heaps_ binários ou _pairing heaps_ são complicadas de mais e podem ser mais lentas, apesar do tempo de operação teórico parecer melhor.
2. _Heapify_
    * Operação de criação de um _heap_ a partir de um _array_ de dados.
    * Utiliza os métodos `sift_up` e `sift_down`.
    * `sift_up` move um elemento para cima no _heap_
    * `sift_down` move um elemento para baixo no _heap_
    * Utilizando o algoritmo de Floyd, apenas o método `sift_down` é necessário e a complexidade de tempo é $O(n)$
    : Começando em $\lfloor\frac{n}{2}\rfloor$ até a raiz, faça `sift_down` do elemento.
    : Para $n/2$ elementos, o esforço é zero.
    : Para $n/4$ elementos, o esforço é 1.
    : Para $n/8$ elementos, o esforço é 2.
    : $\dots$
    : Logo, a quantidade de esforço é $n\times\sum_{i=0}^\infty{\frac{i}{2^{i}}} = 2n$, portanto $\Theta(n)$
3. Representação de um _Heap_ em um _array_
    * Dado um nó com índice $i$ no _array_ (base 0):
        * Filho Esquerdo: $2i + 1$
        * Filho direito: $2i + 2$
        * Pai: $\lfloor\frac{i-1}{2}\rfloor$
        * Como as operações são sempre realizadas em números inteiros, as multiplicações e divisões são facilmente implementadas com os operadores $\gg$ e $\ll$.
4. _Heapsort_
    * Crie um _heap máximo_.
    * Substitua a raiz do heap pelo último elemento do _array_
    * Faça `sift_down` da nova raiz.
    * $n-1$ elementos sofrerão `sift_down` com custo $\Theta(\log{n})$, logo, o _heapsort_ tem complexidade $O(n\log{n})$


## Questões

1. **Projeto**: Pesquise e implemente o `introsort`, o algoritmo de ordenação por comparação não-estável da biblioteca padrão da linguagem de programação C++.

