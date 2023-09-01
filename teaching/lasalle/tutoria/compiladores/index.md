---
title: Compiladores (Tutoria)
subtitle: Unilasalle - 2023/2
layout: section
sections:
  - Compiladores
  - automata
  - parser
  - lexer
  - grammar
extra_styles:
  - cronograma
  - page_summary
---
{::options parse_block_html="true" /}
<div id="page_summary">
* [Objetivos](#objetivos)
* [Pré-requisitos](#pré-requisitos)
* [Competências](#competências-trabalhadas)
* [Unidades de Aprendizagem](#unidades-de-aprendizagem)
* [Estratégias Metodológicas](#estratégias-metodológicas)
* [Cronograma](#cronograma) 
* [Avaliação](#avaliacao)
* [Material Complementar](#material-complementar)
</div>
{::options parse_block_html="false" /}

## Objetivos

Apresenta os princípios e conceitos de análise léxica, sintática e semântica, bem como geração e otimização de código, proporcionando entendimento sobre o funcionamento dos componentes de um compilador com enfoque prático; desenvolve experimentos sobre diferentes componentes de um compilador.


## Pré-requisitos

Embora os pré-requisitos não sejam obrigatórios, o seu domínio auxiliará muito na evolução do aprendizado:

* Expressões Regulares
* Gramáticas Livres de Contexto
* Paradigmas de Linguagens de Programação
* Estruturas de dados (Árvores e Tabelas Hash)
* Conhecimento intermediário em Python ou C/C++
* Noções básicas de Git e Github


## Competências trabalhadas

As competências trabalhadas na disciplina são:
* Estudar os conceitos essenciais para o projeto de compiladores incluindo análise léxica, sintática, semântica e geração e otimização de código.
* Realizar experimentos relativos aos componentes de um compilador com enfoque prático desenvolvido durante a disciplina com a utilização de ferramentas de geração de compiladores.


## Unidades de aprendizagem

* Análise reflexiva acerca das fases de análise e síntese de um compilador.
* Identificação e análise crítica dos tipos associados a uma linguagem bem como geração de código intermediário.
* Problematização do processo de otimização de código intermediário comprometida com o desempenho de espaço e tempo.
* Identificação e análise crítica sobre os diferentes tipos de instruções geradas no processo de compilação.
* Implementação das diferentes fases de um compilador utilizando ferramentas para tal propósito de forma individual e cooperativa.


## Estratégias metodológicas

Implementação dos componentes de um compilador para uma máquina virtual de pilha simplificada.

## Cronograma

| Grau | Descrição | Peso na nota final |
| :--: | :------------------ | :--- |
| G1 | [Implementação de um analisador recursivo descendente para uma gramática de expressões aritméticas.](trabalho-01) | 2,0 |
| G1 | [Implementação de um avaliador de expressões aritméticas com atribuição e acesso a variáveis.](trabalho-02) | 2,0 |
| G1 | Definição de uma gramática livre de contexto para uma linguagem procedural Turing-complete. | 1,0 |
| G2 | Implementação de um parser para uma gramática livre de contexto. | 1,5 |
| G2 | Geração de uma árvore de derivação com uso tabela de símbolos, para uma gramática livre de contexto. | 1,5 |
| G2 | Geração de código alvo para uma máquina virtual de pilha simplificada. | 2,0 |


## Procedimentos e Critérios de Avaliação {#avaliacao}

A nota final será composta por trabalhos práticos de implementação, e será calculada com  a média (M) dada pela regra `M = (G1 + G2) / 2`, sendo G1 e G2 graus parciais formados totalmente por trabalhos práticos.

Para obter a aprovação, o aluno deve obter uma média (M) igual ou superior a **6**, com frequência mínima de 8 encontros presenciais.

## Material Complementar

### Bibilografia

* Aho, Lam, Sethi e Ulmann. **Compiladores: Princípios, Técnicas e Ferramentas**. 2<sup>a</sup> ed. Pearson Addison Wesley, 2008.
