# c909285e • 002 • example_1 • investigate_coder

---
```python
"""
1.  **Identify Repeating Pattern:** Examine the input grid to locate a repeating subgrid pattern. This pattern repeats both horizontally and vertically.
2.  **Determine the top left corner:** look at the top left pixel.
3.  **Isolate One Instance:** Extract one complete instance of the repeating subgrid pattern.
4.  **Replace Green with Gray** if there is any Green in the isolated instance, replace it with Gray (0).
5.  **Output:** The extracted and possibly recolored subgrid becomes the output grid.
"""

import numpy as np

def find_repeating_pattern(grid):
    # Find the smallest repeating pattern in the grid
    rows, cols = grid.shape
    for i in range(1, rows // 2 + 1):
        for j in range(1, cols // 2 + 1):
            if rows % i == 0 and cols % j == 0:
                pattern = grid[:i, :j]
                valid_pattern = True
                for row_mult in range(rows // i):
                    for col_mult in range(cols // j):
                        if not np.array_equal(grid[row_mult*i:(row_mult+1)*i, col_mult*j:(col_mult+1)*j], pattern):
                            valid_pattern = False
                            break
                    if not valid_pattern:
                        break
                if valid_pattern:
                    return pattern
    return None

def transform(input_grid):
    # Convert the input grid to a NumPy array for easier manipulation
    input_grid = np.array(input_grid)
    
    # Find the repeating pattern
    pattern = find_repeating_pattern(input_grid)
    if pattern is None: return input_grid #should not occur, but handling

    # Replace green (3) with gray (0)
    output_grid = np.where(pattern == 3, 0, pattern)

    return output_grid.tolist()
```
