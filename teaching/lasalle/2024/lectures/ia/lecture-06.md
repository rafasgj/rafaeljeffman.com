---
section: Inteligência Artificial
title: Busca em Jogos
subtitle:
layout: lecture
last_occurrence: 2024-04-08
copy: 2024
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2024/ia
---

## Busca em Jogos

Jogos são interessantes, pois modelam formas de raciocínio do ser humano.

Partimos no estudo com uma pergunta _"Como um computador pode jogar xadrez?"_

1. f(analise, estratégia, tática) -> movimento
    * Não sabemos como modelar isso.
2. Regras IF-THEN
    * Não levam em consideração a avaliação do resultado.
    * Não é possível modelar um bom jogador com essa técnia.
3. Olhar para frente e avaliar
    * Ver todas as consquequências de movimentos e escolher a melhor situação.
    * $s = g(f1, f2, \dots, fn) \rightarrow$ gera um valor estático da "qualaidade' do estado.
        * _Features_ são, por exemplo, a segurança do rei, das pessas, dos possíveis ataques do adversário, tec.
        * Geralmente $g(\dots)$ é um escore linear polinomial, com as features tendo "pesos".
4. Busca de Estados
    * _Branching factor_ (número de filhos por nó) ($b$)
    * Áltura da árvore de estados ($d$)
    * Número de estados = $b^d$
    * Xadrez com British Museum: $10^{120}$ possibilidades para 50 movimentos.
        * Número de átomos no universo: $\~10^{86}$
5. Olhar para a frento, tão longe quanto o possível.

## Algoritmo Minimax

O jogador **MAX** quer maximizar o resultado. O jogador **MIN** quer minimizar o resultado.

```
function minimax(node, depth, maximizingPlayer) is
    if depth = 0 or node is a terminal node then
        return the heuristic value of node
    if maximizingPlayer then
        value := −INF
        for each child of node do
            value := max(value, minimax(child, depth − 1, FALSE))
    else (* minimizing player *)
        value := +INF
        for each child of node do
            value := min(value, minimax(child, depth − 1, TRUE))
    return value
```

Chamada do algoritmo: `minimax(origin, depth, TRUE)`


## ALFA-BETA Prunning

Técnica baseada em _branch and bound_ para reduzir o espaço de busca

```
function alphabeta(node, depth, α, β, maximizingPlayer) is
    if depth == 0 or node is terminal then
        return the heuristic value of node
    if maximizingPlayer then
        value := −INF
        for each child of node do
            value := max(value, alphabeta(child, depth − 1, α, β, FALSE))
            α := max(α, value)
            if value >= β then
                break (* β cutoff *)
    else
        value := +INF
        for each child of node do
            value := min(value, alphabeta(child, depth − 1, α, β, TRUE))
            β := min(β, value)
            if value <= α then
                break (* α cutoff *)
    return value
```

Chamada do algoritmo: `alphabeta(origin, depth, −INF, +INF, TRUE)`

## _Iterative_ ou _Progressive Deepening_

* A cada nível que não precisa ser avaliado o número de avaliações é reduzindo em $\frac{1}{b}$ (ou seja reduz 1 do expoente).
* Limita o número de níveis que são avaliados. 

## Deep Blue

Construído em 1997, realizada 2 milhões de avaliações estáticas por segundo, avaliava 14 níveis, utilizando:
* Minimax + alfa-beta pruning + Progressive deepening
* computação paralela
* Livro de aberturas e finais de jogos (conhecimento específico do Xadrez)
* Criação desbalanceada da árvore

