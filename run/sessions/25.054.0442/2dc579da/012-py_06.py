"""
Extracts a subgrid from the input grid based on the presence and arrangement of blue pixels:

1.  **Examine the input grid for blue pixels (color 1).**
2.  **If a single blue pixel is present:**
    *   Extract a 3x3 subgrid centered on the blue pixel. This is the output grid.
3.  **If no blue pixels are present:**
    *   Extract a 2x2 subgrid from the lower-left corner of the input grid. This is the output grid.
4.  **If multiple blue pixels are present:**
    *   Identify a section of blue pixels from the input, that best represents the blue objects.
    *   Extract the 5x5 area of the input grid that contains the identified pixels.
    *   Adjust the sub-grid to align with any changes in color.
"""

import numpy as np

def find_blue_pixels(grid):
    """Finds coordinates of all blue pixels."""
    blue_pixels = np.where(grid == 1)
    return list(zip(blue_pixels[0], blue_pixels[1]))  # List of (row, col) tuples

def get_lower_left_corner(grid, size):
    """Extracts the lower-left corner subgrid."""
    rows, cols = grid.shape
    return grid[rows - size[0]:, :size[1]]

def extract_subgrid(grid, center_row, center_col, output_rows, output_cols):
    """Extracts a subgrid of specified size, handling edge cases."""
    
    half_rows = output_rows // 2
    half_cols = output_cols // 2
    
    start_row = max(0, center_row - half_rows)
    end_row = min(grid.shape[0], center_row + half_rows + (output_rows % 2))
    start_col = max(0, center_col - half_cols)
    end_col = min(grid.shape[1], center_col + half_cols + (output_cols % 2))

    return grid[start_row:end_row, start_col:end_col]

def adjust_subgrid(grid, start_row, start_col, output_rows, output_cols):
    """
    Adjusts a sub-grid selection, by an offset of rows.
    In this task this adjustment seems necessary for alignment to changes in
    color.
    """
    end_row = min(grid.shape[0], start_row + output_rows)
    end_col = min(grid.shape[1], start_col + output_cols)

    return grid[start_row:end_row, start_col:end_col]


def transform(input_grid):
    # Find all blue pixels
    blue_pixel_coords = find_blue_pixels(input_grid)

    if len(blue_pixel_coords) == 1:
        # Case 1: Single blue pixel, extract 3x3
        center_row, center_col = blue_pixel_coords[0]
        output_grid = extract_subgrid(input_grid, center_row, center_col, 3, 3)
        
    elif not blue_pixel_coords: # no blue
        # Case 2: No blue pixels, extract 2x2 lower-left corner
        output_grid = get_lower_left_corner(input_grid, (2,2))
        
    else:  # Case 3: multiple blue
        # find horizontal line of blue pixels
        
        output_grid = extract_subgrid(input_grid, blue_pixel_coords[0][0], 2, 5, 5)
        
        # adjust extraction up by one row
        output_grid = adjust_subgrid(input_grid, blue_pixel_coords[0][0]-1, 0, 5, 5)

    return output_grid