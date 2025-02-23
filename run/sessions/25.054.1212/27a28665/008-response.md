# 27a28665 • 008 • example_2 • investigate_coder

---
```python
"""
The transformation rule involves counting the number of 2x2 squares of azure (8) pixels within the input grid and outputting this count as a single integer with a red (2) background. If no such squares exist, the output is 0.
"""

import numpy as np

def find_2x2_squares(grid, target_color):
    """
    Finds all 2x2 squares of a target color in a grid.

    Args:
        grid: A 2D numpy array representing the input grid.
        target_color: The color of the 2x2 square to search for.

    Returns:
        A list of tuples, where each tuple represents the top-left coordinates
        of a 2x2 square of the target color.
    """    
    squares = []
    rows, cols = grid.shape
    for i in range(rows - 1):
        for j in range(cols - 1):
            if (grid[i, j] == target_color and
                grid[i + 1, j] == target_color and
                grid[i, j + 1] == target_color and
                grid[i + 1, j + 1] == target_color):
                squares.append((i, j))
    return squares

def transform(input_grid):
    """
    Transforms the input grid according to the rule: count 2x2 azure squares.
    """
    # Convert the input grid to a NumPy array
    grid = np.array(input_grid)

    # Find 2x2 squares of azure (8)
    azure_squares = find_2x2_squares(grid, 8)

    # Get the count of 2x2 azure squares
    count = len(azure_squares)

    # if there is a non zero count, return the number as the only array element,
    # with background = 2
    output_grid = np.array([[count]])

    return output_grid.tolist()
```
