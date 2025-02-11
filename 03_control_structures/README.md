# Estructuras de Control en Python (Sección 03)

Esta sección cubre los mecanismos de control de flujo en Python, incluyendo condicionales y bucles.

## Estructura del Directorio 

## Descripción del Código

- **loops.py**: Demuestra varios constructos de bucles en Python.
- **loop_control.py**: Muestra cómo controlar la ejecución de bucles con declaraciones como `break` y `continue`.
- **conditionals.py**: Ilustra la toma de decisiones en Python utilizando declaraciones condicionales.

## Contenido de Esta Sección

Esta sección proporciona ejemplos prácticos y explicaciones sobre las estructuras de control en Python, enfocándose en cómo gestionar el flujo de ejecución en tus programas mediante bucles y condicionales.

## Objetivos de Aprendizaje
- Comprender los diferentes tipos de bucles en Python y cuándo utilizarlos.
- Aprender a controlar la ejecución de bucles con declaraciones como `break`, `continue` y `pass`.
- Adquirir destreza en el uso de declaraciones condicionales para tomar decisiones en el código.

## Descripción Detallada del Código

### conditionals.py
Este archivo muestra cómo utilizar **estructuras condicionales en Python**, como `if`, `elif` y `else`, para tomar decisiones en función de diferentes condiciones.

**Ejemplos de código:**
```python
age = 18
if age >= 18:
    print("You are an adult")
```
```python
temperature = 25
if temperature > 30:
    print("It's hot!")
else:
    print("It's not too hot")
```

### loop_control.py
Este archivo ilustra cómo controlar la ejecución de **bucles en Python** utilizando declaraciones como `break`, `continue` y `pass`.

**Ejemplos de código:**
```python
for i in range(1, 6):
    if i == 4:
        break
    print(i)
```
```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

### loops.py
Este archivo presenta diferentes tipos de **bucles en Python**, como `for` y `while`, para repetir acciones.

**Ejemplos de código:**
```python
for i in range(5):
    print(i)
```
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

## Cómo Ejecutar los Programas

1. Asegúrate de tener Python instalado en tu máquina.
2. Abre una terminal o consola de comandos.
3. Navega al directorio que contiene los archivos.
4. Ejecuta el programa deseado utilizando el comando:
   ```bash
   python <nombre_archivo>.py
   ```
   Reemplaza `<nombre_archivo>` con `loops`, `loop_control` o `conditionals` según sea necesario.

