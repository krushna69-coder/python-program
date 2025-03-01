import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

# Load the dataset
df = pd.read_csv('Linex_d.csv')  # Ensure the file is in the same directory or provide the correct path

# Check the first few rows to confirm the dataset structure
print("First few rows of the dataset:")
print(df.head())

# Check for missing values in the dataset
print("\nMissing values in the dataset:")
print(df.isnull().sum())

# Handle missing values using forward fill
df.fillna(method='ffill', inplace=True)

# Dropping any rows with NaN values just in case
df.dropna(inplace=True)

# Check the cleaned dataset for missing values again
print("\nMissing values after filling:")
print(df.isnull().sum())

# Select only the 'area' and 'price' columns
df_binary = df[['area', 'price']]

# Rename the columns for clarity
df_binary.columns = ['Area', 'Price']

# Visualize the data to check the linearity of the relationship
plt.scatter(df_binary['Area'], df_binary['Price'])
plt.xlabel('Area')
plt.ylabel('Price')
plt.title('Area vs Price')
plt.show()

# Convert the data into numpy arrays for independent (X) and dependent (y) variables
X = np.array(df_binary['Area']).reshape(-1, 1)  # Independent variable (Area)
y = np.array(df_binary['Price'])  # Dependent variable (Price)

# Splitting the data into training and testing datasets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
regr = LinearRegression()

# Train the model using the training data
regr.fit(X_train, y_train)

# Accuracy on training data (R-squared)
train_accuracy = regr.score(X_train, y_train)
print(f"\nAccuracy on training data (R-squared): {train_accuracy:.4f}")

# Make predictions on the test set
y_pred = regr.predict(X_test)

# Print R-squared and Mean Squared Error to evaluate the model performance
print("\nModel Evaluation Metrics:")
print(f"R-squared: {r2_score(y_test, y_pred):.4f}")
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.4f}")

# If the R-squared is still low, try polynomial regression to improve accuracy+

# Transforming the feature (Area) into polynomial features (quadratic)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Splitting the data again into train and test sets
X_train_poly, X_test_poly, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
regr_poly = LinearRegression()

# Train the model using the polynomial features
regr_poly.fit(X_train_poly, y_train)

# Accuracy on training data (R-squared) for polynomial regression
train_accuracy_poly = regr_poly.score(X_train_poly, y_train)
print(f"\nAccuracy on training data (R-squared) with Polynomial Regression: {train_accuracy_poly:.4f}")

# Make predictions on the test set with polynomial features
y_pred_poly = regr_poly.predict(X_test_poly)

# Print R-squared and Mean Squared Error to evaluate the model performance
print("\nModel Evaluation Metrics with Polynomial Regression:")
print(f"R-squared: {r2_score(y_test, y_pred_poly):.4f}")
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred_poly):.4f}")

# Plotting the actual data points and the regression line for polynomial interpolation
area_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)  # 100 points between min and max
area_range_poly = poly.transform(area_range)  # Transform to polynomial features

# Predict the corresponding prices for these values
price_pred_poly = regr_poly.predict(area_range_poly)

# Plotting the actual data points and the regression line for polynomial interpolation
plt.scatter(X_test, y_test, color='blue', label='Actual Prices')  # Actual test data points
plt.plot(area_range, price_pred_poly, color='red', linewidth=2, label='Polynomial Regression Line')  # Polynomial regression line

# Adding labels and title
plt.xlabel('Area (sq ft)')
plt.ylabel('Price ($)')
plt.title('Polynomial Regression: Area vs Price')
plt.legend()

# Show the plot
plt.show()

# Display predictions for a few values between the known data points (e.g., for areas 2500, 3500, 4500)
print("\nPredictions for values between known data points using Polynomial Regression:")
area_values_to_predict = [2500, 3500, 4500]  # Example areas between known data points
for area_value in area_values_to_predict:
    predicted_price = regr_poly.predict(poly.transform(np.array([[area_value]])))
    print(f"Predicted price for area {area_value} sq ft: ${predicted_price[0]:.2f}")
