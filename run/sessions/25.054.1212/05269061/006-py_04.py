"""
1.  **Identify Non-Zero Pixels:** Extract all pixels from the input grid that have a value other than 0 (black).

2.  **Find the Smallest Mirrored Unit:** Determine the smallest rectangular block (the "pattern unit") within the *input grid's non-zero pixels* that can be mirrored both horizontally and vertically to reproduce all non-zero pixel locations in the *output grid*. This pattern unit does *not* necessarily start at the top-left corner and *does not* include any zero-value pixels.

3.  **Replicate and Mirror:** Create an output grid of the same dimensions as the *input* grid. For each cell in the output grid:

    *   Calculate the corresponding row and column indices within the pattern unit using the modulo operator (`%`) with the pattern unit's dimensions.
    *   Determine if the current output cell falls within a mirrored section. Divide the output row and column indices by the pattern unit dimensions (integer division). If the result is odd, the corresponding dimension (row or column) is mirrored.
    *   If a dimension is mirrored, invert the pattern unit index for that dimension by subtracting it from the pattern unit dimension minus 1.
    *   Copy the pixel value from the pattern unit at the calculated indices to the output grid cell.
    *   If a calculated index in the pattern unit has value 0, use corresponding value from input.

4.  **Output grid size:** the output is always the same size as the input
"""

import numpy as np
from typing import List, Tuple

def find_pattern_unit(input_grid: List[List[int]]) -> Tuple[List[List[int]], Tuple[int, int]]:
    """Finds the smallest mirrored pattern unit within non-zero pixels."""
    input_array = np.array(input_grid)
    rows, cols = input_array.shape
    non_zero_pixels = [(r, c, input_array[r, c]) for r in range(rows) for c in range(cols) if input_array[r, c] != 0]

    if not non_zero_pixels:
        return input_grid, (rows,cols)  # Return original grid if no non-zero pixels

    # Iterate through possible pattern unit sizes
    for height in range(1, rows + 1):
        for width in range(1, cols + 1):
            for start_row in range(rows - height + 1):
                for start_col in range(cols - width + 1):
                    
                    pattern_unit = input_array[start_row:start_row+height, start_col:start_col+width]
                    
                    # check that all values in pattern unit that are zero, are also zero in the input
                    valid_start = True
                    for r in range(height):
                        for c in range(width):
                            if pattern_unit[r,c] == 0 and input_array[start_row+r,start_col+c] != 0:
                                valid_start = False
                                break
                        if not valid_start:
                            break
                    if not valid_start:
                        continue
                    
                    can_reproduce = True
                    for r, c, val in non_zero_pixels:
                        
                        # calculate indices in the core pattern unit
                        unit_row = (r - start_row) % height
                        unit_col = (c - start_col) % width
                        
                        # determine mirroring
                        row_block = (r-start_row) // height
                        col_block = (c-start_col) // width

                        if row_block % 2 == 1:
                            unit_row = height - 1 - unit_row
                        if col_block % 2 == 1:
                            unit_col = width - 1 - unit_col

                        # compare with pattern, if pattern unit would have
                        # value
                        if pattern_unit[unit_row, unit_col] != 0 and pattern_unit[unit_row, unit_col] != val :
                            can_reproduce = False
                            break

                    if can_reproduce:
                        return pattern_unit.tolist(), (height, width)

    return input_grid,(rows,cols)  # Fallback: Return original grid

def transform(input_grid: List[List[int]]) -> List[List[int]]:
    """Transforms the input grid by replicating a mirrored pattern unit."""

    # Find pattern unit and its dimensions
    pattern_unit, (height, width) = find_pattern_unit(input_grid)
    pattern_unit_array = np.array(pattern_unit)

    # initialize output as copy of input
    output_grid = [row[:] for row in input_grid]

    # Iterate through each cell of the output grid
    for r in range(len(input_grid)):
        for c in range(len(input_grid[0])):
            
            start_row = 0
            start_col = 0

            # Calculate indices in the pattern unit
            unit_row = (r-start_row) % height
            unit_col = (c-start_col) % width

            # Determine mirroring
            row_block = (r - start_row) // height
            col_block = (c - start_col) // width

            if row_block % 2 == 1:
                unit_row = height - 1 - unit_row
            if col_block % 2 == 1:
                unit_col = width - 1 - unit_col

            # Copy value from pattern unit to output
            if pattern_unit_array[unit_row, unit_col] != 0:
              output_grid[r][c] = pattern_unit_array[unit_row, unit_col]

    return output_grid