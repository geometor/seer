# 9565186b • 018 • refine_coder

---
```python
"""
1.  **Identify Azure Pixels:** Scan the entire input grid.
2.  **Replace Azure with Gray:**  Everywhere an azure (8) pixel is found, change it to gray (5).
3.  **Identify the horizontal line:** Find the rows that contains the object Azure
4.  **Replace with Grey** Every pixel in the horizontal lines, replace it with grey(5).
"""

import numpy as np

def find_rows_with_color(grid, color):
    """Finds the rows containing a specified color."""
    rows_with_color = []
    for i, row in enumerate(grid):
        if color in row:
            rows_with_color.append(i)
    return rows_with_color

def transform(input_grid):
    # Initialize output_grid as a copy of the input grid.
    output_grid = np.copy(input_grid)
    
    # Find rows containing azure (8).
    rows_with_azure = find_rows_with_color(output_grid, 8)

    # Replace all azure pixels with gray.
    for i in range(output_grid.shape[0]):
        for j in range(output_grid.shape[1]):
            if output_grid[i, j] == 8:
                output_grid[i, j] = 5

    #Replace with Grey all pixels in lines
    for row_index in rows_with_azure:
      for j in range(output_grid.shape[1]):
        output_grid[row_index,j] = 5

    return output_grid
```

