---
title: Escrevendo um compilador com Python e PLY
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

## Construindo o analisador léxico com o Lex

O analisador léxico é responsável pela primeira etapa do processo de compilação, transformando a sequência de caracteres que forma o código fonte do programa em uma sequência de _tokens_ que serão consumidos pelo analisador sintático. 

É comum que o analisador léxico interaja com a tabela de símbolos. Por exemplo, palavras reservadas de uma linguagem são semelhantes a identificadores e o analisador léxico pode consultar a tabela de símbolos para identificar o tipo de token reperesentado pelo lexema.

Para a linguagem que avalia expressões aritméticas, o símbolos reconhecidos pelo analisador sintático serão:

$$
\begin{align}
& id \rightarrow [\_a-zA-z][_a-zA-Z0-9]* \\
& num \rightarrow [+-]?[0-9]+([.][0-9]*)? \\
& operator \rightarrow [+*-/]
\end{align}
$$

Como o analisador léxico é a parte do compilador que lida com o código fonte, ele pode ser utilizado para remover comentários e espaço em branco no código fonte, além de manter um contador de linhas do código fonte, que pode ser utilizado para prover informações, como erros, para o usuário.

### Implementação do analisador léxico com PLY

Para implementar o analisador léxico com o PLY, utilizaremos o módulo `lex`:

```python
from ply import lex
```

Primeiro, definimos osnomes _tokens_ que serão utilizados. Seguindo a gramática apresentada, os _tokens_ são: 

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

Por exemplo, ao encontrar o trecho de código fonte `valor = ...`, seriam criados os objetos `token(value="valor", type="ID)` e `token(value="=", type="OPERATOR")`

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

Note que o PLY permite que a expressão regular seja utilizada na _docstring_ da funcão que define o _token_, não sendo necessário o uso do decorado. No entanto, ao definir a função dessa forma, se perde a oportunidade de comentar o algoritmo utilizado na função, caso isso seja interessante.

Outro ponto importante a ressaltar é que o nome da função, assim como no caso dos _tokens_ definidos como _string_, é importante e define o tipo associado ao _token_.

Outro ponto importante do analisador léxico a ser levado em consideração é que todo o caracter presente no arquivo fonte deve ter uma correspondência na linguagem de programação sendo analisada. Isso pode trazer alguns problemas quando os caracteres utilizados tem como função apenas facilitar a leitura do código e não são relevantes para a linguagem, como as tabulações ("`\t`") e os espaços em branco ("` `") em diversas linguagems.

O PLY utiliza a variável global `t_ignore` para para definir um conjunto de caracteres que, se encontrados no código fonte, será apenas ignorado e não serão adicionados à sequência de _tokens_ gerada. No exemplo a seguir, configuramos o PLY para ignorar espaços em branco, tabulações e o retorno de carro:

```python
t_ignore = " \t\r"
```

Outra função normalmente associada ao analisador léxico é contar o número de linhas no arquivo fonte de entrada, principalmente para o relatório de erros.

No exemplo a seguir, criamos uma função que irá contar as linhas do código fonte, adicionando o número de caracteres de nova linha ("`\n`") existentes no `value` do token encontrado.

```python
@lex.TOKEN(r"\n+")
def t_newline(token):
    """Count new lines."""
    # For some unknown reason, new lines are being doubled
    token.lexer.lineno += len(token.value) // 2
```

> Nota: Na versão 3.11 do PLY, a última disponível como pacote e instalável via `pip`, existe um problema na contagem de linhas, e o número de caracteres para o lexema é duplicado. A solução mais simples que parece funcionar para todos os casos´é fazer a divisão inteira do tamanho do lexema por 2.

O analisador léxico não possui muita informação sobre os erros que podem ocorrer na análise do código fonte além dos caracteres que são processados, portanto, um erro na leitura dos dados significa que um caracter inválido foi encontrado.

Para gerar uma condição de erro, deve ser definida uma função `t_error()`:

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

Para utilizar, ou testar o analisador léxico, pode-se utilizar um código como:

