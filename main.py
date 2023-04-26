import pandas as pd
import numpy as np

# Load the existing dataset (replace with the path to your dataset)
data = pd.read_csv('your_dataset.csv')

# Set a random seed for reproducibility
np.random.seed(42)

# Specify the desired number of synthetic rows
num_synthetic_rows = 500

# Generate synthetic numerical columns
def generate_synthetic_numerical(column):
    mean_val = column.mean()
    std_val = column.std()
    return np.random.normal(mean_val, std_val, num_synthetic_rows)

# Generate synthetic categorical columns
def generate_synthetic_categorical(column):
    return column.sample(num_synthetic_rows, replace=True).reset_index(drop=True)

# Generate the specified number of synthetic rows
numerical_columns = data.select_dtypes(include=[np.number]).columns
categorical_columns = data.select_dtypes(exclude=[np.number]).columns

synthetic_numerical_data = pd.DataFrame({col: generate_synthetic_numerical(data[col]) for col in numerical_columns})
synthetic_categorical_data = pd.DataFrame({col: generate_synthetic_categorical(data[col]) for col in categorical_columns})

synthetic_data = pd.concat([synthetic_numerical_data, synthetic_categorical_data], axis=1)

# Save the synthetic dataset to a new file
synthetic_data.to_csv('synthetic_data_with_strings.csv', index=False)
