# ---------------------------------------------------------
# Step 1: Import All Necessary Libraries
# ---------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

# ---------------------------------------------------------
# Step 2: Load and Explore the Dataset
# ---------------------------------------------------------
# Load the dataset from CSV file
dfnew = pd.read_csv("CO2 Emissions_Canada.csv")

# Display statistical summary and first 10 rows
print(dfnew.describe())
print(dfnew.head(10))

# ---------------------------------------------------------
# Step 3: Data Preprocessing
# ---------------------------------------------------------
# Define features (X) by dropping non-numeric and redundant columns
# Note: Added 'Fuel Consumption Comb (mpg)' to drop list to avoid multicollinearity
x = dfnew.drop(['CO2 Emissions(g/km)', 'Make', 'Model', 'Vehicle Class', 
                'Transmission', 'Fuel Type', 'Fuel Consumption Comb (mpg)'], axis=1)

# Define target variable (y)
y = dfnew['CO2 Emissions(g/km)']

# ---------------------------------------------------------
# Step 4: Split Data and Train the Model
# ---------------------------------------------------------
# Split data into training (80%) and testing (20%) sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
myco2model = linear_model.LinearRegression()
myco2model.fit(x_train, y_train)

# ---------------------------------------------------------
# Step 5: Make Predictions and Evaluate
# ---------------------------------------------------------
# Predict CO2 emissions for the test set
y_test_predict = myco2model.predict(x_test)

# Calculate performance metrics
score = r2_score(y_test, y_test_predict)
mae = mean_absolute_error(y_test, y_test_predict)
mape = np.mean(np.abs((y_test - y_test_predict) / y_test)) * 100
accuracy = 100 - mape

# Print evaluation results
print(f"\n--- Model Evaluation Results ---")
print(f"R2 Score: {score:.2f}")
print(f"Mean Absolute Error: {mae:.2f} g/km")
print(f"Model Accuracy Percentage: {accuracy:.2f}%")

# ---------------------------------------------------------
# Step 6: Visualization
# ---------------------------------------------------------
# Plot the residuals (errors) to visualize model performance
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_test - y_test_predict, color='orange', alpha=0.5)
plt.axhline(y=0, color='black', linestyle='--')
plt.xlabel("Actual Values")
plt.ylabel("Residuals (Errors)")
plt.title("Error Distribution (Residual Plot)")
plt.show()