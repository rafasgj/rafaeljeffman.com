---
title: T2 - Analisador de expressão com tabela de símbolos
section: Compiladores
layout: lecture
last_occurrence: "2023/02"
copy: 2023
institution:
  name: Universidade Lasalle Canoas
  link: index.html
---

## Objetivo

Entender o processo de definição de uma linguagem de programação simples e a implementação utilizando tabelas de símbolos.

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

Alterar a gramática para que seja possível realizar operações de potenciação com o operador $\^$, por exemplo $2\^5 = 32$, e operações de atribuição de valores a identificadores, onde os identificadores podem ser definidos como $id \rightarrow [\_a-zA-Z][\_a-zA-Z0-9]^{\*}$, e que esses identificadores possam ser utilizados nas expressões, por exemplo $a = 2 * 3 + 4\ /\ b$.

Altere a [implementação do trabalho T1](trabalho-01) para que o avaliador de expressões utilize a nova gramática. O novo avaliador deve aceitar múltiplas expressões, sendo que cada expressão deve ser definida em uma linha, por exemplo:
```nohl
b = 18 * 2

```

## Artefatos

Deve ser entregue apenas o _link_ para um repositório público no [Github](https://github.com) ou outro serviço de armazenamento de repositórios [Git](https://git-scm.org).

O repositório deverá conter a implementação do trabalho, e um arquivo README (sugere-se o formato Markdown e um arquivo README.md) contendo instruções para a execução do sistema.

A nova gramática deve estar descrita no arquivo README do repositório.

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

