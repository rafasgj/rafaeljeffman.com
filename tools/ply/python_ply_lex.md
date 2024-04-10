---
section: Compiladores
title: Implementação do Analisador Léxico com PLY
layout: main
tags:
  - compiladores
  - analisador léxico
  - lexer
  - python
  - ply
copy: 2024
date: 2024-04-10
---

<!--
> Este artigo é parte de uma série de artigos sobre a [implementação de um compilador com Python e PLY](python_ply_compiler).
-->

O analisador léxico é responsável pela primeira etapa do processo de compilação, transformando a sequência de caracteres que forma o código fonte do programa em uma sequência de _tokens_ que serão consumidos pelo analisador sintático. 

É comum que o analisador léxico interaja com a tabela de símbolos. Por exemplo, palavras reservadas de uma linguagem são semelhantes a identificadores e o analisador léxico pode consultar a tabela de símbolos para identificar o tipo de token reperesentado pelo lexema, ou criar uma entrada na tabela de símbolos para um novo identificador na tabela de símbolos.

Nesta série de artigos, é utilizada a seguinte :

$$
\begin{align}
& P \rightarrow S\ O \\
& O \rightarrow S\ O\ |\ \epsilon \\
& S \rightarrow A\ L\ |\ E\ L\\
& A \rightarrow \textbf{id} = E \\
& E \rightarrow E + E\ |\ E - E\ |\ E * E\ |\ E\ /\ E\ |\ (\ E\ )\ |\ \textbf{id}\ |\ \textbf{num} \\
& L \rightarrow \textbf{eoe}
\end{align}
$$

Para esta linguagem de avaliação de expressões aritméticas, devemos reconhecer os símbolos terminais que representam operadores (${operator}$), parênteses, números (${num}$) e identificadores de variáveis (${id}$). Cada um dos símbolos pode ser representado por uma expressão regular.

Os _operadores_ possuem um único caracter, e este carecter está contido no conjunto $\lbrace+, -, *, /, =\rbrace$. Os parênteses podem ser vistos como operadores.

Os _números_ podem ser inteiros ou valores de ponto flutuante. Um _número inteiro_ é um número com _um ou mais_ dígitos decimais ($\lbrace0, 1, 2, 3, ,4, 5, 6, 7, 8, 9\rbrace$). Os _números de ponto flutuante_ podem ser definidos como um número inteiro seguindo de um ponto ('.') e _zero ou mais_ dígitos decimais. Qualquer número pode ser precedido pelos sinais $+$ ou $-$, indicando ser um número positivo ou negativo. Ou seja, um _número_ possui um sinal opcional, uma sequencia de um ou mais dígitos decimais, e uma parte opcional contendo um ponto e zero ou mais dígitos decimais.

Os identificadores de variáveis seguem as regras tradicionais das linguagens de programação derivadas da linguagem C, onde um identificador começa com uma letra maiúscula ou minúscula ou um símbolo de _sublinhado_ ('_') seguido de zero ou mais letras maiúsculas ou minúsculas, símbolos de sublinhado ou dígitos decimais.

Conevertendo essas regras para expressões regurares, os símbolos reconhecidos pelo analisador léxico podem ser definidos como:

$$
\begin{align}
id & \rightarrow [\_a-zA-Z][_a-zA-Z0-9]* \\
num & \rightarrow [+-]?[0-9]+([.][0-9]*)? \\
operator & \rightarrow [-*+/()=]
\end{align}
$$

Como o analisador léxico é a parte do compilador que lida diretamente com o código fonte, ele pode ser utilizado para remover comentários e espaço em branco no código fonte, além de manter um contador de linhas do código fonte, que pode ser utilizado para prover informações, como erros, para o usuário.

### Implementação do analisador léxico com PLY

Para implementar o analisador léxico com o PLY, utilizaremos o módulo `lex`:

```python
from ply import lex
```

Primeiro, definimos os _tokens_ que serão utilizados. Seguindo a gramática apresentada, os _tokens_ serão: 

```python
tokens = (
    "ADD_OP",
    "MUL_OP",
    "ASSIGN_OP",
    "OPEN_PAR",
    "CLOSE_PAR",
    "ID",
    "NUM",
)
```

