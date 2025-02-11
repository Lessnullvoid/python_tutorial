# Basic Classes and Objects in Python

class Person:
    """
    A class to represent a person.
    Demonstrates basic class features.
    """
    
    # Class variable (shared by all instances)
    species = "Homo Sapiens"
    
    # Constructor (initialization) method
    def __init__(self, name, age):
        # Instance variables (unique to each instance)
        self.name = name
        self.age = age
        self._email = None  # Protected attribute
        
    # Instance method
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
    # Property decorator - getter
    @property
    def email(self):
        if self._email is None:
            return f"{self.name.lower()}@example.com"
        return self._email
    
    # Property decorator - setter
    @email.setter
    def email(self, value):
        if '@' not in value:
            raise ValueError("Invalid email address")
        self._email = value
    
    # Static method (doesn't need self)
    @staticmethod
    def is_adult(age):
        return age >= 18
    
    # Class method (works with class, not instance)
    @classmethod
    def create_child(cls, name):
        return cls(name, 0)
    
    # String representation
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

# Using the Person class
if __name__ == "__main__":
    # Creating instances
    person1 = Person("Alice", 25)
    person2 = Person("Bob", 30)
    
    # Using instance methods
    print(person1.introduce())
    print(person2.introduce())
    
    # Accessing class variable
    print(f"\nSpecies: {Person.species}")
    
    # Using property
    print(f"\nEmail: {person1.email}")
    person1.email = "alice@gmail.com"
    print(f"New email: {person1.email}")
    
    # Using static method
    age = 20
    print(f"\nIs {age} adult? {Person.is_adult(age)}")
    
    # Using class method
    baby = Person.create_child("Charlie")
    print(f"\nBaby: {baby}")
    
    # String representations
    print(f"\nStr representation: {str(person1)}")
    print(f"Repr representation: {repr(person1)}")
    
    # Demonstrating attribute access
    print(f"\nDirect attribute access: {person1.name}")
    
    # Try to access protected attribute
    print(f"Protected attribute: {person1._email}")  # Note: Still accessible but not recommended 