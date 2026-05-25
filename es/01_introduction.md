# Introduccion a la Programacion en Python

Esta seccion cubre los conceptos basicos de la programacion en Python.

## Contenido
1. Programa "Hello World"
2. Declaraciones basicas de `print`
3. Formateo simple de cadenas

## Objetivos de Aprendizaje
- Escribir tu primer programa en Python
- Comprender las declaraciones basicas de `print`
- Aprender a mostrar cadenas de texto con formato basico

## Conceptos

### Que es Python?

Python es un lenguaje de programacion de alto nivel disenado para ser facil de leer y escribir. Es uno de los lenguajes mas populares del mundo, utilizado en desarrollo web, ciencia de datos, inteligencia artificial, automatizacion y mucho mas. Su sintaxis simple lo convierte en una excelente opcion para principiantes.

### Que es un programa?

Un programa es un conjunto de instrucciones que le dice a la computadora que hacer, paso a paso. Cuando escribes un programa en Python, estas escribiendo esas instrucciones en un lenguaje que la computadora puede entender (despues de que Python las traduce).

Piensa en ello como una receta de cocina: cada linea es un paso, y la computadora los sigue en orden de arriba hacia abajo.

### Que es `print()`?

`print()` es una funcion integrada que muestra informacion en la pantalla (la terminal/consola). Es la forma mas basica de ver el resultado de tu programa.

Sintaxis:

```python
print("texto que quieres mostrar")
print(42)       # tambien puedes imprimir numeros
print(True)     # o valores booleanos
```

### Que son los f-strings?

Un f-string (cadena formateada) te permite insertar variables directamente dentro de una cadena de texto. Se coloca el prefijo `f` antes de la cadena y los nombres de variables dentro de llaves `{}`.

Sintaxis:

```python
name = "Alice"
print(f"Hello, {name}!")  # Salida: Hello, Alice!
```

Esto evita la concatenacion complicada de cadenas y hace que tu salida sea mas legible.

## Como Ejecutar el Programa
1. Abre tu terminal.
2. Navega al directorio del proyecto.
3. Ejecuta el comando: `python 01_introduction/hello_world.py`

## Descripcion del Codigo

**Archivo:** [`hello_world.py`](../01_introduction/hello_world.py)

Este archivo contiene ejemplos basicos para introducir la sintaxis y las funcionalidades mas elementales de Python. A continuacion, se explica cada parte del codigo:

1. **Primer programa en Python: "Hello, World!"**
   ```python
   print("Hello, World!")
   ```
   Este es el clasico primer programa en cualquier lenguaje de programacion. La funcion `print()` se utiliza para mostrar texto en la consola.

2. **Multiples declaraciones `print`**
   ```python
   print("Welcome to Python Programming!")
   print("This is your first step in learning Python.")
   ```
   Aqui se utilizan varias llamadas a `print()` para mostrar multiples mensajes uno tras otro.

3. **Impresion de diferentes tipos de datos**
   ```python
   print(42)    # Imprime un numero entero
   print(3.14)  # Imprime un numero flotante
   print(True)  # Imprime un valor booleano
   ```
   Python permite imprimir distintos tipos de datos directamente usando la funcion `print()`.

4. **Formato basico de cadenas (String Formatting)**
   ```python
   name = "Learner"
   print(f"Hello, {name}!")
   ```
   Aqui se demuestra el uso de la interpolacion de cadenas (`f-strings`), que permite insertar variables dentro de cadenas de texto.
