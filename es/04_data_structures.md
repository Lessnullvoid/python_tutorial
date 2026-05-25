# Estructuras de Datos en Python (Seccion 04)

Esta seccion cubre las estructuras de datos incorporadas en Python y sus operaciones.

## Descripcion del Codigo

- [`lists_example.py`](../04_data_structures/lists_example.py): Muestra como crear, acceder y manipular listas en Python.
- [`tuples_example.py`](../04_data_structures/tuples_example.py): Explica como usar tuplas, destacando su inmutabilidad y casos practicos.
- [`dictionaries_example.py`](../04_data_structures/dictionaries_example.py): Presenta el uso de diccionarios, incluyendo acceso seguro y metodos comunes.
- [`sets_example.py`](../04_data_structures/sets_example.py): Demuestra como trabajar con conjuntos y realizar operaciones como union e interseccion.
- [`list_comprehension.py`](../04_data_structures/list_comprehension.py): Contiene ejemplos avanzados de comprension de listas y diccionarios para manipulacion eficiente de datos.

## Objetivos de Aprendizaje
1. Comprender y utilizar las estructuras de datos incorporadas en Python de manera efectiva.
2. Realizar operaciones con listas, tuplas, diccionarios y conjuntos.
3. Implementar comprensiones de listas y diccionarios para manipulacion de datos.
4. Aplicar estas estructuras en escenarios practicos de programacion.

## Conceptos

### Que es una estructura de datos?

Una estructura de datos es una forma de organizar y almacenar multiples datos para que puedas acceder a ellos y modificarlos de manera eficiente. En lugar de crear variables separadas para 100 elementos, los colocas en una sola estructura.

### Que es una lista?

Una lista es una coleccion ordenada y mutable de elementos. "Ordenada" significa que los elementos mantienen su posicion. "Mutable" significa que puedes agregar, eliminar o cambiar elementos despues de crear la lista.

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # agregar al final
fruits[0]                 # acceder por posicion: "apple"
```

Usa listas cuando tengas una secuencia de elementos que podrian cambiar.

### Que es una tupla?

Una tupla es como una lista, pero **inmutable** -- una vez creada, no puedes cambiar su contenido. Esto hace que las tuplas sean utiles para datos que no deben ser modificados accidentalmente.

```python
coordinates = (10, 20)
name, age = ("Alice", 25)  # desempaquetado
```

Usa tuplas para colecciones fijas como coordenadas, colores RGB, o para devolver multiples valores desde una funcion.

### Que es un diccionario?

Un diccionario almacena datos como **pares clave-valor**. En lugar de acceder a los elementos por posicion (indice), accedes a ellos por un nombre de clave unico.

```python
person = {"name": "Alice", "age": 25, "city": "Berlin"}
person["name"]  # "Alice"
```

Piensa en el como un diccionario real: buscas una palabra (clave) para encontrar su definicion (valor). Usa diccionarios cuando quieras etiquetar y buscar datos rapidamente.

### Que es un conjunto (set)?

Un conjunto es una coleccion desordenada de elementos **unicos**. Elimina automaticamente los duplicados y soporta operaciones matematicas como union e interseccion.

```python
colors = {"red", "green", "blue", "red"}  # se convierte en {"red", "green", "blue"}
```

Usa conjuntos cuando necesites eliminar duplicados o realizar pruebas de pertenencia rapidamente.

### Que es una comprension de lista?

Una comprension de lista es una forma concisa de crear una nueva lista aplicando una expresion a cada elemento en una secuencia existente, todo en una sola linea:

```python
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

Reemplaza el patron de: crear lista vacia, iterar, agregar -- haciendo tu codigo mas corto y legible.

## Descripcion Detallada del Codigo

### lists_example.py
Este archivo muestra como trabajar con **listas en Python**, incluyendo su creacion, indexacion, metodos y comprension de listas.

**Ejemplos de codigo:**
```python
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]
```
```python
squares = [x**2 for x in range(5)]
```

### tuples_example.py
Este archivo explica como usar **tuplas en Python**, destacando su inmutabilidad y su uso practico.

**Ejemplos de codigo:**
```python
coordinates = (10, 20)
name, age, city = ("John", 25, "New York")
```

### dictionaries_example.py
Este archivo muestra como crear y manipular **diccionarios en Python**, incluyendo el acceso seguro a claves y el uso de metodos comunes.

**Ejemplos de codigo:**
```python
person = {"name": "John", "age": 30}
print(person["name"])
```
```python
squares = {x: x**2 for x in range(5)}
```

### sets_example.py
Este archivo explica como trabajar con **conjuntos en Python**, incluyendo operaciones como union, interseccion y diferencia.

**Ejemplos de codigo:**
```python
numbers = {1, 2, 3, 4, 5}
union = set1 | set2
```

### list_comprehension.py
Este archivo contiene ejemplos avanzados de **comprension de listas y diccionarios**, mostrando como crear estructuras de datos complejas de forma concisa.

**Ejemplos de codigo:**
```python
squares = [x**2 for x in range(5)]
flattened = [num for row in matrix for num in row]
```

## Como Ejecutar los Programas

1. Asegurate de tener Python instalado en tu maquina.
2. Navega al directorio del proyecto en tu terminal.
3. Utiliza el comando `python 04_data_structures/<nombre_archivo>.py` para ejecutar el programa deseado, reemplazando `<nombre_archivo>` con el nombre del archivo especifico (por ejemplo, `python 04_data_structures/lists_example.py`).
