---
layout: main
section: Matemática para Computação
tags:
  - ciência da computação
  - matemática
  - conceitos básicos
  - conjuntos
title: Conjuntos
subtitle: Conceitos básicos de matemática para computação
copy: 2022-2023
date: 2023-08-01
abstract: |-
  Os conceitos de conjuntos e suas operaçõe são muito utilizados em ciência
  da computação. Neste artigo são tratados os conceitos básicos de conjuntos
  e suas operações, com foco no uso destes conceitos nas disciplinas de
  linguagens formais e bancos de dados.
---

Em diversas áreas da ciência da computação é importante entender conceitos de conjuntos, como nas linguagens formais ou nos bancos de dados. Aqui são apresentados alguns desses conceitos, além das principais operações de conjuntos.

## Conjuntos

Um conjunto é um grupo de objetos representado como uma unidade. É  uma estrutura que armazena elementos de qualquer tipo, sem repetição e sem qualquer ordenação. Um conjunto pode ter zero ou mais elementos distintos. Se um elemento $a$ é um elemento do conjunto $A$, dizemos que _$a$ pertence ao conjunto $A$_, e denotamos a pertinência por:

$$ a \in A $$

Uma forma de representação que facilita a visualização de conjuntos é o _diagrama de Venn_. Graficamente a pertinência de um elemento $a$ ao conjunto $A$ pode ser vista como:

<div class="image">
    <svg height="200" width="100" class="teaching-svg">
        <ellipse cx="50" cy="120" rx="40" ry="75" fill="#f0f0f0" stroke="#222" />
        <circle cx="43" cy="115" r="2.5" fill="#333" />
        <text x="50" y="120">a</text>
        <text x="40" y="25">A</text>
    </svg>
</div>

Caso queria se afirmar que _$a$ não pertence ao conjunto $A$_, utilizamos:

$$ a \notin A $$

O _diagrama de Venn_ para esta relação entre o elemento $a$ e o conjunto $A$ é:

<div class="image">
    <svg height="200" width="160" class="teaching-svg">
        <ellipse cx="50" cy="120" rx="40" ry="75" fill="#f0f0f0" stroke="#222" />
        <circle cx="130" cy="125" r="2.5" fill="#333" />
        <text x="140" y="130">a</text>
        <text x="40" y="25">A</text>
    </svg>
</div>


### Definição de Conjuntos

Uma forma de definir um conjunto é listar todos os elementos do conjunto, por exemplo

$$ {Vogais} = \{ a, e, i, o, u \} $$

Ao listar todos os elementos de um conjunto, quando o padrão do conjunto é óbvio e de fácil interpretação, podemos utilizar "$\dots$":

$$
\begin{align}
& Alfabeto = \{ a, b, c, d, \dots, x, y, z \} \\
& Impares = \{ 1, 3, 5, \dots \}
\end{align}
$$

Outra forma de definir um conjunto é a partir de uma propriedade. Por exemplo, assumindo que $\mathbb{N}$ seja o conjunto dos números naturais, e $\bmod{}$ como a operação que retorna o resto da divisão inteira, podemos definir o conjunto dos números pares como:

$$ {Pares} = \{ x \in \mathbb{N} \:|\: x \bmod{2} = 0 \} $$

Esta definição de conjunto pode ser interpretada como o _conjunto de todos os elementos pertencentes aos números naturais, $\mathbb N$, tal que o resto da divisão inteira seja igual a 0_.

A forma geral para a definição de um conjunto em relação a uma propriedade $p$ é:

$$ \{ x \:|\: x \in A \land P(x) \} \hspace{2em} \text{ou} \hspace{2em} \{ x \in A \:|\: P(x) \} $$


### Continência

Se todos os elementos de um conjunto $A$ são elementos de um conjunto $B$, afirma-se que _$A$ está contido em $B$_, e denota-se por:

$$ A \subseteq B $$

Alternativamente, podemos dizer que _$B$ contém $A$_, denotando a relação por:

$$ B \supseteq A $$

Nesse caso, quando $A \subseteq B$ ou $B \supseteq A$, dizemos que _$A$ é um subconjunto de $B$_.

Para que um conjunto $A$ seja subconjunto do conjunto $B$ é necessário que a seguinte regra seja satisfeita:

$$ x \in A \Longrightarrow x \in B $$

Graficamente um subconjunto $A$ de um subconjunto $B$ pode ser visto como:

