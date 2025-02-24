"""
1. **Identify Corners:** Locate all red pixels (value 2) in the input grid that exist in the corners of any rectangle which has opposite corner also red.
2. **Find Bounding Box**: Select the smallest 3x3 box which contains red in its corners.

3.  **Construct Output:** Create a 3x3 output grid. Fill with contents extracted from the 3x3 box in the original image.
"""

import numpy as np

def find_red_corners(input_grid):
    red_pixels = []
    rows, cols = input_grid.shape
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 2:
                red_pixels.append((r, c))
    return red_pixels

def extract_subgrid(input_grid, red_pixels):

    if len(red_pixels) < 2:
       return None #not enough red
    
    min_row = min(r for r, c in red_pixels)
    max_row = max(r for r, c in red_pixels)
    min_col = min(c for r, c in red_pixels)
    max_col = max(c for r, c in red_pixels)

    output_grid = input_grid[min_row:min_row + 3, min_col: min_col+3].copy()  # Extract 3x3 subgrid
    
    return output_grid



def transform(input_grid):
    """
    Transforms the input grid to the output grid based on the observed rule.
    """
    # Convert input to numpy array
    input_grid = np.array(input_grid)

    # Find red pixels
    red_pixels = find_red_corners(input_grid)

    # extract 3x3 box
    output_grid = extract_subgrid(input_grid, red_pixels)
    if output_grid is None:
       return input_grid.tolist() #handle edge case
    
    return output_grid.tolist()