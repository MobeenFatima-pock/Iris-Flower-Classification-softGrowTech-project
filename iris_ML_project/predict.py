import joblib
import numpy as np

# Load trained model
model = joblib.load("iris_model.pkl")

# User input
sepal_length = float(input("Enter Sepal Length: "))
sepal_width = float(input("Enter Sepal Width: "))
petal_length = float(input("Enter Petal Length: "))
petal_width = float(input("Enter Petal Width: "))

features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

prediction = model.predict(features)

species = ["Setosa", "Versicolor", "Virginica"]

print("Predicted Species:", species[prediction[0]])