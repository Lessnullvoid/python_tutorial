# Programación Orientada a Objetos en Python (Sección 08)

Esta sección cubre los conceptos de programación orientada a objetos (POO) y su implementación en Python.

## Descripción del Código

- **classes.py**: Introduce la creación y uso de clases y objetos, incluyendo métodos y atributos.
- **encapsulation.py**: Muestra cómo implementar encapsulación para proteger datos internos de una clase.
- **inheritance.py**: Demuestra cómo funciona la herencia, incluyendo herencia simple y múltiple.
- **polymorphism.py**: Ilustra el polimorfismo mediante clases abstractas, sobrecarga de métodos y operadores.

## Contenido de Esta Sección

En esta sección, exploraremos los conceptos fundamentales de la programación orientada a objetos, como:
1. Clases y Objetos
2. Encapsulación
3. Herencia
4. Polimorfismo

## Descripción Detallada del Código

### classes.py
Este archivo introduce la creación y uso de **clases y objetos en Python**.

**Ejemplos de código:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def introduce(self):
    return f"Hi, I'm {self.name} and I'm {self.age} years old."
```
```python
@staticmethod
def is_adult(age):
    return age >= 18
```

### encapsulation.py
Este archivo muestra cómo implementar **encapsulación en Python**, protegiendo datos internos de una clase.

**Ejemplos de código:**
```python
self._account_holder = account_holder  # Atributo protegido
self.__balance = initial_balance       # Atributo privado
```
```python
def deposit(self, amount):
    self.__balance += amount
```

### inheritance.py
Este archivo demuestra cómo funciona la **herencia en Python**, incluyendo la herencia simple y múltiple.

**Ejemplos de código:**
```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed
```
```python
def make_sound(self):
    return "Woof!"
```

### polymorphism.py
Este archivo ilustra el **polimorfismo en Python** mediante clases abstractas y sobrecarga de operadores.

**Ejemplos de código:**
```python
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```
```python
def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)
```
```python
def make_it_swim_and_sound(thing):
    print(thing.make_sound())
    print(thing.swim())
```

## Cómo Ejecutar los Programas

1. Asegúrate de tener Python instalado en tu máquina.
2. Navega al directorio que contiene los archivos de código.
3. Utiliza la línea de comandos para ejecutar un programa específico. Por ejemplo:
   ```bash
   python classes.py
   ```
4. Sigue las instrucciones proporcionadas en cada archivo para más detalles sobre su uso.