Note que os operadores são agrupados de forma que os operadores relacionados a soma (a subtração pode ser vista como a soma de um número negativo), a multiplicação (a divisão pode ser vista como a multiplicação por $1/x$), e o operador de atribuição e os parenteses são reconhecidos de forma independente.

Com os tokens definidos, criamos associação dos nomes dos tokens com as expressões regulares que eles representam. Essa associação pode ser realizado sob a forma de uma variável global ou com uma função, caso o processamento do _token_ envolva mais do que simplesmente a comparação em relação à expressão regular.

```python
t_ADD_OP = "[-+]"
t_MUL_OP = "[/*]"
t_ASSIGN_OP = "="
t_OPEN_PAR = "[(]"
t_CLOSE_PAR = "[)]"
t_ID = "[_a-zA-Z][_a-zA-Z0-9]*"
```

Com esse formato de definição do token, sempre que um lexema encontrado no código fonte for compatível com as expressões regulares, um objeto _token_ será criado como a seguinte estrutura:

$$
\begin{align}
& token.type\ =\ <token name> \\
& token.value\ =\ <caracteres\ associados\ à\ expressão\ regular>
\end{align}
$$

Por exemplo, ao encontrar o trecho de código fonte `valor = ...`, seriam criados os objetos `token(value="valor", type="ID")` e `token(value="=", type="OPERATOR")`

Para _tokens_ que precisam de um tratamento mais complexo é possível definir o tratamento do lexema a partir de uma função, utilizando o decorador `TOKEN`. Podemos, por exemplo utilizar uma função para converter o valor do lexema para o tipo de dado desejado, por exemplo, no tratamento de literais numéricos:

```python
@lex.TOKEN(r"[+-]?\d+([.]\d*)?")
def t_NUM(token):
    """Extract a number."""
    if "." in token.value:
        token.value = float(token.value)
    else:
        token.value = int(token.value)
    return token
```

O PLY permite que a expressão regular seja utilizada na _docstring_ da funcão que define o _token_, não sendo necessário o uso do decorador. No entanto, ao definir a função dessa forma, se perde a oportunidade de inserir comentários sobre o algoritmo utilizado na função, por exemplo, explicando o formato do valor (_token.value_) criado para o _token_.

Outro ponto importante a ressaltar é que o nome da função, assim como no caso dos _tokens_ definidos como _string_, é importante e define o tipo associado ao _token_. O nome da função deve começar com `t_` seguido do _token_ reconhecido.

O analisador léxico deve avaliar todo e qualquer caracter presente no arquivo fonte, e cada um desses caracteres deve ter uma correspondência na linguagem de programação sendo analisada. Isso pode trazer alguns problemas quando os caracteres utilizados tem como função apenas facilitar a leitura do código e não são relevantes para a linguagem, como as tabulações ("`\t`") e os espaços em branco ("` `") em diversas linguagems.

O PLY utiliza a variável global `t_ignore` para para definir um conjunto de caracteres que, se encontrados no código fonte, será apenas ignorado e não serão adicionados à sequência de _tokens_ gerada. No exemplo a seguir, configuramos o PLY para ignorar espaços em branco, tabulações e o retorno de carro:

```python
t_ignore = " \t\r"
```

Outra função normalmente associada ao analisador léxico é contar o número de linhas no arquivo fonte de entrada, principalmente para o relatório de erros. No exemplo a seguir, é criada uma função que irá contar as linhas do código fonte, adicionando o número de caracteres de nova linha ("`\n`") existentes no `value` do token encontrado:

```python
@lex.TOKEN(r"\n+")
def t_newline(token):
    """Count new lines."""
    token.lexer.lineno += len(token.value)
```

O analisador léxico não possui muita informação sobre os erros que podem ocorrer na análise do código fonte além dos caracteres que são processados, portanto, um erro na leitura dos dados significa que um caracter inválido foi encontrado. A correção de erros no analisador léxico pode utilizar a técnica de _Modo Pânico_, onde a entrada é ignorada até que um lexema de sincronismo seja encotrado (`;`, `}` ou `end`).

O tratamento erros é implementado na função `t_error()`, e como nesse caso não existe um lexema que possa ser utilizado facilmente para sincronismo, a execução é interrompida com um erro:

