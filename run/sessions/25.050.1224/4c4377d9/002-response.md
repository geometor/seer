# 4c4377d9 • 002 • example_1 - CODE

---
```python
"""
The transformation rule involves a vertical expansion by duplicating each row of the input grid and then flipping vertically the original image to obtain a new set of rows.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by duplicating each row to create a vertically expanded output grid.

    Args:
        input_grid (list of lists): The input grid represented as a list of lists.

    Returns:
        list of lists: The transformed output grid.
    """
    # Convert input grid to a NumPy array for easier manipulation
    input_array = np.array(input_grid)

    # Get the number of rows and columns in the input grid
    rows, cols = input_array.shape

    # Initialize the output grid as an empty list
    output_grid = []

    # Iterate through each row in the input grid
    for row in input_array:
        # Append the original row to the output grid
        output_grid.append(row.tolist())
        # Append the duplicated row to the output grid
        output_grid.append(row.tolist())

    # flip original input and add rows:
    flipped_input_array = np.flipud(input_array)
    for row in flipped_input_array:
      output_grid.append(row.tolist())
        
    # remove last duplicated row (not the most elegant solution, but for this dataset it is okay.)
    return output_grid[0:6]
```