```python
analisador_lexico = lex.lex()
analisador_lexico.input(codigo_fonte)
for tk in analizador_lexico:
    print(f"Token: {tk}")
```

O arquivo fonte completo do lexer:

[](code/compiler/lexer.py){:class="download fa fa-download"}
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
    # For some unknown reason, new lines are being doubled
    token.lexer.lineno += len(token.value) // 2


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
        the_lexer.input("".join(source_file.readlines()))
    for tk in the_lexer:
        print(tk)
```

## Construindo o analisador sintático com YACC

Por definição, linguagens de programação possuem regras rígidas para descrever a estrutura sintática de programas bem formados. Um programa pode ser analisado a partir de uma gramática da lingugame e, se aceito pela gramática, considerado um programa bem formado para aquela linguagem de programação.

Podemos definir, para diversas linguagens de programação, gramáticas livres de contexto que definem as estruturas gramaticais que serão utilizadas pelos programas escritos nessa linguagem. O uso de gramáticas provê uma especificação precisa e fácil de entender e extender a linguagem. A estrutura imposta a uma linguagem por uma gramática devidamente projetada facilita a tradução de programas fonte da linguagem para código objeto.

A gramática para a qual queremos implementar o analisador sintático é a mesma vista anteriormente:

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

Para a aceitação e tradução de um programa na linguagem fonte para o código objeto podemos utilizar a tradução dirigida por sintaxe, a qual depende de uma árvore sintática e de uma tabela de símbolos definidos pelo código fonte. Obteremos essas estrutras a partir de um analisador sintático.

O analisador sintático rebebe uma sequência de _tokens_ de um analisador léxico e verifica se essa cadeia de tokens pertence a linguagem representada pela gramática.

Podemos processar uma gramática utilizando uma estratégia universal, que no entanto é pouco eficiente, uma estratégia descendente, que apesar de eficiente requer algumas regras específicas da gramática, ou uma estratégia ascendente. Utilizaremos a estratégia ascendente (com algoritmos LALR) por ser a estratégia utilizada pelas ferramentas baseadas no Yacc.

O primeiro passo para criar um analisador sintático é definir a gramática e suas regras. Já temos a gramática definida, e as regras nos são ditadas pelas regras de avaliação de expressões aritméticas infixas, com seus ordenamentos de precedência e associatividade de operadores.

Em diversas situações é muito bom ter uma gramática não-ambígua, pois o analisador sintático sempre saberá que ação tomar dado o próximo _token_ disponível. No entanto, levando em consideração as regras de associatividade e precedência de operadores na avilação de expressões aritméticas, sabemos que a gramática apresentada é uma gramática ambígua.

Essa ambiguidade ocorre, por exemplo, quando o analisador sintático tem em sua pilha `E + E`, e o próximo token é um `*`. Nesse momento, o analizador precisa decidir se reduz a pilha de acordo com a regra $E \rightarrow E + E$ ou se empilha `*`, seguindo a análise.

Uma forma de resolver essa ambiguidade é rescrever a parte da avaliação de expressões de forma que a precedência seja resolvida pela gramática, como no exemplo:

$$
\begin{align}
& E \rightarrow E + T\ |\ E - T\ |\ T \\
& T \rightarrow T * F\ |\ T\ /\ F\ |\ F \\
& F \rightarrow (\ E\ )\ |\ \textbf{id}\ |\ \textbf{num}
\end{align}
$$

Outra forma de solucionar a ambiguidade na resolução das expressões é informar ao parser LALR qual é a associatividade e a precedência dos operadores. Dessa forma o analisador sintático tem informações suficientes para decidir sobre qual ação tomar.

Para implementar uma tradução dirigida por sintaxe, extendemos a gramática com regras que definem as ações a serem tomadas quando uma redução ocorre. Por exemplo:

$$
\begin{align}
& A \rightarrow \textbf{id} = E && \{ add\_symbol(id,\ 'var',\ value=E);\ \$\$ = E\} &\\
& E \rightarrow E + E && \{ \$\$ = E + E \}\\
& E \rightarrow  E - E && \{ \$\$ = E - E \}\\
& E \rightarrow  E * E && \{ \$|$ = E \times E \}\\
& E \rightarrow  E\ /\ E && \{ \$\$ = E \div E \}\\
& E \rightarrow (\ E\ ) && \{ \$\$ = E \}\\
& E \rightarrow \textbf{id} && \{ \$\$ = get\_symbol(id).value \}\\
& E \rightarrow  \textbf{num} && \{ \$\$ = int(num) \}\\
\end{align}
$$

Com a gramática e suas regras associadas, e com um analisador léxico para a linguagem definido, a implementação do analisador sintático fica bastante facitlitada.

### Implementação do analisador sintático com PLY

Para implementar o analisador sintático com o PLY, utilizaremos o módulo `yacc`:

```python
from ply import yacc
```

Utilizaremos também o analizador léxico criado anteriormente (note que precisamos dos _tokens_ definidos para o analisador léxico):

```python
from lexer import lexer, tokens
```

Uma última alteração que faremos é utilizar nomes mais descritivos na gramática, uma vez que é a melhor forma de definir a gramática da linguagem, e ficará muito mais simples de entender o código gerado. Por exemplo, $P$ será `programa` e $S$ será `statement`.

A implemnetação do analisador sintático é bem mais direta e envolve menos configurações que o analisador léxico. A primeira regra $P \rightarrow S\ O$ pode ser implementada como:

```python
def p_program(prod):
    """program : statement other_statement"""
    statements = [prod[1]]
    if prod[2]:
        statements.extend(prod[2])
    prod[0] = statements
