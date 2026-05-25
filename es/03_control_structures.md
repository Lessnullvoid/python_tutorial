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

## Conceptos

### Que es el control de flujo?

Por defecto, Python ejecuta tu codigo linea por linea de arriba hacia abajo. El control de flujo te permite cambiar esto: puedes saltar lineas, repetir lineas o elegir entre diferentes caminos. Los condicionales y los bucles son las dos herramientas principales para el control de flujo.

### Que es un condicional?

Un condicional permite que tu programa tome decisiones. En lugar de ejecutar cada linea, el programa verifica una condicion y elige que camino seguir.

Piensa en ello como una bifurcacion en el camino: "Si esta lloviendo, lleva un paraguas. De lo contrario, usa lentes de sol."

En Python, escribes condicionales con `if`, `elif` y `else`:

```python
if condicion:
    # se ejecuta solo cuando condicion es True
elif otra_condicion:
    # se ejecuta si la primera fue False pero esta es True
else:
    # se ejecuta cuando ninguna de las anteriores fue True
```

El bloque indentado debajo de cada palabra clave es lo que se ejecuta para esa rama. Solo UNA rama se ejecuta.

### Que es un bucle?

Un bucle repite un bloque de codigo multiples veces. En lugar de escribir la misma instruccion 100 veces, la escribes una vez dentro de un bucle.

Python tiene dos tipos de bucles:

- **bucle for** -- se repite una vez por cada elemento en una secuencia (una lista, un rango de numeros, etc.)
- **bucle while** -- se repite mientras una condicion siga siendo True

```python
for elemento in secuencia:
    # hacer algo con elemento

while condicion:
    # hacer algo hasta que condicion sea False
```

Un bucle `for` es mejor cuando sabes cuantas veces repetir. Un bucle `while` es mejor cuando repites hasta que algo cambie.

### Que es el control de bucles?

A veces necesitas alterar el comportamiento de un bucle durante su ejecucion:

- `break` -- detiene el bucle por completo y continua con el codigo despues de el
- `continue` -- salta el resto de la iteracion actual y pasa a la siguiente
- `pass` -- no hace nada (un marcador de posicion cuando la sintaxis requiere un cuerpo pero aun no tienes nada que hacer)

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
