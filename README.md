# House-Price-Prediction-Linear-Regression-ML-
# 🏠 House Price Prediction using Linear Regression

## 📌 Project Overview

This project predicts house prices using **Machine Learning (Linear Regression)**. The model is trained on various house features such as area, number of bedrooms, bathrooms, stories, parking, and other amenities to estimate the selling price of a house.

This project demonstrates the complete Machine Learning workflow, including data preprocessing, model training, evaluation, prediction, and data visualization.

---

# 🎯 Objectives

* Predict house prices based on house features.
* Learn the fundamentals of Linear Regression.
* Perform data preprocessing and feature selection.
* Evaluate model performance using regression metrics.
* Visualize the distribution of house prices.

---

# 📂 Dataset Features

The dataset contains the following features:

* Area
* Bedrooms
* Bathrooms
* Stories
* Main Road Access
* Guest Room
* Basement
* Hot Water Heating
* Air Conditioning
* Parking

### Target Variable

* Price

---

# ⚙️ Technologies Used

* Python
* Pandas
* Matplotlib
* Scikit-learn

---

# 📚 Machine Learning Workflow

### 1. Import Libraries

Imported the required Python libraries for data manipulation, visualization, model training, and evaluation.

### 2. Load Dataset

Loaded the Housing dataset using Pandas.

### 3. Data Preprocessing

Converted categorical columns into numerical values.

Example:

* Yes → 1
* No → 0

Converted columns:

* Main Road
* Guest Room
* Basement
* Hot Water Heating
* Air Conditioning

---

### 4. Feature Selection

Selected the following features:

* Area
* Bedrooms
* Bathrooms
* Stories
* Main Road
* Guest Room
* Basement
* Hot Water Heating
* Air Conditioning
* Parking

Target:

* Price

---

### 5. Train-Test Split

The dataset was divided into:

* 80% Training Data
* 20% Testing Data

This allows the model to learn from one portion of the data and evaluate its performance on unseen data.

---

### 6. Model Training

A **Linear Regression** model was trained using the training dataset.

---

### 7. Model Evaluation

The model performance was evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score

These metrics measure how accurately the model predicts house prices.

---

### 8. Price Prediction

After training, the model predicts the price of a new house based on user-provided features.

Example Input:

* Area: 8664
* Bedrooms: 6
* Bathrooms: 2
* Stories: 1
* Main Road: Yes
* Guest Room: No
* Basement: No
* Hot Water Heating: Yes
* Air Conditioning: Yes
* Parking: 5

The trained model estimates the selling price for this house.

---

### 9. Data Visualization

A histogram is plotted to visualize the distribution of house prices in the dataset.

This helps understand:

* Price ranges
* Frequency of houses
* Overall price distribution

---

# 📊 Performance Metrics

The model evaluates performance using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* R² Score

A higher R² Score indicates better predictive performance.

---

# 📁 Project Structure

```
House-Price-Prediction/
│
├── Housing.csv
├── house_price_prediction.py
├── README.md
```

---

# 🚀 Future Improvements

Possible improvements for this project include:

* Feature Scaling
* One-Hot Encoding for additional categorical features
* Feature Engineering
* Hyperparameter Tuning
* Comparing multiple regression algorithms:

  * Decision Tree Regressor
  * Random Forest Regressor
  * XGBoost Regressor

---

# 📖 Learning Outcomes

Through this project, I learned:

* Data preprocessing
* Encoding categorical variables
* Feature selection
* Train-Test Split
* Linear Regression
* Model evaluation
* Predicting unseen data
* Data visualization using Matplotlib

---

# 👨‍💻 Author

**Nakul**

Machine Learning & AI Enthusiast

This project is part of my Machine Learning learning journey and demonstrates the implementation of Linear Regression for real-world house price prediction.
