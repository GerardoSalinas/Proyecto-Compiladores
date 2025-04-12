import sys
import lark
from grammar import grammar
from grammar import grammarEx
from LanguageTransformer import LanguageTransformer

if __name__ == "__main__":
    parser = lark.Lark(grammarEx)
    interpreter = lark.Lark(grammar, parser="lalr", transformer=LanguageTransformer())
    def processInput(str):
        print("\n###########################")
        print("     ARBOL SINTÁCTICO      ")
        print("###########################")
        print(parser.parse(str).pretty())
        print("\n")
        print("###########################")
        print("         RESULTADO         ")
        print("###########################")
        print(interpreter.parse(str))
        print("\n")
    flag = sys.argv[1]
    if (flag == "-f"):
        filePath = sys.argv[2]
        try:
            file = open(filePath, "r")
            for line in file:
                processInput(line)
            file.close()
        except FileNotFoundError:
            print(f"Error: el archivo en la ruta {filePath} no existe")
    elif (flag == "-c"):
        while True: 
            userInput = input("PHPascal> ")
            processInput(userInput)
    

