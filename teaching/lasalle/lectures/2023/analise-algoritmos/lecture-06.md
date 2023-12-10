---
title: Recursão, Método Master e Árvores Binárias de Pesquisa
subtitle: Complexidade de Algoritmos e Análise de Desempenho
layout: lecture
last_occurrence: 2023-09-11
copy: 2023
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2023-02-analise-algoritmos
---
## Assunto

1. Recursão
2. Divisão e Conquista
    * Muitos algoritmos úteis são _recursivos_ na sua estrutura. Para resolver um problema eles chamam a si mesmos resolvendo instâncias mais simples do mesmo problema, resolvendo os subproblemas recursivamente e combinando as soluções para resorver o preblema original
    * Passos do paradigma _Divisão e Conquista_:
        1. **Divisão**
            : Divide o problema em subproblemas que são instâncias menore que o problema original
        2. **Conquista**
            : Resolve os problemas menores, onde, em alguns casos, a solução é trivial.
        3. **Combinação**
            : Combina as soluções dos subproblemas para resolver o problema original.
    * Exemplo: _Merge Sort_
        * **Divisão**
            : Divide a sequência de $n$ elementos a ser ordenada em duas subsequências de n/2 elementos cada.
        * **Conquista**
            : Ordena as duas subsequências recursivamente, utilizando o _merge sort_.
        * **Combinação**
            : Junta as duas sequências, mantendo o resultado ordenado, para produzir a resposta.
        * Note que a recursão termina quando a ordenação do _array_ é trivial e não precisa ser executada (_array_ de um elemento).
        * A operação chave é a combinação dos dois _arrays_ ordenados, onde a complexidade de tempo é $\Theta(n)$ 
    * Análise de complexidade em algoritmos de divisão e conquista
        * Podemos descrever o tempo de execução do algoritom utilizando uma **equação de recorrência**, que descreve o tempo de execução do problema de tamanho $n$ em termos do tempo de execução dos problemas menores.
        * Dado que $T(n)$ o tempo de execução do problema de tamanho $n$.
        * Dado que para um problema pequeno o suficiente, quando $n \le c$ para uma constante $c$, a solução trivial é executada em tempo constante, $\Theta(1)$
        * Se dividirmos o problema em $a$ subproblemas, cada um com tamanho $\frac{1}{b}$ do tamanho original, e levando $D(n)$ tempo para a divisão e $C(n)$ tempo para combinar as soluções, obtemos então a equação de recorrência:
$$
T(n) = 
\begin{cases}
\: \Theta(1) & \quad se \: n \le c \\
\: aT(n/b) + D(n) + C(n) & \quad caso \: contrário \\
\end{cases}
$$
    * Análise do _Merge Sort_
        * Para simplificar a análise do _merge sort_, assumimos que o tamanho da entrada é uma potência de 2 $\(n = 2^{\Theta(1)}\)$.
        * A cada divisão os subproblemas tem os $n$ elementos divididos em $\frac{n}{2}$ elementos.
        * Quando o subproblema tem $n = 1$ elementos, a ordenação é trivial, não necessitando de nenhuma operação, logo $\Theta(1)$ se $n = 1$.
        * Para $n \gt 1:
            * **Divisão**
                : Basta calcular o índice do elemento do meio do _subarray_, que pode ser feito em tempo constante, logo $D(n) = \Theta(1)$
            * **Conquista**
                : Recursivamente se resolve dois subprobleams ($a = 2$) de tamanho $\frac{n}{2}$ ($b = 2$), que contribui com $2T\(\frac{n}{2}\)$ para o tempo de execução
            * **Combinação**
                : Já vimos que a complexidade de tempo para combinar os elementos é $\Theta(n)$, logo, $C(n) = \Theta(n)$
        * Logo a recorrência para o tempo de execução do pior caso do _merge sorte_ é dada por:
$$
T(n) = 
\begin{cases}
\: \Theta(1) & \quad se \: n = 1 \\
\: 2T(n/2) + \Theta(n) & \quad se \: n \gt 1 \\
\end{cases}
$$

        * Intuitivamente, podemos resolver essa recorrência. Reescrevemos a recorrência como:
$$
T(n) = 
\begin{cases}
\: c & \quad se \: n = 1 \\
\: 2T(n/2) + cn & \quad se \: n \gt 1 \\
\end{cases}
$$

        * Sabemos que o tempo total de execução é $T(n)$, que é o tempo da combinação $cn$ somado aos tempos dos subproblemas de tamanho $\frac{n}{2}$, ou seja, $T(\frac{n}{2})$.
        * Cada subproblema $T(n/2)$ leva $\frac{cn}{2}$ mais $T(n/4)$, e assim sucessivamente até que o problema seja trivial ($n = 1$) onde o custo de resolver cada um dos problemas é $c$
        * Se representarmos esse problema como uma árvore de recursão, a soma dos tempos de cada nível da árvore é $cn$, e a altura da árvore é $1 + \log(n)$ (mais especificamente $1 + \log_{2}{n}$)
        * Logo o tempo total de execução é $cn \log n + cn$, onde, pela análise assintótica, temos $\Theta(n \log{n})$.
