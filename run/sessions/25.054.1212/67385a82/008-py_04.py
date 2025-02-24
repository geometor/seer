"""
Identifies groups of horizontally adjacent green pixels and changes them to azure.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by changing horizontally contiguous green pixels to azure.
    
    Args:
        input_grid (list of lists): The input grid represented as a list of lists.
    
    Returns:
        list of lists: The transformed grid.
    """
    output_grid = [row[:] for row in input_grid]  # Create a copy to avoid modifying the original
    rows = len(input_grid)
    cols = len(input_grid[0]) if rows > 0 else 0

    for r in range(rows):
        for c in range(cols):
            # Check if the current pixel is green
            if input_grid[r][c] == 3:
                # Check for horizontal adjacency to other green pixels
                if (c > 0 and input_grid[r][c-1] == 3) or (c < cols - 1 and input_grid[r][c+1] == 3):
                    output_grid[r][c] = 8  # Change to azure

    return output_grid