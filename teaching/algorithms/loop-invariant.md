---
layout: main
section: Algortimos
tags:
  - algoritmos
  - análise de algoritmos
  - algoritmos iterativos
title: Prova de correção por invariantes de laço
copy: 2022
date: 2022-02-13
---

Uma `invariante de laço` é uma propriedade do algoritmo iterativo, em relação às suas variáveis, que deve se manter verdadeira _antes_, _durante_ e _depois_ da execução do laço. Uma vez que a invariante de laço mantenha-se verdadeira, podemos afirmar que, em relação à propriedade escolhida, o algoritmo está correto.

Sobre a invariante de laço, devemos demonstrar seu estado da em três momentos, para demonstrar a correção do algoritmo:

* **Inicialização**: É verdadeira antes da primeira iteração do laço.
* **Manutenção**: É verdadeira antes de uma iteração do laço, e mantém-se verdadeira antes da próxima iteração.
* **Finalização**: É verdadeira quando o loop termina.

A prova de correção de algoritmos por invariantes de laço são semelhantes à prova por indução.

Para entender melhor como funcionam as invariantes de laço, três exemplos serão analizados.


## Busca Linear

A busta linear, ou sequencial, é um algoritmo de busca exaustiva em listas. O algoritmo verifica cada elemento da lista até encontrar uma correspondência, ou até que não existam mais elementos na lista.

O pseudo-código para a busca linear pode ser definido como:

```
linear_search(A, v):
   for i in 1..A.length:
       if A[i] == v:
          return i
   return nil
```

> **Nota**: _arrays_ possuem índices começando em 1.  

O algoritmo possui um único laço, onde a iteração será executada para cada um dos elementos da lista.

A definição da invariante do laço para a busca linear é:

> O valor v não está na lista `A[1..i-1]`.

* **Inicialização**:
    * Antes da primeira iteração, `i = 1` e `A[1..i)` é um conjunto vazio, logo, `v` não pertence ao conjunto, sendo a invariante verdadeira.

* **Manutenção**:
    * Para a _i-ésima_ iteração do laço, se `A[i] == v`, o laço termina, logo, a iteração só ocorre se `v` não pertence a `A[i, i+1)`.

* **Finalização**:
    * O algoritmo termina se `A[i] == v`, onde o elemento procurado é encontrado, ou se não existem mais elementos em `A`, sendo que a invariante `v` não pertence a `A[1..i-1]` se mantém verdadeira para abmos os casos.

Como a invariante se mantém sempre verdadeira, o algoritmo está correto.


# Busca Binária

Apesar de simples, e de encontrar um elemento independente da organização dos dados, a busca linear é ineficiente, uma vez que pode ser necessário analisar todos os elementos da lista.

Caso os elementos de uma lista estejam organizadas em ordem crescente em relação a uma chave `k`, a busca por elementos nessa lista pode ser mais eficiente se utilizarmos uma busca binária.

Na busca binária em uma lista ordenada de elementos `A[1..n]`, comparamos uma chave `k` com um elemento da lista `A[i]`, onde `1 <= i <= n`. Se `k <= A[i]`, como a lista está ordenada, sabemos que `k` está no conjunto `A[1..i]`, caso contrário, sabemos que `k` está no conjunto `A[i+1..n]`.

O pseudo-código para a busca binária iterativa pode ser definido da seguinte forma:

```
binary_search(A, k):
    p = 1
    q = A.length
    while p != q:
        m = p + (q - p) / 2
        if k <= A[m]:
            q = m
        else:
            p = m + 1
    if k != A[q]:
        return nil
    return p
```

A invariante do laço pode ser definida como:

> Se `k` está em `A[1..n]`, então `k` está na lista `A[p..q]` que está contida em `A[1..n]`.

* **Inicialização**:
    * Na inicialização do algorimo, `p = 1` e `q = n`, logo, se `k` esta na lista `A[1..n]`, está na lista `A[p..q]`, sendo a invariante verdadeira.

* **Manutenção**:
    * Dado que `p <= m <= q`, como a lista está ordenada, se `k <= A[m]`, `k` está em `A[p..m]`, logo, sendo `q = m`, então `k` está em `A[p..q]`. Caso contrário se `k > A[m]`, logo, sendo `p = m + 1`, então `k` está em `A[p..q]`, sendo verdadeira a invariante.

