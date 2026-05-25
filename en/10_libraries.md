# Python Libraries and Frameworks (Section 10)

This section covers popular Python libraries for data science, web requests, and databases.

## Code Description

- [`matplotlib_examples.py`](../10_libraries/matplotlib_examples.py): Shows how to use Matplotlib to create line, bar, and scatter plots.
- [`numpy_examples.py`](../10_libraries/numpy_examples.py): Introduces NumPy for advanced mathematical operations with arrays.
- [`pandas_examples.py`](../10_libraries/pandas_examples.py): Demonstrates how to work with structured data using Pandas.
- [`pytorch_examples.py`](../10_libraries/pytorch_examples.py): Introduces PyTorch for deep learning and tensor operations.
- [`requests_examples.py`](../10_libraries/requests_examples.py): Shows how to make HTTP requests with the Requests library.
- [`sklearn_examples.py`](../10_libraries/sklearn_examples.py): Provides examples of classification, clustering, and cross-validation with scikit-learn.
- [`sqlalchemy_examples.py`](../10_libraries/sqlalchemy_examples.py): Introduces SQLAlchemy for database management using ORM.

## Section Contents

In this section we will cover:
1. Data visualization with **Matplotlib**.
2. Mathematical operations with **NumPy**.
3. Data manipulation and analysis with **Pandas**.
4. Deep learning with **PyTorch**.
5. HTTP requests with **Requests**.
6. Classification and clustering with **scikit-learn**.
7. Database management with **SQLAlchemy**.

## Detailed Code Description

### matplotlib_examples.py
**Code examples:**
```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title("Line Plot")
plt.show()
```

### numpy_examples.py
**Code examples:**
```python
a = np.array([1, 2, 3])
b = np.zeros((3, 3))
c = np.add(a, 10)
d = np.dot(a, a)
```

### pandas_examples.py
**Code examples:**
```python
df = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30]
})
print(df)
```
```python
df_filtered = df[df['Age'] > 26]
df_sorted = df.sort_values(by='Age')
```

### pytorch_examples.py
**Code examples:**
```python
x = torch.tensor([1, 2, 3])
model = SimpleNN()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
```

### requests_examples.py
**Code examples:**
```python
response = requests.get('https://api.github.com/users/github')
```
```python
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
```

### sklearn_examples.py
**Code examples:**
```python
model = LogisticRegression()
model.fit(X_train, y_train)
kmeans = KMeans(n_clusters=3)
clusters = kmeans.fit_predict(X)
```

### sqlalchemy_examples.py
**Code examples:**
```python
class User(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
```
```python
session.add(User(name="Alice"))
session.commit()
users = session.query(User).all()
```

## How to Run the Programs
1. Make sure Python is installed on your machine.
2. Install the required libraries using `pip`:
   ```bash
   pip install -r requirements.txt
   ```
3. Navigate to the project directory.
4. Run the desired script using:
   ```bash
   python 10_libraries/script_name.py
   ```

---

## Library Descriptions

### 1. Matplotlib
**Matplotlib** is the primary library for creating plots in Python. It is used to generate line, bar, scatter, histogram, and many other types of visualizations.

- **Capabilities:** Static and dynamic plots, advanced chart customization.
- **Use cases:** Data science, exploratory analysis, presenting results.

### 2. NumPy
**NumPy** is a fundamental library for scientific computing in Python. It provides support for multidimensional arrays and a variety of mathematical functions to operate on them.

- **Capabilities:** Linear algebra, random number generation, Fourier transforms.
- **Use cases:** Data processing, mathematical modeling, scientific analysis.

### 3. Pandas
**Pandas** is a library for manipulation and analysis of structured data. It facilitates the creation, cleaning, and analysis of tabular data.

- **Capabilities:** Handling data in CSV, JSON, SQL, and Excel formats.
- **Use cases:** Data science, data preparation, exploratory analysis.

### 4. PyTorch
**PyTorch** is a deep learning library that provides a flexible and efficient framework for building neural networks.

- **Capabilities:** Neural network training, advanced AI models.
- **Use cases:** Computer vision, natural language processing, AI research.

### 5. Requests
**Requests** is a library for making HTTP requests in a simple and elegant way. It is the preferred tool for interacting with APIs.

- **Capabilities:** GET and POST requests, session management, authentication.
- **Use cases:** API consumption, web automation, scraping.

### 6. scikit-learn
**scikit-learn** is a machine learning library. It provides tools for classification, regression, clustering, and dimensionality reduction.

- **Capabilities:** Machine learning algorithms, cross-validation, feature selection.
- **Use cases:** Prediction, data analysis, predictive models.

### 7. SQLAlchemy
**SQLAlchemy** is a library for managing databases in Python using an ORM (Object-Relational Mapping) approach.

- **Capabilities:** Model definition, complex queries, efficient database management.
- **Use cases:** Web development, database applications, data management.

---

These libraries offer a broad set of tools for different areas, from data science to complex application development and machine learning. Each one has a large, well-documented ecosystem that facilitates integration into real projects.
