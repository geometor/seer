# 1-3aa6fb7a • 010 • example_2 - CODE

---
```python
"""
1.  **Initialization:** Start with the input grid.
2.  **Identify:** Identify the positions of all azure colored pixels.
3.  **Locate:** Locate all white colored pixels adjacent to the azure ones
4.  **Check:** Working from upper left and lower right, determine if a white pixel that is adjecent to an azure pixel, has an azure neighbor to the left and or the right.
5.  **Transformation:** If the condition in step 4 is met for a white pixel, change the value/color to blue (1). If multiple white pixels next to azure qualify, transform one at a time, working in from the upper left and lower right.
6.  **Output:** The modified grid is the final output.
"""

import numpy as np

def get_neighbors(grid, row, col):
    """Gets the valid neighbors of a cell."""
    rows, cols = grid.shape
    neighbors = []
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # Only consider orthogonal neighbors
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:
            neighbors.append((new_row, new_col))
    return neighbors

def transform(input_grid):
    # Initialize output_grid as a copy of the input_grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Identify azure pixels
    azure_pixels = [(r, c) for r in range(rows) for c in range(cols) if output_grid[r, c] == 8]

    # Process from upper-left
    for r in range(rows):
        for c in range(cols):
            if output_grid[r, c] == 0:  # If white pixel
                neighbors = get_neighbors(output_grid, r, c)
                azure_neighbors = [(nr, nc) for nr, nc in neighbors if output_grid[nr, nc] == 8]
                if azure_neighbors:
                    # Check for horizontal azure neighbors
                    for ar, ac in azure_neighbors:
                        if ac < c and any(output_grid[ar, nc] == 8 for nc in range(ac + 1, c)): #neighbor to the left
                           output_grid[r,c] = 1
                           break
                        elif ac > c and any(output_grid[ar, nc] == 8 for nc in range(c + 1, ac)): #neighbor to the right
                           output_grid[r,c] = 1
                           break

    # Process from lower-right
    for r in range(rows - 1, -1, -1):
        for c in range(cols - 1, -1, -1):
            if output_grid[r, c] == 0:  # If white pixel
                neighbors = get_neighbors(output_grid, r, c)
                azure_neighbors = [(nr, nc) for nr, nc in neighbors if output_grid[nr, nc] == 8]
                if azure_neighbors:
                    # Check for horizontal azure neighbors
                    for ar, ac in azure_neighbors:
                        if ac < c and any(output_grid[ar, nc] == 8 for nc in range(ac + 1, c)): #neighbor to the left
                           output_grid[r,c] = 1
                           break
                        elif ac > c and any(output_grid[ar, nc] == 8 for nc in range(c + 1, ac)): #neighbor to the right
                           output_grid[r,c] = 1
                           break


    return output_grid
```
