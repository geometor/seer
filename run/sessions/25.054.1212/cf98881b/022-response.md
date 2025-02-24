# cf98881b • 022 • refine_coder

---
```python
"""
1.  **Identify Transition Columns:** Examine the input grid and identify columns that contain *only* the colors white (0), yellow (4), maroon (9) or blue(1).
2. **Observe Transitions:** Focus on the *transitions* between colors within each of these identified columns.
3.  **Select Columns:** Select the transition columns.
4. **Filter Values:** From the selected columns include only 0, 1, 4 and 9.
5.  **Output:** Construct the output grid using these selected and filtered columns.
"""

import numpy as np

def _is_transition_column(column):
    """Checks if a column contains only 0, 1, 4, or 9."""
    unique_values = np.unique(column)
    return all(value in [0, 1, 4, 9] for value in unique_values)

def _filter_column(column):
    """Filters a column, keeping only 0, 1, 4, and 9 values."""
    return [value for value in column if value in [0, 1, 4, 9]]

def transform(input_grid):
    # Convert input_grid to a NumPy array
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    output_grid = []

    # 1. & 2. Identify Transition Columns and Observe
    transition_columns_indices = []
    for j in range(cols):
        if _is_transition_column(input_grid[:, j]):
            transition_columns_indices.append(j)

    # 3. & 4. Select and Filter Columns
    filtered_columns = []
    for j in transition_columns_indices:
        filtered_column = _filter_column(input_grid[:,j])
        filtered_columns.append(filtered_column)


    # 5. Construct Output (Transpose to get correct orientation)
    # Find maximum length of filtered columns for padding.
    max_len = max(len(col) for col in filtered_columns) if filtered_columns else 0

    # Pad the columns
    padded_columns = []
    for col in filtered_columns:
         padded_col = col + [0] * (max_len-len(col))
         padded_columns.append(padded_col)
    
    output_grid = np.array(padded_columns)

    if output_grid.size > 0 :
       output_grid = output_grid.T

    return output_grid
```
