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

import yaml

from symtable import add_symbol, get_symbol

from ply import yacc

# 'tokens' is a global variable required by yacc.yacc().
from lexer import lexer, tokens  # pylint: disable=unused-import

from tree import new_leaf, new_node, append_node

precedence = (
    ("left", "ADD_OP"),
    ("left", "MUL_OP"),
)


def p_program(prod):  # noqa: D205, D400, D403, D415
    """program : expression other_expression"""
    node = new_node("program")
    append_node(node, prod[1])
    if prod[2]:
        append_node(node, prod[2])
    prod[0] = node


def p_other_statement(prod):  # noqa: D205, D400, D403, D415
    """
    other_expression : expression other_expression
        | empty
    """
    if prod[1]:
        node = new_node("other_expression")
        append_node(node, prod[1])
        if prod[2]:
            append_node(node, prod[2])
        prod[0] = node


def p_expression(prod):  # noqa: D205, D400, D403, D415
    """
    expression : value_expr
        | assignment_expression
    """
    node = new_node("expression")
    append_node(node, prod[1])
    prod[0] = node


def p_assignment_expression(prod):  # noqa: D205, D400, D403, D415
    """assignment_expression : ID ASSIGN_OP value_expr"""
    add_symbol(prod[1], "VAR", prod.lineno(1), value=prod[3])
    node = new_node("assignment_expression")
    append_node(node, new_leaf("ID", value=prod[1]))
    append_node(node, new_leaf(prod.slice[2].type, value=prod[2]))
    append_node(node, prod[3])
    prod[0] = node


def p_value_expr_add_mul(prod):  # noqa: D205, D400, D403, D415
    """
    value_expr : value_expr ADD_OP value_expr
        | value_expr MUL_OP value_expr
    """
    node = new_node("value_expr")
    append_node(node, prod[1])
    append_node(node, new_leaf(prod.slice[2].type, value=prod[2]))
    append_node(node, prod[3])
    prod[0] = node


def p_value_expr_par(prod):  # noqa: D205, D400, D403, D415
    """value_expr : OPEN_PAR value_expr CLOSE_PAR"""
    node = new_node("value_expr")
    append_node(node, new_leaf(prod.slice[1].type, value=prod[1]))
    append_node(node, prod[2])
    append_node(node, new_leaf(prod.slice[3].type, value=prod[3]))
    prod[0] = node


def p_value_expr_num(prod):  # noqa: D205, D400, D403, D415
    """value_expr : NUM"""
    node = new_node("value_expr")
    leaf = new_leaf("NUM", value=prod[1])
    append_node(node, leaf)
    prod[0] = node


def p_value_expr_id(prod):  # noqa: D205, D400, D403, D415
    """value_expr : ID"""
    sym = get_symbol(prod[1])
    if sym is None:
        raise Exception(f"Undefined symbol: {prod[1]}: {prod.lineno(1)}")
    node = new_node("value_expr")
    leaf = new_leaf("ID", value=prod[1])
    append_node(node, leaf)
    prod[0] = node


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
    print(yaml.dump(program, indent=2, sort_keys=False))