```

A funcão `p_progam` é utilizar pelo parser criado pelo PLY sempre que a redução `program : statement other_statement` ocorrer. E o código da função representam as ações assosciadas à regra da gramática. Note que a `docstring` é importante e **é parte da definição do analisador léxico** pois é utilizada pelo PLY para definir a função que será utilizada quando a regra ocorrer. Ao contrário do módulo `lex`, o nome da função não é mais tão importante.

O parâmetro `prod` (um objeto do tipo `ply.yacc.YaccProduction`) funciona de forma semelhante à uma lista, sendo que o número de elementos depende da regra associada à função.

Mais de uma regra podem ser associadas à mesma função, ou mais de uma derivação da mesma regra, como no exemplo:


```python
def p_other_statement(prod):
    """
    other_expression : expression other_expression
        | empty
    """
    if prod[1]:
        statements = [prod[1]]
        if prod[2]:
            statements.extend(prod[2])
        prod[0] = statements
```

A definição de como tratar as regras, nesse caso, deve ser feita através do código, por isso, recomenda-se que apenas regras semelhates sejam agrupadas. Veja um exemplo de uma  regra com suas diferentes alternativas dividida em várias funções:

```python
def p_value_expr_add_mul(prod):  # noqa: D205, D400, D403, D415
    """
    value_expr : value_expr ADD_OP value_expr
        | value_expr MUL_OP value_expr
    """
    oper = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    prod[0] = oper[prod[2]](prod[1], prod[3])


def p_value_expr_par(prod):
    """value_expr : OPEN_PAR value_expr CLOSE_PAR"""
    prod[0] = prod[2]


def p_value_expr_num(prod):
    """value_expr : NUM"""
    prod[0] = prod[1]


def p_value_expr_id(prod):
    """value_expr : ID"""
    sym = get_symbol(prod[1])
    if sym is None:
        raise Exception(f"Undefined symbol: {prod[1]}: {prod.lineno(1)}")
    prod[0] = sym["value"]
