---
section: Linguagens Formais e Autômatos
title: Exercícios de Revisão
subtitle:
layout: lecture
last_occurrence: 
copy: 2024
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2024/automata
extra_styles:
  - tikzimage
---

<style>
table {
  border-collapse: collapse;
  margin: 0 auto;
  max-width: 70ch;
}
thead, tr, td {
  border: thin solid black;
  margin: 0;
  padding: 5px;
}
td {
   min-width: 10ch;
   text-align: center;
}
table.minimal td {
  min-width: 2ch !important;
}
</style>

## Questão 1

Semelhante a um autômato finito mas com uma memória ilimitada e irrestrita, uma máquina de Turing é um modelo muito mais preciso de um computador de propósito geral. Uma máquina de Turing pode fazer tudo o que um computador real pode fazer, entretanto mesmo ela não pode resolver certos problemas. Num sentido muito real, esses problemas estão além dos limites teóricos da computação.

Considere a seguinte máquina de Turing M que aceita apenas números binários palíndromos cujo comprimento é par:

![MT 1](/images/mt_enade_2021_ciencia_computacao_31.svg){:style="min-width: 75% !important;max-height: 60vh !important;"}

Considerando que o estado inicial de M é $q0$, que a sua fita se encontra inicializada com a entrada $110011$ e infinitos símbolos $B$ à esquerda e à direita, e que a cabeça de leitura encontra-se inicialmente no símbolo mais à esquerda da entrada, avalie as afirmações a seguir.

1. Após 4 movimentos de M, o conteúdo da fita, excluindo-se os símbolos "B", é "110011".
2. Após 8 movimentos de M, o conteúdo da fita, excluindo-se os símbolos "B", é "1001".
3. A máquina irá certamente travar em um estado de aceitação.
4. Existe um autômato com pilha que também aceita a linguagem de M.

Quais afirmações são corretas?

Corrija as afirmações falsas.

## Questão 2

Dado o alfabeto $\Sigma = \\{(,),0,1,2,3,4,5,6,7,8,9,+,-\\}$ e uma linguagem $L$ definida sobre esse alfabeto, $L=\\{w\|w\in\Sigma^{*}, \text{para cada ocorrência de '(' em w, existe uma ocorrência de ')'}\\}$.

Com relação a linguagem $L$, avalia as asserções a seguir e a relação proposta entre elas.

1. A linguagem $L$ não pode ser considerada regular

**PORQUE**
{:style="text-align: center; width:100%; margin: auto 0;"}

2. Autômatos finitos não possuem mecanismos que permitam contar infinitamento o número de ocorrências de determinado símbolo em uma cadeia.
{:start="2"}

A respeito dessas asserçỗes, assinale a opção correta.

* As asserções 1 e 2 são proposições verdadeiras, e a 2 é uma justificativa correta da 1.
* As asserções 1 e 2 são proposições verdadeiras, mas a 2 não é  uma justificativa correta da 1.
* A asserção 1 é verdadeira, e a asserçao 2 é falsa. 
* A asserção 1 é falsa, e a asserçao 2 é verdadeira.
* As asserçẽs 1 e 2 são falsas.
{:class="lettered"}

## Questão 3

| estado | símbolo lido na fita | símbolo gravado na fita | direção | próximo estado |
| :----: | :----: | :----: | :----: | :----: |
| início | ! | ! | direita | 0 |
| 0 | 0 | 1 | direita | 0 |
| 0 | 1 | 0 | direita | 0 |
| 0 | - | - | esquerda | 1 |
| 1 | 0 | 0 | esquerda | 1 |
| 1 | 1 | 1 | esquerda | 1 |
| 1 | ! | ! | direita | parada |

Na tabela acima, estão descritas as ações correspondentes a cada
um dos quatro estados (início, 0, 1, parada) de uma máquina de
Turing, que começa a operar no estado `início` processando
símbolos do alfabeto $\Sigma=\{0,1,\!, -\}$, em que "!" representa o início da fita e, "$-$" representa o espaço
em branco. Considere que, no estado `início`, a fita a ser
processada esteja com a cabeça de leitura/gravação na posição 1,
conforme ilustrado a seguir.

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | ... |
| ! | 0 | 1 | 1 | 0 | 1 | - | - | - | - | - | ... |
{:class="minimal"}

Considerando essa situação, qual o conteúdo da fita (12 primeiras posições) após a máquina atingir o estado de `parada`.

<details>
    <summary>Resposta...</summary>
    <blockquote><code>! 1 0 0 1 0 - - - - - -</code></blockquote>
</details>

## Questão 4

Qualquer expressão aritmética binária pode ser convertida em uma expressão totalmente
parentizada, bastando reescrever cada subexpressão binária $a \otimes b$ como $(a \otimes b)$, em que $\otimes$ denota
um operador binário. Expressões nesse formato podem ser definidas por regras de uma gramática
livre de contexto, conforme apresentado a seguir. Nessa gramática, os símbolos não-terminais $E$, $S$, $O$ e $L$ representam expressões, subexpressões, operadores e literais, respectivamente, e os demais símbolos das regras são terminais.

$$
\begin{align}
E \rightarrow & \: ( S O S ) \\
S \rightarrow & \: L | E \\
O \rightarrow & \: + | - | \times | \div \\
L \rightarrow & \: a | b | c | d | e \\
\end{align}
$$

Tendo como referência as informações acima, faça o que se pede a seguir:

1. Mostre que a expressão $(a \times (b \div c))$ pode ser obtida a partir da gramática dada.
2. Dada a expressão $(((a + b) \times c) + (d \times e))$, existe apenas uma árvore de derivação possível? É correto afirmar que a gramática acima é ambígua? Justifique sua resposta.

## Questão 5

> Nota: Difícil, mas boa para testar o conhecimento aprofundado dessa disciplina.

Seja `BAL`<sub><small><code>AFD</code></small></sub> = { $\langle$ M \rangle \| M$ é um AFD que aceita alguma cadeia que contém o mesmo número de 0 e 1 }. Mostre que `BAL`<sub><small><code>AFD</code></small></sub> é decidível. (Dica os teoremas de Linguages Livres de Contexto são úteis aqui.)

<details>
   <summary>Resposta...</summary>.
<blockquote>A linguagem de todas as cadeias com igam número de <code>0</code>s e <code>1</code>s é uma linguagem livre de contexto, gerada pela gramática $S \rightarrow 1S0S | 0S1S | \varepsilon$. Seja <code>P</code> o autômato de pilha (AP) que reconece essa linguagem, construa uma MT <code>B</code> para <code>BAL<sub><small>AFD</small></sub></code>, que opera da seguinte forma: Sobre a entrada $\langle B \rangle$, onde <code>B</code> é um AFD, use <code>B</code> e <code>P</code> para construir um novo AP <code>R</code> que reconheça a intersecção das linguagens de <code>B</code> e <code>P</code>. Então, teste se a linguagem de <code>R</code> é vazia. Se sua linguagem for vazia, <i>rejeite</i>, caso contrário, <i>aceite</i>.</blockquote>

</details>
