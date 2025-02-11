# Módulos y Paquetes en Python (Sección 06)

Esta sección cubre la creación de módulos, importación y organización de paquetes en Python.

## Descripción del Código

- **my_module.py**: Demuestra cómo crear un módulo con funciones matemáticas básicas y una clase `Circle`.
- **using_modules.py**: Muestra cómo importar y usar módulos estándar y personalizados.
- **__init__.py**: Inicializa el paquete, haciendo accesibles las funciones y clases principales a nivel del paquete.
- **main.py**: Define la funcionalidad principal del paquete, incluyendo la clase `Calculator` y una función de saludo.
- **utils.py**: Proporciona funciones utilitarias para formatear cadenas y validar números.

## Contenido de Esta Sección

Esta sección incluye ejemplos prácticos para comprender cómo crear, organizar y utilizar módulos y paquetes en Python.

## Objetivos de Aprendizaje
1. Crear y utilizar módulos en Python.
2. Importar módulos estándar y personalizados.
3. Organizar archivos Python en paquetes.
4. Utilizar paquetes de terceros mediante `pip`.
5. Crear y probar tu propio paquete de Python.

## Descripción Detallada del Código

### my_module.py
Este archivo muestra cómo crear un **módulo personalizado en Python** con funciones, constantes y clases.

**Ejemplos de código:**
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
Este archivo muestra cómo **importar y usar módulos estándar y personalizados** en Python.

**Ejemplos de código:**
```python
import math
print(math.sqrt(16))  # Resultado: 4.0

import my_module
print(my_module.add(10, 5))
```

### __init__.py
Este archivo inicializa el paquete y **hace accesibles las funciones y clases principales** a nivel del paquete.

**Contenido clave:**
```python
PACKAGE_VERSION = "1.0.0"
AUTHOR = "Your Name"
from .main import greet, Calculator
from .utils import format_string
```

### main.py
Este archivo define la **funcionalidad principal del paquete**.

**Ejemplos de código:**
```python
def greet(name):
    return f"Hello, {name}!"

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
```

### utils.py
Este archivo proporciona **funciones utilitarias** para formatear cadenas y validar números.

**Ejemplos de código:**
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

## Cómo Ejecutar los Programas

1. Asegúrate de tener Python instalado en tu máquina.
2. Navega al directorio que contiene los archivos de código.
3. Utiliza la línea de comandos para ejecutar un programa específico. Por ejemplo:
   ```bash
   python using_modules.py
   ```
4. Sigue las instrucciones proporcionadas en cada archivo para más detalles sobre su uso.

