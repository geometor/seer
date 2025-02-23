# 0a938d79 • 004 • refine_coder

---
```python
"""
1.  **Identify Key Rows:** Examine each row of the input grid. Identify "key rows" as those containing any non-zero color other than white (0). Record the color and the entire row.
2.  **Iterate and Replicate with alternating pattern** For each key row found, starting at the same row index:
    a. Create an output row of the same dimensions as the input grid.
    b. Fill the created output row with the non-zero color found in the key row.
    3. If another key row is found, add to the output after a number of blank rows.
    4. If a similar pattern of rows repeats, repeat the same output row combination.
3. **Default:** If no key rows are found, return an output grid of the same size, filled with 0.
"""

import numpy as np

def find_key_rows(grid):
    """Finds rows with non-zero values and returns them with their colors and indices."""
    key_rows = []
    for i, row in enumerate(grid):
        non_zero_values = row[row != 0]
        if non_zero_values.size > 0:
            color = non_zero_values[0]  # Assumes only one non-zero color per key row
            key_rows.append({'color': color, 'row': row, 'index': i})
    return key_rows

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # find key rows
    key_rows_info = find_key_rows(input_grid)

    if not key_rows_info:
      return output_grid

    output_row_index = 0
    
    # build the output grid row index
    for i in range(len(key_rows_info)):
      current_key_row_info = key_rows_info[i]
      
      # skip to correct output row index based on discovered key row
      if output_row_index < current_key_row_info['index']:
        output_row_index = current_key_row_info['index']

      if output_row_index < rows: # prevents index out of range
        # fill entire row with color
        output_grid[output_row_index, :] = current_key_row_info['color']
        output_row_index += 1
        
    
    # detect repetition patterns from example 3 and 4:
    if len(key_rows_info) == 2:
      row_index_1 = key_rows_info[0]['index']
      row_index_2 = key_rows_info[1]['index']
      color_1 = key_rows_info[0]['color']
      color_2 = key_rows_info[1]['color']

      blank_rows_between = row_index_2 - row_index_1 -1

      # if there is a consistent space, consider it a repeating element
      if blank_rows_between >= 0:
         pattern = [color_1] + ([0] * blank_rows_between) + [color_2]
         
         pattern_length = len(pattern)
         pattern_start = row_index_1

         while pattern_start + pattern_length <= rows:
            for i in range(pattern_length):
                if pattern_start + i < rows:  # Check to prevent out-of-bounds
                    output_grid[pattern_start+i, :] = pattern[i]
            pattern_start += pattern_length
    return output_grid
```