<div class="image">
    <svg height="175" width="185" class="teaching-svg">
        <defs>
          <pattern id="gradient-fill"
                   width="5" height="10"
                   patternUnits="userSpaceOnUse"
                   patternTransform="rotate(45 50 50)">
               <line stroke="#aaa" stroke-width="7px" y2="10"/>
          </pattern>
        </defs>
        <ellipse cx="90" cy="80" rx="75" ry="60" fill="#f0f0f0" stroke="#222" />
        <ellipse cx="70" cy="85" rx="45" ry="30" fill="url(#gradient-fill)" stroke="#222" />
        <text x="120" y="90">A</text>
        <text x="165" y="55">B</text>
    </svg>
</div>


### Subconjunto próprio

Dados os conjuntos $A$ e $B$ e as relações:

$$
\begin{eqnarray}
A \in B & \\
b \notin A & \\
b \in B
\end{eqnarray}
$$

podemos afirmar que _$A$ é subconjunto próprio de $B$_, e denota-se essa relação como:

$$ A \subset B $$

Alternativamente, dizemos que _$B$ contém propriamente $A$_, utilizando:

$$ B \supset A $$


### Igualdade de conjuntos

Dois conjuntos são iguais se e somente se todos os elementos de um conjunto também pertence ao outro conjunto:

$$ A = B \iff A \subseteq B \land B \subseteq A $$

A partir da definição da igualdade de conjuntos, podemos demonstrar que elementos repetidos não influenciam na definição do conjunto, uma vez que, mesmo que existam elementos repetidos, a condição $A \subseteq B \land B \subseteq A$ continua válida, como mostra a imagem:

<div class="image">
    <svg width="400" height="250" class="teaching-svg">
        <!-- Conjunto B -->
        <ellipse cx="310" cy="140" rx="55" ry="100" fill="#f0f0f0" stroke="#222" />
        <text style="font-size:80%;" x="300" y="20">B</text>
        <text style="font-size:80%;" x="310" y="80">1</text>
        <circle cx="300" cy="77" r="2.5" fill="#333" />
        <text style="font-size:80%;" x="310" y="105">2</text>
        <circle cx="300" cy="102" r="2.5" fill="#333" />
        <text style="font-size:80%;" x="310" y="130">2</text>
        <circle cx="300" cy="127" r="2.5" fill="#333" />
        <text style="font-size:80%;" x="310" y="155">3</text>
        <circle cx="300" cy="152" r="2.5" fill="#333" />
        <text style="font-size:80%;" x="310" y="180">3</text>
        <circle cx="300" cy="177" r="2.5" fill="#333" />
        <text style="font-size:80%;" x="310" y="205">3</text>
        <circle cx="300" cy="202" r="2.5" fill="#333" />
        <!-- Conjunto A -->
        <ellipse cx="80" cy="140" rx="55" ry="100" fill="#f0f0f0" stroke="#222" />
        <text x="70" y="20">A</text>
        <text style="font-size:80%;" x="65" y="80">1</text>
        <circle cx="82" cy="75" r="2.5" fill="#333" />
        <text style="font-size:80%;" x="65" y="140">2</text>
        <circle cx="82" cy="135" r="2.5" fill="#333" />
        <text style="font-size:80%;" x="65" y="210">3</text>
        <circle cx="82" cy="205" r="2.5" fill="#333" />
        <!-- Conexões -->
        <line x1="300" y1="77"  x2="82" y2="75" />
        <line x1="300" y1="102" x2="82" y2="135" />
        <line x1="300" y1="127" x2="82" y2="135" />
        <line x1="300" y1="152" x2="82" y2="205" />
        <line x1="300" y1="177" x2="82" y2="205" />
        <line x1="300" y1="202" x2="82" y2="205" />
    </svg>
</div>

Como não existe elemento $x$ em $A$ tal que $x \notin B$ ou em $B$ tal que $x \notin A$, os conjuntos são iguais, logo, a repetição de elementos não altera o conjunto.


### Conjunto vazio

Um conjunto importante é o conjunto que não contém nenhum elemento, o **conjunto vazio**, $\\{\\ \\}$, usualmente representado pelo símbolo $\varnothing$.

Um conjunto vazio não representa _nada_, ele representa um conjunto sem nenhum elemento dentro.

O conjunto vazio está contido que qualquer conjunto $A$. Podemos demonstrar isso a partira da definição de subconjunto e da _regra da implicação_. É necessário que a condição $x \in \varnothing \Longrightarrow x \in A$ seja verdadeira, e como o antecedente $x \in \varnothing$ é _**falso**_ para qualquer $x$, a condição será verdadeira, logo $\varnothing \subseteq A$.


### Operações sobre conjuntos

As principais operações sobre conjuntos são a união, a diferença, o complemento, o conjunto das partes e o produto cartesiano. O resultado de uma operação sobre conjuntos será outro conjunto.


#### União

Sejam $A$ e $B$ conjuntos, a união ($\cup$) dos conjuntos resultará em um conjunto com todos os elementos de $A$ e de $B$.

