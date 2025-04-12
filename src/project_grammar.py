import lark
from lark import Transformer

expression_grammar = """
?start: expression
?expression: arith
?arith:   term   | term "+" arith  -> add | term "-" arith      -> sub
?term:    factor | factor "*" term -> mul | factor "/" term     -> div | factor "%" term -> mod
?factor:  pow    | "+" factor      -> pos | "-" factor          -> neg
?pow:     call ["**" factor]
?call:    atom   | call trailer
?atom:    "(" expression ")" | CNAME -> symbol | INT -> integer | FLOAT -> float |  ESCAPED_STRING -> literal
?trailer: "(" arglist ")"
?arglist: expression ("," expression)*

%import common.CNAME
%import common.NUMBER
%import common.ESCAPED_STRING
%import common.INT
%import common.FLOAT
%import common.WORD
%import common.INT
%import common.WS
"""

class LanguageTransformer(Transformer):
    def integer(self, node):
        # Números enteros
        return int(node[0])
    
    def float(self, node):
        # Números flotantes
        return float(node[0])
    
    
    def symbol(self, node):
        # Variables
        return str(node[0])
    
    def literal(self, node):
        # Cadenas
        return str(node[0].replace("\"", ""))
    
    def neg(self, node):
        # Números negativos
        return -node[0]
    
    def add(self, node):
        result = node[0] + node[1]
        try:
            float(result)
            return result
        except ValueError:
            result = result.replace("\"", "")
            return f"\"{result}\""
    
    def sub(self, node):
        return node[0] - node[1]
    
    def mul(self, node):
        return node[0] * node[1]
    
    def div(self, node):
        return node[0] / node[1]
    
    def mod(self, node):
        return node[0] % node[1]

grammar = "\n".join(["%ignore WS"]) + expression_grammar

parser = lark.Lark(grammar)
interpreter = lark.Lark(grammar, parser="lalr", transformer=LanguageTransformer())

print("###########################")
print("ARBOL SINTÁCTICO")
print("###########################")
print(parser.parse('5.3 % 3.3').pretty())

print("###########################")
print("RESULTADO")
print("###########################")
print(interpreter.parse('5.3 % 3.3'))