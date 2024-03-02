---
title: LogoVM
subtitle: Uma máquina virtual para o ensino de projeto e implementação de compiladores.
layout: section
copy: 2022-2024
date: 2024-03-02
lang: pt
sections:
  - LogoVM
tags:
  - compiladores
  - ensino
  - linguagens de programação
abstract: |
  LogoVM é uma máquina virtual de pilha que provê um ambiente de
  execução simplificado, para o ensino do projeto e implementação
  de compiladores.  A máquina virtual é uma máquina de pilha com um
  conjunto reduzido de instruções, instruções de alto nível, e
  manipulação de elementos de memória (_heap_ e _stack_)
  simplificados.
---

LogoVM é uma máquina virtual de pilha que provê um ambiente de
execução simplificado, para o ensino do projeto e implementação
de compiladores.  A máquina virtual é uma máquina de pilha com um
conjunto reduzido de instruções, instruções de alto nível, e
manipulação de elementos de memória (_heap_ e _stack_) simplificados.

A máquina virtual também provê facilidades para desenho (pontos e
linhas), dado que o objetivo original era a implementação de um
compilador da linguagem `Logo`, de onde vem o nome do projeto.

## Motivação

No ano de 2022, lecionei a disciplina [Compiladores] para o curso de Ciência da Computação na [Universidade LaSalle Canoas], onde a ementa incluia todas as fases do processo de compilação, desde a análise léxica, até a geração de código executável, com apenas 16 aulas para exposição e discussão dos assuntos. Embora seja um cronograma bastante comum nas faculdades da região, é um cronograma, na minha opinião, muito agressivo, que exige uma grande dedicação dos alunos, talvez, um nível dedicação que eles não consigam ou não possam atingir, por falta de tempo, interesse (a disciplina é obrigatória), ou mesmo conhecimento prévio.

Embora a construção de um compilador do início ao fim, da gramática a geração de código, seja um desafio interessante para se propor aos alunos, devido ao tempo disponível, esse pode ser um desafio difícil de atingir, principalmente pelo desconhecimento de código de baixo nível, como assembly x86 ou ARM, ou os detalhes de baixo nível da Java Virtual Machine (bytecode, Java assembler, ou a estrutura de arquivos ".class").

A LogoVM foi desenvolvida com o intuito de reduzir a curva de aprendizado do ambiente de execução, facilitar a depuração do código gerado, e prover um ambiente completo o suficiente para que o conhecimento adquirido seja facilmente adaptado a outros ambientes, como por exemplo, a Java Virtual Machine, na qual a LogoVM foi inspirada.

## Documentos e Repositórios relacionados

* [LogoVM Repository](https://github.com/rafasgj/logovm){:target="\_blank"}

[compiladores]: /teaching/lasalle
[github repository]: https://github.com/rafasgj/logovm
[universidade lasalle canoas]: https://unilasalle.edu.br/canoas
