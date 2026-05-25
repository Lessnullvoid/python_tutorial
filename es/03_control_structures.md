# Estructuras de Control en Python (Seccion 03)

Esta seccion cubre los mecanismos de control de flujo en Python, incluyendo condicionales y bucles.

## Descripcion del Codigo

- [`conditionals.py`](../03_control_structures/conditionals.py): Ilustra la toma de decisiones en Python utilizando declaraciones condicionales.
- [`loops.py`](../03_control_structures/loops.py): Demuestra varios constructos de bucles en Python.
- [`loop_control.py`](../03_control_structures/loop_control.py): Muestra como controlar la ejecucion de bucles con declaraciones como `break` y `continue`.

## Objetivos de Aprendizaje
- Comprender los diferentes tipos de bucles en Python y cuando utilizarlos.
- Aprender a controlar la ejecucion de bucles con declaraciones como `break`, `continue` y `pass`.
- Adquirir destreza en el uso de declaraciones condicionales para tomar decisiones en el codigo.

## Descripcion Detallada del Codigo

### conditionals.py
Este archivo muestra como utilizar **estructuras condicionales en Python**, como `if`, `elif` y `else`, para tomar decisiones en funcion de diferentes condiciones.

**Ejemplos de codigo:**
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

### loops.py
Este archivo presenta diferentes tipos de **bucles en Python**, como `for` y `while`, para repetir acciones.

**Ejemplos de codigo:**
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

### loop_control.py
Este archivo ilustra como controlar la ejecucion de **bucles en Python** utilizando declaraciones como `break`, `continue` y `pass`.

**Ejemplos de codigo:**
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

## Como Ejecutar los Programas

1. Asegurate de tener Python instalado en tu maquina.
2. Abre una terminal o consola de comandos.
3. Navega al directorio del proyecto.
4. Ejecuta el programa deseado utilizando el comando:
   ```bash
   python 03_control_structures/<nombre_archivo>.py
   ```
   Reemplaza `<nombre_archivo>` con `loops`, `loop_control` o `conditionals` segun sea necesario.