```

Apesar do maior número de funções o código fica muito mais simples e fácil de entender e manter. A versão desse mesmo código utilizando uma única função teria que tratar, na função, todos os casos, e fica muito mais difícil de entender:

```python
def p_value_expr(prod):  # noqa: D205, D400, D403, D415
    """
    value_expr : value_expr ADD_OP value_expr
        | value_expr MUL_OP value_expr
        | OPEN_PAR value_expr CLOSE_PAR
        | NUM
        | ID
    """
    if len(prod) == 2:
        if isinstance(prod[1], str):
            sym = get_symbol(prod[1])
            if sym is None:
                raise Exception(f"Undefined symbol: {prod[1]}: {prod.lineno(1)}")
            prod[0] = sym["value"]
        else:
            prod[0] = prod[1]
    elif prod[1] == "(":
        prod[0] = prod[2]
    else:
        oper = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }
        prod[0] = oper[prod[2]](prod[1], prod[3])
```

No código acima, utilizamos uma regra ambígua para a definição das operações aritiméticas,

$$
E \rightarrow E + E | E - E | E * E | E / E
$$

e precisamos prover para o _parser_ a contfiguração referente à associatividade e à precedência dos operadores. No caso do PLY, essa configuração é feita pela variável global `precedence`:

```python
precedence = (
    ("left", "ADD_OP"),
    ("left", "MUL_OP"),
)
```

Com essa configuração, sendo que $ADD\\_OPP = [-+]$ e $MUL\\_OP = [/*]$, as regras serão avaliadas na ordem correta para as expressões aritméticas.

Em alguns casos, uma regra pode levar a uma derivação vazia ($\\epsilon$), e esse caso deve ser explicitamente tratado pelo código, por exemplo:


```python
def p_other_statement(prod):
    """
    other_expression : expression other_expression
        | empty
    """
    if prod[1]:
        statements = [prod[1]]
        if prod[2]:
            statements.extend(prod[2])
        prod[0] = statements
```

A derivação vazia deve ser uma regra explícita para o PLY, e como é uma regra, deve ter uma função associada:

```python
def p_empty(prod):  # noqa: D205, D400, D403, D415
    """empty :"""
    prod[0] = None
```

É possível tratar uma série de erros com o PLY, no entanto, o tratamento de erros da gramática está fora do escopo desse documento. Uma maneira simples mostrar ao usuário que existe um erro de sintaxe no programa fonte, é encerrar a execução da análise sintático no primeiro erro encontrado, e isso é feito definindo a função `p_error`, como no exemplo:

```python
def p_error(token):
    """Provide a simple error message."""
    if token:
        raise Exception(
            f"Unexpected token:{token.lineno}: {token.type}:'{token.value}'"
        )

    raise Exception("Syntax error at EOF.")
```

Um último ponto importante na construção do analisador sintático utilizando o PLY, é o uso de informações do _lexer_ na regra de derivação. Veja um exemplo:

```python
def p_assignment_expression(prod):  # noqa: D205, D400, D403, D415
    """assignment_expression : ID ASSIGN_OP value_expr"""
    add_symbol(prod[1], "VAR", prod.lineno(1), value=prod[3])
    prod[0] = f"{prod[1]} = {prod[3]}"
```

Na execução das ações dessa regra um símbolo é adicionado à tabela de símbolos, incluindo informações como a linha na qual o _token_ foi identificado. Essa informação está disponível no método `prod.lineno`, que recebe o número da produção e retorna a linha onde o token referente àquela produção foi identificado. 

Para executar o analisador sintático criado, devemos instanciar _lexer_, o _parser_, e executar o analisador sintático, que retornará a produçào `p[0]` da regra inicial da gramática.

```python
mylex = lexer()
parser = yacc.yacc(start="program")
program = parser.parse(SOURCE, lexer=mylex, tracking=False)
```

Na primeira execução do analisador léxico, serão criados dois arquivos, o arquivo `parsetab.py` com o código dos autômatos do parser LALR(1) gerado, e o arquivo `parser.out` que contêm as descrições dos estados gerados pelo analisador sintático.

O arquivo `parser.out` pode ser utilizado para depurar o analisador sintático, e verificar a gramática criada. Por exemplo, uma parte desse arquivo para o exemplo desenvolvido mostra a gramática implementada:

```
Grammar

