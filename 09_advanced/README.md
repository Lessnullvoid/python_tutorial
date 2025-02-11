# Conceptos Avanzados de Python (Sección 09)

Esta sección explora características avanzadas de Python y técnicas de programación.

## Descripción del Código

- **context_managers.py**: Muestra cómo implementar administradores de contexto para manejar recursos de manera eficiente.
- **decorators.py**: Demuestra el uso de decoradores para modificar el comportamiento de funciones y clases.
- **generators.py**: Ilustra el uso de generadores e iteradores para manejar secuencias de datos de forma eficiente.

## Contenido de Esta Sección

En esta sección cubriremos:
1. **Decoradores**: Modificación del comportamiento de funciones.
2. **Administradores de Contexto**: Gestión eficiente de recursos con `with`.
3. **Generadores e Iteradores**: Creación de secuencias y flujos de datos.

## Descripción Detallada del Código

### context_managers.py
Este archivo muestra cómo implementar **administradores de contexto** en Python.

**Ejemplos de código:**
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

**Ejemplos de código:**
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
Este archivo muestra cómo utilizar **generadores e iteradores en Python**.

**Ejemplos de código:**
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

## Cómo Ejecutar los Programas

1. Asegúrate de tener Python instalado en tu máquina.
2. Navega al directorio `09_advanced` en tu terminal.
3. Utiliza la línea de comandos para ejecutar un programa. Por ejemplo:
   ```bash
   python decorators.py
   ```
4. Sigue las instrucciones proporcionadas en cada archivo para más detalles sobre su uso.

