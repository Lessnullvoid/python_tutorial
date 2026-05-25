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
