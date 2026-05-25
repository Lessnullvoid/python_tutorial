# Sintaxis Basica de Python (Seccion 02)

Esta seccion cubre la sintaxis fundamental de Python y conceptos basicos de programacion.

## Descripcion del Codigo

- [`variables.py`](../02_basic_syntax/variables.py): Demuestra la declaracion, asignacion y uso de variables en Python.
- [`operators.py`](../02_basic_syntax/operators.py): Ilustra el uso de operadores aritmeticos, de comparacion y logicos con ejemplos.
- [`comments.py`](../02_basic_syntax/comments.py): Muestra como escribir comentarios de una sola linea y de multiples lineas en Python.
- [`input_output.py`](../02_basic_syntax/input_output.py): Proporciona ejemplos de como usar `input()` para entrada de usuario y `print()` para mostrar resultados.

## Objetivos de Aprendizaje

Al final de esta seccion, deberas ser capaz de:
1. Declarar y usar variables en Python.
2. Comprender y aplicar diferentes tipos de operadores.
3. Escribir comentarios efectivos en tu codigo.
4. Manejar la entrada y salida de datos en programas de Python.

## Descripcion Detallada del Codigo

### variables.py
Este archivo introduce el uso de **variables y tipos de datos en Python**. Incluye ejemplos sobre como declarar y asignar variables, asi como verificar sus tipos.

**Ejemplos de codigo:**
```python
name = "John Doe"  # Cadena de texto
age = 25           # Numero entero
height = 1.75      # Numero flotante
is_student = True  # Valor booleano
```

### operators.py
Este archivo muestra como utilizar **operadores en Python**, incluyendo operadores aritmeticos, de comparacion, logicos y de asignacion.

**Ejemplos de codigo:**
```python
a = 10
b = 3
print(a + b, a - b, a * b, a / b, a % b)
```

### comments.py
Este archivo explica como escribir **comentarios en Python** para documentar y organizar el codigo.

**Ejemplos de codigo:**
```python
# Este es un comentario de una linea
"""
Este es un comentario de multiples lineas
que sirve como documentacion.
"""
```

### input_output.py
Este archivo ilustra como manejar **entrada y salida en Python** utilizando `input()` para leer datos del usuario y `print()` para mostrar resultados.

**Ejemplos de codigo:**
```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello, {name}! Next year, you will be {age + 1}.")
```

## Como Ejecutar los Programas

1. Asegurate de tener Python instalado en tu maquina.
2. Abre una terminal o consola de comandos.
3. Navega al directorio del proyecto.
4. Ejecuta un programa con el comando: `python 02_basic_syntax/nombre_archivo.py`, reemplazando `nombre_archivo.py` con el nombre del archivo que deseas ejecutar (por ejemplo, `python 02_basic_syntax/variables.py`).
