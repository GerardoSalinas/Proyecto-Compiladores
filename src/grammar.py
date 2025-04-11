expression_grammar = """
?start: expression
?expression: arith | imprimir_op | postfix_arith
?imprimir_op: "imprimirResultado" "(" expression ")"
?arith:   term   | term "+" arith  -> add | term "-" arith      -> sub
?term:    factor | factor "*" term -> mul | factor "/" term     -> div | factor "%" term -> mod
?factor:  pow    | "+" factor      -> pos | "-" factor          -> neg
?pow: call | atom "**" factor -> pow
?postfix_arith: INT INT OPERATOR -> arithmetic_postfix
?call:    atom   | call trailer
?atom:    "(" expression ")" | CNAME -> symbol | INT -> integer | FLOAT -> float | ESCAPED_STRING -> literal
?trailer: "(" arglist ")"
?arglist: [expression ("," expression)*]

OPERATOR: "+" | "-" | "*" | "/" | "%"

%import common.CNAME
%import common.NUMBER
%import common.ESCAPED_STRING
%import common.INT
%import common.FLOAT
%import common.WORD
%import common.WS
"""

grammar = "\n".join(["%ignore WS"]) + expression_grammar
# ?pow:     call "**"