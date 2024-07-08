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
  - lecture
---

## Autômatos Finitos Determinísticos

1. Dado o alfabeto $\Sigma = \{a, b\}$ e as seguintes descrições de linguagens, defina o autômato finito determinístico correspondente.
    * $\\{w \| w\;\text{tem o mesmo numero de pares de ab e ba}\\}$, por exemplo $aba$, $abba$ pertencem a linguagem, mas $aab$, $bbaa$ não pertencem a linguagem.
    * $\\{w \| w\;\text{tem o um numero impar de a's e b's}\\}$
    * $\\{w \| w\;\text{tem pelo menos uma das subsstrings aab, aba, bab eu bba}\\}$
    * $\\{w \| w\;\text{tem, no máximo duas letras b}\\}$
    * $\\{w \| w\;\text{tem o mesmo símbolo na primeira e na última posição}\\}$
    {:class="lettered"}
2. Para os seguintes autômatos finitos determinísticos, defina a regra de formação das linguagens definidas pelos autômatos.
    * ![exercício 2.1](/images/dfa_ex_1.svg){:style="min-height:150px !important;min-width: 35ch !important;vertical-align:middle !important; display:inline; padding: 20px 0px !important;"}
    * ![exercício 2.2](/images/dfa_ex_2.svg){:style="min-height:100px !important;min-width: 25ch !important;vertical-align:middle !important; display:inline; padding: 20px 0px !important;"}
    * ![exercício 2.3](/images/dfa_ex_3.svg){:style="min-height:150px !important;min-width: 35ch !important;vertical-align:middle !important; display:inline; padding: 20px 0px !important;"}
    {:class="lettered"}

## Conversão de NFA-DFA

1. Dados os seguintes autômatos finitos não-determinísticos, determine o conjunto $\varepsilon\text{-closure}$ para todos os estados do autômato:
    * ![exercício 3.1](/images/dfa_ex_4.svg){:style="min-height:150px !important;min-width: 35ch !important;vertical-align:middle !important; display:inline; padding: 20px 0px !important;"}
    * ![exercício 3.2](/images/dfa_ex_6.svg){:style="min-height:200px !important;min-width: 45ch !important;vertical-align:middle !important; display:inline; padding: 20px 0px !important;"}
    {:class="lettered"}
2. Dados os seguintes autômatos finitos não determinísticos, converta-os em autômatos finitos determinísticos.
    * ![exercício 4.1](/images/dfa_ex_4.svg){:style="min-height:150px !important;min-width: 35ch !important;vertical-align:middle !important; display:inline; padding: 20px 0px !important;"}
    * ![exercício 4.2](/images/dfa_ex_5.svg){:style="min-height:150px !important;min-width: 35ch !important;vertical-align:middle !important; display:inline; padding: 20px 0px !important;"}
    * ![exercício 4.3](/images/dfa_ex_6.svg){:style="min-height:200px !important;min-width: 45ch !important;vertical-align:middle !important; display:inline; padding: 20px 0px !important;"}
    {:class="lettered"}

## Expressões Regulares

1. Dados os seguintes autômatos finitos, defina a expressão regular equivalente:
    * ![exercício 5.1](/images/dfa_ex_3.svg){:style="min-height:150px !important;min-width: 35ch !important;vertical-align:middle !important; display:inline; padding: 20px 0px !important;"}
    * ![exercício 5.2](/images/dfa_ex_5.svg){:style="min-height:150px !important;min-width: 35ch !important;vertical-align:middle !important; display:inline; padding: 20px 0px !important;"}
    * ![exercício 4.3](/images/dfa_ex_6.svg){:style="min-height:200px !important;min-width: 45ch !important;vertical-align:middle !important; display:inline; padding: 20px 0px !important;"}
    {:class="lettered"}
2. Dadas as expressões regulares, defina o **autômato finito determinístico** equivalente:
    * $(0(0\|1)^{\*}0)\|(1(0\|1)^{\*}1)\|0\|1$
    * $(0\|1)^{\*}010(0\|1)^{\*}$
    * $(a\|b)^{\*}aabb^{\*}$
    {:class="lettered"}
