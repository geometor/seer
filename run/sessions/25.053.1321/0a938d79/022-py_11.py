"""
1.  **Identify Seed Rows:** Find all rows in the input grid that contain at least one non-white pixel. These are the "seed rows."

2.  **Iterate Through Seed Rows (Top to Bottom):**
    * Record the row index of the seed row.

3.  **Process Each Seed Pixel:** For each seed row, iterate through each non-white pixel in the row from left to right:
    *   Record the color and column index of the seed pixel.
    *   Fill the cell at the current row and column with the seed pixel's color.
    *   The colors of each of the seed pixels in the seed rows will fill every
        row of the grid, alternating between each of the colors in order.

4. **Combine Colors**: The output grid will consist of the combined color
   patterns, stacked.
"""

import numpy as np

def get_seed_rows(grid):
    """Identifies rows with at least one non-white pixel and extracts seed pixel information."""
    seed_rows = []
    for row_index, row in enumerate(grid):
        non_white_pixels = []
        for col_index, pixel_value in enumerate(row):
            if pixel_value != 0:
                non_white_pixels.append({"col": col_index, "color": pixel_value})
        if non_white_pixels:
            seed_rows.append({"row_index": row_index, "seed_pixels": non_white_pixels})
    return seed_rows

def transform(input_grid):
    """Transforms the input grid according to the observed rule."""
    output_grid = np.zeros_like(input_grid)
    rows = len(output_grid)
    cols = len(output_grid[0])

    # Find seed rows.
    seed_rows = get_seed_rows(input_grid)

    # Collect all seed pixels from all seed rows
    all_seed_pixels = []
    for seed_row in seed_rows:
        all_seed_pixels.extend([
            (seed_row["row_index"], pixel_info["col"], pixel_info["color"])
            for pixel_info in seed_row["seed_pixels"]
        ])
    
    # Iterate through all rows of the output grid
    for row_index in range(rows):
        # Use the modulo operator to alternate between colors
        pixel_index = row_index % len(all_seed_pixels)
        
        if all_seed_pixels:  # Handle the case where there are no seed pixels
            _, col, color = all_seed_pixels[pixel_index]
            output_grid[row_index, :] = color
            #  Fill based on original column position
            #  The prior code caused an index out of bounds so doing it
            #  this way now
            for i in range(cols):
              if i == col:
                output_grid[row_index,i] = color
              elif i < col:
                output_grid[row_index,i] = 0 #color
              else:
                output_grid[row_index,i] = color

    return output_grid