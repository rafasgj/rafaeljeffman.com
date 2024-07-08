---
section: Linguagens Formais e Autômatos
title: Propriedades das Linguagens Livres de Contexto
subtitle:
layout: lecture
last_occurrence: 
copy: 2024
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2024/automata
---

## Propriedades das linguagens livres de contexto

* Aqui, pretendemos descobrir:
    1. Como determinar se uma linguagem é livre de contexto?
    2. A classe das linguagens livres de contexto é fechada para:
        * União?
        * Intersecção?
        * Concatenação?
        * Complemento?
    3. Como verificar se uma linguagem livre de contexto é finita, infinita ou vazia?
* O que temos certeza é que não temos um algoritmo capaz de analizar duas linguagens livres do contexto quaisquer e decidir se são iguais ou diferentes.


### Como determinar se uma linguagem é livre de contexto?

Para mostrar que uma linguagem é livre de contexto, é suficiente que se crie um autômato de pilha ou uma gramática livre de contexto para expressá-la.

Para demontrar que uma linguagem não é livre do contexto, utilizamos o **lema do bombeamento para lingagens livres de contexto**, de forma análoga às linguagens regulares.

O lema do bombeamento para linguagens livres de contexto define que, se $L$ é uma linguagem livre de contexto, então:

* existe uma constante $n$, tal que:
    * para qualquer palavra $w \in L$, onde $\|w\| \ge n$, $w$ pode ser definida com $w = u\;x\;v\;y\;w$, onde:
        * $\|x\;v\;y\| \le n$
        * $\|x\;y\| \ge 1$
    * para todo $i \ge 0$, temos que $ux^{i}vy^{i}w \in L$

Assim como no caso das linguagens regulares, a prova é por contradição.


#### Exemplo 1

* A linguagem $L = a^{n}b^{n}c^{n}$ é uma LLC?

Assumimos que $L$ é uma LLC, e que existe $w \in L$, logo $w = a^{n}b^{n}c^{n}$.

Pelo lema do bombeamento, $w = uxvyz$ e $\|xvy\| \le n$, logo, sabemos que $xvy$ só pode conter:

* apenas $a$
* apenas $b$
* apenas $c$
* uma combinação de $a$ e $b$
* uma combinação de $b$ e $c$

É impossível conter $a$, $b$ e $c$, porque $xvy$ não é grande o suficiente para isso (uma vez que $\|xvy\| \le n$).

Agora, bombeamos "para baixo", fazendo com que $i = 0$, e a palavra resultante $uvw$ não pode mais conter o mesmo número de $a$, $b$ e $c$, porque a palavra $xy$ só pode conter, no máximo, dois dos símbolos, e portanto o resultado não fará parte de $L$.


#### Exemplo 2

* A linguagem $a^{i}b^{j}c^{k}, 0 \le i \le j \le k$ é uma LLC? 

Para essa demonstração vamos partir do mesmo princípio do exemplo anterior e assumir que $i = j = k$, e assim como antes, $xvy$ não pode conter o mesmo número de $a$, $b$ e $c$, logo, se $xvy$ contém:

* nenhum $a$
    * bombeando com $i = 0$, o número de $a$ não muda, mas o número de $b$ e $c$ reduz, e portanto $x^{0}vy^{0} \notin L$;
* nenhum $b$, mas contém $a$
    * bombeando com $i = 2$, o número de $a$ será maior que o número de $b$, e portanto $x^{2}vy^{2} \notin L$;
* nenhum $b$, mas contém $c$
    * bombeando com $i = 0$, o número de $b$ não muda, mas o número de $c$ reduz, e portanto $x^{0}vy^{0} \notin L$;
* nenhum $c$
    * bombeando com $i = 2$, o número de $a$ ou $b$ será maior que o número de $c$, e portanto $x^{2}vy^{2} \notin L$.

Como conseguimos uma contradição para todos os casos, a linguagem não é livre de contexto.

#### Exemplo 3

* A linguagem $ww$ é uma LLC? 

Para demonstrar esse caso, precisamos ter cuidado na escolha da palavra para analisar, pois se escolhermos $0^{n}10^{n}1$, poderímos dividir a palavra como:

$$
\underbrace{000\dots000}_{u}\underbrace{0}_{x}\underbrace{1}_{v}\underbrace{0}_{y}\underbrace{000\dots 000}_{w}
$$

E conseguiríamos bombear $x^{i}vy^{i}$.

Mas se escolhermos a palava $0^{n}1^{n}0^{n}1^{n}$, podemos demonstrar que essa palavra não pode ser bombeada.

* Se $xvy$ contem os primeiros $0$, ao bombearmos com $i = 2$ teremos mais zeros na primeira metade, logo $w \notin L$;
* Obtemos o mesmo resultado escolhendo apenas um dos símbolos em qualquer ponto da palavra.
* Se escolhermos uma combinação de $0$ e $1$ em qualquer metade da palavra e bombearmos com $i \gt 2$, obteremos mais elementos nessa metade do que na outra metade palavra, logo $w \notin L$;
* Só nos resta escolhermos uma posição no meio da palvra, e se bombearmos com $i ] 0$, obteremos $0^{n}1^{i}0^{j}1{n}$, e claramente, $i \lt n$ e $j \lt n$, logo $w \notin L$.

Logo, $L = ww$ não é uma LLC.


## Fechamento de operações nas LLC

### União

As LLC são fechadas para a união.

Dado um autômato de pilha $M_1$ que reconhece $L_1$ e um autômato de pilha $M_2$ que reconhece $L_2$, basta criar um automato de pilha não determinístico $M_3$ que reconhece $M_1$ e $M2$, e decide por um ou outro caminho sem consumir a entrada ($\varepsilon$) e sem modificar a pilha. O autômoto $M_3$ reconhecerá $L_3 = L_1 \cup L_2$. 

### Concatenação

As LLC são fechadas para a concatenação.

Dada uma gramática $G_1 = (V_1, T_1, P_1, S_1)$ e uma gramática $G_2 = (V_2, T_2, P_2, S_2)$, podemos criar uma gramática $G_3$ como

$$
G_3 = (V_1 \cup V_2 \cup {S}, T_1 \cup T_2, P_1 \cup P_2 \cup \{S \rightarrow S_1 S_2\}, S)
$$

Claramente, $G_3$ é uma linguagem livre de contexto e formada pela concatenação de uma palavra de $L_1$ e uma palavra de $L_2$.

### Intersecção

As linguagens livres de contexto não são fechadas para a intersecção.

Sejam $L_1 = \\{a^{n}b^{n}c^{m} \| n \ge 0, m \ge 0\\}$ e $L_2 = \\{a^{m}b^{n}c^{n} \| n \ge 0, m \ge 0\\}$, ambas linguagens são livres de contexto (_Desafio: você consegue demonstrar isso?_), pela intersecção das duas linguagens, podemos obter $L_3$

$$
L_3 = \{ a^{n}b^{n}c^{n} | n \ge 0 \}
$$

Como sabemos que $L_3$ não é uma linguagem livre de contexto, demonstramos que a intersecção não é fechada para as LLC pro contra-exemplo.


### Complemento

Como a intersecção pode ser representada em termos da união e do complemento, e considerando que a intersecção não é fechada para as linguagens livres de contexto, não se pode afirmar que o complemento de uma linguagem livre de contexto é livre de contexto.


## Recursos para esta aula

### Recursos _online_

* [The Pumping Lemma for Context Free Grammars](http://www.math.uaa.alaska.edu/~afkjm/csce351/handouts/cfg-pumping.pdf)

