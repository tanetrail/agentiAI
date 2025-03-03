import numpy as np
import pandas as pd

# Set a random seed for reproducibility
np.random.seed(42)

# Generate 1000 samples
n_samples = 1000

# Create random features (e.g., 3 features)
X1 = np.random.rand(n_samples) * 10  # Feature 1 (Random numbers scaled by 10)
X2 = np.random.rand(n_samples) * 20  # Feature 2 (Random numbers scaled by 20)
X3 = np.random.rand(n_samples) * 30  # Feature 3 (Random numbers scaled by 30)

# Create a target variable (Y) with some noise
y = 2 * X1 + 3 * X2 + 4 * X3 + np.random.normal(0, 5, n_samples)  # Linear relationship + noise

# Create a pandas DataFrame to hold the data
df = pd.DataFrame({'X1': X1, 'X2': X2, 'X3': X3, 'Target': y})

df.to_csv("data.csv",index=False)

# Show the first few rows of the DataFrame
print(df.head())