"""
1. **Identify Key Columns:** Examine the input grid and identify columns that contain *only* the colors yellow (4), maroon (9) or blue(1).
2. **Select Columns**: Select those key columns
3.  **Crop**: produce the output using the key columns
"""

import numpy as np

def transform(input_grid):
    # Convert input_grid to a NumPy array for easier manipulation
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = []

    # 1. & 2. Identify and Select Key Columns
    key_columns = []
    for j in range(cols):
        column_values = input_grid[:, j]
        unique_values = np.unique(column_values)
        if all(value in [1, 4, 9, 0] for value in unique_values): #include 0!
           key_columns.append(j)

    # 3. Crop and Create Output
    #print(key_columns)
    for j in key_columns:
      output_grid.append(input_grid[:,j])

    return np.array(output_grid).T