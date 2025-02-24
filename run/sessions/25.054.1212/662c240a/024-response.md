# 662c240a • 024 • refine_coder

---
```python
"""
The output grid is a 3x3 subgrid of the input grid. The output grid matches a 3x3 section of the input grid. If multiple matches are found, the top-leftmost match is selected.
"""

import numpy as np

def find_subgrid(input_array, subgrid_array):
    """
    Finds the top-leftmost occurrence of a subgrid within a larger grid.

    Args:
        input_array: The larger grid (NumPy array).
        subgrid_array: The subgrid to search for (NumPy array).

    Returns:
        A tuple (row, col) representing the top-left corner of the first
        occurrence of the subgrid, or None if the subgrid is not found.
    """
    sub_rows, sub_cols = subgrid_array.shape
    rows, cols = input_array.shape

    for i in range(rows - sub_rows + 1):
        for j in range(cols - sub_cols + 1):
            if np.array_equal(input_array[i:i+sub_rows, j:j+sub_cols], subgrid_array):
                return (i, j)  # Return top-left corner
    return None

def transform(input_grid):
    """
    Extracts a 3x3 subgrid from the input grid. The output grid is a 3x3 section of the input that.
    If there are multiple occurrences, select the top-left one.
    """
    input_array = np.array(input_grid)
    rows, cols = input_array.shape

    # Iterate through all possible 3x3 subgrids
    for i in range(rows - 2):
        for j in range(cols - 2):
            potential_output = input_array[i:i+3, j:j+3]
            # Check if the subgrid exists elsewhere, prioritize top-leftmost.

            found_location = find_subgrid(input_array, potential_output)
            if found_location == (i,j):
                output_grid = potential_output.tolist()
                return output_grid

    # Fallback in case no 3x3 subgrid is valid (shouldn't happen given the prompt,
    #  but good practice to have a fallback)
    return input_array[max(0, rows - 3):, max(0, cols - 3):].tolist()
```
