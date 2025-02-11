# Bibliotecas y Frameworks de Python (Sección 10)

Esta sección cubre bibliotecas populares de Python para ciencia de datos, solicitudes web y bases de datos.

## Descripción del Código

- **matplotlib_examples.py**: Muestra cómo utilizar Matplotlib para crear gráficos de líneas, barras y dispersión.
- **numpy_examples.py**: Introduce NumPy para operaciones matemáticas avanzadas con arrays.
- **pandas_examples.py**: Demuestra cómo trabajar con datos estructurados usando Pandas.
- **pytorch_examples.py**: Introduce PyTorch para aprendizaje profundo y operaciones con tensores.
- **requests_examples.py**: Muestra cómo realizar solicitudes HTTP con la biblioteca Requests.
- **sklearn_examples.py**: Proporciona ejemplos de clasificación, agrupamiento y validación cruzada con scikit-learn.
- **sqlalchemy_examples.py**: Introduce SQLAlchemy para manejar bases de datos utilizando ORM.

## Contenido de Esta Sección

En esta sección cubriremos:
1. Visualización de datos con **Matplotlib**.
2. Operaciones matemáticas con **NumPy**.
3. Manipulación y análisis de datos con **Pandas**.
4. Aprendizaje profundo con **PyTorch**.
5. Solicitudes HTTP con **Requests**.
6. Clasificación y agrupamiento con **scikit-learn**.
7. Manejo de bases de datos con **SQLAlchemy**.

## Descripción Detallada del Código

### matplotlib_examples.py
**Ejemplos de código:**
```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title("Gráfico de Líneas")
plt.show()
```

### numpy_examples.py
**Ejemplos de código:**
```python
a = np.array([1, 2, 3])
b = np.zeros((3, 3))
c = np.add(a, 10)
d = np.dot(a, a)
```

### pandas_examples.py
**Ejemplos de código:**
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
**Ejemplos de código:**
```python
x = torch.tensor([1, 2, 3])
model = SimpleNN()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
```

### requests_examples.py
**Ejemplos de código:**
```python
response = requests.get('https://api.github.com/users/github')
```
```python
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
```

### sklearn_examples.py
**Ejemplos de código:**
```python
model = LogisticRegression()
model.fit(X_train, y_train)
kmeans = KMeans(n_clusters=3)
clusters = kmeans.fit_predict(X)
```

### sqlalchemy_examples.py
**Ejemplos de código:**
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

## Cómo Ejecutar los Programas
1. Asegúrate de tener Python instalado en tu máquina.
2. Instala las bibliotecas requeridas utilizando `pip`:
   ```bash
   pip install pandas numpy requests sqlalchemy scikit-learn torch matplotlib
   ```
3. Navega al directorio que contiene los archivos de código.
4. Ejecuta el script deseado utilizando:
   ```bash
   python script_name.py
   ```
5. Sigue las instrucciones proporcionadas en cada archivo para más detalles sobre su uso.

---

## Descripción de las Bibliotecas Utilizadas

### 1. Matplotlib
**Matplotlib** es la biblioteca principal para la creación de gráficos en Python. Se utiliza para generar gráficos de líneas, barras, dispersión, histogramas y muchos otros tipos de visualizaciones. Ideal para visualizar datos de forma rápida y efectiva.

- **Posibilidades:** Gráficos estáticos y dinámicos, personalización avanzada de gráficos.
- **Usos:** Ciencia de datos, análisis exploratorio, presentación de resultados.

### 2. NumPy
**NumPy** es una biblioteca fundamental para la computación científica en Python. Proporciona soporte para arrays multidimensionales y una variedad de funciones matemáticas para operar con ellos.

- **Posibilidades:** Álgebra lineal, generación de números aleatorios, transformadas de Fourier.
- **Usos:** Procesamiento de datos, modelado matemático, análisis científico.

### 3. Pandas
**Pandas** es una biblioteca para la manipulación y análisis de datos estructurados. Facilita la creación, limpieza y análisis de datos tabulares.

- **Posibilidades:** Manejo de datos en formato CSV, JSON, SQL, y Excel.
- **Usos:** Ciencia de datos, preparación de datos, análisis exploratorio.

### 4. PyTorch
**PyTorch** es una biblioteca para aprendizaje profundo que proporciona un marco flexible y eficiente para construir redes neuronales.

- **Posibilidades:** Entrenamiento de redes neuronales, modelos avanzados de inteligencia artificial.
- **Usos:** Visión por computadora, procesamiento de lenguaje natural, investigación en IA.

### 5. Requests
**Requests** es una biblioteca para hacer solicitudes HTTP de manera sencilla y elegante. Es la herramienta preferida para interactuar con APIs.

- **Posibilidades:** Solicitudes GET, POST, manejo de sesiones, autenticación.
- **Usos:** Consumo de APIs, automatización web, scraping.

### 6. scikit-learn
**scikit-learn** es una biblioteca para aprendizaje automático. Proporciona herramientas para clasificación, regresión, agrupamiento y reducción de dimensionalidad.

- **Posibilidades:** Algoritmos de machine learning, validación cruzada, selección de características.
- **Usos:** Predicción, análisis de datos, modelos predictivos.

### 7. SQLAlchemy
**SQLAlchemy** es una biblioteca para manejar bases de datos en Python usando un enfoque ORM (Object-Relational Mapping).

- **Posibilidades:** Definición de modelos, consultas complejas, manejo eficiente de bases de datos.
- **Usos:** Desarrollo web, aplicaciones de bases de datos, gestión de datos.

---

Estas bibliotecas ofrecen un amplio conjunto de herramientas para diferentes áreas, desde la ciencia de datos hasta el desarrollo de aplicaciones complejas y el aprendizaje automático. Cada una tiene un ecosistema grande y bien documentado, lo que facilita su integración en proyectos reales.