Rule 0     S' -> program
Rule 1     program -> expression other_expression
Rule 2     other_expression -> expression other_expression
Rule 3     other_expression -> empty
Rule 4     expression -> value_expr
Rule 5     expression -> assignment_expression
Rule 6     assignment_expression -> ID ASSIGN_OP value_expr
Rule 7     value_expr -> value_expr ADD_OP value_expr
Rule 8     value_expr -> value_expr MUL_OP value_expr
Rule 9     value_expr -> OPEN_PAR value_expr CLOSE_PAR
Rule 10    value_expr -> NUM
Rule 11    value_expr -> ID
Rule 12    empty -> <empty>
```

Como esses arquivos são gerados na primeira execução, não há necessidade de armazená-los em repositórios de código, por exemplo.

O código completo do parser desenvolvido pode ser visto abaixo:

[](code/compiler/parser.py){:class="download fa fa-download"}
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

"""Implemente a simple arithmetic parser that generates a syntatic tree."""

import operator

from symtable import add_symbol, get_symbol

from ply import yacc

# 'tokens' is a global variable required by yacc.yacc().
from lexer import lexer, tokens  # pylint: disable=unused-import


precedence = (
    ("left", "ADD_OP"),
    ("left", "MUL_OP"),
)


def p_program(prod):  # noqa: D205, D400, D403, D415
    """program : expression other_expression"""
    statements = [prod[1]]
    if prod[2]:
        statements.extend(prod[2])
    prod[0] = statements
    print("\n".join(str(s) for s in statements))


def p_other_statement(prod):  # noqa: D205, D400, D403, D415
    """
    other_expression : expression other_expression
        | empty
    """
    if prod[1]:
        statements = [prod[1]]
        if prod[2]:
            statements.extend(prod[2])
        prod[0] = statements


def p_expression(prod):  # noqa: D205, D400, D403, D415
    """
    expression : value_expr
        | assignment_expression
    """
    prod[0] = prod[1]


def p_assignment_expression(prod):  # noqa: D205, D400, D403, D415
    """assignment_expression : ID ASSIGN_OP value_expr"""
    add_symbol(prod[1], "VAR", prod.lineno(1), value=prod[3])
    prod[0] = f"{prod[1]} = {prod[3]}"


def p_value_expr_add_mul(prod):  # noqa: D205, D400, D403, D415
    """
    value_expr : value_expr ADD_OP value_expr
        | value_expr MUL_OP value_expr
    """
    oper = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    prod[0] = oper[prod[2]](prod[1], prod[3])


def p_value_expr_par(prod):  # noqa: D205, D400, D403, D415
    """value_expr : OPEN_PAR value_expr CLOSE_PAR"""
    prod[0] = prod[2]


def p_value_expr_num(prod):  # noqa: D205, D400, D403, D415
    """value_expr : NUM"""
    prod[0] = prod[1]


def p_value_expr_id(prod):  # noqa: D205, D400, D403, D415
    """value_expr : ID"""
    sym = get_symbol(prod[1])
    if sym is None:
        raise Exception(f"Undefined symbol: {prod[1]}: {prod.lineno(1)}")
    prod[0] = sym["value"]


def p_empty(prod):  # noqa: D205, D400, D403, D415
    """empty :"""
    prod[0] = None


def p_error(token):
    """Provide a simple error message."""
    if token:
        raise Exception(
            f"Unexpected token:{token.lineno}: {token.type}:'{token.value}'"
        )

    raise Exception("Syntax error at EOF.")


if __name__ == "__main__":
    import sys

    # read source file
    with (
        open(sys.argv[1], "rt") if len(sys.argv) > 1 else sys.stdin
    ) as source_file:
        SOURCE = "\n".join(source_file.readlines())
    # parse source data
    mylex = lexer()
    parser = yacc.yacc(start="program")
    program = parser.parse(SOURCE, lexer=mylex, tracking=False)
```

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

[](code/compiler/symtable.py){:class="download fa fa-download"}
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