* **Finalização**:
    * O algoritmo termina quando `p = q`, sendo que se `k == A[q]` a chave foi encontrada, caso contrario, o elemento não existe na lista.


## Insertion Sort

Para que a _busca binária_ possa ser utilizada é necessáro que a lista de elementos esteja ordenada de acordo com uma chave. O problema da ordenação pode ser definido em função da sua entrada e saída esperada:

> Entrada: lista de N elementos A = {a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n-1</sub>, a<sub>n</sub>} <br/>
> Saída: lista de N elementos A<sup>'</sup>, tal que A<sup>'</sup> = {a<sup>'</sup><sub>1</sub> <= a<sup>'</sup><sub>2</sub> <= ... <= a<sup>'</sup><sub>n-1</sub> <= a<sup>'</sup><sub>n</sub>} e a<sup>'</sup><sub>j</sub> pertence a A, para todo j pertencente a [1..n].

Podemos definir o pseudo-código para o algoritmo `Insertion Sort` como:

```
insertion_sort(A):
    for j in 2 to A.length:
        k = A[j]
        i = j - 1
        while i > 0 and A[i] > k:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = k
```

> **Nota**: _arrays_ possuem índices começando em 1.  

O algoritmo é formado por dois laços. O laço externo irá iterar sobre todos os elementos da lista, a partir do segundo elemento, e o laço interno ira iterar sobre todos os elementos anteriores ao _i-ésimo_ elemento.

Para verificar a correção do algoritmo _insertion sort_, definimos a invariante de laço como:

> A cada iteração de laço `for`, a sub-sequência A[1..j-1] consiste dos elementos originais em A[1..j-1], porém, ordenados.

E verificamos se a invariante é verdadeira:

* **Inicialização**:
  * Antes da primeira iteração, quando j = 2, a sub-sequência A[1..j-1] é formado por um único elemento, o elemento original A[1], e obviamente, esta sub-sequência está ordenada, logo, a invariante de laço é verdadeira na inicialização.

* **Manutenção**:
    * Informalmente, o laço `for` move elementos A[j-1], A[j-2], A[j-3] e assim por diante, uma posição à direita, até que encontre a posição adequada para o elemento A[j]. Nesse ponto, os elementos da sub-sequência A[1..j] consistem dos elementos originais A[1..j] ordenados. Incrementando o valor de j para a próxima iteração garante que a invariante de laço mantém-se verdadeira.

* **Finalização**:
    * A condição que faz com que o laço `for` termine é que j seja maior que o número de elementos em A (n). Como incrementamos j de 1 em 1, o loop terminará com j = n + 1. Substituindo j na invariante do laço, temos que a sub-sequência A[1..n+1-1], ou seja A[1..n], consiste dos elementos originais de A e está ordenada. Como a sequência A[1..n] é a sequência completa concluímos que todos os elementos foram ordenados.

Para uma prova de todo o algoritmo, devemos demostrar que o laço interno, o `while`, está correto:

Invariante do laço: os elementos A[i..j] são maiores ou iguais a k.

* **Inicialização**:
    * Na inicialização, o laço só inicia caso A[i] > k, dado i = j - 1 e k = A[j], logo, a invariante é verdadeira.

* **Manutenção**:
    * A invariante é mantida movendo valores em A que são sabidamente maiores que k, movendo o valor de A[i] para a posição A[i + 1], que se sabe que tinha um valor, pelo menos, igual ou maior que k.

* **Finalização**:
    * O loop termina quando A[i] <= k, e como os elementos A[1..j] estão ordenados, todos os elementos A[i..j] são maiores ou iguais a k, sendo verdadeira a invariante.


## Uso de invariantes de laço

Podemos utilizar invariantes de laço para demonstrar se um algoritmo iterativo está correto ou não. Para isso definimos a invariante de laço e demonstramos que é verdadeira na _inicialização_, _manutenção_ e _finalização_ do laço. Se a propriedade avaliada pela invariante de laço for verdadeira nas três situações, dizemos que o programa está correto segundo a propriedade escolhida.


## Referências

1. Cormen et al. **Introduction to Algoritms**. MIT Press. 2014.
2. Robert Sedwick; Kevin Wayne. **Algorithms**. Addisson-Wesley Professional. 2011.
