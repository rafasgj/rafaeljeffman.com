---
title: Compiladores
institution: Lasalle
nickname: compilers
start: 2023-08-03
end: 2023-12-21
layout: tutor
section: LaSalle
sections:
  - linguagens formais
  - compiladores
extra_styles:
  - cronograma
  - page_summary
objectives:
  - |-
    Apresentar os princípios e conceitos de análise léxica, sintática e semântica,
    bem como geração e otimização de código, proporcionando entendimento sobre o
    funcionamento dos componentes de um compilador com enfoque prático
  - Desenvolver experimentos sobre diferentes componentes de um compilador.
requirements:
  - Lingugens regulares, automatos finitos e expressões Regulares
  - Gramáticas Livres de Contexto
  - Paradimas de Linguagens de Programação
  - "Estruturas de dados (Árvores, Grafos e Tebelas _Hash_)"
  - Conhecimento intermediário da linguagem Python
  - Noções básicas de Git e Github
competences:
  - studar os conceitos essenciais para o projeto de compiladores incluindo análise léxica, sintática, semântica e geração e otimização de código.
  - Realizar experimentos relativos aos componentes de um compilador com enfoque prático desenvolvido durante a disciplina com a utilização de ferramentas de geração de compiladores.
learning_unities:
  - Análise reflexiva acerca das fases de análise e síntese de um compilador.
  - Identificação e análise crítica dos tipos associados a uma linguagem bem como geração de código intermediário.
  - Problematização do processo de otimização de código intermediário comprometida com o desempenho de espaço e tempo.
  - Identificação e análise crítica sobre os diferentes tipos de instruções geradas no processo de compilação.
  - Implementação das diferentes fases de um compilador utilizando ferramentas para tal propósito de forma individual e cooperativa.
references:
  "bibliografia":
  - "Aho, Lam, Sethi e Ulmann. **Compiladores: Princípios, Técnicas e Ferramentas**. 2<sup>a</sup> ed. Pearson Addison Wesley, 2008."
grading:
  - name: g1
    deliverables:
    - code: T1
      weight: 4.0
      brief: Implementação de um analisador recursivo descendente para uma gramática de expressões aritméticas.
      due: 6
      url: "trabalho-01"
    - code: T2
      weight: 4.0
      brief: Implementação de um avaliador de expressões aritméticas com atribuição e acesso a variáveis.
      due: 8
      url: "trabalho-02"
    - code: T3
      weight: 2.0
      brief: Definição de uma gramática livre de contexto para uma linguagem procedural Turing-complete.
      due: 9
      url: "trabalho-03"
  - name: g2
    deliverables:
    - code: T4
      weight: 3.0
      brief: Implementação de um parser para uma gramática livre de contexto.
      due: 12
      url: "trabalho-04"
    - code: T5
      weight: 3.0
      brief: Geração de uma árvore de derivação com uso tabela de símbolos, para uma gramática livre de contexto.
      due: 16
      url: "trabalho-05"
    - code: T6
      weight: 4.0
      brief: Geração de código alvo para uma máquina virtual de pilha simplificada.
      due: 19
      url: "trabalho-06"
---
