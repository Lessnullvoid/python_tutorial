# JSON File Operations in Python
import json
from datetime import datetime

# Sample data
sample_data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "hiking", "photography"],
    "children": None,
    "married": True,
    "details": {
        "height": 175,
        "weight": 70
    }
}

# Writing JSON to a file
def write_json_example():
    print("Writing to JSON file:")
    with open('data.json', 'w') as file:
        json.dump(sample_data, file, indent=4)
    print("JSON file written successfully")

# Reading JSON from a file
def read_json_example():
    print("\nReading from JSON file:")
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
            print("Loaded data:")
            print(json.dumps(data, indent=2))
    except FileNotFoundError:
        print("Error: JSON file not found!")

# Working with complex data types
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

def complex_json_example():
    print("\nHandling complex data types:")
    complex_data = {
        "name": "Event Log",
        "timestamp": datetime.now(),
        "events": [
            {"id": 1, "time": datetime.now(), "type": "login"},
            {"id": 2, "time": datetime.now(), "type": "logout"}
        ]
    }
    
    # Writing complex data
    with open('complex_data.json', 'w') as file:
        json.dump(complex_data, file, cls=DateTimeEncoder, indent=4)
    
    print("Complex JSON file written successfully")

# JSON string operations
def json_string_operations():
    print("\nJSON string operations:")
    
    # Converting Python object to JSON string
    json_string = json.dumps(sample_data, indent=2)
    print("JSON string:")
    print(json_string)
    
    # Parsing JSON string
    parsed_data = json.loads(json_string)
    print("\nParsed data type:", type(parsed_data))
    print("Accessing nested data:", parsed_data['details']['height'])

if __name__ == "__main__":
    write_json_example()
    read_json_example()
    complex_json_example()
    json_string_operations() 