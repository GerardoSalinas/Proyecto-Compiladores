from flask import Flask, render_template, request, jsonify

import lark

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.grammar import grammar, grammarEx
from src.LanguageTransformer import LanguageTransformer

app = Flask(__name__)

parser = lark.Lark(grammarEx)

interpreter = lark.Lark(grammar, parser="lalr", transformer=LanguageTransformer())

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/procesar", methods=["POST"])
def procesar():
    expression = request.form.get("expression", "")
    
    if not expression:
        return jsonify({"error": "No se proporcionó expresión"}), 400

    try:
        tree = parser.parse(expression)
        tree_pretty = tree.pretty()

        resultado = interpreter.parse(expression)

        return jsonify({
            "tree": tree_pretty,
            "resultado": resultado
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
