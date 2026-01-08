# 🚗 CO2 Emission Prediction Project 💨

This project uses **Machine Learning** to find out how much CO2 a car produces. We use a dataset from Canada with information about many different cars. I used a **Multiple Linear Regression** model for this project.

## 📊 About the Data

The data has information about 7,385 cars. Some important parts are:

* **Engine Size (L)**: The size of the car's engine.
* **Cylinders**: The number of cylinders in the engine.
* **Fuel Consumption**: How much fuel the car uses in the city and on highways.
* **CO2 Emissions**: This is what we want to predict (Target).

## 🛠️ What I Changed in the Data

I cleaned the data to make the model work better:

1. **Removed Text**: I removed columns with words like `Make` and `Model` because the computer needs numbers.
2. **Removed Double Info**: I deleted the `mpg` column because it was the same as `L/100 km`. This helps the math stay simple.
3. **Fixed Errors**: I removed empty columns like `Unnamed: 5`.

## 🧠 Why I Used This Model?

I chose **Multiple Linear Regression** because:

* We have more than one thing (like Engine Size and Cylinders) that affects the CO2.
* It is a great way to see the relationship between car features and pollution.
* It is easy to understand and very fast.

## 📈 Results

I trained the model with 80% of the data and tested it with 20%. The results are very good:

| Metric | Result |
| --- | --- |
| **Accuracy Percentage** | **94.41%** |
| **Average Error (MAE)** | **13.51 g/km** |
| **R2 Score** | **0.88** |

In the **Residual Plot** (the orange picture), you can see most points are near the zero line. This means my model's guesses are very close to the real numbers.

## ✅ Final Result

This project was successful! With **94.41% accuracy**, we can say this model is very reliable for predicting car pollution. It shows that bigger engines and more cylinders usually mean more CO2.
