# Modulos y Paquetes en Python (Seccion 06)

Esta seccion cubre la creacion de modulos, importacion y organizacion de paquetes en Python.

## Descripcion del Codigo

- [`my_module.py`](../06_modules/my_module.py): Demuestra como crear un modulo con funciones matematicas basicas y una clase `Circle`.
- [`using_modules.py`](../06_modules/using_modules.py): Muestra como importar y usar modulos estandar y personalizados.
- [`package_example/`](../06_modules/package_example/): Un paquete de ejemplo que contiene:
  - [`__init__.py`](../06_modules/package_example/__init__.py): Inicializa el paquete, haciendo accesibles las funciones y clases principales.
  - [`main.py`](../06_modules/package_example/main.py): Define la funcionalidad principal del paquete, incluyendo la clase `Calculator`.
  - [`utils.py`](../06_modules/package_example/utils.py): Proporciona funciones utilitarias para formatear cadenas y validar numeros.

## Objetivos de Aprendizaje
1. Crear y utilizar modulos en Python.
2. Importar modulos estandar y personalizados.
3. Organizar archivos Python en paquetes.
4. Utilizar paquetes de terceros mediante `pip`.
5. Crear y probar tu propio paquete de Python.

## Descripcion Detallada del Codigo

### my_module.py
Este archivo muestra como crear un **modulo personalizado en Python** con funciones, constantes y clases.

**Ejemplos de codigo:**
```python
def add(a, b):
    return a + b

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return PI * self.radius ** 2
```

### using_modules.py
Este archivo muestra como **importar y usar modulos estandar y personalizados** en Python.

**Ejemplos de codigo:**
```python
import math
print(math.sqrt(16))  # Resultado: 4.0

import my_module
print(my_module.add(10, 5))
```

### package_example/__init__.py
Este archivo inicializa el paquete y **hace accesibles las funciones y clases principales** a nivel del paquete.

**Contenido clave:**
```python
PACKAGE_VERSION = "1.0.0"
AUTHOR = "Your Name"
from .main import greet, Calculator
from .utils import format_string
```

### package_example/main.py
Este archivo define la **funcionalidad principal del paquete**.

**Ejemplos de codigo:**
```python
def greet(name):
    return f"Hello, {name}!"

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
```

### package_example/utils.py
Este archivo proporciona **funciones utilitarias** para formatear cadenas y validar numeros.

**Ejemplos de codigo:**
```python
def format_string(text, uppercase=False):
    return text.upper() if uppercase else text.lower()

def validate_number(number):
    try:
        float(number)
        return True
    except (TypeError, ValueError):
        return False
```

## Como Ejecutar los Programas

1. Asegurate de tener Python instalado en tu maquina.
2. Navega al directorio del proyecto.
3. Utiliza la linea de comandos para ejecutar un programa especifico. Por ejemplo:
   ```bash
   python 06_modules/using_modules.py
   ```
