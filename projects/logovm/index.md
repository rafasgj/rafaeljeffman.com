---
title: LogoVM
subtitle: Uma máquina virtual para o ensino de compiladores.
layout: section
---

LogoVM é uma máquina virtual de pilha que provê um ambiente de execução simplificado, para o ensino do projeto e implementação de compiladores.  A máquina virtual é uma máquina de pilha com um set reduzido de instruções, instruçẽs de alto nível, e primitivas para _turtle graphics_, facilitando a tradução de programas da linguagem Logo para uma linguagem de baixo nível.

* [Introdução](#motivação)
* [Especificação da VM](logovm_specs)
* [LogoASM](logovm_asm)
* [LogoVM 
Repository](https://github.com/rafasgj/logovm){:target="\_blank"}
* [LogoVM ASM](https://github.com/rafasgj/logoasm){:target="\_blank"}

## Motivação

No ano de 2022, lecionei a disciplina [Compiladores] para o curso de Ciência da Computação na [Universidade LaSalle Canoas], onde a ementa incluiatodas as fases do processo ed compilação, desde a análise léxica, até a geração de código executável, com apenas 16 aulas para exposição e discussão dos assuntos. Embora seja um cronograma bastante comum nas faculdades da região, é um cronograma, na minha opinião, muito agressivo, que exige uma grande dedicação dos alunos, talvez, um nível dedicação que eles não consigam ou não possam atingir, por falta de tempo, interesse (a disciplina é obrigatória), ou mesmo conhecimento prévio.

Embora a construção de um compilador do início ao fim, da gramática a geração de código, seja um desafio interessante para se propor aos alunos, devido ao tempo disponível, esse pode ser um desafio difícil de atingir, principalmente pelo desconhecimento de linguagens de baixo nível, como assembly x86 ou ARM, ou os detalhes de baixo nível da Java Virtual Machine (bytecode, Java assembler, ou a estrutura de arquivos ".class").

A LogoVM foi desenvolvida com o intuito de reduzir a curva de aprendizado do ambiente de execução, facilitar a depuração do código gerado, e prover um ambiente completo o suficiente para que o conhecimento adquirido seja facilmente adaptado a outros ambientes, como por exemplo, a Java Virtual Machine, na qual a LogoVM foi inspirada.


[compiladores]: /teaching/lasalle
[github repository]: https://github.com/rafasgj/logovm
[universidade lasalle canoas]: https://unilasalle.edu.br/canoas
