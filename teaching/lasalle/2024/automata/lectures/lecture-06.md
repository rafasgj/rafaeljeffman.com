---
section: Linguagens Formais e Autômatos
title: Automatos Finitos
subtitle:
layout: lecture
last_occurrence: 2024-04-11
copy: 2024
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2024/automata
extra_styles:
  - lecture
  - tikzimage
---

## Linguagens Regulares

A _Hierarquia de Chomsky_ é uma forma de classificar tipos de linguagens, proposta originalmente por Noam Chomsky. Esta classificação tem sido utilizada em áreas como linguística, ciência da computação e teoria de lingagens formais.

Uma gramática formal descreve como criar palavras, a partir de um alfabeto, que são válidas de acordo com as regras sitáticas da linguagem. A hierarquia de Chomsky contém quatra classes de linguagens de complexidade crescente, onde cada classe mais complexa consegue gerar as linguagens mais simples.

![Hierarquia de Chomsky](/images/Chomsky-hierarchy.svg)

A classe de linguagens mais simples da hierarquia de Chomsky é a clase das linguagens regulares.

A gramática de uma liguagem regular é limitada a um único símbolo não terminal à esquerda, e um símbolo terminal, possivelmente seguido de um símbolo não terminal a direita:

$$
\begin{align}
& S \rightarrow aS  \\
& S \rightarrow a
\end{align}
$$

Podemos definir formalmente uma linguagem regular sobre um alfabeto $\Sigma$ de forma recursiva:

* A linguagem vazia, $\varnothing$, é uma linguagem regular
* $\forall a \in \Sigma$, o conjunto unitário $\{a\}$ é uma linguagem regular.
* Se $A$ é uma linguagem regular, $A^\*$ é uma linguagem regular (e por isso que $\{\varepsilon\}$ é uma linguagem regular}.
* Se $A$ e $B$ são linguagens regulares, então $A \cup B$ (união, também representada como $A \mid B$) e $A \centerdot B$ (concatenação, também representada como $AB$), são linguagens regulares
* Nenhuma outra lingugem sbore $\Sigma$ é regular.

> **Teorema**: Toda linguagem regular pode ser reconhecida por uma automato finito determinístico.

Ao longo do texto provaremos essas afirmações.

## Autômatos Finitos Determitísticos (DFA)

