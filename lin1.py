import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import r2_score, mean_squared_error

# Load the dataset
df = pd.read_csv('Linex_d.csv') 

# Select only the 'area' and 'price' columns
df_binary = df[['area', 'price']] 

# Rename the columns for clarity
df_binary.columns = ['Area', 'Price'] 

# Handle missing values using forward fill
df_binary.fillna(method='ffill', inplace=True)

# Dropping any rows with NaN values just in case
df_binary.dropna(inplace=True)

# Convert the data into numpy arrays for independent (X) and dependent (y) variables
X = np.array(df_binary['Area']).reshape(-1, 1)  # Independent variable (Area)
y = np.array(df_binary['Price']).reshape(-1, 1)  # Dependent variable (Price)

# Splitting the data into training and testing datasets (75% training, 25% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Initialize the Linear Regression model
regr = LinearRegression()

# Train the model using the training data
regr.fit(X_train, y_train)

# Make predictions
y_pred = regr.predict(X_test)

# Plotting the scatter plot of actual values and the regression line
plt.scatter(X_test, y_test, color='blue', label='Actual Prices')  # Scatter plot of actual values
plt.plot(X_test, y_pred, color='black', linewidth=2, label='Regression Line')  # Regression line

# # Adding labels and title
# plt.xlabel('Area (sq ft)')
# plt.ylabel('Price ($)')
# plt.title('Linear Regression: Area vs Price')
# plt.legend()

# # Show the plot
# plt.show()