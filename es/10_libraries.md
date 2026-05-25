# Bibliotecas y Frameworks de Python (Seccion 10)

Esta seccion cubre bibliotecas populares de Python para ciencia de datos, solicitudes web y bases de datos.

## Descripcion del Codigo

- [`matplotlib_examples.py`](../10_libraries/matplotlib_examples.py): Muestra como utilizar Matplotlib para crear graficos de lineas, barras y dispersion.
- [`numpy_examples.py`](../10_libraries/numpy_examples.py): Introduce NumPy para operaciones matematicas avanzadas con arrays.
- [`pandas_examples.py`](../10_libraries/pandas_examples.py): Demuestra como trabajar con datos estructurados usando Pandas.
- [`pytorch_examples.py`](../10_libraries/pytorch_examples.py): Introduce PyTorch para aprendizaje profundo y operaciones con tensores.
- [`requests_examples.py`](../10_libraries/requests_examples.py): Muestra como realizar solicitudes HTTP con la biblioteca Requests.
- [`sklearn_examples.py`](../10_libraries/sklearn_examples.py): Proporciona ejemplos de clasificacion, agrupamiento y validacion cruzada con scikit-learn.
- [`sqlalchemy_examples.py`](../10_libraries/sqlalchemy_examples.py): Introduce SQLAlchemy para manejar bases de datos utilizando ORM.

## Contenido de Esta Seccion

En esta seccion cubriremos:
1. Visualizacion de datos con **Matplotlib**.
2. Operaciones matematicas con **NumPy**.
3. Manipulacion y analisis de datos con **Pandas**.
4. Aprendizaje profundo con **PyTorch**.
5. Solicitudes HTTP con **Requests**.
6. Clasificacion y agrupamiento con **scikit-learn**.
7. Manejo de bases de datos con **SQLAlchemy**.

## Conceptos

### Que es una biblioteca?

Una biblioteca (tambien llamada paquete) es una coleccion de codigo pre-escrito que resuelve problemas comunes, para que no tengas que construir todo desde cero. El ecosistema de Python tiene miles de bibliotecas para casi cualquier dominio.

Instalar una biblioteca se hace con `pip install nombre_biblioteca`, y usarla requiere una declaracion `import`.

### Por que usar bibliotecas?

Los programas del mundo real raramente empiezan desde cero. Las bibliotecas te dan soluciones probadas y optimizadas para:
- Visualizar datos (Matplotlib)
- Computacion numerica (NumPy)
- Analisis de datos (Pandas)
- Aprendizaje automatico (scikit-learn, PyTorch)
- Comunicarse con APIs web (Requests)
- Trabajar con bases de datos (SQLAlchemy)

Aprender a elegir y usar la biblioteca correcta es una de las habilidades de programacion mas valiosas.

### Vista rapida de cada biblioteca

| Biblioteca | Que hace | Caso de uso tipico |
|------------|----------|-------------------|
| **Matplotlib** | Crea graficos y plots | Visualizar tendencias, comparar datos |
| **NumPy** | Matematicas rapidas con arrays de numeros | Computacion cientifica, operaciones matriciales |
| **Pandas** | Manipulacion de datos tabulares | Limpiar, filtrar y analizar datos CSV/Excel |
| **PyTorch** | Construir y entrenar redes neuronales | Reconocimiento de imagenes, NLP, investigacion en IA |
| **Requests** | Enviar solicitudes HTTP | Obtener datos de APIs web |
| **scikit-learn** | Aprendizaje automatico clasico | Clasificacion, agrupamiento, prediccion |
| **SQLAlchemy** | Interaccion con bases de datos via objetos Python | Almacenar y consultar datos estructurados |

## Descripcion Detallada del Codigo

### matplotlib_examples.py
**Ejemplos de codigo:**
```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title("Grafico de Lineas")
plt.show()
```

### numpy_examples.py
**Ejemplos de codigo:**
```python
a = np.array([1, 2, 3])
b = np.zeros((3, 3))
c = np.add(a, 10)
d = np.dot(a, a)
```