```python
class IllegalCharacter(Exception):
    """Lexer exception."""

    def __init__(self, char, line):
        """Initialize error with detected invalid char."""
        super().__init__(f"Illegal character: '{char}', at line {line}")


def t_error(token):
    """Report lexer error."""
    raise IllegalCharacter(token.value[0], token.lexer.lineno)
```

Para testar o analisador léxico, pode-se iterar sobre os tokens retornados pelo _lexer_:

```python
analisador_lexico = lex.lex()
analisador_lexico.input(codigo_fonte)
for tk in analisador_lexico:
    print(f"Token: {tk}")
```

## Principais tópicos

* A análise léxica é a primeira etapa na compilação de um programa.
* A entrada do analisador léxico é uma sequencia (_stream_) de caracteres, formada pelo código fonte. 
* A saída do analizador léxico é uma sequencia (_stream_) de _tokens_.
* Um _token_ é representado por um símbolo astrato representando o tipo de unidade léxica, e, normalmente, por um valor obtido a partir do lexema identificado.
* O analisador léxico não tem muitas informações a respeito da linguagem sendo processada, e portanto, a correção de erros normalmente é feita utilizando _Modo Pânico_, onde a entrada é ignorada até que um caracter de sincronismo seja encontrado.

## Instalação do PLY

O _PLY_ não é mais distribuído como um pacote instalável, e para utilizá-lo em um projeto deve ser realizado um método conhecido como _vendoring_, que consiste em adicionar o código ao seu próprio projeto.

Para isso, basta copiar o diretório `src/ply` do repositório do _PLY_ para o seu projeto:
```sh
git clone https://github.com/dabeaz/ply
cp -r ply/src/ply <diretorio_do_projeto>
```

<!--

## Construindo um compilador

Este artigo é parte de uma série de artigos sobre a implementação de um compilador com Python e PLY, você pode segir para a próxima etapa, [a implementação do _parser_](python_ply_yacc), ou escolher onde continuar:

* [Implementando um compilador com Python e PLY](python_ply_compiler)
* _Implementação do Analisador Léxico com PLY_
* [Implementação do Analisador Sintático com PLY](python_ply_yacc)
* [Implementação da tabela de símbolos com Python](compiler_symtable_implementation)
* [Criação da árvore sintática com Python e PLY](python_ply_syntax_tree)

-->

----

Arquivo fonte completo do analisador léxico para a linguagem de avaliação de expressões aritméticas:

[](code/compiler/lexer.py){:class="download fa-solid fa-download"}
```python
# MIT No Attribution
#
# Copyright 2022 Rafael Guterres Jeffman
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THESOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

"""Logo language Lexer."""

from ply import lex


class IllegalCharacter(Exception):
    """Lexer exception."""

    def __init__(self, char, line):
        """Initialize error with detected invalid char."""
        super().__init__(f"Illegal character: '{char}', at line {line}")


tokens = (
    "ADD_OP",
    "MUL_OP",
    "ASSIGN_OP",
    "OPEN_PAR",
    "CLOSE_PAR",
    "ID",
    "NUM",
)

# Characters to be ignored by lexer.
t_ignore = " \t\r"

t_ADD_OP = "[-+]"
t_MUL_OP = "[/*]"
t_ASSIGN_OP = "="
t_OPEN_PAR = "[(]"
t_CLOSE_PAR = "[)]"
t_ID = r"[_a-zA-Z][_a-zA-Z0-9]*"


@lex.TOKEN(r"[+-]?\d+([.]\d*)?")
def t_NUM(token):
    """Extract a number."""
    if "." in token.value:
        token.value = float(token.value)
    else:
        token.value = int(token.value)
    return token


@lex.TOKEN(r"\n+")
def t_newline(token):
    """Count new lines."""
    token.lexer.lineno += len(token.value)


def t_error(token):
    """Report lexer error."""
    raise IllegalCharacter(token.value[0], token.lexer.lineno)


def lexer():
    """Create a new lexer object."""
    return lex.lex()


if __name__ == "__main__":
    import sys

    the_lexer = lexer()
    with (
        open(sys.argv[1], "rt") if len(sys.argv) > 1 else sys.stdin
    ) as source_file:
        the_lexer.input(source_file.read())
    for tk in the_lexer:
        print(tk)
```

## Referências

1. [Repositório do PLY](https://github.com/dabeaz/ply)
2. [Documentação do PLY](https://ply.readthedocs.io/en/latest/)

