# Matplotlib Examples
import matplotlib.pyplot as plt
import numpy as np

def basic_line_plot():
    """Create a basic line plot"""
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='sin(x)')
    plt.title('Basic Line Plot')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.grid(True)
    plt.legend()
    plt.show()

def multiple_plots():
    """Create multiple plots in one figure"""
    x = np.linspace(0, 10, 100)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, np.sin(x), label='sin(x)')
    plt.plot(x, np.cos(x), label='cos(x)')
    plt.plot(x, np.tan(x), label='tan(x)')
    plt.title('Multiple Functions')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

def subplot_example():
    """Create multiple subplots"""
    x = np.linspace(0, 10, 100)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    ax1.plot(x, np.sin(x))
    ax1.set_title('Sine Wave')
    
    ax2.plot(x, np.cos(x))
    ax2.set_title('Cosine Wave')
    
    plt.tight_layout()
    plt.show()

def scatter_plot():
    """Create a scatter plot"""
    x = np.random.rand(50)
    y = np.random.rand(50)
    colors = np.random.rand(50)
    sizes = 1000 * np.random.rand(50)
    
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)
    plt.title('Scatter Plot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.colorbar()
    plt.show()

def bar_chart():
    """Create a bar chart"""
    categories = ['A', 'B', 'C', 'D']
    values = [3, 7, 2, 5]
    
    plt.figure(figsize=(8, 6))
    plt.bar(categories, values)
    plt.title('Bar Chart')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.show()

def pie_chart():
    """Create a pie chart"""
    sizes = [30, 20, 25, 15, 10]
    labels = ['A', 'B', 'C', 'D', 'E']
    explode = (0.1, 0, 0, 0, 0)
    
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    plt.axis('equal')
    plt.title('Pie Chart')
    plt.show()

def histogram():
    """Create a histogram"""
    data = np.random.randn(1000)
    
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=30, density=True, alpha=0.7)
    plt.title('Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    basic_line_plot()
    multiple_plots()
    subplot_example()
    scatter_plot()
    bar_chart()
    pie_chart()
    histogram() 