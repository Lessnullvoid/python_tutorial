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

## Conceptos

### Que es la Programacion Orientada a Objetos?

La Programacion Orientada a Objetos (POO) es una forma de organizar codigo alrededor de "objetos" -- cosas que combinan datos y comportamiento juntos. En lugar de tener variables y funciones separadas dispersas, agrupas datos relacionados y las funciones que operan sobre esos datos en una sola unidad.

Piensa en ello como modelar el mundo real: un objeto "Coche" tiene datos (color, velocidad, nivel de combustible) y comportamientos (acelerar, frenar, recargar).

### Que es una clase?

Una clase es un plano o plantilla para crear objetos. Define que datos (atributos) y comportamientos (metodos) tendran los objetos.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name      # atributo
        self.breed = breed    # atributo

    def bark(self):           # metodo
        return "Woof!"
```

### Que es un objeto?

Un objeto es una instancia especifica creada a partir de una clase. Puedes crear muchos objetos de la misma clase, cada uno con datos diferentes.

```python
my_dog = Dog("Rex", "Labrador")   # objeto 1
your_dog = Dog("Luna", "Poodle")  # objeto 2
```

### Que es la encapsulacion?

La encapsulacion significa ocultar los datos internos de una clase y exponer solo lo necesario a traves de metodos. Esto protege los datos de ser cambiados accidentalmente.

- `_nombre` -- convencion para "protegido" (no deberia accederse directamente desde fuera)
- `__nombre` -- "privado" (Python dificulta su acceso desde fuera)

Piensa en ello como una cuenta bancaria: no puedes cambiar directamente el saldo; debes usar depositar() o retirar() que aplican reglas.

### Que es la herencia?

La herencia permite que una nueva clase (hija) reutilice el codigo de una clase existente (padre). La hija obtiene todos los atributos y metodos del padre, y puede agregar o sobreescribir los existentes.

```python
class Animal:         # padre
    def speak(self):
        pass

class Cat(Animal):    # hija hereda de Animal
    def speak(self):
        return "Meow!"
```

Esto evita duplicar codigo cuando multiples clases comparten comportamiento comun.

### Que es el polimorfismo?

Polimorfismo significa "muchas formas" -- diferentes clases pueden tener metodos con el mismo nombre que se comportan de manera diferente. Esto te permite escribir codigo que funciona con cualquier objeto que tenga el metodo esperado, sin importar su clase especifica.

```python
for animal in [Cat(), Dog(), Duck()]:
    print(animal.speak())  # cada uno responde diferente
```

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
