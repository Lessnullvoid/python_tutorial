# Inheritance in Python

class Animal:
    """Base class for all animals"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        return "Some generic animal sound"
    
    def describe(self):
        return f"I am {self.name}, a {self.species}"

class Dog(Animal):
    """Dog class inheriting from Animal"""
    
    def __init__(self, name, breed):
        # Call parent class's __init__
        super().__init__(name, species="Dog")
        self.breed = breed
    
    # Override parent's method
    def make_sound(self):
        return "Woof!"
    
    # Add new method
    def fetch(self):
        return f"{self.name} is fetching the ball"

class Cat(Animal):
    """Cat class inheriting from Animal"""
    
    def __init__(self, name, indoor=True):
        super().__init__(name, species="Cat")
        self.indoor = indoor
    
    def make_sound(self):
        return "Meow!"
    
    def scratch(self):
        return f"{self.name} is scratching"

# Multiple inheritance
class Pet:
    """Mixin class for pet-specific behavior"""
    
    def __init__(self):
        self.has_owner = True
    
    def get_owner(self):
        return "I have a loving owner"

class HouseCat(Cat, Pet):
    """HouseCat class inheriting from both Cat and Pet"""
    
    def __init__(self, name):
        Cat.__init__(self, name, indoor=True)
        Pet.__init__(self)
    
    def describe(self):
        return f"{super().describe()} and {self.get_owner()}"

# Method Resolution Order (MRO)
def demonstrate_mro():
    print("\nMethod Resolution Order for HouseCat:")
    for c in HouseCat.__mro__:
        print(c.__name__)

if __name__ == "__main__":
    # Create instances
    dog = Dog("Rex", "German Shepherd")
    cat = Cat("Whiskers")
    house_cat = HouseCat("Fluffy")
    
    # Demonstrate inheritance
    print("Basic inheritance:")
    print(dog.describe())
    print(dog.make_sound())
    print(dog.fetch())
    
    print("\nCat behavior:")
    print(cat.describe())
    print(cat.make_sound())
    print(cat.scratch())
    
    # Demonstrate multiple inheritance
    print("\nMultiple inheritance:")
    print(house_cat.describe())
    print(house_cat.make_sound())
    print(house_cat.get_owner())
    
    # Show MRO
    demonstrate_mro()
    
    # isinstance and issubclass
    print("\nType checking:")
    print(f"Is dog an Animal? {isinstance(dog, Animal)}")
    print(f"Is HouseCat a subclass of Pet? {issubclass(HouseCat, Pet)}") 