$$ A \cup B = \{ x \:|\: x \in A \lor x \in B \} $$

<svg width="300" height="200" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <circle r="85" id="circle_left" cy="100" cx="100" fill="" stroke="" />
        <circle r="85" id="circle_right" cy="100" cx="200" fill="" stroke="" />
        <mask id="mask_right">
            <rect width="300" height="200" fill="#fff" stroke="#fff" />
            <use xlink:href="#circle_left" fill="#000" />
        </mask>
        <mask id="mask_left">
            <rect width="300" height="200" fill="#fff" stroke="#fff" />
            <use xlink:href="#circle_right" fill="#000" />
        </mask>
        <mask id="mask_inverse_right">
            <rect width="300" height="200" fill="#000" stroke="#000" />
            <use xlink:href="#circle_left" fill="#fff" />
        </mask>
        <mask id="mask_inverse_left">
            <rect width="300" height="200" fill="#000" stroke="#000" />
            <use xlink:href="#circle_right" fill="#fff" />
        </mask>
        <clipPath id="clip_right">
            <use xlink:href="#circle_right" />
        </clipPath>
        <clipPath id="clip_left">
            <use xlink:href="#circle_left" />
        </clipPath>
    </defs>
    <g>
        <use xlink:href="#circle_right" stroke-width="1.5" stroke="#222" fill="url(#gradient-fill)" mask="url(#mask_right)" />
        <use xlink:href="#circle_left" stroke-width="1.5" stroke="#222" fill="url(#gradient-fill)" mask="url(#mask_left)" />
        <use xlink:href="#circle_left" stroke-width="1.5" stroke="" fill="url(#gradient-fill)" clip-path="url(#clip_right)" />
        <text x="70" y="105" font-weight="bolder" font-size="150%">A</text>
        <text x="200" y="105" font-weight="bolder" font-size="150%">B</text>
    </g>
</svg>


#### Intersecção

Sejam $A$ e $B$ conjuntos, a intersecção ($\cap$) dos conjuntos resultará em um conjunto contendo apenas os elementos presente tanto em $A$ quanto em $B$.

$$ A \cup B = \{ x \:|\: x \in A \land x \in B \} $$

<a name="disjoint-set" />Quando temos que $A \cap B = \varnothing$ dizemos que $A$ e $B$ são conjuntos disjuntos, independentes ou mutuamente exclusivos.

<svg width="300" height="200" xmlns="http://www.w3.org/2000/svg">
    <g>
        <use xlink:href="#circle_left" id="center" fill="url(#gradient-fill)" clip-path="url(#clip_right)"/>
        <use xlink:href="#circle_left" stroke-width="1.5" stroke="#222" fill="none"/>
        <use xlink:href="#circle_right" stroke-width="1.5" stroke="#222" fill="none"/>
        <text x="70" y="105" font-weight="bolder" font-size="150%">A</text>
        <text x="200" y="105" font-weight="bolder" font-size="150%">B</text>
    </g>
</svg>

#### Complemento

Dado um conjunto fixo $U$, denominado _conjunto universo_, o complemento de um conjunto $A$ é formado por todos os elementos de $U$ que não existem em $A$.

$$ \thicksim\! A = \{ x \:|\: x \in U \land x \notin A \} $$

<svg width="300" height="200" xmlns="http://www.w3.org/2000/svg">
    <g>
        <use xlink:href="#circle_right" stroke-width="1.5" stroke="#222" fill="url(#gradient-fill)" mask="url(#mask_right)" />
        <use xlink:href="#circle_left" stroke-width="1.5" stroke="#bbb" fill="#fff" mask="url(#mask_left)" />
        <use xlink:href="#circle_left" stroke-width="1.5" stroke="#222" fill="#fff" clip-path="url(#clip_right)" />
        <text x="70" y="105" font-weight="bolder" font-size="150%">A</text>
        <text x="200" y="105" font-weight="bolder" font-size="150%">B</text>
    </g>
</svg>

#### Diferença

A diferença entre os conjuntos $A$ e $B$ é um cojunto com os elementos existentes em $A$ que não existem em $B$.

$$
\begin{align}
& A - B = A \cap \thicksim\! B
& A - B = \{ x \:|\: x \in A \land x \notin B \}
\end{align}
$$

<svg width="300" height="200" xmlns="http://www.w3.org/2000/svg">
    <g>
        <use xlink:href="#circle_right" stroke-width="1.5" stroke="#bbb" fill="#fff" mask="url(#mask_right)" />
        <use xlink:href="#circle_left" stroke-width="1.5" stroke="#222" fill="url(#gradient-fill)" mask="url(#mask_left)" />
        <use xlink:href="#circle_right" stroke-width="1.5" stroke="#222" fill="#fff" clip-path="url(#clip_left)" />
        <text x="70" y="105" font-weight="bolder" font-size="150%">A</text>
        <text x="200" y="105" font-weight="bolder" font-size="150%">B</text>
    </g>
