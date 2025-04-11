import lark
from lark import Transformer

grammar = r"""
?start: imprimir_op

imprimir_op: "imprimirResultado" "(" expression ")"

?expression: arithmetic
           | repetition
arithmetic: INT "+"      -> arithmetic

repetition: INT "*" CNAME  -> repetition

%import common.INT
%import common.CNAME
%import common.WS
%ignore WS
"""

class PrintTransformer(Transformer):
    def imprimir_op(self, items):
        resultado = items[0]
        print("OperacionImpresion=>", resultado)
        return resultado

    def arithmetic(self, items):
        num_str = items[0]
        return sum(int(ch) for ch in num_str)

    def repetition(self, items):
        count = int(items[0])
        word = str(items[1])
        return word * count

parser = lark.Lark(grammar, parser="lalr")
interpreter = lark.Lark(grammar, parser="lalr", transformer=PrintTransformer())

codigo1 = 'imprimirResultado(53+)'
print("###########################")
print("ÁRBOL SINTÁCTICO (ejemplo aritmético)")
print("###########################")
tree1 = parser.parse(codigo1)
print(tree1.pretty())
print("###########################")
print("RESULTADO (ejemplo aritmético)")
print("###########################")
interpreter.parse(codigo1)

print("\n---------------------------------\n")

codigo2 = 'imprimirResultado(2*casa)'
print("###########################")
print("ÁRBOL SINTÁCTICO (ejemplo repetición)")
print("###########################")
tree2 = parser.parse(codigo2)
print(tree2.pretty())
print("###########################")
print("RESULTADO (ejemplo repetición)")
print("###########################")
interpreter.parse(codigo2)