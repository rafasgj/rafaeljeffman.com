---
title: Linguagens Formais e Autômatos
institution: Universidade LaSalle Canoas
nickname: automata
start: 2024-03-07
layout: class_plan
section: lasalle
sections:
  - Teoria da Computação
  - Matemática para Computação
extra_styles:
  - cronograma
  - page_summary
objectives:
  - Apresentar modelos matemáticos para formalização, especificação e reconhecimento de linguagens computacionais
  - Capacitar o aluno para a compreensão e/ou desenvolvimento de software básico incluindo compiladores e linguagens de programação
  - Estudar os principais fundamentos da teoria da computação associados à computabilidade e solucionabilidade de problemas
  - Estudar formalização de programas, máquinas, computação e formalismos que os definem
requirements:
  - Implementação de estruturas de dados (listas encadeadas e mapas)
  - Grafos
  - Fundamentos de matemática para computação (matemática discreta)
  - Conhecimentos básicos da linguagem de programação Python
  - Conhecimentos básicos de controle de versão com Git e Github
competences:
  - Tratar problemas computacionais de maneira formal. 
  - Formalizar e especificar modelos matemáticos capazes de reconhecer linguagens com base nos conceitos teóricos da computação.
  - Desenvolver aplicações computacionais tais como compiladores, modelagem de sistemas e linguagens de programação.
  - Aprimorar aplicações computacionais já existentes.
learning_unities:
  - Análise crítica sobre os diversos tipos de autômatos finitos como reconhecedores de linguagens.
  - Compreensão sobre os formalismos geradores de palavras para criação de uma linguagem de programação.
  - Análise reflexiva das diferentes propriedades das linguagens regulares.
  - Estudo e prática de forma colaborativa sobre as gramáticas livres de contexto, árvore de derivação e suas simplificações correlacionando e contextualizando com as fases de um compilador.
  - Visão sistêmica sobre as formas normais de Chomsky como ferramenta de padronização de geradores de linguagens.
  - Compreensão sobre os formalismos associados às linguagens livres de contexto para o seu reconhecimento com postura analítica.
  - Identificação e análise reflexiva acerca das propriedades de fechamento e lema do bombeamento das linguagens livres de contexto.
  - Análise crítica para aplicação da Máquina de Turing como reconhecedor de linguagem.
  - Realização de simulações e experimentos práticos de linguagens formais, solucionando problemas de forma individual e cooperativa.
grading:
  g1:
    t1: 1.0
    t2: 2.0
    t3: 2.0
    p1: 5.0
  g2:
    t4: 1.0
    t5: 2.0
    t6: 2.0
    p2: 5.0
references:
  bibliografia:
    - "SIPSER, Michael. [**Introdução a Teoria da Computação**](https://integrada.minhabiblioteca.com.br/#/books/9788522108862/){:target='_blank'}. Cengage Learning. 2015"
    - "Menezes, Paulo Blath. [**Linguagens Formais e Autômatos**](https://integrada.minhabiblioteca.com.br/reader/books/9788577807994){:_target='_blank'}. 6<sup>a</sup> ed. Bookman, 2011."
    - "<span id='hopcroft'>HOPCROFT, John E.; ULLMAN, Jeffrey D.; MOTWANI, Rajeev</span>. **Introdução à Teoria de Autômatos, Linguagens e Computação**. Tradução da 2<sup>a</sup> Ed. Elsevier, 2002."
    - "LEHMAN, Eric; LEIGHTON, F. Thomson; MAYER, Albert R. [**Mathematics for Computer Science**](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf). MIT. 2015"
    - "AHO & ULLMAN. [**Foundations of Computer Science**](http://infolab.stanford.edu/~ullman/focs.html) - fora de catálogo."
  "recursos _online_":
    - "[MIT 18.040j Theory of Computation](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/) - Michael Sipser"
    - "[MIT 6.042j Mathematics for Computer Science](https://openlearninglibrary.mit.edu/courses/course-v1:OCW+6.042J+2T2019/course/) - _Unit 1 - Proofs_ (2019)"
    - "[MIT 6.042j Mathematics for Computer Science](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/) - Inclui video aulas (2010)"
    - "[Stanford CS154 - Introduction to the Theory of Computation](https://www.youtube.com/playlist?list=PLjG2IDGftWft9Y11xC0sfgeT5jyTJqB-i) - Omer Reingold (2020)"
    - "[Simulador de DFA, NFA e PDA](http://automatonsimulator.com/)"
lectures:
  - topics:
    - Apresentação da disciplina
    - Lingagens e Problemas
    - Aplicação prática da Teoria da Computação
    - Avaliações e logística da disciplina
    - Revisão de conceitos básicos
    lecture: true
  - topics:
    - Revisão de conceitos básicos
    - Demonstrações e Provas
    lecture: true
  - topics:
    - Demonstrações e Provas
    lecture: true
  - topics:
    - _Feriado_
    lecture: false
  - topics:
    - Gramáticas, Linguagens e Autômatos
    lecture: true
  - topics:
    - Liguagens Regulares e Autômatos Finitos
    lecture: true
  - topics:
    - Conversão de automatos finitos não-determinísticos em automatos finitos determinísticos
    - Expressões regulares
    - Especificação dos trabalhos [T1](lectures/automata/trabalho-01) e [T2](lectures/automata/trabalho-02).
    lecture: false 
  - topics:
    - Fecho das linguagens regulares
    - Lema do Bombeamento
    - Gramáticas Livres de Contexto
    - Automatos de Pilha
    lecture: true
  - topics:
    - Exercícios de revisão (online devido a eventos climáticos)
    lecture: true
  - topics:
    - Aula convertida em exercícios domiciliares devido a enchentes no RS.
    lecture: false
  - topics:
    - Aula convertida em exercícios domiciliares devido a enchentes no RS.
    lecture: false
  - topics:
    - Retorno as aulas online. Revisão de conteúdos.
    lecture: false
  - topics:
    - _Feriado_
    lecture: false
  - topics:
    - Gramáticas Livres de Contexto
    lecture: false
  - topics:
    - Propriedades das Linguagens Livres de Contexto
    - Lema do bombeamento para linguagens livres de contexto
    lecture: true
  - topics:
    - Revisão das Linguagens Livres de Contexto
    - Máquinas universais
    - Decidibilidade
    lecture: false
  - topics:
    - Problemas indecidíveis
    - Redutibilidade
    - Exercícios
    lecture: false
  - topics:
    - Exercícios de revisão
    lecture: false
  - topics:
    - Prova G2 (P1)
    - Correção da Prova e Exercícios de Revisão.
    lecture: false
  - topics:
    - Prova G2 (P2)
    lecture: false
homework:
    - T1: DFA evaluation
    - T2: NFA->DFA conversion
    - T3: Exercises
    - T4: GLC definition (for a simple prgramming language)
    - T5: Regex->DFA conversion
    - T6: Turing Machine implementation
---
