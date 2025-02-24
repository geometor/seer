"""
Expands a 3x3 input grid into a 6x6 output grid. Non-zero pixels from the input are propagated diagonally downwards and to the right in the output. The color and relative order of the non-zero input pixels are preserved. Empty cells are filled with 0 (white).
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the diagonal expansion rule.
    """
    input_grid = np.array(input_grid)
    output_grid = np.zeros((6, 6), dtype=int)  # Initialize output grid with zeros

    # 1. Identify Non-Zero Pixels (and their order)
    non_zero_pixels = []
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if input_grid[i, j] != 0:
                non_zero_pixels.append((input_grid[i, j], i, j))

    # 2. Diagonal Expansion
    output_row, output_col = 0, 0
    for pixel_value, _, _ in non_zero_pixels:
        current_row, current_col = output_row, output_col
        while current_row < 6 and current_col < 6:
            output_grid[current_row, current_col] = pixel_value
            current_row += 1
            current_col += 1
        output_row +=1

    return output_grid.tolist()