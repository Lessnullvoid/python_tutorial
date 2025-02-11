# Basic File Operations in Python

# Writing to a text file
def write_example():
    print("Writing to a file:")
    # Using 'with' statement (context manager) to handle file operations
    with open("sample.txt", "w") as file:
        file.write("Hello, this is line 1\n")
        file.write("This is line 2\n")
        file.write("And this is line 3")
    print("File written successfully")

# Reading from a text file
def read_example():
    print("\nReading from a file:")
    try:
        with open("sample.txt", "r") as file:
            # Read entire file
            content = file.read()
            print("Entire file content:")
            print(content)
            
        # Reading line by line
        print("\nReading line by line:")
        with open("sample.txt", "r") as file:
            for line in file:
                print(f"Line: {line.strip()}")
                
    except FileNotFoundError:
        print("Error: File not found!")

# Appending to a file
def append_example():
    print("\nAppending to a file:")
    with open("sample.txt", "a") as file:
        file.write("\nThis line is appended")
        file.write("\nAnother appended line")
    print("Content appended successfully")

# Reading and writing with different modes
def file_modes_example():
    print("\nDemonstrating different file modes:")
    
    # Write binary data
    with open("binary_file.bin", "wb") as file:
        file.write(b"Hello in binary\n")
        
    # Read binary data
    with open("binary_file.bin", "rb") as file:
        binary_content = file.read()
        print(f"Binary content: {binary_content}")

# File position operations
def file_position_example():
    print("\nFile position operations:")
    with open("sample.txt", "r") as file:
        # Read first line
        first_line = file.readline()
        print(f"Current position: {file.tell()}")
        
        # Move to beginning
        file.seek(0)
        print("After seeking to beginning:")
        print(file.readline())

if __name__ == "__main__":
    write_example()
    read_example()
    append_example()
    read_example()  # Read again to see appended content
    file_modes_example()
    file_position_example() 