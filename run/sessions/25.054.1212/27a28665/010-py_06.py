"""
The transformation rule involves counting the number of non-overlapping 2x2 squares of any color within the input grid and outputting this count as a single integer. The output grid is always 1x1.
"""

import numpy as np

def find_2x2_squares(grid):
    """
    Finds all non-overlapping 2x2 squares of any color in a grid.

    Args:
        grid: A 2D numpy array representing the input grid.

    Returns:
        An integer representing the number of 2x2 squares.
    """
    squares_count = 0
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)  # Keep track of visited cells

    for i in range(rows - 1):
        for j in range(cols - 1):
            if not visited[i, j]:  # Check if the top-left cell has been visited
                if (grid[i, j] == grid[i + 1, j] and
                    grid[i, j] == grid[i, j + 1] and
                    grid[i, j] == grid[i + 1, j + 1]):
                    squares_count += 1
                    # Mark the entire 2x2 square as visited
                    visited[i:i+2, j:j+2] = True
    return squares_count

def transform(input_grid):
    """
    Transforms the input grid according to the rule: count non-overlapping 2x2 squares.
    """
    # Convert the input grid to a NumPy array
    grid = np.array(input_grid)

    # Find and count non-overlapping 2x2 squares of any color
    count = find_2x2_squares(grid)

    # Create a 1x1 output grid with the count
    output_grid = np.array([[count]])

    return output_grid.tolist()