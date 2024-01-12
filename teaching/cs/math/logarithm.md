---
layout: main
section: Matemática para Computação
tags:
  - ciência da computação
  - conceitos básicos
  - matemática
  - logaritmos
title: Propriedades dos Logaritmos
subtitle: Conceitos básicos de matemática para computação
copy: 2023
date: 2023-08-03
abstract:
---
O logaritmo de um número $n$ para uma base $b$ é a potência ao qual a base deve ser elevada para obter-se $n$:

$$
\begin{align}
& \log_{b} n = x\ \rightarrow b^x = n & {onde}\ b \gt 0 \ {e}\ b \ne 1
\end{align}
$$

De onde tiramos os exemplos:

$$
\begin{eqnarray}
\log_{10}\ {1000} = {3} & \\
\log_{2}\ {64} = {6} & \\
\log_{3}\ {7} = {1.7712} & \\
\end{eqnarray}
$$

Algumas propriedades dos logaritmos que devem ser lembradas:

* O logaritmo do produto de dois números é igual a soma dos logaritmos:

$$
\log_{a} (n \cdot m) = \log_{a} n + \log_{a} m
$$

* O logaritmo da divisão de dois números é igual a diferença dos logaritmos: 

$$
\log_{a} \left( \frac{n}{m} \right) = \log_{a} n - \log_{a} m
$$

* O logaritmo da potência é igual a multiplicação do expoente pelo logaritmo:

$$
\log_{a} n^{m} = m\cdot\log_{a} n
$$

* Expoentes:

$$
a^{\log_{c} b} = b^{\log_{c} a}
$$

* Troca de base:

$$
\begin{eqnarray}
\log_{a} n = \log_{b} n \cdot \log_{a} b & \\
\log_{a} n = \frac{\log_{b} n}{\log_{b} a} &\\
\end{eqnarray}
$$
