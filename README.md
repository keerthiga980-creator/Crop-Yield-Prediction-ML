# 🌾 Crop Yield Prediction using Machine Learning

A Machine Learning project that predicts crop yield using agricultural and environmental factors. The project uses a real-world crop yield dataset and Random Forest Regression.

## 📌 Project Overview

Crop yield can be affected by factors such as rainfall, temperature, pesticide usage, crop type, and location.

This project uses Machine Learning to predict crop yield based on these factors.

## 🤖 Machine Learning Algorithm

**Random Forest Regression**

Random Forest Regression combines multiple decision trees to produce a prediction for crop yield.

## 📊 Input Features

- Area
- Year
- Average Annual Rainfall
- Pesticides Usage
- Average Temperature
- Crop Type

## 🎯 Target

**Crop Yield (`value_hg_ha`)**

The target represents crop yield in hectograms per hectare (hg/ha).

## 🔄 Project Workflow

1. Load the real-world crop yield dataset
2. Check dataset information
3. Check missing values and duplicate records
4. Select input features and target
5. Encode categorical features
6. Split data into training and testing sets
7. Train Random Forest Regression model
8. Predict crop yield
9. Evaluate model performance
10. Visualize actual vs predicted values
11. Analyze feature importance
12. Save the trained model and preprocessor
13. Test a new crop input

## 📈 Model Evaluation

The model was evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

The model achieved an **R² Score of approximately 0.984** on the test set.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib
- Google Colab

## 📂 Project Files

| File | Description |
|---|---|
| `Crop_Yield_Prediction_Real_Dataset.ipynb` | Complete ML notebook |
| `crop_yield_real_random_forest.pkl` | Trained Random Forest model |
| `crop_yield_preprocessor.pkl` | Feature preprocessing object |

## 📚 Dataset

The project uses the **Dataset for Crop Yield Prediction** published on Zenodo.

Dataset source: Zenodo

## 👩‍💻 Author

**Keerthiga J**

B.Sc. Computer Science with Artificial Intelligence
