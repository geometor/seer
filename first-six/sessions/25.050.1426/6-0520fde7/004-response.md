# 6-0520fde7 • 004 • example_2 - CODE

---
**input**
```
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 5
0 0 0 0 0 0
0 0 0 0 0 0
```

![Image](002-test_1_input.png)


**output**
```
0 0 0
0 0 0
0 0 0
```

![Image](002-test_1_output.png)

```python
"""
If the input grid contains a vertical column of gray color (5), the output is a fixed 3x3 grid with specific red pixels (2) at positions (0, 1), (1, 2), and (2, 1), and white color (0) elsewhere. The input's content otherwise is ignored.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid based on the presence of a gray column.

    Args:
        input_grid (list of lists): The input grid.

    Returns:
        list of lists: The transformed output grid.
    """
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape

    # Check if any column is entirely composed of the color 5 (gray).
    gray_column_present = False
    for j in range(cols):
        if np.all(input_grid[:, j] == 5):
            gray_column_present = True
            break

    # Initialize a 3x3 output grid filled with 0 (white).
    output_grid = np.zeros((3, 3), dtype=int)

    # If a gray column is present, set the specific red pixel locations.
    if gray_column_present:
        output_grid[0, 1] = 2
        output_grid[1, 2] = 2
        output_grid[2, 1] = 2

    return output_grid.tolist()
```
