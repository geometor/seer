"""
1.  **Find Significant Rows:** Scan the input grid and identify rows containing exactly one non-zero color. Record the row index and the color value for each of these "significant rows."

2.  **Determine Repeating Sections:** Divide the input grid into sections based on the significant rows:
        - Section 1: from input row zero to the first sig row, inclusive
        - Section 2: from the first sig row to the second sig row, inclusive
        - etc.

3.  **Build Output**: Build the output by repeating each section.
    - The output grid should start by repeating section 1.
    - Repeat section 2
    - repeat as necessary to build an output the same size as the input
"""

import numpy as np

def get_significant_rows(grid):
    """Finds rows with exactly one non-zero color."""
    significant_rows = []
    for i, row in enumerate(grid):
        non_zeros = row[row != 0]
        if len(non_zeros) == 1:
            significant_rows.append((i, non_zeros[0]))
    return significant_rows

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)

    # Find significant rows
    significant_rows = get_significant_rows(input_grid)
    
    # Handle no significant rows
    if not significant_rows:
        return output_grid

    # Build the sections
    sections = []
    start_row = 0
    for row_index, _ in significant_rows:
      sections.append(input_grid[start_row:row_index+1])
      start_row = row_index + 1 #start after current sig row
    
    
    # Build Output
    output_row_index = 0
    section_index = 0
    while output_row_index < output_grid.shape[0]:
        current_section = sections[section_index % len(sections)] #cycle through sections
        for row in current_section:
            if output_row_index < output_grid.shape[0]:
              output_grid[output_row_index] = row
              output_row_index += 1
            else:
              break #output full
        section_index+=1 #move to the next section

    return output_grid