4. Método Master
    * Podemos resolver as recorrências dos algoritmos recursivos através de:
        * **Método da Substituição**
            : Escolhemos um limite e utilizamos indução matemática para provar que nossa escolha estava correta.
        * **Método da árvore de recursão**
            : Convertemos a recorrência numa árvore onde os nós representam os custos de execução em cada um dos níveis da recursão e utilizamos técnicas para encotrar os limites dos somatórias para resolver a recorrência
        * **Método master**
            : Que provê limites para recorrências do tipo $T(n) = aT(\frac{n}{b})+f(n)$, quando $a \ge 1$, $b \gt 1$.
    * Para utilizar o **método master** é preciso decorar três casos, e, com isso, você consegue determinar os limites assintóticos para diversas recorrências.
    * O **método master** depende do **Teorema Master**:
        * Sejam $a \ge 1$ e $b \gt 1$ constantes, seja $f(n)$ uma função, e $T(n)$ definido para inteiros não-negativos pela recorrência $T(n) = aT(\frac{n}{b}) + f(n)$, onde $\frac{n}{b}$ significa $\lceil\frac{n}{b}\rceil$ ou $\lfloor\frac{n}{b}\rfloor$,
        * Então $T(n)$  tem os seguintes limites assintóticos:
            * **Caso 1**
                : Se $f(n) = O(n^{\log_{b}a - \epsilon})$ para alguma constante $\epsilon \gt 0$, então $T(n) = \Theta(n^{\log_{b}a})$
                : ou seja, o tempo de resolver os subproblemas se sobropõe ao tempo de dividir/combinar.
            * **Caso 2**
                : Se $f(n) = \Theta(n^{\log_{b}a}\log^{k}n)$, então $T(n) = \Theta(n^{\log_{b}a}\log^{k+1}{n})$
                : ou seja, os tempos de resolver os subproblemas e de dividir/combinar são semelhantes. $T(n) = \Theta(n^{\log_{b}a} \log{n}) = \Theta(f(n) \log{n})$
            * **Caso 3**
                : Se $f(n) = \Omega(n^{\log_{b}a + \epsilon})$ para alguma constante $\epsilon \gt 0$, e se $af(\frac{n}{b}) \le cf(n)$ para alguma constante $c \lt 1$ e todo $n$ suficientemente grande, então $T(n) = \Theta(f(n))$
                : ou seja, o tempo de dividir/combinar se sobrepõe ao tempo de resolver os subproblemas.
    * Para os casos entre o caso 2 e 3, temos as seguintes extensões:
        * **Caso 2a**
            : Se $f(n) = \Theta(n^{\log_{b}a - \epsilon}\log^{k}n)$ para $k \gt -1$, então $T(n) \Theta(n^{\log_{b}a - \epsilon}\log^{k+1}n)$
        * **Caso 2b**
            : Se $f(n) = \Theta(n^{\log_{b}a - \epsilon}\log^{k}n)$ para $k = -1$, então $T(n) \Theta(n^{\log_{b}a - \epsilon}\log\log{n})$
        * **Caso 2c**
            : Se $f(n) = \Theta(n^{\log_{b}a - \epsilon}\log^{k}n)$ para $k \lt -1$, então $T(n) \Theta(n^{\log_{b}a - \epsilon})$ 
    * Exemplos de aplicação do _método master_
        * $T(n) = 9T(\frac{n}{3}) + n$
            * a = 9
            * b = 3
            * $f(n) = n$
            * Onde temos que $n^{\log_{b}a} = n^{\log_{3}9} = \Theta(n^2)$
            * Como $f(n) = O(n^{\log_{3}9})$, com $\epsilon = 1$, podemos aplicar o caso 1
            * Logo $T(n) = \Theta(n^2)$
        * $T(n) = T(\frac{2n}{3}) + 1$
            * a = 1
            * b = $\frac{3}{2}$
            * $f(n) = 1$
            * Onde temos que $n^{\log_{b}a} = n^{\log_{\frac{3}{2}}1} = n^0 = 1$
            * Como $f(n) = \Theta(1)$ podemos aplicar o caso 2
            * Logo $T(n) = \Theta(\log{n})$
        * $T(n) = 3T(\frac{n}{4}) + n\log{n}$
            * a = 3
            * b = 4
            * $f(n) = n\log{n}$
            * Onde temos que $n^{\log_{b}a} = n^{\log_{4}3} = O(n^{0.793})$
            * Como $f(n) = \Omega(n^{\log_{4}3+\epsilon})$, onde $\epsilon \approx 0.2$ podemos aplicar o caso 3, caso possamos mostrar que a condição de regularidade é valida para $f(n)$.
            * Para um $n$ suficientemente largo, temos $af(\frac{n}{b}) = 3(\frac{n}{4})\log(\frac{n}{4}) \le (\frac{3}{4})n\log{n} = cf(n)$ para $c = \frac{3}{4}$. 
            * Logo, podemos aplicar o caso 3, e $T(n) = \Theta(n\log{n})$
        * $T(n) = 2T(\frac{n}{2}) + n\log{n}$
            * a = 2
            * b = 2
            * $f(n) = n\log{n}$
            * $n^{\log_{b}a} = n$
            * Aparentemente, poderíamos aplicar o caso 3, uma vez que $f(n) = n\log{n}$ é assintóticamente maior que $n^{\log_{b}a} = n$, porém não é **polinomialmente maior**.
            * A razão $\frac{f(n)}{n^{\log_{b}a}} = \frac{(n\log{n})}{n} = \log{n} $, que é assintoticamente menor que $n^\epsilon$ para qualquer $\epsilon$ positivo e constante, porém não é polinomialmente maior.
            * Porém, podemos aplicar o **caso 2a**, uma vez que $k = 1$, logo temos $T(n) = \Theta(n^{\log_{2}2}\log^{1+1}n) = \Theta(n\log^{2}n)$
