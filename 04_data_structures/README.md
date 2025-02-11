# Estructuras de Datos en Python (Sección 04)

Esta sección cubre las estructuras de datos incorporadas en Python y sus operaciones.

## Descripción del Código

- **lists_example.py**: Muestra cómo crear, acceder y manipular listas en Python.
- **tuples_example.py**: Explica cómo usar tuplas, destacando su inmutabilidad y casos prácticos.
- **dictionaries_example.py**: Presenta el uso de diccionarios, incluyendo acceso seguro y métodos comunes.
- **sets_example.py**: Demuestra cómo trabajar con conjuntos y realizar operaciones como unión e intersección.
- **list_comprehension.py**: Contiene ejemplos avanzados de comprensión de listas y diccionarios para manipulación eficiente de datos.

## Contenido de Esta Sección

Incluye ejercicios prácticos y ejemplos que ilustran el uso de estructuras de datos en Python. Cada ejercicio está diseñado para reforzar los conceptos y proporcionar experiencia práctica.

## Objetivos de Aprendizaje
1. Comprender y utilizar las estructuras de datos incorporadas en Python de manera efectiva.
2. Realizar operaciones con listas, tuplas, diccionarios y conjuntos.
3. Implementar comprensiones de listas y diccionarios para manipulación de datos.
4. Aplicar estas estructuras en escenarios prácticos de programación.

## Descripción Detallada del Código

### lists_example.py
Este archivo muestra cómo trabajar con **listas en Python**, incluyendo su creación, indexación, métodos y comprensión de listas.

**Ejemplos de código:**
```python
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]
```
```python
squares = [x**2 for x in range(5)]
```

### tuples_example.py
Este archivo explica cómo usar **tuplas en Python**, destacando su inmutabilidad y su uso práctico.

**Ejemplos de código:**
```python
coordinates = (10, 20)
name, age, city = ("John", 25, "New York")
```

### dictionaries_example.py
Este archivo muestra cómo crear y manipular **diccionarios en Python**, incluyendo el acceso seguro a claves y el uso de métodos comunes.

**Ejemplos de código:**
```python
person = {"name": "John", "age": 30}
print(person["name"])
```
```python
squares = {x: x**2 for x in range(5)}
```

### sets_example.py
Este archivo explica cómo trabajar con **conjuntos en Python**, incluyendo operaciones como unión, intersección y diferencia.

**Ejemplos de código:**
```python
numbers = {1, 2, 3, 4, 5}
union = set1 | set2
```

### list_comprehension.py
Este archivo contiene ejemplos avanzados de **comprensión de listas y diccionarios**, mostrando cómo crear estructuras de datos complejas de forma concisa.

**Ejemplos de código:**
```python
squares = [x**2 for x in range(5)]
flattened = [num for row in matrix for num in row]
```

## Cómo Ejecutar los Programas

Para ejecutar los programas en esta sección, sigue estos pasos:
1. Asegúrate de tener Python instalado en tu máquina.
2. Navega al directorio `04_data_structures` en tu terminal.
3. Utiliza el comando `python <nombre_archivo>.py` para ejecutar el programa deseado, reemplazando `<nombre_archivo>` con el nombre del archivo específico (por ejemplo, `python lists_example.py`).