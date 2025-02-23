"""
1.  **Identify Colored Rows:** Find all rows in the input grid that contain at least one non-white pixel. Store these row indices.
2.  **Identify Blank Rows:** Find all rows that contain *only* white pixels. Store these row indices.
3. **Expand Colored Rows**: For each colored row, create a full row in which each pixel is set to the color found in the original colored row's non-white pixels.
4. **Alternate Colors**: Process the color pixels in each expanded row. If the input has two colors in a row, alternate them in the output row. If more than two colors, create an alternating sequence.
5.  **Construct Output:** Create the output grid by repeating the block of modified colored rows, including white (blank) rows. The repetition continues until the height of the output grid matches the input.
"""

import numpy as np

def get_colored_rows(grid):
    colored_rows = []
    for i, row in enumerate(grid):
        if any(pixel != 0 for pixel in row):
            colored_rows.append(i)
    return colored_rows

def get_blank_rows(grid):
    blank_rows = []
    for i, row in enumerate(grid):
        if all(pixel == 0 for pixel in row):
            blank_rows.append(i)
    return blank_rows

def expand_colored_rows(colored_rows_indices, input_grid):
    expanded_rows = {}
    for row_index in colored_rows_indices:
      colors = [pixel for pixel in input_grid[row_index] if pixel !=0]
      if len(colors) > 0:
        expanded_rows[row_index] = colors
    return expanded_rows

def alternate_colors(expanded_rows, width):
  
    alternated_rows = {}
    for row_index, colors in expanded_rows.items():
      new_row = []
      for i in range(width):
        new_row.append(colors[i % len(colors)])

      alternated_rows[row_index] = new_row
    return alternated_rows

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros(input_grid.shape, dtype=int)
    input_grid = np.array(input_grid) # ensure numpy array

    # identify colored and blank rows
    colored_rows_indices = get_colored_rows(input_grid)
    blank_rows_indices = get_blank_rows(input_grid)
    
    # Handle edge case of no colored rows
    if not colored_rows_indices:
        return output_grid

    # expand colored rows
    expanded_colored_rows = expand_colored_rows(colored_rows_indices, input_grid)
    
    #alternate the colors in the expanded row
    alternated_colored_rows = alternate_colors(expanded_colored_rows, input_grid.shape[1])

    # construct the output grid
    output_row_index = 0
    
    # create repeating block of color and blank rows
    while output_row_index < input_grid.shape[0]:

      # add color rows
      for row_index in alternated_colored_rows:
        if output_row_index < input_grid.shape[0]:
          output_grid[output_row_index] = alternated_colored_rows[row_index]
          output_row_index += 1

      # add blank rows between color rows
      for _ in blank_rows_indices: # add the same number of blank rows as original
        if output_row_index < input_grid.shape[0]:
          output_row_index += 1 # already all zeros
        else:
          break

    return output_grid