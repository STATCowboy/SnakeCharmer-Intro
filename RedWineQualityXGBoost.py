# Train XGBoost model for Detecting Wine Quality
# Save model to file using pickle
# Load model and make predictions and validation set
#
# Adapted from https://machinelearningmastery.com/save-gradient-boosting-models-xgboost-python/
#
# How to install XGBoost on Windows - http://www.picnet.com.au/blogs/guido/post/2016/09/22/xgboost-windows-x64-binaries-for-download/


from numpy import loadtxt, vstack, column_stack
import xgboost
import pickle
from sklearn import model_selection
from sklearn.metrics import accuracy_score

# Load the Wine Data
dataset = loadtxt('winequality-red-NoHeader.csv', delimiter=",")

# Headers of Data
# "fixed acidity","volatile acidity","citric acid","residual sugar","chlorides","free sulfur dioxide","total sulfur dioxide","density","pH","sulphates","alcohol","quality"

# Split the wine data into X (independent variable) and y (dependent variable)
X = dataset[:, 0:11]
Y = dataset[:, 11]

# Split wine data into train and validation sets
seed = 7
test_size = 0.3
X_train, X_valid, y_train, y_valid = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)

# Fit model on Wine Training Data and save model to Pickle file
model = xgboost.XGBClassifier()
model.fit(X_train, y_train)
# save model to file
pickle.dump(model, open("winequality-red.pickle.dat", "wb"))

# Load model from Pickle file
loaded_model = pickle.load(open("winequality-red.pickle.dat", "rb"))

# Make predictions for Validation data
y_pred = loaded_model.predict(X_valid)
predictions = [round(value) for value in y_pred]

# Evaluate predictions
accuracy = accuracy_score(y_valid, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))

# Create Dataset with Prediction and Inputs
predictionResult = column_stack(([X_valid, vstack(y_valid), vstack(y_pred)]))

# Try a Simple Decision Tree
# Adapted from http://scikit-learn.org/stable/modules/tree.html
from sklearn import tree

# Train Model
wineTree = tree.DecisionTreeClassifier()
wineTree = wineTree.fit(X_train, y_train)

# Predict a Wine Quality (Class) from inputs
wineTree.predict([[6.8, .47, .08, 2.2, .0064, 18.0, 38.0, .999933, 3.2, .64, 9.8, ]])

# Display Tree Visually
import graphviz

# Install steps for it to work
# 1. Install windows package from: http://www.graphviz.org/Download_windows.php
# 2. Install python graphviz package
# 3. Add C:\Program Files (x86)\Graphviz2.38\bin to User path

dot_data = tree.export_graphviz(wineTree, out_file=None)
graph = graphviz.Source(dot_data)
graph.render('wineTree.gv', view=True)
