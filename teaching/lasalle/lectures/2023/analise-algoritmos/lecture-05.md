---
title: Algoritmos eficientes de ordenação.
subtitle: Complexidade de Algoritmos e Análise de Desempenho
layout: lecture
last_occurrence: 2023-08-28
copy: 2023
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2023/analise-algoritmos
  link: /teaching/lasalle/2023/analise-algoritmos
---

## Assuntos

1. Revisando Ordenação
    1. Problema
        * Dado uma lista qualquer, $\{ a\_{1}, a\_{2}, \ldots, a\_{n-1}, a\_{n} \}$, obter uma lista $\{ a^\prime\_{1}, a^\prime\_{2}, \ldots, a^\prime\_{n-1}, a^\prime\_{n} \}$, tal que $\{a^\prime\_i \le a^\prime\_{i+1} \}$.
    2. Permutation Sort (Bogosort)
        ```nohl
        func permutation_sort(A):
            for B in permutations(A):
                if is_sorted(B):
                    return B
        ```
        Complexidade de Tempo: $O(n! \times n)$ <br/>
        Complexidade de Espaço: $O(1)$
    3. Prova que algoritmos de ordenação por comparação tem $\Omega(n\log{n})$
        * Modelo computacional: **Modelo de Comparação**
            * Todos os items de entrada são _caixas pretas_ (ADT)
            * as únicas operações permitidas são comparações ($\le, \lt, =, \neq, \gt, \ge$)
            * Custo em tempo é definido pelo número de comparações
        * Árvore de decisão
            * Todo algoritmo de comparação pode ser visto como uma árvore de todas as possíveis comparações e o resultado final.
            * Mostra todas as combinações possíveis do algoritmo.
            * Um nó interno na árvore de decisão resulta em uma decisão binário (comparação) no algoritmo.
            * Uma folha da árvore de decisão representa uma resposta encontrada.
            * Um caminho da raíz até uma folha é uma execução do algoritmo.
            * O tamanho do caminho representa o tempo de execução do algoritmo.
            * O pior caso no tempo de execução é dado pela altura da raiz.
            * ex: Busca Binária (n=3)
                * A[1] < x ?
                    * Se não: A[0] < x ?
                        * Se não: x <= A[0]
                        * Se sim: A[0] < x <= A[1]
                    * Se sim: A[2] < x ?
                        * Se não: A[1] < x <= A[2]
                        * Se sim: A[2] < x
            * _Hipótese_: Dados $n$ items ordenados, encontrar um item entre eles, no modelo de comparação requer $\Omega(\log{n})$ no pior caso.
            * _Prova_:
                * A árvore de decisão é binária e precisa ter, pelo menos, $n$ folhas, uma para cada resposta possível, logo, a altura da árvore é, pelo menos, $\log{n}$.
        * Utilizams a árvore de decisão para provar que o limite inferior dos algoritmos de ordenação é $\Theta(n\times\log(n)$.
        * O número de respostas possíveis para um algoritmo de ordenação é, pelo menos, todas as combinações possíveis do elementos de entrada, que é $n!$.
        * A altura da árvore é, pelo menos, $\log(n!)$
        * Aplicando a [aproximação de Stirling](https://en.wikipedia.org/wiki/Stirling%27s_approximation), chegamos em $\ln(n!) = n \ln n - n + O(\ln n)$, fica claro que $\Omega(n\log{n})$
    4. Como visto na última aula, o `insertion sort` tem $O(n^{2})$ para o pior caso e $\Omega(n)$ para o melhor caso.
    5. Merge Sort
        * Utiliza o método de divisão e conquista.
        * Divide o array até que a ordenação seja trivial.
        * Junta dois arrays de forma ordenada, num novo array

        ```nohl
        func merge_sort(A, i = 0, j = A.length - 1):
            if 1 < j - 1:
                m = i + (j - 1) / 2
                merge_sort(A, i, m)
                merge_sort(A, m + 1, j)
                A = merge(A, i, m, A, m + 1, j)

        func merge(A, sa, ea, B, sb, eb):
            C = Array((ea - sa) + (eb - sb))
            i = ea
            j = eb
            k = C.length
            while sa < i and sb < j:
                k -= 1
                if A[i] < A[j]:
                    C[k] = A[i]
                    i -= 1
                else:
                    C[k] = A[j]
                    j -= 1
            while sa < i:
                C[k] = A[i]
                i -= 1
            while sb < j:
                C[k] = A[j]
                j -= 1
            return C    
        ```
        * `Merge Sort` tem complexidade de tempo $O(n\times\log{n})$ e $\Omega(n\times\log{n})$ (ou seja $\Theta(n\times\log{n})$), sendo um algoritmo de ordenação ótimo em relação ao modelo de comparação.
        * A complexidade de espaço do `merge sort` é $O(n)$.
        * O `merge sort` é um algoritmo estável em relação às chaves ordenadas.
        * O algoritmo `timsort` utilizado pelo Python e pelo Java é baseado no `merge sort`.
    6. Outras características importantes dos algoritmos de ordenação:
        * Complexidade de Espaço
        * Estabilidade de Chaves
            * Um algoritmo de ordenação é estável em relação as chaves se as chaves equivalentes mantém a mesma ordem relativa da entrada, no resultado final.

4. Algoritmos de ordenação em O(N)
    * _Integer Sorting_
        * Requer que as chaves são inteiros entre $\{0, 1, \ldots, K-1\}$
        * Pode-se fazer muito mais que apenas comparações
        * Para $k = n^{O(1)}$, pode-se ordenar com complexidade de tempo $O(n)$
    * `Pidgeonhole Sorting`:
        ```nohl
        L = array de k listas vazias
        for j in 0...(n-1):
            L[key(A[j])].append(A[j])
        output = []
        for i in 0..(k-1):
            output.extend(L[k])
        ```
    * `Counting Sort`
        * Dado um _array_ com $n$ elementos e $k$ chaves.
        * Cria um _array_ com $k$ posições e um _array_ de retorno de $n$.
        * Para cada chave, soma 1 na posição da chave.
        * Percorre o algoritmo adicionando as chaves ao array.
        * `Counting sort`:
            ```nohl
            function CountingSort(input, k)

                count ← array of k + 1 zeros
                output ← array of same length as input

                for i = 0 to length(input) - 1 do
                    j = key(input[i])
                    count[j] = count[j] + 1

                for i = 1 to k do
                    count[i] = count[i] + count[i - 1]

                for i = length(input) - 1 down to 0 do
                    j = key(input[i])
                    count[j] = count[j] - 1
                    output[count[j]] = input[i]

                return output
            ```
        * Características:
            * Complexidade de Tempo: $O(n + k)$
            * Complexidade de espaço: $O(n + k)$
            * O `counting sort` é estável.
    * `Radix Sort`
        - Imagine os inteiros como sendo inteiros em uma base $b$.
        - número de dígitos é $d = \log_{b}k$
        - Ordenar os números do dígito menos significativo para o dígito mais significativo, com um algoritmo de ordenação estável.
        - Tempo de ordenação: $O(d(n + k))$, quando $k = n^{O(1)}$, $O(n)$
            

## Questões

1. Mostre, intuitivamente, que o algoritmo `Selection Sort` não é estável para as chaves.
2. O que é necessário para que a implementação do algoritmo `Insertion Sort` seja estável para as chaves?
3. Implemente o algoritmo `Quicksort`. Qual a complexidade de espaço utilizada na sua implementação?
4. Baseado no uso de um `max_heap`, o algoritmo `Heapsort` tem complexidade de tempo $\Theta(n\log{n})$ e de espaço $O(1)$. Escreva um artigo, de no máximo duas páginas, incluindo o código ou pseudocódgio do algoritmo, e demonstrando a sua complexidade. Crie uma hipótese para o motivo dele não ser estável em relação à ordenaçào das chaves.

## Recursos para essa aula

1. Algoritmos de ordenação [implementados em Python](/teaching/code/algorithms/sorting.py)

