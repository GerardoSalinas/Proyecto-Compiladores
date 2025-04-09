from src.grammar import grammar
import lark
from src.transformers.TreeToRepetition import TreeToRepetition

repetitionParser = lark.Lark(grammar ,start='repetition')

def test_repetition1():
    repetitionTree = repetitionParser.parse("3*hola")
    assert TreeToRepetition().transform(repetitionTree) == "holaholahola"

    repetitionTree = repetitionParser.parse("1*hola")
    assert TreeToRepetition().transform(repetitionTree) == "hola"

    repetitionTree = repetitionParser.parse("0*hola")
    assert TreeToRepetition().transform(repetitionTree) == ""

""" def test_repetition2():
    repetitionTree = repetitionParser.parse("*hola")
    assert TreeToRepetition().transform(repetitionTree) == "La cadena de entrada no concuerda con la operacion repetición" """