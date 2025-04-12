# Proyecto-Compiladores

## Dependencias

1. Python 3.10 o superior
2. Pytest

Para instalar pytest:

```python
pip install -U pytest
```

## Enunciado del Problema

Tener la entrada de caracteres que representen un lenguaje definido por ustedes donde se tengan las siguientes operaciones (al menos estas 4, pero ustedes pueden agregar más operaciones):

- Operaciones de Suma y Resta.
- Operaciones de Concatenación.
- Operaciones de Repetición.
- Operaciones de impresión

Ejemplos:

```markdown
                    Cadenas-operación-salida
    52+ => OperacionSuma=>7
    3*Palabra=>OperacionRepeticion=>PalabraPalabraPalabra
    imprimirResultado(53+)=>OperacionImpresion=>8
    imprimirResultado(2*casa)=>OperacionImpresion=>casacasa
    A=Soy B=feliz C=con esta clase =>OperacionConcatenacion=>ABC=>Soy feliz con esta clase
```

Recuerde que esto es un ejemplo de una línea del txt, el grupo tiene la libertar de trabajar con diferentes nombres y formas de identificar los elementos. La propuesta debe ser de como aplicación de escritorio o entorno web.

## Ejecución

El script puede leer entradas de una archivo txt usando la bandera **-f** junto con la ruta del archivo que se quiere leer. Muestra "Error: el archivo en la ruta *ruta_de_archivo* no existe" si el archivo indicado no existe.

```bash
python3 main.py -f "./../samples/example.txt"
```

También se puede ejecutar simulando entradas del usuario (una a la vez) usando la bandera **-c**. Debe ver como cambia el prompt inmediatamente a *PHPascal>*

```bash
python3 main.py -c
```

También se puede ejecutar con un entorno web con el siguiente comando:

```bash
python3 web_app/app.py
```

## Tests

Para ejecutar los tests, navegar al directorio test/ y ejecutar el comando

```bash
pytest test_LanguageTransformer.py
```

## Proceso de Creación de lenguaje

1. Declarar ejemplos de cadenas correctas e incorrectas para cada funcionalidad del nuevo lenguaje

2. Definir la gramatica

3. Crear el parser

4. Generar el arbol

5. Evaluar el arbol

6. Optimizar

## Descripcion rapida

Lark es un parser, nos permite darle cadenas como entrada y produce el arbol sintactico para dicha entrada basandose en una gramatica previamente definida. Primero se deben generar ejemplos de cadenas que queremos que nuestro lenguaje acepte, luego debemos definir la gramtica para nuestro lenguaje. Seguidamente podemos pasarle nuestra gramatica a lark (aclarando que regla debe comenzar a leer primero) para que este pueda generar un parser. 
El siguiente paso es usar el parser para crear el arbol sintactico para una entrada en especifico

```python
text1 = '$xyz:=17'
result1 = assignment_parser.parse(text1)
```

Y para simular la ejecucion del codigo de nuestro nuevo lenguaje, Lark utiliza transformers, los transformers son metodos que tienen el mismo nombre de los no terminales de nuestro lenguaje. De modo que lark puede recorrer el arbol, y por cada no terminal ejecutar el metodo que corresponda.