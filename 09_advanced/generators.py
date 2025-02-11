# Generators and Iterators in Python

def fibonacci_generator(n):
    """Generate first n Fibonacci numbers"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Generator expression
def squares_generator(n):
    """Generate squares using generator expression"""
    return (x * x for x in range(n))

# Custom iterator class
class CountDown:
    """Iterator that counts down from n to 0"""
    
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start < 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current

# Infinite generator
def infinite_counter():
    """Generate an infinite sequence of numbers"""
    num = 0
    while True:
        yield num
        num += 1

# Generator with send() method
def echo_generator():
    """Generator that echoes received values"""
    while True:
        received = yield
        print(f"Received: {received}")

# Generator with multiple yields
def range_with_status(n):
    """Generate numbers with status messages"""
    yield "Starting"
    for i in range(n):
        yield i
    yield "Finished"

if __name__ == "__main__":
    # Using fibonacci generator
    print("Fibonacci sequence:")
    for num in fibonacci_generator(10):
        print(num, end=" ")
    print()
    
    # Using generator expression
    print("\nSquares:")
    squares = squares_generator(5)
    print(list(squares))
    
    # Using custom iterator
    print("\nCountdown:")
    for num in CountDown(5):
        print(num, end=" ")
    print()
    
    # Using infinite generator (with limit)
    print("\nInfinite counter (limited to 5):")
    counter = infinite_counter()
    for _ in range(5):
        print(next(counter), end=" ")
    print()
    
    # Using generator with send()
    print("\nEcho generator:")
    echo = echo_generator()
    next(echo)  # Prime the generator
    echo.send("Hello")
    echo.send(42)
    
    # Using generator with status
    print("\nRange with status:")
    for item in range_with_status(3):
        print(item)
    
    # Generator pipeline example
    def numbers_pipeline():
        numbers = range(1, 11)  # Generate 1-10
        squares = (n * n for n in numbers)  # Square each number
        filtered = (n for n in squares if n % 2 == 0)  # Keep even numbers
        return filtered
    
    print("\nGenerator pipeline result:")
    print(list(numbers_pipeline())) 