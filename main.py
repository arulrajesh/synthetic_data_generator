import pandas as pd
import numpy as np

# Load the existing dataset (replace with the path to your dataset)
data = pd.read_csv('your_dataset.csv')

# Set a random seed for reproducibility
np.random.seed(43)

# Define the noise level (e.g., 0.05 = 5% of the range of each numerical column)
noise_level = 0.05

# Specify the desired number of synthetic rows
num_synthetic_rows = 500

# Helper function to add noise to numerical columns
def add_noise(column):
    column_range = np.abs(column.max() - column.min())
    if column_range < np.finfo(np.float64).max:
        noise = np.random.uniform(-column_range * noise_level, column_range * noise_level, column.shape)
        return column + noise
    else:
        return column

# Generate the specified number of synthetic rows
synthetic_data = pd.DataFrame(columns=data.columns)

for _ in range(num_synthetic_rows):
    random_row = data.sample()
    
    # Apply noise to numerical columns
    numerical_columns = random_row.select_dtypes(include=[np.number])
    numerical_columns = numerical_columns.astype(np.float64)  # Convert to float64 to avoid overflow
    numerical_columns = numerical_columns.apply(add_noise)
    
    # Sample categorical columns
    categorical_columns = random_row.select_dtypes(exclude=[np.number])
    
    # Combine the processed numerical and categorical columns
    synthetic_row = pd.concat([numerical_columns, categorical_columns], axis=1)
    synthetic_data = synthetic_data.append(synthetic_row, ignore_index=True)

# Save the synthetic dataset to a new file
synthetic_data.to_csv('synthetic_data_500.csv', index=False)
