"""
1.  **Iterate through each row of the input grid.**
2.  **Identify background rows:** If a row contains only the color black (0), keep it as is in the output grid.
3.  **Identify repeating fill rows:** If a row contains one color and black(0), fill the whole line with the non-zero color.
4.  **Identify alternating fill rows.** If a row contains multiple non-black(0) colors and black(0), create a repeating sequence of non-zero color values to fill the whole line, preserving the order of appearance.
5.  **Vertical Repetition**: Repeat the fill rows vertically, starting from the first filled row and wrapping around if reaching the last row.
6.  **Output Size**: The output grid has the same dimensions as the input grid.
"""

import numpy as np

def get_row_type(row):
    """Classifies a row as background, fill, or alternating_fill."""
    unique_colors = np.unique(row)
    if len(unique_colors) == 1 and unique_colors[0] == 0:
        return "background"
    elif len(unique_colors) == 2 and 0 in unique_colors:
        return "fill"
    elif 0 in unique_colors:
        return "alternating_fill"
    else:
      return "other"

def fill_row(row, color):
    """Fills an entire row with a single color."""
    return np.full_like(row, color)

def alternating_fill(row):
    """Fills a row with a repeating pattern of its non-zero colors."""
    non_zero_colors = row[row != 0]
    if len(non_zero_colors)==0:
        return row
    
    filled_row = np.zeros_like(row)
    for i in range(len(row)):
        filled_row[i] = non_zero_colors[i % len(non_zero_colors)]
    return filled_row

def transform(input_grid):
    """Transforms the input grid according to the defined rules."""
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape
    
    row_types = []
    filled_rows = []

    # Identify row types and create filled rows where applicable
    for i in range(rows):
        row = input_grid[i]
        row_type = get_row_type(row)
        row_types.append(row_type)

        if row_type == "fill":
            non_zero_color = row[row != 0][0]
            filled_rows.append(fill_row(row, non_zero_color))
        elif row_type == "alternating_fill":
            filled_rows.append(alternating_fill(row))
        else:
            filled_rows.append(None)  # Placeholder for background and other rows

    # Apply vertical repetition
    filled_row_indices = [i for i, row in enumerate(filled_rows) if row is not None]
    if not filled_row_indices: #handle edge case of no non-zero rows
        return output_grid
      
    fill_index = 0
    for i in range(rows):
        if row_types[i] == "background":
            continue  # Keep background rows as they are
        elif row_types[i] == "other":
            continue
        else:
          output_grid[i] = filled_rows[filled_row_indices[fill_index % len(filled_row_indices)]]
          fill_index += 1


    return output_grid