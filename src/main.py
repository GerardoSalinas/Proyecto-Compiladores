import sys
from grammar import grammar
import lark
from transformers.TreeToRepetition import TreeToRepetition

if __name__ == "__main__":
    """ filePath = sys.argv[1]
    file = open(filePath, "r")
    for line in file:
        print(line) """
    
    repetitionParser = lark.Lark(grammar,start='repetition')
    while True: 
        userInput = input("PHPascal> ")
        
        repetitionTree = repetitionParser.parse(userInput)
        print(TreeToRepetition().transform(repetitionTree))

