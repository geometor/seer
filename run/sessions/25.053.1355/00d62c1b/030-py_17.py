"""
1. Identify Connected Green Regions: Find all connected components (regions) of green (3) pixels in the input grid. Adjacency includes diagonals.

2. Define and Find Internal Pixels: For *each* connected green region:
    *   A green pixel is considered "internal" if *all* of its eight neighbors (up, down, left, right, and the four diagonals) are also green.

3. Transform: Change the color of all identified "internal" green pixels from green (3) to yellow (4).

4. Preserve Other Pixels: All other pixels (white and any green pixels that are *not* identified as "internal") retain their original color values.

5. Output: The output grid has the same dimensions as the input grid, with the color changes applied according to steps 2 and 3.
"""

import numpy as np
from scipy.ndimage import label, generate_binary_structure

def get_all_neighbors(grid, row, col):
    """
    Returns a list of all neighbors (including diagonals) of a given cell.
    """
    rows, cols = grid.shape
    neighbors = []
    
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue  # Skip the cell itself
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols:
                neighbors.append((r, c))
                
    return neighbors

def find_internal_pixels(grid, labeled_grid, region_label):
    """
    Identifies internal pixels within a specific labeled region.
    """
    internal_pixels = []
    rows, cols = grid.shape
    for row in range(rows):
        for col in range(cols):
            if labeled_grid[row, col] == region_label:
                neighbors = get_all_neighbors(grid, row, col)
                all_neighbors_green = True
                for r, c in neighbors:
                    if grid[r, c] != 3:
                        all_neighbors_green = False
                        break
                if all_neighbors_green:
                    internal_pixels.append((row, col))
    return internal_pixels

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Identify Connected Green Regions
    green_pixels = (input_grid == 3).astype(int)
    # Use 8-connectivity (including diagonals)
    s = generate_binary_structure(2, 2)
    labeled_grid, num_labels = label(green_pixels, structure=s)

    # Find and Transform Internal Pixels
    for region_label in range(1, num_labels + 1):  # Iterate through each region
        internal_pixels = find_internal_pixels(input_grid, labeled_grid, region_label)
        for r, c in internal_pixels:
            output_grid[r, c] = 4  # Change to yellow

    return output_grid