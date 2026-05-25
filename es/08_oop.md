# Programacion Orientada a Objetos en Python (Seccion 08)

Esta seccion cubre los conceptos de programacion orientada a objetos (POO) y su implementacion en Python.

## Descripcion del Codigo

- [`classes.py`](../08_oop/classes.py): Introduce la creacion y uso de clases y objetos, incluyendo metodos y atributos.
- [`encapsulation.py`](../08_oop/encapsulation.py): Muestra como implementar encapsulacion para proteger datos internos de una clase.
- [`inheritance.py`](../08_oop/inheritance.py): Demuestra como funciona la herencia, incluyendo herencia simple y multiple.
- [`polymorphism.py`](../08_oop/polymorphism.py): Ilustra el polimorfismo mediante clases abstractas, sobrecarga de metodos y operadores.

## Contenido de Esta Seccion

En esta seccion, exploraremos los conceptos fundamentales de la programacion orientada a objetos:
1. Clases y Objetos
2. Encapsulacion
3. Herencia
4. Polimorfismo

## Descripcion Detallada del Codigo

### classes.py
Este archivo introduce la creacion y uso de **clases y objetos en Python**.

**Ejemplos de codigo:**
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
Este archivo muestra como implementar **encapsulacion en Python**, protegiendo datos internos de una clase.

**Ejemplos de codigo:**
```python
self._account_holder = account_holder  # Atributo protegido
self.__balance = initial_balance       # Atributo privado
```
```python
def deposit(self, amount):
    self.__balance += amount
```

### inheritance.py
Este archivo demuestra como funciona la **herencia en Python**, incluyendo la herencia simple y multiple.

**Ejemplos de codigo:**
```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof!"
```

### polymorphism.py
Este archivo ilustra el **polimorfismo en Python** mediante clases abstractas y sobrecarga de operadores.

**Ejemplos de codigo:**
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

## Como Ejecutar los Programas

1. Asegurate de tener Python instalado en tu maquina.
2. Navega al directorio del proyecto.
3. Utiliza la linea de comandos para ejecutar un programa especifico. Por ejemplo:
   ```bash
   python 08_oop/classes.py
   ```