</svg>

#### Conjunto das Partes

O conjunto das partes (ou _conjunto potência_) de um conjunto $A$ é o conjunto de todos os subconjuntos de $A$.

Seja $A = \{ a, b, c \}$, a lista completa de subconjuntos $S$ de $A$ é $\varnothing$, $\\{a\\}$, $\\{b\\}$, $\\{c\\}$, $\\{a, b\\}$, $\\{a, c\\}$, $\\{b, c\\}$, $\\{a, b, c\\}$, portanto, o conjunto das partes de $A$ tem 8 elementos:

$$ 2^A = \mathcal{P}(A) = \{ \varnothing, \{a\}, \{b\}, \{c\}, \{a, b\}, \{a, c\}, \{b, c\}, \{a, b, c\} \} $$

Podemos definir o conjunto das partes como:

$$ 2^A = \mathcal{P}(A) = \{ S \:|\: S \subseteq A \} $$


#### Produto Cartesiano

O produto cartesiano de dois conjuntos é o conjunto de pares ordenados $(a, b)$, sendo que $a \in A$ e $b \in B$.

$$ A \times B = \{ (a, b) \:|\: a \in A \land b \in B \} $$

Esta não é uma operação comutativa. Note que a ordem dos elementos é importante, e $A \times B \neq B \times A$.

A operação pode ser _multidimensional_, ou seja, executada sobre múltipos conjuntos, como em

$$ A \times B \times C = \{(a,b,c) \:|\: a \in A \land b \in B \land c \in C\} $$

Esta operação também não é associativa. Seja o conjunto $A = \\{1\\}$, então $(A \times A) \times A$ resulta em $\\{(1, 1), 1\\}$, enquanto $A \times (A \times A)$ resulta em $\\{1, (1, 1)\\}$.

É usual usar _expoentes_ quando do produto cartesiano de um conjunto com ele mesmo, como em $\mathbb{R}^2 = \mathbb{R} \times \mathbb{R}$, ou $\mathbb{R}^3 = \mathbb{R} \times \mathbb{R} \times \mathbb{R}$.


### Propriedades das operações sobre conjuntos

As propriedades analisadas, a seguir, presupõe a existência do universo $U$ e dos conjuntos $A$, $B$ e $C$.


#### Idempotência

O resultado da união ou intersecção de um conjunto com ele mesmo é o próprio conjunto.

$$
\begin{align}
& A \cup A = A \\
& A \cap A = A
\end{align}
$$


#### Comutativa

As operações de intersecção e união são comutativas.

$$
\begin{align}
& A \cup B = B \cup A \\
& A \cap B = B \cap A
\end{align}
$$


#### Associativa

A ordem das operações de união e intersecção pode ser qualquer:

$$
\begin{align}
& (A \cup B) \cup C = A \cup (B \cup C) \\
& (A \cap B) \cap C = A \cap (B \cap C)
\end{align}
$$

Com isso temos que o uso de parenteses é desnecessário, uma vez que

$$
(A \cup B) \cup C = A \cup (B \cup C) = A \cup B \cup C
$$


#### Distributiva

A união de conjuntos é distributiva sobre a intersecção, e a intersecção de conjuntos é distributiva sobre a união.

$$
\begin{align}
& A \cap (B \cup C) = (A \cap B) \cup (A \cap C) \\
& A \cup (B \cap C) = (A \cup B) \cap (A \cup C)
\end{align}
$$


#### Duplo Complemento

O complemento do complemento de um conjunto $A$, em relação ao universo $U$, é o próprio conjunto.

$$ \thicksim\! ( \thicksim\! A ) = A $$


#### DeMorgan

O complemento da união de dois conjuntos é a intersecção dos complementos desses conjuntos.

$$
\thicksim\! (A \cup B) = \; \thicksim\! A \; \cap \thicksim\! B
$$ 

O complemento da intersecção de dois conjuntos é a união dos complementos desses conjuntos.

$$
\thicksim\! (A \cap B) = \; \thicksim\! A \; \cup \thicksim\! B
$$


### Conjunto universo e conjunto vazio.

Podemos obter o conjunto universo $U$ e o conjunto vazio $\varnothing$ a partir da união ou intersecção de um conjunto com o seu complemento:

$$
\begin{align}
& A \cup \thicksim A = U \\
& A \cap \thicksim A = \varnothing
\end{align}
$$
