---
title: T1 - Analisador recursivo descendente
section: Compiladores
layout: lecture
last_occurrence: "2023/02"
copy: 2023
institution:
  name: Universidade Lasalle Canoas
  link: index.html
---

## Objetivo

Compreender as estruturas básicas de implementação de um parser.


## Tarefas

Dada a gramática livre de contexto:

$$
\begin{align}
& E \rightarrow TE^\prime \\
& E^\prime \rightarrow E \\
& E^\prime \rightarrow \varepsilon \\
& T \rightarrow FT^\prime \\
& T^\prime \rightarrow + E \\
& T^\prime \rightarrow - E \\
& T^\prime \rightarrow \varepsilon \\
& F \rightarrow VF^\prime \\
& F^\prime \rightarrow * E \\
& F^\prime \rightarrow / E \\
& F^\prime \rightarrow \varepsilon \\
& V \rightarrow num \\
& num \rightarrow [0-9][0-9]^{*} \\
\end{align}
$$<br/><br/>

onde $+$ representa a operação de soma, $-$ representa a operação de subtração, $\*$ representa a operação de multiplicação e $/$ representa a operação de divisão; e que $[a-z]$ representa um conjunto de caracters ASCII iniciado em $a$ e terminado em $z$, e que $a^{*}$ representa zero ou mais repetições do caracter $a$.

Implemente um avaliador de expressões aritméticas utilizando a gramática apresentada. Para implementar o avaliador, utilize um analisador sintático recursivo descendente para realizar a análise sintática da expressão.

Responda também às seguintes questões:
* Para a gramática apresentada quais são os conjuntos **FIRST** e **FOLLOW**? 


## Artefatos

Deve ser entregue apenas o _link_ para um repositório público no [Github](https://github.com) ou outro serviço de armazenamento de repositórios [Git](https://git-scm.org).

O repositório deverá conter a implementação do trabalho, e um arquivo README (sugere-se o formato Markdown e um arquivo README.md) contendo instruções para a execução do sistema.

Caso o trabalho inclua questões a serem respondidas, essas questões devem ser respondidas no README.


## Observações

* Em trabalhos que envolvem implementações, a entrega é apenas o link para o repositório público do trabalho
* Em trabalhso que envolvem implemnetações e perguntas, as perguntas devem ser respondidas em um arquivo README, incluído no repositório.
* Em caso de plágio, a nota atribuída ao trabalho será 0 (zero).


## Recursos para a elaboração deste trabalho

* Aho, Lam, Sethi e Ulmann. **Compiladores: Princípios, Técnicas e Ferramentas**. 2<sup>a</sup> ed. Pearson Addison Wesley, 2008.
    * **Capítulo 2**
    * **Páginas 138-147**
* [Recursive descent parser](https://en.wikipedia.org/wiki/Recursive_descent_parser) (Wikipedia)
* [Analizador sintático descendente recursivo](https://pt.wikipedia.org/wiki/Analisador_sint%C3%A1tico_descendente_recursivo) (Wikipedia)

