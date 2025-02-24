"""
1.  **Copy Input:** Create a copy of the input grid as the output grid.
2.  **Identify Repeating Section:** Find the index of the first row that contains the value 0.  The "repeating section" consists of all rows *before* this index.
3.  **Iterate through Remaining Rows:** Iterate through each subsequent row of the *output* grid, *starting* from the first row index that contained a 0 in the input grid.
4. **Sequential Replacement**  Fill the remaining rows by repeatedly copying *all* rows from repeating section. The row index should be calculated using the modulo operator against length of the repeating section.
5.  **Output:** Return the modified output grid.
"""

import numpy as np

def transform(input_grid):
    # Copy input grid to output grid
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Identify Repeating Section
    repeating_section_end = 0
    for i in range(rows):
        if 0 in input_grid[i]:
            repeating_section_end = i
            break
    else:  # No 0 found in any row, so no repeating section (or repeat entire grid, which is the same in this case)
        return output_grid
    
    repeating_section = input_grid[:repeating_section_end]
    num_repeating_rows = repeating_section.shape[0]

    # Iterate through remaining rows and perform sequential replacement.
    for i in range(repeating_section_end, rows):
        repeat_row_index = (i - repeating_section_end) % num_repeating_rows
        output_grid[i] = repeating_section[repeat_row_index]
        
    return output_grid