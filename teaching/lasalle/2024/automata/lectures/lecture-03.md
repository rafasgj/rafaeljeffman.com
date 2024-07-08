---
section: Linguagens Formais e Autômatos
title: Demonstrações e Provas
subtitle:
layout: lecture
last_occurrence: 2024-03-21
copy: 2024
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2024/automata
---

## Demonstrações

* Demonstrações são métodos para averiguar a verdade.
* Como averiguar a verdade na sociedade?
    * Experimentação e Observação
    * Amostragem e contra-exemplo
    * Juízes e juris
        * Verdade baseada em evidências "suficientes"
    * Religião (Mundo de Deus)
        * Convicção e Dogmas
    * Chefes e clientes
    * Autoridades
        * ex.: Professores

Uma **prova matemática** é a verificação de uma proposição através de uma cadeia de deduçẽos lógicas de um conjunto de axiomas.

Uma **proposição** é uma afirmação que pode ser VERDADEIRA ou FALSA. Por exemplo, $\forall n \in \mathbb{N}, n^2 + n + 41$ é primo.

> * $\forall \rightarrow$ _para todo_

Um **predicado** é uma proposição cuja verdade depende do valor de uma variável.

É importante que a demonstração matemática seja completa, e, por isso, não pode ser baseada unicamente na observação.

Vamos utilizar o exemplo da proposição $a^4 + b^4 + c^4 = d^4$ não te msolução com positivos inteiros.

