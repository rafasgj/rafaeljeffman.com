---
title: Revisão de Conceitos
subtitle: Complexidade de Algoritmos e Análise de Desempenho
layout: lecture
last-occurrence: 2023-08-14
copy: 2023
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2023-02-analise-algoritmos
---

## Assunto

1. Linguagens Regulares e Automatos Finitos
    1. DFA, NFA e &-NFA
    2. Conversão NFA-\>DFA
    3. Lema do Bomboamento
        * Seja $L$ uma linguagem regular, existe uma palavra $\omega \in L$ que pode ser escrita como $\omega = xyz$, onde $\\abs{\omega} \ge p$ e $p \ge 1$, tal que:
        1. $\abs{y} \ge 1$
        2. $\abs{xy} \le p$
        3. $(\forall n \ge 0)(xy^{n}z \in L)$
2. Linguagens Livres de Contexto e Automatos de Pilha
    * $L = \\{ a^{n}b^{n}\ \|\ n \ge 0 \\}$
3. Linguagens Recursivas (Automato Linearmente Limitado, Decidibilidade)
4. Linguagens Recursivamente Enumeráveis (Turing Machine)
5. Equivalência de Máquinas

## Questões

1. Prove que $L = \\{ a^{n}b^{n}\ \|\ n \ge 0 \\}$ não é uma linguagem regular.
2. Prove que $L = \\{ a^{n}b^{n}c^{n}\ \|\ n \ge 0 \\}$ não é uma linguagem livre de contexto.
3. **Projeto**
    > Implemente um simulador de automados finitos determinísticos, sendo que a entrada para o programa é dada por um arquivo no formato:
```nohl
q0
a b
q0 q1 q2 q3
q1 q3
q0 q1 a
q1 q1 a
q1 q2 b
q2 q1 b
q2 q3 a
```
    > onde:
    * Linha 1 define o estado inicial
    * Linha 2 define os símbolos do alfabeto
    * Linha 3 define o conjunto de estados
    * Linha 4 define o conjunto de estados finais
    * Linhas 5-_fim do arquivo_ definem as transições entre os estados
4. **Projeto**: Modifique o projeto do item **3** dando suporte a automatos finitos não-determinísticos, sendo que a palavra vazia é representada pelo caracter '&'
5. **Projeto**: Modifique o projeto do item **4** adicionando uma opção para converter o NFA em DFA. 
6. Apesar dos _parsers_ de linguagem de programação, em geral, serem implementados a partir de uma gramática livre de contexto, demonstre que muitas das linguagens de programação de uso geral, como C, C++, Java, Javascript ou Python, são frutos de gramáticas sensíveis ao contexto.

## Recursos para essa aula

### Bibliografia

1. Menezes, Paulo Blauth. **Linguagens Formais e Automatos**. 3<sup>a</sup> Ed. Bookman, 2011. 
2. Hopcroft, John E., Ullman, D. Jeffrey, Motwani, Rajeev. **Introdução à Teoria de Autômatos, Linguagens e Computação**. Elsevier, 2002. 
3. Sipser, Michael. **Introdução à Teoria da Computação**. Cengage Learning, 2015.

<!--
S->aXbC
X->S | &
Cb->bC
C->c
-->
