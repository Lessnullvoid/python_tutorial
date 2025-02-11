# CSV File Operations in Python
import csv
from datetime import datetime

# Sample data
sample_data = [
    ['Name', 'Age', 'City'],
    ['John Doe', '30', 'New York'],
    ['Jane Smith', '25', 'Los Angeles'],
    ['Bob Johnson', '35', 'Chicago']
]

# Writing to a CSV file
def write_csv_example():
    print("Writing to CSV file:")
    with open('people.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(sample_data)
    print("CSV file written successfully")

# Reading from a CSV file
def read_csv_example():
    print("\nReading from CSV file:")
    try:
        with open('people.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"Row: {row}")
    except FileNotFoundError:
        print("Error: CSV file not found!")

# Using CSV with dictionaries
def dict_csv_example():
    print("\nUsing CSV with dictionaries:")
    
    # Writing dictionary data
    dict_data = [
        {'name': 'Alice', 'age': '28', 'city': 'Boston'},
        {'name': 'Charlie', 'age': '32', 'city': 'Seattle'}
    ]
    
    with open('people_dict.csv', 'w', newline='') as file:
        fieldnames = ['name', 'age', 'city']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(dict_data)
    
    # Reading dictionary data
    print("\nReading dictionary CSV:")
    with open('people_dict.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

# Working with custom CSV formats
def custom_csv_example():
    print("\nCustom CSV format:")
    data = [
        ['Date', 'Product', 'Price'],
        [datetime.now(), 'Product A', 19.99],
        [datetime.now(), 'Product B', 29.99]
    ]
    
    with open('sales.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerows(data)
    
    print("\nReading custom formatted CSV:")
    with open('sales.csv', 'r') as file:
        reader = csv.reader(file, delimiter='|')
        for row in reader:
            print(row)

if __name__ == "__main__":
    write_csv_example()
    read_csv_example()
    dict_csv_example()
    custom_csv_example() 