### pandas_examples.py
**Ejemplos de codigo:**
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
**Ejemplos de codigo:**
```python
x = torch.tensor([1, 2, 3])
model = SimpleNN()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
```

### requests_examples.py
**Ejemplos de codigo:**
```python
response = requests.get('https://api.github.com/users/github')
```
```python
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
```

### sklearn_examples.py
**Ejemplos de codigo:**
```python
model = LogisticRegression()
model.fit(X_train, y_train)
kmeans = KMeans(n_clusters=3)
clusters = kmeans.fit_predict(X)
```

### sqlalchemy_examples.py
**Ejemplos de codigo:**
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

## Como Ejecutar los Programas
1. Asegurate de tener Python instalado en tu maquina.
2. Instala las bibliotecas requeridas utilizando `pip`:
   ```bash
   pip install -r requirements.txt
   ```
3. Navega al directorio del proyecto.
4. Ejecuta el script deseado utilizando:
   ```bash
   python 10_libraries/script_name.py
   ```

---

## Descripcion de las Bibliotecas Utilizadas

### 1. Matplotlib
**Matplotlib** es la biblioteca principal para la creacion de graficos en Python. Se utiliza para generar graficos de lineas, barras, dispersion, histogramas y muchos otros tipos de visualizaciones.

- **Posibilidades:** Graficos estaticos y dinamicos, personalizacion avanzada de graficos.
- **Usos:** Ciencia de datos, analisis exploratorio, presentacion de resultados.

### 2. NumPy
**NumPy** es una biblioteca fundamental para la computacion cientifica en Python. Proporciona soporte para arrays multidimensionales y una variedad de funciones matematicas para operar con ellos.

- **Posibilidades:** Algebra lineal, generacion de numeros aleatorios, transformadas de Fourier.
- **Usos:** Procesamiento de datos, modelado matematico, analisis cientifico.

### 3. Pandas
**Pandas** es una biblioteca para la manipulacion y analisis de datos estructurados. Facilita la creacion, limpieza y analisis de datos tabulares.

- **Posibilidades:** Manejo de datos en formato CSV, JSON, SQL, y Excel.
- **Usos:** Ciencia de datos, preparacion de datos, analisis exploratorio.

### 4. PyTorch
**PyTorch** es una biblioteca para aprendizaje profundo que proporciona un marco flexible y eficiente para construir redes neuronales.

- **Posibilidades:** Entrenamiento de redes neuronales, modelos avanzados de inteligencia artificial.
- **Usos:** Vision por computadora, procesamiento de lenguaje natural, investigacion en IA.

### 5. Requests
**Requests** es una biblioteca para hacer solicitudes HTTP de manera sencilla y elegante. Es la herramienta preferida para interactuar con APIs.

- **Posibilidades:** Solicitudes GET, POST, manejo de sesiones, autenticacion.
- **Usos:** Consumo de APIs, automatizacion web, scraping.

### 6. scikit-learn
**scikit-learn** es una biblioteca para aprendizaje automatico. Proporciona herramientas para clasificacion, regresion, agrupamiento y reduccion de dimensionalidad.

- **Posibilidades:** Algoritmos de machine learning, validacion cruzada, seleccion de caracteristicas.
- **Usos:** Prediccion, analisis de datos, modelos predictivos.

### 7. SQLAlchemy
**SQLAlchemy** es una biblioteca para manejar bases de datos en Python usando un enfoque ORM (Object-Relational Mapping).

- **Posibilidades:** Definicion de modelos, consultas complejas, manejo eficiente de bases de datos.
- **Usos:** Desarrollo web, aplicaciones de bases de datos, gestion de datos.

---

Estas bibliotecas ofrecen un amplio conjunto de herramientas para diferentes areas, desde la ciencia de datos hasta el desarrollo de aplicaciones complejas y el aprendizaje automatico.
