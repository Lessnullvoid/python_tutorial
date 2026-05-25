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
