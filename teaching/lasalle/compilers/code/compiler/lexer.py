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
t_ignore = " \t\r"  # pylint: disable=invalid-name

# pylint: disable=invalid-name
t_ADD_OP = "[-+]"
t_MUL_OP = "[/*]"
t_ASSIGN_OP = "="
t_OPEN_PAR = "[(]"
t_CLOSE_PAR = "[)]"
t_ID = r"[_a-zA-Z][_a-zA-Z0-9]*"
# pylint: enable=invalid-name


@lex.TOKEN(r"[+-]?\d+([.]\d*)?")
def t_NUM(token):  # pylint: disable=invalid-name
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
