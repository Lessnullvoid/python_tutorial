# Funciones en Python (Seccion 05)

Esta seccion explora la definicion de funciones, argumentos y conceptos avanzados de funciones.

## Descripcion del Codigo

- [`basic_functions.py`](../05_functions/basic_functions.py): Introduce la sintaxis para definir funciones basicas.
- [`arguments_returns.py`](../05_functions/arguments_returns.py): Muestra el uso de argumentos posicionales, por palabra clave y valores de retorno multiples.
- [`lambda_functions.py`](../05_functions/lambda_functions.py): Proporciona ejemplos de funciones lambda y su uso practico.
- [`scope_examples.py`](../05_functions/scope_examples.py): Explica el ambito de las variables en Python, incluyendo `global` y `nonlocal`.

## Objetivos de Aprendizaje
1. Definir y llamar funciones en Python.
2. Comprender y utilizar diferentes tipos de argumentos de funcion.
3. Retornar valores de funciones de manera efectiva.
4. Crear y usar funciones lambda.
5. Comprender el ambito de las variables locales y globales.

## Descripcion Detallada del Codigo

### basic_functions.py
Este archivo introduce la definicion y uso de **funciones basicas en Python**.

**Ejemplos de codigo:**
```python
def greet():
    print("Hello, World!")

def add_numbers(a, b):
    return a + b
```

### arguments_returns.py
Este archivo muestra como trabajar con **diferentes tipos de argumentos y valores de retorno en funciones**.

**Ejemplos de codigo:**
```python
def print_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

def sum_all(*args):
    return sum(args)
```

### lambda_functions.py
Este archivo introduce **funciones lambda (funciones anonimas)** y como se utilizan en combinacion con `map()`, `filter()` y `sorted()`.

**Ejemplos de codigo:**
```python
square = lambda x: x**2
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
```

### scope_examples.py
Este archivo explica el concepto de **ambito de variables en Python**.

**Ejemplos de codigo:**
```python
global_var = "I am global"
def demonstrate_scope():
    local_var = "I am local"
    print(local_var)
    print(global_var)
```
```python
def outer_function():
    outer_var = "Outer"
    def inner_function():
        nonlocal outer_var
        outer_var = "Modified"
```

## Como Ejecutar los Programas

1. Asegurate de tener Python instalado en tu maquina.
2. Navega al directorio del proyecto.
3. Utiliza la linea de comandos para ejecutar un programa especifico. Por ejemplo:
   ```bash
   python 05_functions/basic_functions.py
   ```
