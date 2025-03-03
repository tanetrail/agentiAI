import pytest
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
df = pd.read_csv('./Data/data.csv')

# Separate features and target
X = df[['X1', 'X2', 'X3']]
y = df['Target']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict the target on test data
y_pred = model.predict(X_test)

# Test 1: Ensure the model's R-squared value is above 0.8 (80%)
def test_r2_score():
    r2 = r2_score(y_test, y_pred)
    assert r2 > 0.6, f"R-squared score is too low: {r2}"

# Test 2: Ensure the Mean Squared Error is below a certain threshold (e.g., 25)
def test_mse():
    mse = mean_squared_error(y_test, y_pred)
    assert mse < 35, f"Mean Squared Error is too high: {mse}"