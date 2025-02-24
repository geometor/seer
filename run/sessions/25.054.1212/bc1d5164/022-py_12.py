"""
1.  **Identify** all non-white pixels in the input grid.
2.  **Determine** the smallest bounding box that encompasses all non-white pixels.
3. **Create** a new 3x3 output grid, initialized with all white pixels (0).
4.  **Map** the positions of all non-white pixels *relative to the minimal bounding box*. Resize proportionally into the output grid.
5.  **Fill** the corresponding cells in the output grid with the pixel's color, preserving the relative positions within the resized bounding box, and the rest of the pixels as white (value 0).
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
    """Transforms the input grid by extracting non-white pixels and placing them in a 3x3 grid."""

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

    # 4. Map non-white pixel positions to the output grid.
    for row, col, pixel in non_white_pixels:
        # Normalize row and col positions to the range [0, 2]
        norm_row = int(((row - min_row) / (max_row - min_row)) * 2) if (max_row - min_row) > 0 else 0
        norm_col = int(((col - min_col) / (max_col - min_col)) * 2) if (max_col - min_col) > 0 else 0

        # Place the pixel in output
        output_grid[norm_row, norm_col] = pixel

    # 5. Output grid is already filled with 0s (white) where no colored pixels are mapped.
    return output_grid