# Dictionaries in Python

# Creating dictionaries
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Different ways to create dictionaries
dict_constructor = dict(name="Alice", age=25, city="London")
dict_from_tuples = dict([("name", "Bob"), ("age", 35), ("city", "Paris")])

# Accessing values
print("Dictionary access:")
print(f"Name: {person['name']}")
print(f"Age: {person.get('age')}")  # Using get() method
print(f"Country: {person.get('country', 'Unknown')}")  # With default value

# Modifying dictionaries
print("\nModifying dictionary:")
person["email"] = "john@example.com"  # Adding new key-value pair
person["age"] = 31                    # Modifying existing value
print(person)

# Dictionary methods
print("\nDictionary methods:")
print(f"Keys: {person.keys()}")
print(f"Values: {person.values()}")
print(f"Items: {person.items()}")

# Removing items
removed_value = person.pop("email")    # Remove and return value
print(f"\nRemoved value: {removed_value}")
print(f"After pop: {person}")

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
print(f"\nDictionary comprehension: {squares}")

# Nested dictionaries
contacts = {
    "John": {
        "phone": "123-456-7890",
        "email": "john@example.com"
    },
    "Alice": {
        "phone": "098-765-4321",
        "email": "alice@example.com"
    }
}

print("\nNested dictionaries:")
print(f"John's phone: {contacts['John']['phone']}")

# Merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Python 3.5+
merged = {**dict1, **dict2}
print(f"\nMerged dictionaries: {merged}")

# Dictionary methods for merging
dict1.update(dict2)
print(f"Updated dict1: {dict1}")

# Safe dictionary access
print("\nSafe dictionary access:")
for key in ["name", "country"]:
    if key in person:
        print(f"{key}: {person[key]}")
    else:
        print(f"{key} not found") 