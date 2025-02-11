# Exception Handling in File Operations

def safe_file_operations():
    # Basic try-except
    try:
        with open("nonexistent.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("Error: File does not exist")
    except IOError:
        print("Error: IO operation failed")
    except Exception as e:
        print(f"Unexpected error: {e}")

def multiple_exceptions():
    try:
        # Attempting risky operations
        file = open("test.txt", "r")
        number = int(file.readline())
        result = 10 / number
        file.close()
    except FileNotFoundError:
        print("Error: File not found")
    except ValueError:
        print("Error: Invalid number format in file")
    except ZeroDivisionError:
        print("Error: Division by zero")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("This code always executes")

def custom_exception_handling():
    class FileProcessingError(Exception):
        """Custom exception for file processing errors"""
        pass

    try:
        with open("data.txt", "r") as file:
            if file.readline().strip() == "":
                raise FileProcessingError("File is empty")
    except FileProcessingError as e:
        print(f"Custom error: {e}")

def context_manager_example():
    class FileHandler:
        def __init__(self, filename, mode):
            self.filename = filename
            self.mode = mode
            self.file = None

        def __enter__(self):
            try:
                self.file = open(self.filename, self.mode)
                return self.file
            except Exception as e:
                print(f"Error opening file: {e}")
                return None

        def __exit__(self, exc_type, exc_val, exc_tb):
            if self.file:
                self.file.close()
                print("File closed successfully")
            if exc_type is not None:
                print(f"An error occurred: {exc_val}")
                return True  # Suppress the exception

    # Using the custom context manager
    with FileHandler("test.txt", "w") as file:
        if file:
            file.write("Hello, World!")

if __name__ == "__main__":
    print("Testing safe file operations:")
    safe_file_operations()
    
    print("\nTesting multiple exceptions:")
    multiple_exceptions()
    
    print("\nTesting custom exception handling:")
    custom_exception_handling()
    
    print("\nTesting context manager:")
    context_manager_example() 