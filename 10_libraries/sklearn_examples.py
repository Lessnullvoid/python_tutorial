# Scikit-learn Examples
import numpy as np
from sklearn import datasets, model_selection, preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans

def classification_example():
    """Demonstrate basic classification with scikit-learn"""
    # Load iris dataset
    iris = datasets.load_iris()
    X, y = iris.data, iris.target
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = model_selection.train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    
    # Train logistic regression model
    print("Logistic Regression Example:")
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    
    # Make predictions
    predictions = model.predict(X_test)
    
    # Evaluate model
    print(f"Accuracy: {accuracy_score(y_test, predictions):.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, predictions, target_names=iris.target_names))

def model_comparison():
    """Compare different classification models"""
    # Load breast cancer dataset
    cancer = datasets.load_breast_cancer()
    X, y = cancer.data, cancer.target
    
    # Split data
    X_train, X_test, y_train, y_test = model_selection.train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    
    # Define models to compare
    models = {
        'Logistic Regression': LogisticRegression(max_iter=200),
        'Decision Tree': DecisionTreeClassifier(),
        'Random Forest': RandomForestClassifier()
    }
    
    print("\nModel Comparison:")
    # Train and evaluate each model
    for name, model in models.items():
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        print(f"{name} Accuracy: {accuracy:.2f}")

def preprocessing_pipeline():
    """Demonstrate preprocessing pipeline"""
    # Create sample data with different scales
    X = np.array([
        [1000, 3],
        [2000, 5],
        [3000, 8],
        [4000, 2],
        [5000, 4]
    ])
    y = np.array([0, 0, 1, 1, 1])
    
    # Create pipeline
    pipeline = Pipeline([
        ('scaler', preprocessing.StandardScaler()),
        ('classifier', LogisticRegression())
    ])
    
    # Fit and predict
    print("\nPipeline Example:")
    pipeline.fit(X, y)
    sample = np.array([[2500, 6]])
    prediction = pipeline.predict(sample)
    print(f"Prediction for sample {sample}: {prediction}")

def clustering_example():
    """Demonstrate K-means clustering"""
    # Generate sample data
    X, y = datasets.make_blobs(
        n_samples=300,
        centers=4,
        cluster_std=0.60,
        random_state=0
    )
    
    # Perform k-means clustering
    print("\nK-means Clustering Example:")
    kmeans = KMeans(n_clusters=4, random_state=0)
    clusters = kmeans.fit_predict(X)
    
    # Print cluster centers and sizes
    print("Cluster Centers:")
    print(kmeans.cluster_centers_)
    print("\nCluster Sizes:")
    for i in range(4):
        print(f"Cluster {i}: {np.sum(clusters == i)} samples")

def cross_validation_example():
    """Demonstrate cross-validation"""
    # Load diabetes dataset
    diabetes = datasets.load_diabetes()
    X, y = diabetes.data, diabetes.target
    
    # Create model
    model = RandomForestClassifier(random_state=42)
    
    # Perform k-fold cross-validation
    print("\nCross-validation Example:")
    cv_scores = model_selection.cross_val_score(
        model, X, y, cv=5, scoring='neg_mean_squared_error'
    )
    
    # Convert MSE to RMSE
    rmse_scores = np.sqrt(-cv_scores)
    print("RMSE scores for each fold:")
    print(rmse_scores)
    print(f"Average RMSE: {rmse_scores.mean():.2f}")
    print(f"Standard deviation: {rmse_scores.std():.2f}")

if __name__ == "__main__":
    classification_example()
    model_comparison()
    preprocessing_pipeline()
    clustering_example()
    cross_validation_example() 