# Funciones en Python (Sección 05)

Esta sección explora la definición de funciones, argumentos y conceptos avanzados de funciones.

## Descripción del Código

- **basic_functions.py**: Introduce la sintaxis para definir funciones básicas.
- **arguments_returns.py**: Muestra el uso de argumentos posicionales, por palabra clave y valores de retorno múltiples.
- **lambda_functions.py**: Proporciona ejemplos de funciones lambda y su uso práctico.
- **scope_examples.py**: Explica el ámbito de las variables en Python, incluyendo `global` y `nonlocal`.

## Contenido de Esta Sección

Esta sección contiene ejercicios que te guiarán a través de los conceptos fundamentales de las funciones en Python, desde su definición hasta temas avanzados como funciones lambda y ámbito de variables.

## Objetivos de Aprendizaje
1. Definir y llamar funciones en Python.
2. Comprender y utilizar diferentes tipos de argumentos de función.
3. Retornar valores de funciones de manera efectiva.
4. Crear y usar funciones lambda.
5. Comprender el ámbito de las variables locales y globales.

## Descripción Detallada del Código

### basic_functions.py
Este archivo introduce la definición y uso de **funciones básicas en Python**.

**Ejemplos de código:**
```python
def greet():
    print("Hello, World!")

def add_numbers(a, b):
    return a + b
```

### arguments_returns.py
Este archivo muestra cómo trabajar con **diferentes tipos de argumentos y valores de retorno en funciones**.

**Ejemplos de código:**
```python
def print_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

def sum_all(*args):
    return sum(args)
```

### lambda_functions.py
Este archivo introduce **funciones lambda (funciones anónimas)** y cómo se utilizan en combinación con `map()`, `filter()` y `sorted()`.

**Ejemplos de código:**
```python
square = lambda x: x**2
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
```

### scope_examples.py
Este archivo explica el concepto de **ámbito de variables en Python**.

**Ejemplos de código:**
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

## Cómo Ejecutar los Programas

1. Asegúrate de tener Python instalado en tu máquina.
2. Navega al directorio que contiene los archivos de código.
3. Utiliza la línea de comandos para ejecutar un programa específico. Por ejemplo:
   ```bash
   python basic_functions.py
   ```
4. Sigue las instrucciones proporcionadas en cada archivo de código para más detalles sobre su uso.

