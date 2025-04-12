# Importamos Flask y las herramientas necesarias para manejar solicitudes web
from flask import Flask, render_template, request, jsonify

# Importamos lark para el análisis sintáctico
import lark

# Estas dos líneas permiten que Python encuentre el módulo 'src' aunque estemos en otra carpeta
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ahora que ya configuramos la ruta, podemos importar nuestra gramática y el transformer
from src.grammar import grammar, grammarEx
from src.LanguageTransformer import LanguageTransformer

# Creamos una instancia de Flask, que será nuestro servidor web
app = Flask(__name__)

# Este parser es solo para generar y mostrar el árbol sintáctico de una expresión
parser = lark.Lark(grammarEx)

# Este otro parser es el que realmente interpreta la expresión, aplicando nuestro transformer
interpreter = lark.Lark(grammar, parser="lalr", transformer=LanguageTransformer())

# Esta ruta carga la página principal con el formulario
@app.route("/")
def index():
    return render_template("index.html")

# Esta ruta recibe la expresión desde el formulario y la procesa
@app.route("/procesar", methods=["POST"])
def procesar():
    # Obtenemos la expresión enviada desde el frontend
    expression = request.form.get("expression", "")
    
    # Si el campo está vacío, devolvemos un error
    if not expression:
        return jsonify({"error": "No se proporcionó expresión"}), 400

    try:
        # Parseamos la expresión para generar el árbol sintáctico en texto
        tree = parser.parse(expression)
        tree_pretty = tree.pretty()

        # Interpretamos la expresión con el transformer, obteniendo el resultado
        resultado = interpreter.parse(expression)

        # Devolvemos todo al frontend como JSON
        return jsonify({
            "tree": tree_pretty,
            "resultado": resultado
        })
    except Exception as e:
        # Si algo falla lo enviamos al frontend
        return jsonify({"error": str(e)}), 500

# Esto hace que la app se ejecute si se corre directamente este archivo
if __name__ == "__main__":
    app.run(debug=True)  # El modo debug nos da errores detallados en desarrollo

# Ejecutalo con: python web_app/app.py y luego http://127.0.0.1:5000 en el buscador.