Vimos a [definição de autômatos finitos determinísticos](lecture-05#autômato-finito) na última aula.

É importante frisar que a relação de transição $\delta: Q\times\Sigma\rightarrow{Q}$ retorna um único estado possível. É essa característica que determina que o autômato finito tenha um comportamento determinístico, pois dado um estado $q \in Q$ e um símbolo $\alpha \in \Sigma$, só existe, no máximo, um estado $q^\prime \in Q$ que é resultado dessa relação.

Um autômato finito determinístico pode decidir (reconhecer) se uma palavra pertence a lingugem que ele define se, iniciando no estado $q_0$, e trocando de estado pela aplicação da relação de transição para cada símbolo da entrada, na ordem e m que se apresentam, o estado resultante seja $q_n \in F$ (onde $F$ é o conjunto de estados finais ou de aceitação).

## Autômatos Finitos Não-determinísticos (NFA)

Ao contrário da computação determinística, onde sabemos qual o estado a máquina assume dado o estado atual um símbolo de entrada, em uma máquina não-determinística várias escolhas podem existir para o próximo estado em qualquer ponto. 

![NFA](/images/nfa.svg)

Para simular um autômato finito não-determinístico, podemos utilizar técnicas de _backtraking_ ou execução concorrente, onde cada caminho possível é executado em paralelo.

Um automato finito não-determinístico reconhece uma palavra se qualquer caminho executado terminar em um estado de aceitação.

Un NFA pode ter, em um mesmo estado, várias transições com o mesmo símbolo, para outros estados. Pode também ter transições envolvendo a palavra vazia.

Formalmente, um autômato finito não-determinístico é definido como uma 5-upla $(Q, \Sigma, \delta, q_0, F)$, onde:
* $Q$ é o conjunto de estados do autômato;
* $\Sigma$ é o alfabeto sobre a qual a linguagem é definida;
* $\delta: Q\times\Sigma\rightarrow\mathcal{P}(Q)$ é a função de transição;
* $q_0 \in Q$ é o estado inicial;
* $F \subseteq Q$ é o conjunto de estados de acitação.

Note que a diferença de um NFA para um DFA é a definição da relação de transição ($\delta), pois agora o resultado dessa relação é um conjunto de estados em $Q$.

![NFA-e](/images/nfa-e.svg)


## Equivalência NFA-DFA

Apesar do poder de representação de um NFA ser maior que de um DFA, o poder computacional das máquinas criadas com eles é o mesmo, ou seja, qualquer linguagem reconhecida por um NFA pode ser reconhecida por um DFA.

> **Teorema**: Todo autômato finito não-determinístico possui um autômato finito determinístico equivalente.



## Fecho sob as operaçỗes regulares

> **NOTA:** O _fecho_ de uma operação significa que a aplicação desta operação sobre um ou mais elementos de um conjunto  resulta em um elemento do mesmo conjunto.

**Teorema**: A classe das linguagens regulares é fechada sob a operação de união.


**Teorema**: A classe das linguagens regulares é fechada sob a operação de concatenação.


**Teorema**: A classe das linguagens regulares é fechada sob o fecho de Kleene.

### Questões

<!--
1. Dadas as seguintes linguagens, contrua um automato finito que as reconheça:
    *
    *
    *
    *
2. Converta os automatos finitos não-determinísticos em automatos finitos determinísticos:
    *
    *
    *
    *
-->

3. Implemente, utilizando a linguagem Python, um reconhecedor de linguagens regulares baseado em automatos finitos determinísticos:
    * Dados dois conjuntos de dados, sendo:
        * Um a descrição de um automato, contendo:
            * Uma lista de símbolos do alfabeto;
            * Uma lista de estados;
            * Um conjunto de estados finais;
            * Nome do estado inicial;
            * Uma lista de regras de transição, onde cada regra é uma tupla contendo `(origem, símbolo, destino)`
        * Outro, uma lista de palavras.
    * O programa deve validar se a descrição do automato é válida e construir uma estrutura representando o automato.
    * Para cada palavra da lista de palavras:
        * Verificar se uma palavra válida, ou seja, se todos os símbolos da palavra fazem parte do alfabeto da lingugaem;
        * Verificar se o automato finito determinístico reconhece a palavra.
    * O programa deve retornar uma lista de pares contendo`(palavra, resultado)`, onde `resultado` poder ser um valor do conjunto $\\{\text{ACEITA}, \text{REJEITA}, \text{INVALIDA}\\}$

## Preparação para a próxima aula

### Bibliografia

1. [Capítulo 1](https://integrada.minhabiblioteca.com.br/reader/books/9788522108862/pageid/53){:target="\_blank"}, seções 1.3 e 1.4 (a partir da página 65) do livro [**Introdução a Teoria da Computação**](https://integrada.minhabiblioteca.com.br/reader/books/9788522108862){:id="sipser" target="\_blank"}
2. Capítulos 3 (a partir da seção 3.6) e 4 do livro [Linguages Formais e Autômatos](https://integrada.minhabiblioteca.com.br/reader/books/9788577807994){:target="\_blank"}  de Paulo Blauth Menezes.
3. Capítulo 3 e seção 4.1 do [Livro do Hopcroft](/teaching/lasalle/2024/automata#hopcroft)

### Videos

1. [Theory of Computation - Lecture 2](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/nondeterminism-closure-properties-regular-expressions-2192-finite-automata/), Michael Sipser, MIT, 2020.
2. [Theory of Computation - Lecture 3](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/regular-pumping-lemma-finite-automata-2192-regular-expressions-cfgs/), Michael Sipser, MIT, 2020.

## Recursos para essa aula

### Bibliografia

1. [Capítulo 1](https://integrada.minhabiblioteca.com.br/reader/books/9788522108862/pageid/53){:target="\_blank"} até a seção 1.2 (página 64) do livro [**Introdução a Teoria da Computação**](https://integrada.minhabiblioteca.com.br/reader/books/9788522108862){:id="sipser" target="\_blank"}
2. capítulo 3 (até a seção 3.5) do livro [Linguages Formais e Autômatos](https://integrada.minhabiblioteca.com.br/reader/books/9788577807994){:target="\_blank"}  de Paulo Blauth Menezes.
3. Capítulo 2 e 4 (menos a seção 4.1) do [Livro do Hopcroft](/teaching/lasalle/2024/automata#hopcroft)

### Videos

1. [Theory of Computation - Lecture 1](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/introduction-finite-automata-regular-expressions/), Michael Sipser, MIT, 2020.
2. [Theory of Computation - Lecture 2](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/resources/nondeterminism-closure-properties-regular-expressions-2192-finite-automata/), Michael Sipser, MIT, 2020.

