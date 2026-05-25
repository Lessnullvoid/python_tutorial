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

## Conceptos

### Que es una funcion?

Una funcion es un bloque de codigo reutilizable que realiza una tarea especifica. En lugar de escribir el mismo codigo una y otra vez, lo defines una vez en una funcion y la llamas cada vez que la necesites.

Piensa en ella como una receta con nombre: "hacer_cafe()" -- cada vez que la llamas, se ejecutan los mismos pasos.

```python
def greet(name):
    return f"Hello, {name}!"
```

Las funciones te ayudan a organizar el codigo, evitar la repeticion y hacer que los programas sean mas faciles de entender y depurar.

### Que son los parametros y argumentos?

- **Parametros** son los nombres de variable en la definicion de la funcion (marcadores de posicion).
- **Argumentos** son los valores reales que pasas al llamar a la funcion.

```python
def add(a, b):       # a y b son parametros
    return a + b

add(3, 5)            # 3 y 5 son argumentos
```

Python soporta varios tipos de argumentos:
- **Posicionales**: se emparejan por orden
- **Por palabra clave**: se emparejan por nombre (`add(a=3, b=5)`)
- **Por defecto**: tienen un valor predeterminado (`def greet(name="World")`)
- **Longitud variable**: `*args` (cualquier numero de posicionales) y `**kwargs` (cualquier numero de palabra clave)

### Que es un valor de retorno?

Una funcion puede enviar un resultado de vuelta al llamador usando `return`. Sin el, la funcion devuelve `None` por defecto.

```python
def square(x):
    return x ** 2

result = square(4)  # result es 16
```

Una funcion puede devolver multiples valores como una tupla: `return a, b, c`

### Que es una funcion lambda?

Una lambda es una funcion anonima pequena escrita en una sola linea. Es util para operaciones cortas que no necesitas nombrar.

```python
square = lambda x: x ** 2
```

Las lambdas se usan comunmente con `map()`, `filter()` y `sorted()` para transformaciones rapidas.

### Que es el ambito de variables?

El ambito determina donde es accesible una variable en tu codigo:

- **Ambito local**: variables creadas dentro de una funcion existen solo dentro de esa funcion.
- **Ambito global**: variables creadas fuera de todas las funciones son accesibles en todas partes.
- **Palabra clave `global`**: te permite modificar una variable global desde dentro de una funcion.
- **Palabra clave `nonlocal`**: permite que una funcion interna modifique una variable de su funcion envolvente.

```python
x = 10          # global

def example():
    y = 5       # local -- solo existe dentro de example()
    print(x)    # puede LEER la x global
```

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
