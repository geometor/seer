"""
1.  **Identify Seed Rows:** Examine the input grid and identify "seed rows," which are rows containing at least one non-white pixel.
2.  **Create Color Sequence For Each Seed Row**: Scan each seed row from left to right. For each non-white pixel encountered, record its color. The ordered sequence of colors becomes the color sequence for that seed row.
3.  **Stack Seed Rows**: Repeat the stack of seed rows until the height of the stack equals the height of the input grid.
"""

import numpy as np

def get_seed_rows(grid):
    """Identifies rows with at least one non-white pixel and extracts their color sequences."""
    seed_rows = []
    for row_index, row in enumerate(grid):
        color_sequence = []
        for pixel_value in row:
            if pixel_value != 0:
                color_sequence.append(pixel_value)
        if color_sequence:
            seed_rows.append({"row_index": row_index, "color_sequence": color_sequence})
    return seed_rows

def transform(input_grid):
    """Transforms the input grid by stacking seed rows with color sequences."""
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    rows = len(output_grid)
    cols = len(output_grid[0])

    # Find seed rows and their color sequences.
    seed_rows = get_seed_rows(input_grid)

    # Handle the case where there are no seed rows.
    if not seed_rows:
        return output_grid

    # Create stacked seed rows.
    stacked_rows = []
    for seed_row in seed_rows:
      row = np.array(seed_row["color_sequence"])
      full_row = np.tile(row, cols // len(row) + 1)[:cols]  # Repeat to fill width
      stacked_rows.append(full_row)
    
    # Stack and repeat
    num_repeats = rows // len(stacked_rows)
    remainder = rows % len(stacked_rows)
    
    final_stack = []
    
    for _ in range(num_repeats):
      for row in stacked_rows:
        final_stack.append(row)
    for i in range(remainder):
      final_stack.append(stacked_rows[i])

    for i in range(len(final_stack)):
      output_grid[i,:] = final_stack[i]
    
    return output_grid