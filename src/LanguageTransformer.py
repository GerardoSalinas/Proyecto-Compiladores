from lark import Transformer

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
        return -node[0].children[0]
    
    def pow(self,node):
        return node[0]**node[1]
    
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
        try:
            result = node[0] / node[1]
            return result 
        except ZeroDivisionError:
            return "Error al divir por 0"
    
    def mod(self, node):
        return node[0] % node[1]
    
    def imprimir_op(self, items):
        if isinstance(items, list):
            resultado = items[0]
        else:
            resultado = items
        print("OperacionImpresion=>", resultado)
        return resultado
    
    def call(self,items):
        newString= ""
        for element in items[1].children:
            newString = newString + element 
        return newString
    
    def repetition(self,n):
        try:
            word = n[0]
            count = int(n[1])
            return count * word
        except:
            raise Exception("Error al repetir cadena")
    
    def arithmetic_postfix(self, items):
        a = int(items[0])
        b = int(items[1])
        op = str(items[2])
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            return a / b
        elif op == "%":
            return a % b
        else:
            raise ValueError(f"Operador no válido: {op}")