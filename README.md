# House Price Prediction (ML)

This repository contains a Python-based Machine Learning model that predicts house prices using **Multiple Linear Regression**. The project demonstrates the full workflow from data cleaning to visualization and prediction.

## 📊 Dataset Features
The model uses a CSV dataset (`houseprices.csv`) with the following parameters:
* **Beds**: Number of bedrooms.
* **Baths**: Number of bathrooms.
* **Size**: Total square footage of the property.
* **Zip Code**: Geographic location identifier.
* **Price**: The target variable (house cost).

## 🛠️ Technologies Used
* **Python 3**
* **Pandas**: For data manipulation and cleaning.
* **Scikit-Learn**: For implementing the Linear Regression model.
* **Matplotlib**: For data visualization.

## 🚀 How it Works
1. **Data Cleaning**: Uses `index_col=0` and `.strip()` to handle formatting issues and remove unnecessary index columns.
2. **Training**: Fits a `LinearRegression` model using multiple independent variables.
3. **Prediction**: Estimates a house price based on custom inputs (e.g., 3 beds, 2 baths, 3000 sqft).
4. **Visualization**: Generates a scatter plot of house parameters against price.

## 📈 Visualizations
The script generates a scatter plot saved as `house_price.png` to help visualize the correlation between the features and the final price.

## 🏁 How to Run
1. Clone the repository.
2. Ensure you have the required libraries installed:
   ```bash
   pip install pandas scikit-learn matplotlib
