# Conceptos Avanzados de Python (Seccion 09)

Esta seccion explora caracteristicas avanzadas de Python y tecnicas de programacion.

## Descripcion del Codigo

- [`context_managers.py`](../09_advanced/context_managers.py): Muestra como implementar administradores de contexto para manejar recursos de manera eficiente.
- [`decorators.py`](../09_advanced/decorators.py): Demuestra el uso de decoradores para modificar el comportamiento de funciones y clases.
- [`generators.py`](../09_advanced/generators.py): Ilustra el uso de generadores e iteradores para manejar secuencias de datos de forma eficiente.

## Contenido de Esta Seccion

En esta seccion cubriremos:
1. **Decoradores**: Modificacion del comportamiento de funciones.
2. **Administradores de Contexto**: Gestion eficiente de recursos con `with`.
3. **Generadores e Iteradores**: Creacion de secuencias y flujos de datos.

## Descripcion Detallada del Codigo

### context_managers.py
Este archivo muestra como implementar **administradores de contexto** en Python.

**Ejemplos de codigo:**
```python
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Duration: {time.time() - self.start:.2f} seconds")
```
```python
@contextmanager
def temporary_attribute(obj, name, value):
    original = getattr(obj, name, None)
    setattr(obj, name, value)
    yield
    setattr(obj, name, original)
```

### decorators.py
Este archivo introduce el uso de **decoradores en Python**.

**Ejemplos de codigo:**
```python
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f} seconds")
        return result
    return wrapper
```
```python
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance
```

### generators.py
Este archivo muestra como utilizar **generadores e iteradores en Python**.

**Ejemplos de codigo:**
```python
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
```
```python
def infinite_counter():
    num = 0
    while True:
        yield num
        num += 1
```
```python
def echo_generator():
    while True:
        received = yield
        print(f"Received: {received}")
```

## Como Ejecutar los Programas

1. Asegurate de tener Python instalado en tu maquina.
2. Navega al directorio del proyecto en tu terminal.
3. Utiliza la linea de comandos para ejecutar un programa. Por ejemplo:
   ```bash
   python 09_advanced/decorators.py
   ```
