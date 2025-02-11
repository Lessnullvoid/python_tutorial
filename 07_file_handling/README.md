# Manejo de Archivos en Python (Sección 07)

Esta sección cubre operaciones con archivos, incluyendo texto, CSV, JSON y manejo de excepciones.

## Descripción del Código

- **file_operations.py**: Muestra cómo realizar operaciones básicas de lectura, escritura y anexado en archivos de texto.
- **csv_operations.py**: Demuestra cómo manejar archivos CSV utilizando el módulo `csv`.
- **json_operations.py**: Ilustra cómo trabajar con datos JSON, incluyendo serialización y deserialización.
- **exception_handling.py**: Proporciona ejemplos de manejo de excepciones para garantizar operaciones de archivo seguras.

## Contenido de Esta Sección

Aprenderás a:
1. Abrir y cerrar archivos en Python.
2. Leer y escribir archivos de texto, CSV y JSON.
3. Implementar manejo de errores para asegurar operaciones robustas.

## Descripción Detallada del Código

### file_operations.py
Este archivo muestra cómo realizar **operaciones básicas de archivos en Python**.

**Ejemplos de código:**
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
Este archivo demuestra cómo manejar **archivos CSV en Python** utilizando el módulo `csv`.

**Ejemplos de código:**
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
Este archivo ilustra cómo trabajar con **archivos JSON en Python**.

**Ejemplos de código:**
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
Este archivo muestra cómo implementar **manejo de excepciones en operaciones de archivo**.

**Ejemplos de código:**
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

## Cómo Ejecutar los Programas

1. Asegúrate de tener Python instalado en tu máquina.
2. Navega al directorio `07_file_handling` en tu terminal.
3. Ejecuta el script deseado utilizando el comando:
   ```bash
   python <script_name>.py
   ```
   Reemplaza `<script_name>` con el nombre del archivo que deseas ejecutar (por ejemplo, `file_operations.py`).

