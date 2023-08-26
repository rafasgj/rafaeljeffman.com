---
title: Análise Assintótica
subtitle: Complexidade de Algoritmos e Análise de Desempenho
layout: lecture
last_occurrence: 2023-08-21
copy: 2023
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2023-02-analise-algoritmos
---

## Assunto

1. Complexidade de Algoritmos
    * A complexidade de um algoritmo reflete o esforço computacional requerido para executá-lo.
    * As principais medidas de complexidade são a velocidade de execução, o consumo de memória e a quantidade de comunicação (mais utilizada em algoritmos distribuídos).
    * A análise matemática do tempo de execução de um algoritmo permite que a análise seja independente da implementação, hardware e ambiente, reduzindo o número de variáveis na obtenção de um comportamento esperado para o algoritmo.
    * O esforço computacional está, normalmente, relacionado ao tamanho da entrada de dados do algoritmo (ex.: ordenação de elementos, inversão de matriz, número de Fibonacci).
    * Além do tamanho da entrada, a organização dos elementos pode ser relevante na determinação do desempenho do algoritmo.
2. Complexidade de Tempo
    * Em geral é o tipo de complexidade que mais nos preocupamos.
    * Está relacionada ao tempo de execução de um algoritmo.
    * Medida em relação ao número de operações que o algoritmo executa no modelo computacional utilizado na sua criação.
3. Complexidade de Espaço
    * Medida de desempenho relacionada a quantidade de memória necessária para a execução de um algoritmo.
4. Complexidade de Comunicação
    * Em algoritmos distribuídos, o tempo de comunicação é muito relevante e é mais uma medida de complexidade que deve ser considerada.
    * A complexidade de comunicação esta fora do escopo dessa disciplina, porém acredito que com a base proporcionada, aliada a de outras disciplinas, permitirá que o aluno encentre as soluções para esse tipo de problema.
5. Modelo computacional para análise de desempenho
    * Para analizar o desempenho de um algoritmo, precisamos definir o modelo computacional sobre o qual queremos verificar o número de operações
    * Definimos uma _operação fundamental_ que é a base do algoritmo, e assumimos que o algoritmo irá executar mais rapidamente com a redução do número de execuções dessa operação (ex.: comparação em relação a ordem em algoritmos de ordenação, comparação em relação a igualdade em algoritmos de busca).
6. Exemplo: Valor máximo em uma lista.
7. Tempo de Execução de um algoritmo<br/>
$$
t(a,n) = \frac{c + T(a)\times{n}}{\frac{op}{s}}
$$ 
<br/>Dada uma máquina com $X$ operações por segundo, e outra com $2X$ operações por segundo, a segunda máquina executaria o mesmo algoritmo em, aproximadamente, metade do tempo da primeira, para a mesma entrada.
8. Complexidade de Algoritmos
    * A _complexidade assintótica_ é definida pelo crescimento da complexidade para entradas suficientemente grandes.
    * Levando em consideração a execução de dois algoritmos na mesma máquina, com a mesma entrada, temos uma comparação entre $c_{1} + T(a_{1})\times{n}$ com $c_{2} + T(a_{2}\times{n})$, onde claramente as constantes associadas aos algoritmos ($c_{1}$ e $c_{2}$) tem influência na comparação.
    * No entanto, para valores muito grandes de $n$, a diferença entre as contantes tende a ser desprezível, fazendo com que a diferença da complexidade de tempo dos algoritmos domine a comparação.
    * Exemplos:
        * Busca Exaustiva:

        ```nohl
        func linear_search(A, v):
            for i in 1..A.length:
                if A[i] == v:
                    return i
            return nil
        ```

        * Busca Binária:

        ```nohl
        func binary_search(A, k):
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

        * Ordenação por Inserção:

        ```nohl
        func insertion_sort(A):
            for j in 2 to A.length:
                k = A[j]
                i = j - 1
                while i > 0 and A[i] > k:
                    A[i + 1] = A[i]
                    i = i - 1
                A[i + 1] = k
```
9. Complexidade Assintótica
    * Usualmente o cálculo da complexidade concentra-se em determinar a ordem de magnitude do número de operações fundamentais na execução de um algoritmo. Podemos utilizar a ideia de _cota assintótica superior_.
    * Dada a função $f(n)$, uma função $g(n)$ representa $O(g(n))$ se $(\exists n\_{0} \in \mathbb{N})\ (\forall n \ge n_{0}): f(n) \le g(n)$
    * Uma função que sempre domine outra (ex. $n^{2} \ge n$) representa uma cota assintótica superior.
    * Basta que uma função domine a outra apenas a partir de um número $n\_{0}$, com _n grande o suficiente_, para que seja considerada uma cota assintótica superior
10. Notação Big-O
    * Se uma função $c \in \mathbb{R}^{+}: c\times{g}(n)$ domina uma função $f(n)$, a partir de um $n\_{0} \in \mathbb{N}$, temos $f(n) = O(g(n))$, ou seja, $(\exists c \in \mathbb{R}^{+})(\exists n_{0} \in \mathbb{N})(\forall n \ge n_{0}): f(n) \le c\times{g}(n)$
    * Dizer que um algoritmo é $O(n)$ significa que o tempo de execução do algoritmo é diretamente proporcional a sua entrada, com limite superior dado por uma função linear $g(n) = c \times n$.
    * Dizer que um algoritom é $O(1)$ significa dizer que o número de operações fundamentais é limitado por uma constante.
11. Notação $\Omega$
    * Se uma função $c \in \mathbb{R}^{+}: {g}(n)$ é dominada por uma função $c\times f(n)$, a partir de um $n\_{0} \in \mathbb{N}$, temos $f(n) = O(g(n))$, ou seja, $(\exists c \in \mathbb{R}^{+})(\exists n_{0} \in \mathbb{N})(\forall n \ge n_{0}): c\times{f}(n) \ge g(n)$.
    * A notação $\Omega$ define uma cota assintótica inferior.
12. Notação $\Theta$
    * Dadas duas funções $f(n)$ e $g(n)$ e duas constanstes $c \in \mathbb{N}$ e $d \in \mathbb{N}$ , $f(n) \ \Theta(g(n))$, se e apenas se, $c\times{g}(n) \le f(n) \le d\times{g}(n)$ 
    * A notação $\Theta$ define um limite assintótico exato.


## Questões

1. Por que a medida de tempo gasto na execução de um algoritmo não é uma boa medida para determinar a complexidade de tempo para um algoritmo?
2. É razoável esperar que o desempenho de um algoritmo sempre cresça com o tamanho da entrada? Justifique sua resposta.
3. Calcule a complexidade do algoritmo de ordenação `Selection Sort`. Qual é a complexidade Big-O? Qual é a complexidade $\Omega$?
4. Qual a complexidade de espaço dos algoritmos apresentados nessa aula?
5. **Projeto de Implementação:** Implementar os algoritmos de ordenação `Insertion Sort` e `Merge Sort` e imprimir ao final da execução o número de operações fundamentais que foram executadas.


## Recursos para essa aula

### Bibliografia

Toscani, Laira Vieira; Veloso, Paulo A. S. **Complexidade de Algoritmos**. Capítulo 2.
