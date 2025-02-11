# NumPy Examples
import numpy as np

def basic_array_operations():
    """Demonstrate basic NumPy array operations"""
    # Creating arrays
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    
    print("Basic array operations:")
    print(f"1D array: {arr1}")
    print(f"2D array:\n{arr2}")
    
    # Array attributes
    print("\nArray attributes:")
    print(f"Shape: {arr2.shape}")
    print(f"Dimensions: {arr2.ndim}")
    print(f"Data type: {arr2.dtype}")
    
    # Array creation functions
    print("\nArray creation:")
    zeros = np.zeros((2, 3))
    ones = np.ones((2, 2))
    random_arr = np.random.rand(3, 3)
    
    print(f"Zeros:\n{zeros}")
    print(f"Ones:\n{ones}")
    print(f"Random:\n{random_arr}")

def array_operations():
    """Demonstrate array mathematical operations"""
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    
    print("Array mathematics:")
    print(f"Addition: {arr1 + arr2}")
    print(f"Multiplication: {arr1 * arr2}")
    print(f"Square root: {np.sqrt(arr1)}")
    
    # Matrix operations
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    
    print("\nMatrix operations:")
    print(f"Matrix multiplication:\n{np.dot(matrix1, matrix2)}")
    print(f"Transpose:\n{matrix1.T}")

def array_indexing():
    """Demonstrate array indexing and slicing"""
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    
    print("Array indexing and slicing:")
    print(f"Original array:\n{arr}")
    print(f"Element at (1,2): {arr[1,2]}")
    print(f"First row: {arr[0,:]}")
    print(f"First column:\n{arr[:,0]}")
    print(f"Subarray:\n{arr[0:2,1:3]}")

def array_manipulation():
    """Demonstrate array manipulation operations"""
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    
    print("Array manipulation:")
    print(f"Original array:\n{arr}")
    print(f"Reshape:\n{arr.reshape(3,2)}")
    print(f"Flatten: {arr.flatten()}")
    
    # Concatenation
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    print(f"\nConcatenate: {np.concatenate((arr1, arr2))}")
    
    # Stacking
    print(f"Vertical stack:\n{np.vstack((arr1, arr2))}")
    print(f"Horizontal stack:\n{np.hstack((arr1, arr2))}")

def statistical_operations():
    """Demonstrate statistical operations"""
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    print("Statistical operations:")
    print(f"Original array:\n{arr}")
    print(f"Mean: {np.mean(arr)}")
    print(f"Standard deviation: {np.std(arr)}")
    print(f"Min: {np.min(arr)}")
    print(f"Max: {np.max(arr)}")
    print(f"Sum: {np.sum(arr)}")
    print(f"Column means: {np.mean(arr, axis=0)}")
    print(f"Row means: {np.mean(arr, axis=1)}")

if __name__ == "__main__":
    basic_array_operations()
    print("\n" + "="*50 + "\n")
    array_operations()
    print("\n" + "="*50 + "\n")
    array_indexing()
    print("\n" + "="*50 + "\n")
    array_manipulation()
    print("\n" + "="*50 + "\n")
    statistical_operations() 