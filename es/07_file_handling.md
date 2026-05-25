# Manejo de Archivos en Python (Seccion 07)

Esta seccion cubre operaciones con archivos, incluyendo texto, CSV, JSON y manejo de excepciones.

## Descripcion del Codigo

- [`file_operations.py`](../07_file_handling/file_operations.py): Muestra como realizar operaciones basicas de lectura, escritura y anexado en archivos de texto.
- [`csv_operations.py`](../07_file_handling/csv_operations.py): Demuestra como manejar archivos CSV utilizando el modulo `csv`.
- [`json_operations.py`](../07_file_handling/json_operations.py): Ilustra como trabajar con datos JSON, incluyendo serializacion y deserializacion.
- [`exception_handling.py`](../07_file_handling/exception_handling.py): Proporciona ejemplos de manejo de excepciones para garantizar operaciones de archivo seguras.

## Objetivos de Aprendizaje

Aprenderas a:
1. Abrir y cerrar archivos en Python.
2. Leer y escribir archivos de texto, CSV y JSON.
3. Implementar manejo de errores para asegurar operaciones robustas.

## Conceptos

### Que es un archivo?

Un archivo es una ubicacion con nombre en tu disco que almacena datos de forma permanente. A diferencia de las variables (que desaparecen cuando tu programa termina), los archivos persisten despues de cerrar el programa. Los programas leen archivos para obtener datos y escriben archivos para guardar resultados.

### Que es leer y escribir?

- **Leer**: abrir un archivo y cargar su contenido en tu programa.
- **Escribir**: crear o sobrescribir un archivo con contenido nuevo.
- **Anexar**: agregar contenido al final de un archivo existente sin borrar lo que habia.

Python usa la funcion `open()` con indicadores de modo:

```python
open("archivo.txt", "r")   # leer
open("archivo.txt", "w")   # escribir (sobrescribe!)
open("archivo.txt", "a")   # anexar
```

La declaracion `with` asegura que el archivo se cierre correctamente al terminar:

```python
with open("archivo.txt", "r") as f:
    content = f.read()
```

### Que es CSV?

CSV (Comma-Separated Values / Valores Separados por Comas) es un formato simple de archivo para datos tabulares (como una hoja de calculo). Cada linea es una fila, y los valores en cada fila estan separados por comas.

```
nombre,edad,ciudad
Alice,25,Berlin
Bob,30,Madrid
```

El modulo integrado `csv` de Python facilita la lectura y escritura de estos archivos.

### Que es JSON?

JSON (JavaScript Object Notation) es un formato ligero para almacenar datos estructurados. Se parece a los diccionarios y listas de Python, lo que lo hace intuitivo para trabajar.

```json
{"name": "Alice", "age": 25, "hobbies": ["reading", "coding"]}
```

El modulo `json` de Python convierte entre objetos Python y cadenas JSON (serializacion/deserializacion).

### Que es una excepcion?

Una excepcion es un error que ocurre mientras tu programa se ejecuta (no un error de escritura en tu codigo, sino algo inesperado como un archivo faltante o entrada invalida). En lugar de que el programa se detenga, puedes "atrapar" excepciones y manejarlas de manera elegante:

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero!")
```

Esto es esencial para operaciones con archivos porque los archivos podrian no existir, estar bloqueados o contener datos inesperados.

## Descripcion Detallada del Codigo

### file_operations.py
Este archivo muestra como realizar **operaciones basicas de archivos en Python**.

**Ejemplos de codigo:**
```python
with open("sample.txt", "w") as file:
    file.write("Hello, this is line 1\n")
```
```python
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
```

### csv_operations.py
Este archivo demuestra como manejar **archivos CSV en Python** utilizando el modulo `csv`.

**Ejemplos de codigo:**
```python
with open('people.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sample_data)
```
```python
with open('people.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

### json_operations.py
Este archivo ilustra como trabajar con **archivos JSON en Python**.

**Ejemplos de codigo:**
```python
with open('data.json', 'w') as file:
    json.dump(sample_data, file, indent=4)
```
```python
with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)
```

### exception_handling.py
Este archivo muestra como implementar **manejo de excepciones en operaciones de archivo**.

**Ejemplos de codigo:**
```python
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File does not exist")
```
```python
try:
    number = int("abc")
except ValueError:
    print("Error: Invalid number format")
```

## Como Ejecutar los Programas

1. Asegurate de tener Python instalado en tu maquina.
2. Navega al directorio del proyecto en tu terminal.
3. Ejecuta el script deseado utilizando el comando:
   ```bash
   python 07_file_handling/<script_name>.py
   ```
   Reemplaza `<script_name>` con el nombre del archivo que deseas ejecutar (por ejemplo, `file_operations`).
