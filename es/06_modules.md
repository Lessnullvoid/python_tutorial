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

## Conceptos

### Que es un modulo?

Un modulo es simplemente un archivo `.py` que contiene codigo Python (funciones, clases, variables). Al poner codigo relacionado en un modulo, puedes reutilizarlo en multiples programas sin copiar y pegar.

```python
import math          # modulo integrado
print(math.sqrt(16)) # usar sus funciones
```

Piensa en los modulos como cajas de herramientas: en lugar de construir cada herramienta desde cero, tomas la caja que tiene lo que necesitas.

### Por que usar modulos?

- **Reutilizacion**: escribe una vez, usa en todas partes.
- **Organizacion**: mantiene funciones relacionadas juntas en un archivo.
- **Aislamiento de nombres**: evita conflictos de nombres entre diferentes partes de tu codigo.
- **Colaboracion**: diferentes miembros del equipo pueden trabajar en diferentes modulos.

### Que es importar?

Importar trae codigo de un modulo a tu programa actual. Python ofrece varias formas:

```python
import math                  # importar modulo completo
from math import sqrt        # importar funcion especifica
from math import sqrt as s   # importar con alias
import my_module             # importar tu propio archivo
```

### Que es un paquete?

Un paquete es una carpeta que contiene multiples modulos relacionados, mas un archivo especial `__init__.py` que le dice a Python "esta carpeta es un paquete."

```
mi_paquete/
    __init__.py
    modulo_a.py
    modulo_b.py
```

Los paquetes te permiten organizar proyectos grandes en grupos logicos. Importas de ellos con notacion de punto: `from mi_paquete import modulo_a`.

### Que es pip?

`pip` es el gestor de paquetes de Python. Descarga e instala paquetes de terceros desde el Python Package Index (PyPI) -- un vasto repositorio de bibliotecas creadas por la comunidad.

```bash
pip install requests    # instalar un paquete
pip list                # ver paquetes instalados
```

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
