"""
1.  **Identify Non-White Pixels:** Locate all pixels in the input grid that are not white (color 0).
2.  **Bounding Box:** Determine the smallest rectangular bounding box that encompasses all identified non-white pixels.
3.  **Create Output Grid:** Initialize a 3x3 output grid filled with white pixels (0).
4.  **Proportional Mapping**: For each non-white pixel in the input:
    *   Calculate its position *relative* to the bounding box's top-left corner, and its width and height. Represent these as normalized row and column values between 0.0 and 1.0. For example, a pixel in the middle of the box will have row and column around 0.5.
    *   Multiply the normalized row and column by 2.
    *   Round the results to the *nearest* integer (0, 1, or 2). This gives the target row and column within the 3x3 output grid.
    *   Place the input pixel's color into the calculated position in the output grid.
5. **Output:** Return the 3 x 3 output grid.
"""

import numpy as np

def get_non_white_pixels(grid):
    # find coordinates of non-white pixels
    non_white_pixels = []
    for row_index, row in enumerate(grid):
        for col_index, pixel in enumerate(row):
            if pixel != 0:
                non_white_pixels.append((row_index, col_index, pixel))
    return non_white_pixels

def transform(input_grid):
    # Convert input to numpy array
    input_grid = np.array(input_grid)
    
    # 1. Identify all non-white pixels.
    non_white_pixels = get_non_white_pixels(input_grid)

    # 2. Determine the bounding box (min/max row/col).
    if not non_white_pixels:  # Handle the case where there are no non-white pixels
        return np.zeros((3, 3), dtype=int)

    min_row, min_col, _ = non_white_pixels[0]
    max_row, max_col, _ = non_white_pixels[0]

    for row, col, _ in non_white_pixels:
        min_row = min(min_row, row)
        max_row = max(max_row, row)
        min_col = min(min_col, col)
        max_col = max(max_col, col)

    # 3. Create a 3x3 output grid initialized with white (0).
    output_grid = np.zeros((3, 3), dtype=int)

    # 4. Map non-white pixel positions to the output grid proportionally.
    for row, col, pixel in non_white_pixels:
        # Normalize row and col positions to the range [0.0, 1.0]
        norm_row = ((row - min_row) / (max_row - min_row)) if (max_row - min_row) > 0 else 0.0
        norm_col = ((col - min_col) / (max_col - min_col)) if (max_col - min_col) > 0 else 0.0

        # Multiply by 2 and round to the nearest integer.
        output_row = round(norm_row * 2)
        output_col = round(norm_col * 2)
        
        # Ensure output row and col are within bounds
        output_row = max(0, min(output_row, 2))
        output_col = max(0, min(output_col, 2))

        # Place the pixel in output
        output_grid[output_row, output_col] = pixel

    # 5. Output grid is already filled with 0s (white) where no colored pixels are mapped.
    return output_grid