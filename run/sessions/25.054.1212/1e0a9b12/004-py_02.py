"""
1.  **Identify Non-zero Pixels:** Locate all pixels within the input grid that have a value other than 0.
2.  **Preserve Row-wise Order:** Maintain the original left-to-right order of these non-zero pixels *as they appear within each row*.
3.  **Move to Bottom:** Move the identified non-zero pixels to the bottom-most available rows of the output grid.
4.  **Row-wise Filling:** When placing pixels in the output grid, prioritize filling the lowest available row. Within that row, place pixels from the same input row in their original order. If pixels from a higher input row need to be placed, and there are still empty positions on rows that had non-zero pixels on lower rows of input, fill the lowest of available rows.
5.  **Fill Remaining:** Fill any remaining cells in the output grid (those not occupied by moved non-zero pixels) with 0.
"""

import numpy as np

def transform(input_grid):
    """
    Transforms the input grid by moving all non-zero pixels to the bottom,
    preserving their original row-wise order, and filling the remaining
    cells with zeros.
    """
    rows, cols = input_grid.shape
    output_grid = np.zeros_like(input_grid)
    non_zero_pixels_by_row = [[] for _ in range(rows)]

    # 1. Identify and store non-zero pixels, preserving row and original order.
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] != 0:
                non_zero_pixels_by_row[r].append((input_grid[r, c], c))

    # 2 & 3. Move to the bottom, maintaining row-wise order.
    output_row = rows - 1
    for row_pixels in reversed(non_zero_pixels_by_row):  # Iterate through original rows from bottom to top
        output_col_indices = [0] * rows # keeps track of where we are in the output for each row
        if not row_pixels:
            continue
        
        for pixel_value, original_col in sorted(row_pixels, key=lambda x: x[1]):
            #find output_col for the current output_row
            output_col = output_col_indices[output_row]
            while output_col < cols and output_grid[output_row, output_col] != 0:
              output_col += 1            
            
            if output_col < cols:            
                output_grid[output_row, output_col] = pixel_value
                output_col_indices[output_row] = output_col + 1 #increment for next time we use this output row
            else:
                #find the next available spot in higher rows
                curr_output_row = output_row - 1
                while curr_output_row >= 0:
                    output_col = output_col_indices[curr_output_row]
                    while output_col < cols and output_grid[curr_output_row, output_col] != 0:
                        output_col += 1
                    
                    if output_col < cols:
                        output_grid[curr_output_row, output_col] = pixel_value
                        output_col_indices[curr_output_row] = output_col + 1
                        break
                    else:
                      curr_output_row -= 1

        output_row -= 1
        if output_row < 0:
            break
        

    # 5. Fill the remaining (already done by initializing output_grid with zeros).
    return output_grid