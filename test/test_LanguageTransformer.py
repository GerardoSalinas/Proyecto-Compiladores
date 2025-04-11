from src.grammar import grammar
import lark
from src.LanguageTransformer import LanguageTransformer

parser = lark.Lark(grammar)
interpreter = lark.Lark(grammar, parser="lalr", transformer=LanguageTransformer())

def test1():
    tree = parser.parse("3+2")
    assert LanguageTransformer().transform(tree) == 5

def test2():
    assert interpreter.parse("3+2") == 5

def test3():
    assert interpreter.parse("10 - 5") == 5

def test4():
    assert interpreter.parse("10/2") == 5

def test5():
    assert interpreter.parse("22*11") == 242

def test6():
    assert interpreter.parse("22**2") == 484 

def test7():
    assert interpreter.parse("3*hola") == "holaholahola"

def test8():
    assert interpreter.parse("imprimirResultado(10 5 +)") == 15

def test9():
    assert interpreter.parse("concat(\"expression1\",\"expression2\")") == "expression1expression2"

def test10():
    assert interpreter.parse("imprimirResultado(22/0)") == "Error al divir por 0"