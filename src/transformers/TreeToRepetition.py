import lark
from lark import Transformer

class TreeToRepetition(Transformer):
    def repetition(self,n):
        newString = ""
        limit = int(n[0])
        for i in range(limit):
            newString = newString + n[1]
        return newString