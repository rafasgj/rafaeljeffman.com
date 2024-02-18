---
title: Funções e Relações
subtitle: 
layout: main
section: Matemática para Computação
sections: []
tags:
  - ciência da computação
  - matemática
  - conceitos básicos
  - funções
  - relações
lang: pt
copy: 2024
date: 2024-01-15
abstract:
---

## Funções

Uma **função** é um objeto que estabelece um relacionamento de _entrada-saída_, ou 
seja, uma função recebe uma sequência de entrada e produz uma sequência de saída. 
Em toda função, a mesma entrada sempre produz a mesma saída. Seja $f$ uma função 
cujo valor de saída é $b$ para um valor de entrada $a$, escrevemos $f(a) = b$.

Uma função também é chamada _mapeamento_, e dado $f(a) = b$, dizemos que _$f$ 
mapeia $a$ para $b$_. 

Por exemplo, a função $\text{abs}(x)$ que pode ser definida como

$$
abs(x) = \begin{cases}
    x & \text{caso x $\ge$ 0} \\
    -x & \text{c.c.}
\end{cases}
$$

que terá o mesmo resultado para $\text{abs}(2) = 2$ ou $\text{abs}(-2) = 2$. A 
addição ($\text{add}(a, b)$ é outra função, que recebe uma sequência de dois 
valores e produz um único valor de saída, representando a soma dos dois valores.

O conjunto de entradas possíveis para uma função é o seu **domínio**, e o conjunto 
de saídas possíveis é o seu **contradomínio**. Uma função $f$ com domínio $D$ e 
contradomínio $C$ pode ser representada como $f: D \to C$. Por exemplo, na função 
$\text{abs}$ estamos trabalhando com inteiros, logo, o dominio é $\mathbb{Z}$, e 
como o contradomínio será positivo, temos $\mathbb{N}$, portanto escrevemos 
$\text{abs}: \mathbb{Z} \to \mathbb{N}$. Já no caso da função $\text{add}$, 
utilizamos dois valores de entrada e, portanto, temos um par de dois inteiros, 
$\mathbb{Z} \times \mathbb{Z}$, com um inteiro sendo produzido na saída, e 
escrevemos $\text{add}: \mathbb{Z}\times\mathbb{Z} \to \mathbb{Z}$, ou então, 
$\text{add}: \mathbb{Z}^{2}\to\mathbb{Z}$.

Uma função que de fato usa todos os elementos do contradomínio_ é dita ser uma 
função _sobre o contradomínio_, ou **sobrejetora**. Uma função com domínio $D$, 
para a qual $f(a) = f(b)$ se e somente se $a = b$, para todo $a \in D$ é dita uma 
função **injetora**. E uma função **bijetora** é uma função ao mesmo tempo 
_sobrejetora_ e _injetora_.

Quando o domínio de uma função $f$ é $A_1\times \cdots \times A_k$ para alguns 
conjuntos $A_1, \dots, A_k$, a entrada para a função $f$ é uma _k-upla_ $\(a_1, 
a_2, \dots, a_k\)$ e chamamos os elementos $a_i$ de **argumentos para $f$**. Uma 
função com _k_ argumentos é dita uma **função k-ária** e _k_ é a **aridade** da 
função. Duas aridades comuns são funções com um argumento, chamadas **funções 
unárias**, e funções com dois argumentos, chamadas **funções binárias**.

Usualmente, escrevemos as funções com a **notação prefixa**, por exemplo, 
$\text{add{\(a, b\)$, no entanto, para certas funçẽs binárias familiares escrevemos 
a função em uma **notação infixa**, como em $a + b$.

## Relações

Um **predicado** ou **propriedade** é uma função cujo contradomínio é 
**{VERDADEIRO, FALSO}** (ou $\\{\bot,\top\\}$). Por exemplo uma função $p = 
\text{par}(n)$, onde $p:\mathbb{N} \rightarrow \\{\bot, \top\\}$  é um predicado, 
cujo valor é VERDADEIRO ($\top$) quando **n** é _par_.

Uma propriedade cujo domínio é um conjunto de k-uplas $A \times cdots \times A$ é 
chamada **relação**. Um exemplo comum de relação é a relação 2-ária, chamada de 
**relação binária**. Quando escrevemos uma relação binária, normalmente utilizamos 
notação infixa, por exemplo $a \lt b$ ($a$ menor que $b$).

Se uma relação $R$ é binária, o enunciado $aRb$ significa que $aRb = 
\text{VERDADEIRO}$. De modo semelhante, caso $R$ seja uma relação _k-ária_, o 
enunciado $R(a_1, \dots, a_k)$ significa que $R(a_1, \dots, a_k) = \top$.

Um tipo especial de relação binária, chamada **relação de equivalência**, captura a 
noção de dois objetos serem iguais com respeito a alguma característica. Uma 
relação binária $R$ é uma relação de equivalência se:
* $R$ é **reflexiva**, se para todo $x$, $xRx$
* $R$ é **simétrica**, se para todo $x$ e $y$, $xRy \implies yRx$
* $R$ é **transitiva**, se para todo $x$, $y$ e $z$, $xRy \land yRz \implies xRz$
