"""
1.  **Count Non-Zero Pixels:** Count the number of non-zero pixels in the input grid. This count determines the side length of the square output grid.
2.  **Create Output Grid:** Create a square output grid with the side from step 1.
3. **Identify interior color.** Count the pixels of each color, and eliminate 0 (background) and 2 (border).
4.  **Create Border:** Fill the outermost rows and columns of the output grid with red (color code 2).
5. **Determine Interior Shape.** Determine the dimensions of the interior shape to be created.
    - count the occurences of each color, excluding 0 and 2
6.  **Fill Interior:** Fill the interior of the output grid (excluding the border created in step 3) with copies of the input object of the identified color in the specified grid locations. The filled object dimensions are determined by counting.
"""

import numpy as np

def get_interior_color_and_count(grid):
    # Count pixels of each color, excluding 0 and 2
    color_counts = {}
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            color = grid[row, col]
            if color != 0 and color != 2:
                if color not in color_counts:
                    color_counts[color] = 0
                color_counts[color] += 1
    
    # Find the interior color and count (assuming only one interior color)
    interior_color = -1
    interior_count = 0
    for color, count in color_counts.items():
        interior_color = color
        interior_count = count
        break  # Assume only one interior color, take the first.

    return interior_color, interior_count
    

def transform(input_grid):
    # Count non-zero pixels to determine output grid size
    non_zero_count = np.count_nonzero(input_grid)
    output_size = non_zero_count
    
    # Create output grid
    output_grid = np.zeros((output_size, output_size), dtype=int)

    # Create border
    output_grid[0, :] = 2
    output_grid[-1, :] = 2
    output_grid[:, 0] = 2
    output_grid[:, -1] = 2

    # identify interior color and count
    interior_color, interior_count = get_interior_color_and_count(input_grid)

    # Fill Interior (if there is an interior color and count is less than the total)
    if interior_color != -1:
        # simple fill
        for row in range(1,output_size-1):
            for col in range(1,output_size-1):
                output_grid[row,col] = interior_color

    return output_grid