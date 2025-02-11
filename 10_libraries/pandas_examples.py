# Pandas Examples
import pandas as pd
import numpy as np

def series_examples():
    """Demonstrate Pandas Series operations"""
    # Creating a Series
    s1 = pd.Series([1, 3, 5, np.nan, 6, 8])
    s2 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
    
    print("Series examples:")
    print(f"Basic series:\n{s1}")
    print(f"\nSeries with custom index:\n{s2}")
    
    # Series operations
    print("\nSeries operations:")
    print(f"Mean: {s1.mean()}")
    print(f"Description:\n{s1.describe()}")
    print(f"Value at 'a': {s2['a']}")

def dataframe_examples():
    """Demonstrate DataFrame operations"""
    # Creating a DataFrame
    df = pd.DataFrame({
        'A': [1, 2, 3, 4],
        'B': pd.Timestamp('20230101'),
        'C': pd.Series(1, index=list(range(4))),
        'D': np.array([3] * 4),
        'E': pd.Categorical(["test", "train", "test", "train"]),
        'F': 'foo'
    })
    
    print("DataFrame examples:")
    print(f"DataFrame:\n{df}")
    print(f"\nDataFrame info:\n{df.info()}")
    print(f"\nDataFrame description:\n{df.describe()}")

def data_manipulation():
    """Demonstrate data manipulation operations"""
    # Create sample data
    df = pd.DataFrame({
        'name': ['John', 'Jane', 'Bob', 'Alice'],
        'age': [25, 30, 35, 28],
        'city': ['New York', 'London', 'Paris', 'Tokyo'],
        'salary': [50000, 60000, 75000, 65000]
    })
    
    print("Data manipulation:")
    print(f"Original DataFrame:\n{df}")
    
    # Filtering
    print("\nFiltering (age > 30):")
    print(df[df['age'] > 30])
    
    # Sorting
    print("\nSorting by age:")
    print(df.sort_values('age'))
    
    # Adding new column
    df['salary_grade'] = df['salary'].apply(lambda x: 'High' if x > 60000 else 'Low')
    print("\nWith new column:")
    print(df)

def data_analysis():
    """Demonstrate data analysis operations"""
    # Create sample data
    df = pd.DataFrame({
        'department': ['IT', 'HR', 'IT', 'HR', 'IT'],
        'salary': [60000, 50000, 70000, 55000, 65000],
        'years': [3, 5, 7, 2, 4]
    })
    
    print("Data analysis:")
    print(f"Original DataFrame:\n{df}")
    
    # Grouping
    print("\nMean salary by department:")
    print(df.groupby('department')['salary'].mean())
    
    # Aggregation
    print("\nMultiple aggregations:")
    print(df.groupby('department').agg({
        'salary': ['mean', 'min', 'max'],
        'years': 'mean'
    }))

def data_cleaning():
    """Demonstrate data cleaning operations"""
    # Create sample data with missing values
    df = pd.DataFrame({
        'A': [1, np.nan, 3, np.nan],
        'B': [5, 6, np.nan, 8],
        'C': ['a', 'b', 'c', None]
    })
    
    print("Data cleaning:")
    print(f"Original DataFrame with missing values:\n{df}")
    
    # Handling missing values
    print("\nDropping NA values:")
    print(df.dropna())
    
    print("\nFilling NA values:")
    print(df.fillna({'A': 0, 'B': 0, 'C': 'unknown'}))

if __name__ == "__main__":
    series_examples()
    print("\n" + "="*50 + "\n")
    dataframe_examples()
    print("\n" + "="*50 + "\n")
    data_manipulation()
    print("\n" + "="*50 + "\n")
    data_analysis()
    print("\n" + "="*50 + "\n")
    data_cleaning() 