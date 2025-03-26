import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import joblib

def train_and_save_model(preprocessed_file, model_output_file):
    # Load the preprocessed data
    data = pd.read_excel(preprocessed_file, engine='openpyxl')

    # Separate features (X) and target variable (y)
    X = data.drop(columns=["Genre"])  # Features
    y = data["Genre"]  # Target variable

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the K-Nearest Neighbors classifier
    knn = KNeighborsClassifier(n_neighbors=5)  # You can tune n_neighbors
    knn.fit(X_train, y_train)

    # Evaluate the model on the test set
    y_pred = knn.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")

    # Save the trained model to a file using joblib
    joblib.dump(knn, model_output_file)
    print(f"Trained model saved to {model_output_file}")

# Example usage
preprocessed_file = "./preprocessed_dataset.xlsx"  
model_output_file = "./knn_model.pkl"
train_and_save_model(preprocessed_file, model_output_file)
