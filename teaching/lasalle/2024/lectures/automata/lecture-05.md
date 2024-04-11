---
section: Linguagens Formais e Autômatos
title: Linguagens, Gramáticas e Autômatos
subtitle:
layout: lecture
last_occurrence: 2024-04-04
copy: 2024
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2024/automata
extra_styles:
  - tikzimage
---

## Linguagens

Um **alfabeto**, representado pelo símbolo $\Sigma$, é um [conjunto](/teaching/cs/math/sets) finito de símbolos ou caracteres.

Uma **palavra**, cadeia de caracteres, sentença ou **string** sobre um alfabeto é uma sequência finita de símbolos do alfabeto justapostos.

Um elemento importante em linguagens é a **palavra vazia**, representada pelo símbolo $\varepsilon$, que é uma palavra de _tamanho zero_, ou seja, uma palavra sem nenhum símbolo.

**Prefixo** de uma palavra é qualquer sequência de símbolos contígua inicial da palavra. **Sufixo** é semelhante, mas no final da plavara. **Subpalavra** (ou **substring**) é qualquer sequência de símbolos contígua de símbolos da palvara. A palavra vazia é sempre um prefixo, sufixo ou subpalavra de uma palavra. 

> Em uma linguagem de programação, uma palavra é um programa.

**Concatenação**: A concatenação é uma operação binária denotada por $a \cdot b$ ou $ab$.

A concatenação é associativa,: $(ab)c = a(bc)$ e por isso não utilizamos parentesespara definir esta operação.

O elemento neutro da concatenação é a palavra vazia, ou seja, $\varepsilon{w} = w = w\varepsilon$.

A concatenação sucessiva é representava por $w^n$, onde $w$ é uma palavro e $n$ é o número de vezes que a palavra é concatedada, por exemplo, $w = a, w^4 = aaaa$

Seja um alfabeto $\Sigma$, então $\Sigma^{\*}$ é o conjunto de todas as palavras possíveis a partir do alfabeto, incluindo $\varepsilon$, e $\Sigma^{+}$ é o conjunto formado por $\Sigma^{\*} - \{\varepsilon\}$.

**Exemplo**, prove por indução que toda palavra $w$ sobre um alfabeto $\Sigma$ é uma palavra de $\Sigma^\*$.
* Base de indução
    * $\varepsilon \in \Sigma^\*$
    * para qualquer $x \in \Sigma$, value que $x \in \Sigma^\*$
* Passo de Indução
    * Seja $u \in \Sigma$, $v \in \Sigma$, logo $u \in \Sigma^\*$ e $v \in \Sigma^\*$
    * Então $uv \in \Sigma^\*\quad\square$ 

Uma **linguagem formal** sobre um alfabeto $\Sigma$, denotada por $L$ é um conjunto de palavras sobre $\Sigma$, logo $L \subseteq \Sigma^\*$

* O conjunto vazio $\varnothing$ e o conjunto formao pela palvara vazia $\{\varepsilon\}$ são linguagens sobre qualquer alfabeto. Obviamente $\varnothing \neq \{\varepsilon\}$.
* Os conjustos $\Sigma^\*$ e $\Sigma^+$ são linguagens sobre um alfabeto $\Sigma$.
* Linguagens podem ser infinitas, por exemplo, seja $\Sigma = \{a, b\}$, a linguagem formada por todos os elementos que formam palíndromos sobre $\Sigma$ é uma linguagem infinita.
* O conjunto de todas as lingugens sobre um alfabeto é dado por $\mathcal{P}(\Sigma^\*)$.


## Gramática

Uma gramática de Chomsky é uma 4-upla $G=(V, T, P, S)$, onde;

* $V$ é um conjunto finito de símbolos não-terminais
* $T$ é um conjunto finito de símbolos terminais
* $V$ e $T$ são disjuntos, logo, $V \cap T = \varnothing$
* $P$ é uma relação finita $P: (V \cup T)^+ \rightarrow (V \cup T)^\*$ onde cada par da relação é uma regra de produção
* $S$ é o símbolo inicial da gramática.

As regras de produção $(\alpha, \beta)$ são representadas por $\alpha \rightarrow \beta$.

É possível que o mesmo símbolo possua várias regras associadas:

$$
\begin{align}
\alpha \rightarrow & \:\beta_1 \\
\alpha \rightarrow & \:\beta_2 \\
\dots \\
\alpha \rightarrow & \:\beta_n
\end{align}
$$

E nesse caso, por conveniência, podemos representar a regra como $\alpha \rightarrow \beta_1 \| \beta_2 \| \dots \| \beta_n$.

A linguagem gerada são todas as palavros de símbolos terminais, deriváveis a partir do símbolo inicial $S$. Podemos definir todas as palavras de uma linguagem $L$ geradas a partir da gramática $G$ como:

$$
L(G) = \{w in T^\* \| S \implies^\+ w\}
$$

