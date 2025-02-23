# 00d62c1b • 026 • example_4 - CODE

---
```python
"""
Identifies and recolors internal green pixels that are fully enclosed by other green pixels to yellow.
"""

import numpy as np

def count_adjacent(grid, row, col, color, diagonal=False):
    """Counts the number of adjacent pixels of a specific color."""
    rows, cols = grid.shape
    count = 0
    
    # Orthogonal neighbors
    neighbors = [
        (row - 1, col), (row + 1, col),
        (row, col - 1), (row, col + 1)
    ]
    
    if diagonal:
    	neighbors.extend([    
        	(row - 1, col - 1), (row - 1, col + 1),
        	(row + 1, col - 1), (row + 1, col + 1)
        ])

    for r, c in neighbors:
        if 0 <= r < rows and 0 <= c < cols and grid[r, c] == color:
            count += 1

    return count

def transform(input_grid):
    """Transforms the input grid according to the defined rule."""
    
    # Initialize output_grid as a copy of input_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through all pixels to find green pixels
    for row in range(rows):
        for col in range(cols):
            if input_grid[row, col] == 3:  # Check if it's green
                # Count adjacent green pixels
                orthogonal_count = count_adjacent(input_grid, row, col, 3)
                diagonal_count = count_adjacent(input_grid, row, col, 3, True)
                # Check if it's surrounded by green pixels
                if orthogonal_count == 4 and diagonal_count in [4,5,6,7,8]:
                    output_grid[row, col] = 4  # Change to yellow

    return output_grid
```
