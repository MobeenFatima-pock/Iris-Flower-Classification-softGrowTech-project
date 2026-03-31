# Iris-Flower-Classification-softGrowTech-project
This project implements a Machine Learning model to classify iris flower species based on sepal and petal measurements using the Scikit-learn library. The model is trained on the Iris dataset and predicts whether a flower belongs to Setosa, Versicolor, or Virginica.
Project Description

The Iris Flower Classification Model is a Machine Learning project that predicts the species of an iris flower based on its physical features. The model uses four input parameters: sepal length, sepal width, petal length, and petal width to classify the flower into one of three species: Setosa, Versicolor, or Virginica.

The model is implemented using Python and Scikit-learn and trained on the well-known Iris dataset.

Working of the Model

The model works in the following steps:

1️⃣ Dataset Loading
The Iris dataset is loaded from the Scikit-learn library, which contains 150 samples of iris flowers with their measurements and species labels.

2️⃣ Data Splitting
The dataset is divided into training data (80%) and testing data (20%).

3️⃣ Model Training
A Random Forest Classifier is used to train the model using the training dataset.

4️⃣ Model Evaluation
The trained model predicts species for the test data, and the accuracy score is calculated.

5️⃣ Model Saving
The trained model is saved as iris_model.pkl using the joblib library.

6️⃣ Prediction
The user enters flower measurements, and the trained model predicts the corresponding iris species.

How to Run the Project
1️⃣ Install Dependencies
pip install -r requirements.txt
2️⃣ Train the Model
python train_model.py
3️⃣ Run the Prediction Program
python predict.py
4️⃣ Enter Input Values

Example:

Enter Sepal Length: 5.1
Enter Sepal Width: 3.5
Enter Petal Length: 1.4
Enter Petal Width: 0.2
5️⃣ Output
Predicted Species: Setosa
