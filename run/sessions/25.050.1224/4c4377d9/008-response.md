# 4c4377d9 • 008 • example_4 - CODE

---
```python
"""
The transformation rule involves a vertical expansion by duplicating each row of the input grid, followed by appending a vertically flipped version of the original input grid. The first 6 rows are then selected as the final output.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by duplicating each row, appending a vertically flipped version,
    and taking the first 6 rows.

    Args:
        input_grid (list of lists): The input grid represented as a list of lists.

    Returns:
        list of lists: The transformed output grid.
    """
    # Convert input grid to a NumPy array
    input_array = np.array(input_grid)

    # Initialize the output grid as an empty list
    output_grid = []

    # Duplicate each row
    for row in input_array:
        output_grid.append(row.tolist())
        output_grid.append(row.tolist())

    # Append a vertically flipped version of the input
    flipped_input_array = np.flipud(input_array)
    for row in flipped_input_array:
        output_grid.append(row.tolist())

    # Take the first 6 rows
    output_grid = output_grid[:6]

    return output_grid
```

