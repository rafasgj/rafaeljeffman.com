---
title: Logica Booleana
subtitle: 
layout: main
section: Lógica
sections:
  - Lógica
tags:
  - lógica
  - lógica booleana
  - matemática
lang: pt
copy: 2024
date: 2024-01-20
abstract: |
  A lógica booleana é um sistema matemático baseado na proposta de George Boole em 1847.
  Neste artigo, é apresentada uma introdução a conceitos e notações da lógica booleana
  aplicáveis diversos campos da ciência da computação.
---

A **lógica booleana** é um sistema matemático baseado no conceito de _VERDADEIRO_ ($1$) e _FALSO_ ($0$), e, embora concebido como um sistema puramente matemático, hoje é considerado como um fundamento da eletrônica digital e do desenho de computadores.

Podemos manipular os **valores booleanos** utilizando **operações booleanas**. A operação de **negação** ou _não lógico_, designada com o símbolo $\lnot$, é a operação mais simples e inverte o valor booleano, logo, $\lnot 0 = 1$ e $\lnot 1 = 0$. As outras operações booleanas são a **conjunção** ou _E lógico_, designada pelo símbolo $\land$, que resulta em _VERDADEIRO_ (ou 1) quando os dois operadores possuem valor _VERDADEIRO_; e a operação de **disjunção** ou _OU lógico_, designada pelo símbolo $\lor$, cujo resultado é _VERDADEIRO_, sempre que qualquer operando tiver o valor _VERDADEIRO_.

$$
\begin{align}
0 \land 0 = 0 & & 0 \lor 0 = 0 & & \lnot 0 = 1 \\
0 \land 1 = 0 & & 0 \lor 1 = 1 & & \lnot 1 = 0 \\
1 \land 0 = 0 & & 1 \lor 0 = 1 & & \\
1 \land 1 = 1 & & 1 \lor 1 = 1 & &
\end{align}
$$

As expressões booleanas são expressas a partir dos operadores boleanos ($\lnot$, $\lor$, $\land$), onde $\lnot$ tem a maior precedência, seguido de $\land$ e finalmente $\lor$, parenteses para inverter a prioridade de operadores, e de **operandos booleanos**, normalmente representados por variáveis booleanas (P, Q, ...) e não diretamente por valores, por exemplo

$$
P \lor (Q \land \lnot R)
$$ 

Um operando booleano representa a veracidade de um enunciado, por exemplo, P = "está chovendo", ou Q = "hoje é segunda-feira". Dessa forma, podemos escrever $\text{P}\land\text{Q}$ para representar o valor-verdade do enunciado "está chovendo e hoje é segunda-feira", de forma similar, podemos representar outros enunciados, como $\lnot\text{P}\lor\text{Q}$.

Uma expressão booleana bastante comum é a expressão **XOR** ou _OU exclusivo_, designada pelo símbolo $\oplus$, que é verdadeira quando um dos dois operandos é verdadeiro, porém não os dois. A operação _XOR_ é equivalente às expressões $\text{P}\land\lnot\text{Q}\lor\lnot\text{P}\land\text{Q}$ e $\(\text{P}\lor\text{Q}\)\land\(\lnot\text{P}\lor\lnot\text{Q}\)$

A operação de **implicação**, designada pelo símbolo $\to$, corresponde ao enunciado _se P então Q_, e é _FALSA_ apenas quando $\text{P}\land\lnot{Q}$ é verdadeira. A operação de **igualdade** ou **equivalência**, designada pelo símbolo $\leftrightarrow$, corresponde ao enunciado "P se e somente se Q" e é _VERDADE_ apenas se P e Q são iguais.

Todas as operações booleanas podem ser representadas utilizando-se apenas as operações $\lnot$ e $\land$ (ou, de forma análoga, $\lnot$ e $\lor$). As identidades abaixo mostram, em cada linha expressões booleanas equivalentes à esquerda e à direita, e a linha abaixo utiliza a equivalência anterior para mostrar que apenas duas das operações são necessárias:

$$
\begin{align}
\text{P} \lor \text{Q} & & & \lnot(\lnot\text{P}\land\lnot\text{Q}) \\
\text{P} \to \text{Q} & & &  \lnot\text{P}\lor\text{Q} \\
\text{P} \leftrightarrow \text{Q} & & & (\text{P}\to\text{Q})\land(\text{Q}\to\text{P}) \\
\text{P} \oplus \text{Q} & & & \lnot(\text{P}\leftrightarrow\text{Q})
\end{align}
$$

A **lei distributiva para E e OU** é análoga a lei distributiva da adição e da multiplicação, nas formas

$$
\begin{align}
\text{P} \land (\text{Q} \lor \text{R}) = & (\text{P} \land \text{Q}) \lor (\text{P} \land \text{R}) \\
\text{P} \lor (\text{Q} \land \text{R}) = & (\text{P} \lor \text{Q}) \land (\text{P} \lor \text{R})
\end{align}
$$

