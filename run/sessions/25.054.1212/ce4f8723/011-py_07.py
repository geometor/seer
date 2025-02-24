"""
1.  **Identify the blue object:** Find the contiguous block of blue (color 1) pixels in the input grid, starting from the top-left corner. Other blue pixels that are not part of this initial contiguous block should be ignored.
2.  **Change color:** Change all pixels within this identified object from blue (1) to green (3).
3.  **Form rectangle:** Create a rectangular shape. The height and width are determined by the bounding box of input blue pixels. The dimensions are determined by adding the number of 0 and 1 value pixels in the input grid, then taking the square root of the sum.
4. **Other colors and pixels:** All the other parts of the input grid are completely discarded.

The input grid is cropped to be the smallest rectangle that contains all the initially detected blue object and surrounding 0-value pixels. This cropped grid is the output, with all of the original blue pixels colored green.
"""

import numpy as np

def find_top_left_object(grid, color):
    # Find the top-left pixel of the specified color
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color:
                return (r, c)
    return None

def get_contiguous_block(grid, start_row, start_col, color):
    # Use a flood-fill algorithm to find contiguous block
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    pixels = []
    stack = [(start_row, start_col)]

    while stack:
        r, c = stack.pop()
        if (0 <= r < rows and 0 <= c < cols and
                grid[r, c] == color and not visited[r, c]):
            visited[r, c] = True
            pixels.append((r, c))
            stack.extend([(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)])
    return pixels

def get_bounding_box(pixels):
    # Find the min and max row and col to define the bounding box
    min_row = min(pixels, key=lambda p: p[0])[0]
    max_row = max(pixels, key=lambda p: p[0])[0]
    min_col = min(pixels, key=lambda p: p[1])[1]
    max_col = max(pixels, key=lambda p: p[1])[1]
    return min_row, max_row, min_col, max_col

def transform(input_grid):
    input_grid = np.array(input_grid)
    # Find the top-left blue object
    start_coords = find_top_left_object(input_grid, 1)
    if start_coords is None:
        return np.array([]) # Return empty if no blue object
    
    blue_object_pixels = get_contiguous_block(input_grid, start_coords[0], start_coords[1], 1)

    # Find bounding box for cropping
    min_row, max_row, min_col, max_col = get_bounding_box(blue_object_pixels)

    #Calculate size by counting 0 and 1 pixels
    count_0_and_1 = np.sum((input_grid == 0) | (input_grid == 1))
    output_side_length = int(np.sqrt(count_0_and_1))

    # Create the output grid
    output_grid = np.zeros((output_side_length, output_side_length), dtype=int) #initialize to all black

    # Translate blue object pixels to new coordinates and change color to green
    for r, c in blue_object_pixels:
      if(min_row <= r < min_row + output_side_length and min_col <= c < min_col + output_side_length):
        output_grid[r-min_row, c-min_col] = 3

    return output_grid