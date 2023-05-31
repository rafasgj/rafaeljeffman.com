---
section: Compiladores
title: Implementando um compilador com Python e PLY
layout: main
tags:
  - compiladores
  - parser
  - tradução baseada em sintaxe
  - python
  - ply
copy: 2022
date: 2022-11-15
---

As duas primeiras fases do processo de compilação de um código fonte são a análise léxica, que transforma a _string_ de entrada em um conjunto de _tokens_, e a análise sintática, que transforma os _tokens_ em uma árvore sintática e uma tabela de símbolos, e é a partir desses dados que as fases seguintes serão capazes de gerar o código alvo do compilador.

Duas ferramentas muito conhecidas para a criação dos analisadores léxico e sintático são o Lex e o Yacc. Vindas do mundo UNIX, o Lex gera um analisador léxico que transforma a entrada em um conjunto de tokens, e o Yacc permite a criação de um _parser_ que consome a entrada de tokens. Ambas as ferramentas foram originalmente criadas para a linguagem de programação C.

Para criar um compilador com a linguagem Python, podemos utilizar o [PLY](https://ply.readthedocs.io/en/latest/index.html), que oferece os módulos `lex` e `yacc` com uma estrutura muito semelhante às ferramentas tradicionais. Uma das principais vantagens do PLY é sua implementação 100% Python, e sem outras dependências externas.

Apesar de oferecer uma estrutura semelhante, o funcionamento do PLY é diferente das ferramentas UNIX, pois não é necessário um arquivo de especificacão do _parser_ separado do código fonte, e as regras da gramática são definidas junto ao código fonte.

Nesse artigo será desenvolvido um pequeno compilador para expressões aritméticas infixas que irá utilizar uma máquina de pilha para geração do código alvo.

Download complete! Use 'dnf system-upgrade reboot' to start the upgrade.
To remove cached metadata and transaction use 'dnf system-upgrade clean'
The downloaded packages were saved in cache until the next successful transaction.
You can remove cached packages by executing 'dnf clean packages'


## Definindo a gramática da linguagem

Para criarmos um compilador ou tradutor de uma lingagem de programação é necessário definir uma gramática para a linguagem de programação. A gramática de uma linguagem de programação é, normalmente, baseada em um gramática livre de contexto. E os símbolos terminais da gramática, definidos por expressões regulares.

Nesse exemplo iremos implementar uma linguagem simples para avaliação de expressões aritméticas com suporte a variáveis. Essa gramática pode ser definida como:

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

Um programa ($P$), nessa linguagem, é um conjunto de um ou mais commandos ($S$), e cada comando pode ser uma atribuição ($A$) ou uma expressão ($E$).

Um programa exemplo dessa lingagem poderia ser escrito como:

```
a = 3 * 4 + 3 - 2
b = 4 + a * a
c = a - b - (3 * b + 6)
8 + 4 * 2
```

A saída esperada desse programa é:

```
a = 13
b = 173
c = -685
16
```

Este artigo tem múltiplas partes, você pode segir para a próxima etapa, [o analisador léxico](python_ply_lex), ou escolher onde continuar:

* [Implementação do Analisador Léxico com PLY](python_ply_lex)
* [Implementação do _Parser_ com PLY](python_ply_yacc)
* [Implementação da tabela de símbolos com Python](compiler_symtable_implementation)
* [Criação da árvore sintática com Python e PLY](python_ply_syntax_tree)


## Implementando a tabela de símbolos.

Sempre que uma linguagem de programação utiliza símbolos representando valores (variáveis) ou procedimentos e funções, é interessante a utilização de uma tabela de símbolos. Essa tabela é utilizada por diversas fases do processo de compilação de um programa, e é criada pelos analisadores léxico e sintático, e acessada e/ou modificada nas outras fases da compilação.

A implementação da tabela de símbolos pode ser simplificada se utilizarmos _dicionários_ do Python como estruturas de armazenamento dos símbolos. Tanto a tabela de símbolos como cada elemento da tabela são implementados como um dicionário.

Como os dicionários, em Python, são implementados como uma _hashtable_, o acesso aos elementos armazenados é bastante eficiente e nos permite pensar nos símbolos armazenados como sendo objetos com um conjunto arbitrário de atributuos.

Três atributos são muito importantes para essa implementação o nome ($id$) do símbolo, o typo do símbolo, e a linha no qual a operação sobre símbolo está sendo executada.

O nome do símbolo é sua chave primária, e deve ser imutável. A linha (_lineno_) onde o símbolo foi originalmente declarado também é imutável, uma vez que desejamos saber onde o símbolo foi originalmente declarado. O typo (_type_) do símbolo não é tão importante para essa gramática, uma vez que o único tipo de símbolos utilizados é `"VARIÁVEL"`. Esse tipo de informação é importante em outras linguagens com outros tipos como `"FUNÇÃO"`.

Ao adicionar um novo símbolo na tabela de símbolos, um erro deve ser gerado se o símbolo já existe. Esse tipo de regra só é interessante quando um símbolo da linguagem não pode ser redefinido na linguagem e precisa ser declarado ou possuir uma atribuição inicial.

```python
def add_symbol(symbol, sym_type, lineno, **kwargs):
    """Create new symbol in the symbol table."""
    # Verifica a existência de um símbolo.
    obj = get_symbol(symbol)
    if obj:
        raise SymbolRedefinitionError(obj, lineno)
    # Adiciona 'name' e 'type' às propriedades do objeto.
    kwargs["name"] = symbol
    kwargs["type"] = sym_type
    kwargs["lineno"] = lineno
    __symtable[symbol] = kwargs

    return __symtable[symbol]
```

Outra função muito utilizada é a recuperação de dados associados a um símbolo. É interessante que essa função seja bastante eficiente, pois é muito utilizada. Em geral, permitimos que a função não falhe caso o objeto não exista, deixando o tratamento de erro para o ponto que requisitou os dados do símbolo, por tem mais informações sobre a situação em que o símbolo não foi encontrado.

```python
def get_symbol(symbol):
    """Retrieve symbol from symbol table."""
    return __symtable.get(symbol)
```

Em diversas situações é interessante que seja possível modificar um objeto da tabela de símbolos, seja modificando atributos ou criando novos atributos.

```python
def set_symbol(symbol, **kwargs):
    """Set values of a symbol in symbol table."""
    obj = get_symbol(symbol)
    if obj is None:
        raise InternalError(f"Symbol not defined: {original}")
    # 'name' é a chave primária do objeto e não pode ser alterado.
    if "name" in kwargs:
        raise InternalError(
            f"Cannot modify symbol '{original}' attribute 'name'."
        )
    # Queremos saber quando o objeto foi declarado, logo,
    # 'lineno' não pede ser alterado.
    if "lineno" in kwargs:
        raise InternalError(
            f"Cannot modify symbol {original} attribute 'line'."
        )
    # atualiza o objeto.
    obj.update(kwargs)
```

Abaixo, o código completo para a implementação da tabela de símbolos utilizada nesse exemplo:

[](code/compiler/symtable.py){:class="download fa-solid fa-download"}
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

"""Implement a symbol table."""

__symtable = {}


class SymbolRedefinitionError(Exception):
    """Error raised when a symbol is already defined."""

    def __init__(self, obj, lineno):
        """Initialize error with proper message."""
        super().__init__(
            f"Redeclaration of symbol: {obj['name']}:{lineno}: "
            + f"Previously declared at line {obj['lineno']}"
        )


class InternalError(Exception):
    """Error raised when a symbol is already defined."""

    def __init__(self, msg):
        """Initialize error with proper message."""
        super().__init__(f"Internal error: {msg}")


def add_symbol(symbol, sym_type, lineno, **kwargs):
    """Create new symbol in the symbol table."""
    obj = get_symbol(symbol)

    if obj:
        raise SymbolRedefinitionError(obj, lineno)

    kwargs["name"] = symbol
    kwargs["type"] = sym_type
    kwargs["lineno"] = lineno
    __symtable[symbol] = kwargs
    return __symtable[symbol]


def set_symbol(symbol, **kwargs):
    """Set values of a symbol in symbol table."""
    obj = get_symbol(symbol)
    if obj is None:
        raise InternalError(f"Symbol not defined: {symbol}")
    if "name" in kwargs:
        raise InternalError(
            f"Cannot modify symbol '{symbol}' attribute 'name'."
        )
    if "lineno" in kwargs:
        raise InternalError(f"Cannot modify symbol {symbol} attribute 'line'.")
    obj.update(kwargs)


def get_symbol(symbol):
    """Retrieve symbol from symbol table."""
    return __symtable.get(symbol)
```

## Gerando uma árvore sintática

Ao reduzira as regras de derivação da gramática, o _parser_ LALR(1) cria uma árvore de derivação a partir das folhas em direção à raiz, por isso dizemos que é uma estratégia ascendente (_bottom-up_) de analise sintática.

Essa árvore de derivação é a árvore sintática do programa, e podemos ver a árvore criando nós _internos_ ou _folhas_ durante a execução do analisador sintático. Por exemplo, podemos criar um nó _folha_ em uma regra que avalia um símbolo terminal, e associar esse nó ao nó _interno_ do não terminal da regra:

```python
def p_value_expr_id(prod):  # noqa: D205, D400, D403, D415
    """value_expr : ID"""
    node = new_node("value_expr")
    leaf = new_leaf("ID", value=prod[1])
    append_node(node, leaf)
    prod[0] = node
```

Em uma regra com várias produções criamos os nós e os adicionamos na ordem em que aparecem na regra, criado, dessa forma, uma árvore que pode ser percorrida depois:

```python
def p_value_expr_par(prod):  # noqa: D205, D400, D403, D415
    """value_expr : OPEN_PAR value_expr CLOSE_PAR"""
    node = new_node("value_expr")
    append_node(node, new_leaf("OPEN_PAR", value="("))
    append_nde(p[2])
    append_node(node, new_leaf("CLOSE_PAR", value=")"))
    prod[0] = node
```

Utilizando dicionários e listas do Python para implementar os métodos de manipulação da árvore, o código fica bastante simples:

```python
def new_node(name):
    """Create a new node object."""
    return dict(name=name, children=[])


def append_node(node, new_node):
    """Append a node or leaf to a node."""
    assert isinstance(node, dict) and "children" in node
    node["children"].append(new_node)


def new_leaf(name, **kwargs):
    """Create a new leaf object."""
    return dict(name=name, value=kwargs)
```

Uma outra vantagem da utilização de dicionários é que é fácil de visualizar, no console, a estrutura de árvore utilizando os módulos `json` ou `yaml` do Python (para utilizar o `yaml` você precisara adicionar um pacote tipo `pyyaml` àsanalisar dependências do projeto):

```python
mylex = lexer()
parser = yacc.yacc(start="program")
program = parser.parse(SOURCE, lexer=mylex, tracking=False)
print(yaml.dump(program, indent=2, sort_keys=False))
```

Executando essa versão na entrada `a = 1 + 3 * 2 * 4` a árvore sintática gerada é:

```yaml
name: program
children:
- name: expression
  children:
  - name: assignment_expression
    children:
    - name: ID
      value:
        value: a
    - name: ASSIGN_OP
      value:
        value: '='
    - name: value_expr
      children:
      - name: value_expr
        children:
        - name: NUM
          value:
            value: 1
      - name: ADD_OP
        value:
          value: +
      - name: value_expr
        children:
        - name: value_expr
          children:
          - name: value_expr
            children:
            - name: NUM
              value:
                value: 3
          - name: MUL_OP
            value:
              value: '*'
          - name: value_expr
            children:
            - name: NUM
              value:
                value: 2
        - name: MUL_OP
          value:
            value: '*'
        - name: value_expr
          children:
          - name: NUM
            value:
              value: 4
```

Você pode baixar os arquvios [tree.py](code/compiler/tree.py) e [parse_tree.py](code/compiler/parse_tree.py) para estudar o código e testar os exemplos.

<!-- ## Tradução Dirigida pela Sintaxe

## Gerando código intermediário

## Gerando código objeto para uma máquina de pilha

Dada uma máquina de pilha com os commandos:

* PUSH \<value>
    : Empilha o valor \<value> (número ou _string_)
* POP
    : Desempilha um valor da pilha
* LOAD \<var>
    : Empilha o valor de uma variável
* STORE \<var>
    : Desempliha um valor e armazena-o na variável \<var>.
* WRITE
    : Desempilha todos os valores da pilha e imprime na tela.
* READ
    : Lê um valor do teclado e empilha.
* ADD
    : Retira dois valores da pilha, soma e empilha o resultado.
* SUB
    : Retira dois valores da pilha, subtrai e empilha o resultado.
* MUL
    : Retira dois valores da pilha, multiplica e empilha o resultado.
* DIV
    : Retira dois valores da pilha, divide e empilha o resultado.
* CAT
    : Rerita duas _strings_ da pilha, concatena e empilha o resultado.
* HALT
    : Termina o programa

Cujo formato do programa executável segue a seguinte gramática:

$$
\begin{align}
& P \rightarrow\ D\ C \\
& D \rightarrow\ '.data'\ L\\
& L \rightarrow\  \textbf{id}\ V\ L\ |\ \epsilon \\
& V \rightarrow\  \textbf{num}\ |\ \textbf{string}\ |\ \epsilon\\
& C \rightarrow\  '.code'\ S\ O \\
& S \rightarrow\  'push'\ \textbf{value}\ |\ 'pop'\ |\ 'write'\ |\ 'read'\ | \dots \\
& O \rightarrow\  S\ O\ |\ \epsilon\\
\end{align}
$$

-->