Onde $S\implies^+ w$ é a aplicação recursiva das regras de produção da gramática $G$, iniciando em $S$ até que $w$ seja gerado.


## Automato Finito

Estudar a teoria da computação a partir de uma máquina complexa como um computador real insere um número muito grande de variáveis para que seja possível construir uma teoria matemática manejável, sobre o o que é computação e o que é um computador. Ao invés disso, utilizamos **modelos computacionais**, que simplificam a forma como descrevemos uma máquina.

O primeiro modelo computacional que estudamos é o modelo mais simples, conhecido como **máquina de estados finitos** ou **autômato finito**.

Uma forma de representar um autômato finito é utilizando uma representação gráfica dos estados e transições:

![Automato Liga-Desliga](/images/on_off_automata.svg)

Um automato finito pode ser definido formalemente como uma 5-upla $M = (\Sigma, Q, S, q_0, F)$, onde:

* $\Sigma$ é um alfabeto
* $Q$ é um conjunto de estados de $M$
* $\gamma$ é uma relação que define as regras de transição definida por $\gamma: (Q \times \Sigma) \rightarrow Q$, ou seja, $\gamma$ é uma função onde dado um estado pertencente a $Q$ e um símbolo do alfabeto $\Sigma$ resulta em um estado de $Q$.
* $q_0$ é um estado e $q_0 \in Q$.
* $F$ é o conjunto de estados finais (ou de aceitação) e $F \subseteq Q$.

Seja $M = (\Sigma, Q, S, q_0, F)$ um autômato finito e suponha que $w = w_{1}w_{2}\dots{w}_n$ seja uma cadeia de caracteres ond cada $w_i$ pertence ao alfabeto $\Sigma$, então $M$ **aceita** $w$ se existe uma sequência de estados $r_0, r_1, \dots, r_n \in Q$ com três condições:

1. $r_0 = q_0$, ou seja, a máquina começa no estado inicial
2. $\gamma(r_i, w_{i+1}) = r_{i+1}$, para i = 0, $\dots$, n-1. (A máquina troca de estados conforme a função de trasição.)
3. $r_n \in F$, que diz que a o último estado atingido é um estado final

Dizemos que $M$ **reconhece a linguagem** $A$ se $A = \\{w \| M\\:\text{aceita}\\:w\\}$.

Por exemplo, dado o seguinte autômato determinísitico:

![(aa\*b)*a*a](/images/no_bb_ends_with_a.svg)

A linguagem aceita pelo autômato é composta por todas as palavras iniciadas e terminadas pela letra $a$, podem conter $b$, mas não possuem a subpalavra $bb$.

Note que para todo símbolo para o qual não há transição a partir de um estado, o autômato deveria ser direcionado a um estado de erro $e$, tal que $e \notin F$, e nesse estado todo símbolo em $\Sigma$ leva novamente a $e$.

Para deixar a representação gráfica mais simples, não incluimos o estado de erro, e assumimos que quando não existe uma transição $\gamma(q_n, \alpha)$ para um estado $q_n \in Q$ e um símbolo $\alpha \in \Sigma$, o autômato $M$ não aceita a palavra.


### Questões

1. Construa autômatos finitos que aceitam as seguintes linguagens:
    * Números pares de a's e b's.
    * Pelo menos um par de a's ou b's
    * Contém $abab$


## Preparação para a próxima aula

1. [Capítulo 1](https://integrada.minhabiblioteca.com.br/reader/books/9788522108862/pageid/53){:target="\_blank"} até a seção 1.4 do livro [**Introdução a Teoria da Computação**](https://integrada.minhabiblioteca.com.br/reader/books/9788522108862){:id="sipser" target="\_blank"}
2. Capítulo 2 e capítulo 3 (até a seção 3.5) do livro [Linguages Formais e Autômatos](https://integrada.minhabiblioteca.com.br/reader/books/9788577807994){:target="\_blank"}  de Paulo Blauth Menezes.
3. Capítulos 2 e 4 (menos a seção 4.1) do [Livro do Hopcroft](/teaching/lasalle/2024/automata#hopcroft)

## Recursos para essa aula

### Bibliografia

1. [Capítulo 1](https://integrada.minhabiblioteca.com.br/reader/books/9788522108862/pageid/53){:target="\_blank"} até a página 44 do livro [**Introdução a Teoria da Computação**](https://integrada.minhabiblioteca.com.br/reader/books/9788522108862){:id="sipser" target="\_blank"}
2. Capítulo 2 e capítulo 3 (até a seção 3.3) do livro [Linguages Formais e Autômatos](https://integrada.minhabiblioteca.com.br/reader/books/9788577807994){:target="\_blank"}  de Paulo Blauth Menezes.
3. Capítulo 1, seção 1.5 e Capítulo 2 até a seção 2.2 do [Livro do Hopcroft](/teaching/lasalle/2024/automata#hopcroft)