3. Árvores Binárias de Pesquisa
    * Regra de criação:
        * `insert(node.left, k) if k < node.key else insert(node.right, k)`
    * Complexidade do pior caso:
        * Inserção: $O(n)$
        * Exclusão: $O(n)$
        * Busca: $O(n)$
    * Complexidade do melhor caso:
        * Inserção: $O(\log{n})$
        * Exclusão: $O(\log{n})$
        * Busca: $O(\log{n})$
    * Árvores Binárias de Pesquisa auto-balanceáveis
        * Árvores AVL
            * Algoritmos:
                * Inserção
                    : após a inserção na BST, os nós, a partir do nó-pai do nó inserido, tem os fatores de balanceamento corrigidos até que a altura do nó não se altere, ou seja corrigida a raiz da árvore.
                * Exclusão
                    : após a exclusão na BST, os nós, a partir do nó-pai do nó removido, tem os fatores de balanceamento corrigidos até que a altura do nó não se altere, ou seja corrigida a raiz da árvore.
                * Validação de um nó AVL:
                    * Fator de Balanceamento: $FB = H(left) - H(right)$
                    * Fator de balanceamento válido: $|FB| \lt 2$
                * Correção do nó AVL:
    >```nohl
if FB(node) == -2:
        if FB(node.left) == +1:
                rotate_left(node.left)
        rotate_right(node)
if FB(node) == +2:
        if FB(node.right) == -1:
                rotate_right(node.right)
        rotate_left(node)
```

            * Complexidade:
                * Busca: $\Theta(\log{n})$
                * Inserção: $\Theta(\log{n})$
                * Exclusão: $\Theta(\log{n})$
            * Rotações: $O(\log{n})$
        * Outros modelos:
            * Árvores Red-Black
            * B-Trees
    * Binary Search Sorting
        * Complexidade de tempo quando se utiliza uma árvore auto-balanceável...
        * Assumindo uma máquina de ponteiros:$\Theta(n\log{n})$
            * Utiliza ponteiros, e cada nó deve armazenar meta dados da estruturas
        * Assumindo uma máquina de acesso aleatório: $O(n\log{n}), amortizado$
            * Cada posiçõa deve armazenar meta dados da estruturas

## Questões

1. Implemente uma árvore binária de pesquisa.
2. Implemente uma árvore binária de pesquisa do tipo AVL.
3. Implemente uma função que verifica se uma sub-árvore é uma árvore AVL válida, com a interface `is_valid_avl(node)`. Qual a complexidade de tempo dessa função?

## Recursos para essa aula

### Bibliografia

1. Cormen, E. et al. **Introduction to Algorithms**. Caps. 2 e 3.
2. [Master Theorem (Analysis of Algorithms)](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms))
3. [Árvores AVL](https://en.wikipedia.org/wiki/AVL_tree) (Wikipedia)
4. [AVL Trees](https://www.geeksforgeeks.org/introduction-to-avl-tree/) (Geeks For Geeks)