Esta proposição (um caso específico da [Conjectura da soma de potências de Euler](https://pt.wikipedia.org/wiki/Conjectura_da_soma_de_pot%C3%AAncias_de_Euler)){:target="\_blank"}, demorou mais de 200 anos para ser provada falsa. Em 1988, Richard Frye mostrou o contra-exemplo com os menores valores, com a=95.800, b=217.519, c=414.560 e d=422.481.

Uma outra proposição ligada a decomposição de inteiros e a teoria dos números é a de que $3\mid 3(x^2 + y^2) = z^2$ não tem solução com inteiros positivos. E esta proposição também é falsa, mas o menor contra-exemplo tem mais de 1.000 dígitos.

> Esse tipo de problema é importante pois são problemas que envolvem curvas elípticas (na concepção ou na prova), e estão intimamente ligados à quebra de sistemas criptográficos.

Uma outra proposição importante é a de que as regiões de um mapa podem ser coloridas com 4 cores de forma que regiões adjacences tem cores diferentes.
* Provas por imagens foram propostas, no entanta já vimos que este tipo de prova sempre levanta suspeitas.
* Em 1977, uma prova utilizando um computador foi proposta, mas ela sofreu a mesma suspeição das provas por imagens (como garantir que não havia erros no programa?)
* Existe uma prova humana, proposa no início do século 21 (~2005), mas até hoje não há verificação da correção da prova.

Uma outra conjectura ainda não provada é a de que, fora o número 2, todo numero inteiro, positivo, e par, é formado pela soma de dois números primos (Goldbach, 1742). Sabemos que a conjectura se mantém até $4\times 10^{48}$, mas ainda não se sabe se a conjectura é sempre verdade. (É um dos problemas em abertos mais antigos da matemática.)

**Axiomas** são proposições assumidas como verdade. São utilizados em provas para definir as premissas utilizadas na prova.

Axiomas podem ser contraditórios em diferentes contextos, por exemplo:

* Na geometria euclidiana, dado uma linha L e um ponto $P \notin L$, existe exatamente uma linga através de P que é paralela a L.
* Na geometria esférica, para a mesma proposição, não existe nenhuma linha paralela a L.
* E na geometria hyperbólica, existem infinitas linhas paralelas a L.

Axiomas deveriam ser consistentes e completos.
    * Axiomas são consistentes se nenhuma proposição pode ser provada simultaneamente VERDADEIRO e FALSO.
    * Axiomas são completos se podem ser utilizados para provar que todas proposições são VERDADEIRO ou FALSO.

Gödel provou que nenhum conjunto de axiomas podem ser consistentes e completos. Normalmente se opta por axiomas consistentes, mesmo que algumas proposições não possam ser provadas.

### Prova por Contradição

Uma prova por contradição é uma forma de prova que estabelece que a verdade ou validade de uma proposição ao mostrar que assumindo que a proposição é falsa leva a uma contradição, e uma vez que a proposição não pode ser falsa, ela só pode ser verdadeira.

> **Theorema**: $\sqrt{2}$ é irracional. 

Para provar o teorema, utilizamos prova por contradição.

* Assumimos que $\sqrt{2}$ é racional.
    * $\sqrt{2} = \frac{a}{b}$
        * $\frac{a}{b}$ é uma fração com termos mínimos, ou seja, _a_ e _b_ não tem divisores comuns
        * $2 = (\frac{a}{b})^2$
        * $2b^2 = a^2$
            * Como o quadrado de todo número ímpar é impar, e o quadrado de $a$ deve ser par, sabemos que _a_ é par, logo $2\mid a$ (_2 divide a_).
        * $4 \mid a^2$
        * $4 | 2 b^2$
        * 2 | b^2
            * Logo, _b_ é par
    * Como $a$ e $b$ são pares, $\frac{a}{b} não pode ser uma fração com termos mínimos, o que é uma contradição em relação a hipótese, logo, ela é falsa.
* Como a hipótese é falsa, por contradição, provamos que $\sqrt{2}$ é irracional. $\square$ 

### Prova por indução

A prova por indução é um método de provar que um predicado é verdadeiro para todo número natural $n$. A prova é realizada provando-se um caso simple, e demonstrando que se assumirmos que se a proposição é verdadeira para um caso, também é verdadeira para o caso seguinte.

> Seja $P(n)$ um predicado, se $P(0)$ é VERDADEIRO e $\forall{n} \in \mathbb{N}, ( P(n) \rightarrow P(n+1))$ é VERDADEIRO, então $\forall{n} \in \mathbb{N}, P(n)$ é verdadeiro.

Um exemplo informal da prova por indução pode ser a prova de que podemos subir numa escada o quanto quisermos, ao provar que podemos subir no primeiro degrau (caso base), e podemos atingir o próximo degrau a partir do degrau atual (passo de indução).

Uma prova por indução consiste de dois casos, o primeiro é o **caso base** que prova que o predicado é verdadeiro para o caso inicial ($P(0)$), sem assumir conhecimento algum sobre os outros casos. O segundo caso é o **passo de indução**, onde deve se provar que, se o predicado é válido para um caso qualquer $P(n)$ então o predicado deve ser verdade também para >$P(n + 1)$.

Com esses dois passos se estabelece que o predicado é valido para qualquer número natural $n$.

O caso base não precisa ser necessariamente o caso onde $n = 0$, mas deve representar o caso mais "simples" (que não depende de nenhum outro) do predicado.

**Exemplo 1**: _Teorema_: $\forall n \ge 0, \sum_{1}^{n} = \frac{n(n+1)}{2}$

* Predicado: $P(n) = \sum_{1}^{n} = \frac{n(n+1)}{2}$ 
* Caso Base: $P(0) = 0$ (podemos utilizar também $P(1) = \frac{1(1+1)}{2} = 1$)
* Passo de Indução: mostrar que $P(n) \rightarrow P(n+1)$
    * A soma de $n$ números é $1 + 2 + \dots + n$, logo, a soma de $n + 1$ números é igual a $1 + 2 + \dots + n + (n + 1)$
    * Logo, $\frac{n(n+1)}{2} + (n+1)$
    * $\frac{n(n+1) + 2(n+1)}{2}$
    * $\frac{n^2 + n + 2n + 2}{2}$
    * $\frac{(n + 1)(n + 2)}{2}$
    * $\frac{(n+1)((n+1) + 1))}{2} = P(n+1)$
    * Logo $P(n) \rightarrow P(n+1)\quad\square$

**Exemplo 2**: _Teorema_: $\forall n \in \mathbb{N}, 3 \mid (n^3 - n)$
* Predicado: $3 \mid (n^3 - n)$
* Caso base: $P(0) = 0, 3\mid 0$
* Passo de Indução:
    * $P(n+1) = 1 \mid (n+1)^3 - (n+1)$
    * $n^3 + 3n^2 + 3n + 1 - n - 1$
    * $n^3 - n +3n^2 + 3n$
    * $P(n) + 3n^2 + 3n$
    * Como assumimos que $P(n)$ é verdadeiro, $3 \mid P(n)$
    * É óbivo que $3 \mid 3n^2 + 3n$.
    * Como $P(n) \rightarrow P(n+1)$ o predicado é verdadeiro. $\square$ 
    

## Questões

1. Prove que $\forall n \in \mathbb{N}, n^2 + n + 41$ é falso.
2. Encontre o erro na seguinte demonstração:

$$
\begin{align}
x = y & & &  \\
x^2 = xy & & & \times x \\
x^2 - y^2 = xy - y^2 & & &  - y^2\\
(x+y)(x-y) = y(x-y) & & & \text{fatoração} \\
x + y = y & & &  \divsymbol (x - y) \\
y + y = y & & & \text{de acordo com x=y} \\
2y = y & & & \text{soma} \\
2 = 1 & & & \divsymbol y
\end{align}
$$

## Preparação para a próxima aula

1. [Capítulo 1](https://integrada.minhabiblioteca.com.br/reader/books/9788522108862/pageid/53){:target="\_blank"} até a página 44 do livro [**Introdução a Teoria da Computação**](https://integrada.minhabiblioteca.com.br/reader/books/9788522108862){:id="sipser" target="\_blank"}
2. Capítulo 2 e capítulo 3 (até a seção 3.3) do livro [Linguages Formais e Autômatos](https://integrada.minhabiblioteca.com.br/reader/books/9788577807994){:target="\_blank"}  de Paulo Blauth Menezes.
3. Capítulo 1, seção 1.5 e Capítulo 2 até a seção 2.2 do [Livro do Hopcroft](/teaching/lasalle/2024/automata#hopcroft)

## Recursos para essa aula

### Bibliografia

1. [Capítulo 0](https://integrada.minhabiblioteca.com.br/reader/books/9788522108862/pageid/23){:target="\_blank"}  do livro [**Introdução a Teoria da Computação**](https://integrada.minhabiblioteca.com.br/reader/books/9788522108862){:id="sipser" target="\_blank"}
2. [Livro do Hopcroft](/teaching/lasalle/2024/automata#hopcroft)(físico), capítulo 1, seções 1.1 até 1.4 (inclusa).

### Videos

3. Aulas 1 e 2 de [MIT 6.042j Mathematics for Computer Science 2010](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/){:target="\_blank"}
4. Videos da unidade 1, _Proofs_, de [MIT 6.042j Mathematics for Computer Science 2019](https://openlearninglibrary.mit.edu/courses/course-v1:OCW+6.042J+2T2019/course/){:target="\_blank"}

