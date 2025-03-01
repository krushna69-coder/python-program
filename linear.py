# # import numpy as np 
# # import pandas as pd 
# # import seaborn as sns 
# # import matplotlib.pyplot as plt 
# # from sklearn.model_selection import train_test_split 
# # from sklearn.linear_model import LinearRegression 
# # from sklearn.metrics import r2_score, mean_squared_error

# # # Load the dataset
# # df = pd.read_csv('Linex_d.csv') 

# # # Select only the 'area' and 'price' columns
# # df_binary = df[['area', 'price']] 

# # # Rename the columns for clarity
# # df_binary.columns = ['Area', 'Price'] 

# # # Handle missing values using forward fill
# # df_binary.fillna(method='ffill', inplace=True)

# # # Dropping any rows with NaN values just in case
# # df_binary.dropna(inplace=True)

# # # Convert the data into numpy arrays for independent (X) and dependent (y) variables
# # X = np.array(df_binary['Area']).reshape(-1, 1)  # Independent variable (Area)
# # y = np.array(df_binary['Price']).reshape(-1, 1)  # Dependent variable (Price)

# # # Splitting the data into training and testing datasets (75% training, 25% testing)
# # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# # # Initialize the Linear Regression model
# # regr = LinearRegression()

# # # Train the model using the training data
# # regr.fit(X_train, y_train)

# # # Make predictions
# # y_pred = regr.predict(X_test)

# # # Plotting the scatter plot of actual values and the regression line
# # plt.scatter(X_test, y_test, color='blue', label='Actual Prices')  # Scatter plot of actual values
# # plt.plot(X_test, y_pred, color='black', linewidth=2, label='Regression Line')  # Regression line

# # # Adding labels and title
# # plt.xlabel('Area (sq ft)')
# # plt.ylabel('Price ($)')
# # plt.title('Linear Regression: Area vs Price')
# # plt.legend()

# # # Show the plot
# # plt.show()




# import numpy as np 
# import pandas as pd 
# import seaborn as sns 
# import matplotlib.pyplot as plt 
# from sklearn.model_selection import train_test_split 
# from sklearn.linear_model import LinearRegression 
# from sklearn.metrics import r2_score, mean_squared_error

# # Load the dataset
# df = pd.read_csv('Linex_d.csv') 

# # Select only the 'area' and 'price' columns
# df_binary = df[['area', 'price']] 

# # Rename the columns for clarity
# df_binary.columns = ['Area', 'Price'] 

# # Handle missing values using forward fill
# df_binary.fillna(method='ffill', inplace=True)

# # Dropping any rows with NaN values just in case
# df_binary.dropna(inplace=True)

# # Convert the data into numpy arrays for independent (X) and dependent (y) variables
# X = np.array(df_binary['Area']).reshape(-1, 1)  # Independent variable (Area)
# y = np.array(df_binary['Price']).reshape(-1, 1)  # Dependent variable (Price)

# # Splitting the data into training and testing datasets (75% training, 25% testing)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# # Initialize the Linear Regression model
# regr = LinearRegression()

# # Train the model using the training data
# regr.fit(X_train, y_train)

# # Make predictions on the test set
# y_pred = regr.predict(X_test)

# # Predict values between the min and max of the Area (for interpolation)
# # Create a range of values for Area within the training data
# area_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)  # 100 points between min and max

# # Predict the corresponding prices for these values
# price_pred = regr.predict(area_range)

# # Plotting the actual data points and the regression line for interpolation
# plt.scatter(X_test, y_test, color='blue', label='Actual Prices')  # Actual test data points
# plt.plot(area_range, price_pred, color='red', linewidth=2, label='Regression Line (Interpolated)')  # Interpolated regression line

# # Adding labels and title
# plt.xlabel('Area (sq ft)')
# plt.ylabel('Price ($)')
# plt.title('Linear Regression: Area vs Price')
# plt.legend()

# # Show the plot
# plt.show()

# # Display predictions for a few values between the known data points
# print("Predictions for values between known data points:")
# for area_value in [2500, 3500, 4500]:  # Example areas between known data points
#     predicted_price = regr.predict(np.array([[area_value]]))
#     print(f"Predicted price for area {area_value} sq ft: ${predicted_price[0][0]:.2f}")


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

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

# Convert the data into numpy arrays for independent (X) and dependent (y) variables
X = np.array(df_binary['Area']).reshape(-1, 1)  # Independent variable (Area)
y = np.array(df_binary['Price'])  # Dependent variable (Price)

# Splitting the data into training and testing datasets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Linear Regression model
regr = LinearRegression()

# Train the model using the training data
regr.fit(X_train, y_train)

# Make predictions on the test set
y_pred = regr.predict(X_test)

# Print R-squared and Mean Squared Error to evaluate the model performance
print("\nModel Evaluation Metrics:")
print(f"R-squared: {r2_score(y_test, y_pred):.4f}")
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.4f}")

# Predict values between the min and max of the Area (for interpolation)
area_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)  # 100 points between min and max

# Predict the corresponding prices for these values
price_pred = regr.predict(area_range)

# Plotting the actual data points and the regression line for interpolation
plt.scatter(X_test, y_test, color='blue', label='Actual Prices')  # Actual test data points
plt.plot(area_range, price_pred, color='red', linewidth=2, label='Regression Line (Interpolated)')  # Interpolated regression line

# Adding labels and title
plt.xlabel('Area (sq ft)')
plt.ylabel('Price ($)')
plt.title('Linear Regression: Area vs Price')
plt.legend()

# Show the plot
plt.show()

# Display predictions for a few values between the known data points (e.g., for areas 2500, 3500, 4500)
print("\nPredictions for values between known data points:")
area_values_to_predict = [2500, 3500, 4500]  # Example areas between known data points
for area_value in area_values_to_predict:
    predicted_price = regr.predict(np.array([[area_value]]))
    print(f"Predicted price for area {area_value} sq ft: ${predicted_price[0]:.2f}")

    

# output =
# Predictions for values between known data points:
# Predicted price for area 2500 sq ft: $585000.00
# Predicted price for area 3500 sq ft: $725000.00
# Predicted price for area 4500 sq ft: $865000.00
