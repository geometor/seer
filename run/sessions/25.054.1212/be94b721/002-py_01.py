"""
1.  **Identify Target:** Locate the contiguous region of red (value '2') pixels within the input grid.
2.  **Isolate:** Discard all pixels that are not part of the target red region.
3.  **Compress:** Remove all white (value '0') rows and columns that contain *only* white pixels, effectively shrinking the grid to tightly enclose the red region. The remaining red region constitutes the core of the output.
4. The result is the output grid.
"""

import numpy as np

def get_object(grid, color):
    # get the coordinates of all pixels of the specified color.
    coords = np.argwhere(grid == color)
    return coords

def compress_object(grid, object_coords):
    # remove all-white rows and columns that are outside the object
    
    if len(object_coords) == 0:
        return np.zeros((0,0), dtype=int)

    min_row = np.min(object_coords[:, 0])
    max_row = np.max(object_coords[:, 0])
    min_col = np.min(object_coords[:, 1])
    max_col = np.max(object_coords[:, 1])
    
    cropped_grid = grid[min_row:max_row + 1, min_col:max_col + 1]

    return cropped_grid

def transform(input_grid):
    # Convert input grid to a NumPy array
    input_grid = np.array(input_grid)

    # 1. Identify Target (Red Region)
    red_coords = get_object(input_grid, 2)

    # 2. Isolate and 3. Compress (combined for efficiency)
    output_grid = compress_object(input_grid, red_coords)

    return output_grid.tolist()