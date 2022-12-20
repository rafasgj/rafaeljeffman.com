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
        SOURCE = source_file.read()
    # parse source data
    mylex = lexer()
    parser = yacc.yacc(start="program")
    program = parser.parse(SOURCE, lexer=mylex, tracking=False)
