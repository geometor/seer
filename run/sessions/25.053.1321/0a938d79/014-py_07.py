"""
1. Identify Seed Rows: Iterate through each row of the input grid. A row is considered a "seed row" if it contains exactly one non-zero (colored) pixel.

2. Store Seed Information: For each seed row, store the row index, the color of the single pixel, and the column index of that pixel.

3. Construct Output: Create a new output grid of the same dimensions as the input grid. Fill the output grid as follows:
    *   Iterate through the rows of the output grid.
    *   Maintain relative column positions of colored pixels from seed rows.
        *   For each seed row, in the output, from the stored seed color's column position to the end of the row, fill the cells with the seed row's color.
        *   Fill the regions between colored pixels by repeating the sequence of colored pixels in the seed rows.

4. If there are rows that are not "filled" after processing all seed rows (like blank rows), maintain those as zero.
"""

import numpy as np

def find_seed_rows(grid):
    """
    Identifies rows with exactly one non-zero pixel and returns their information.
    """
    seed_rows = []
    for i, row in enumerate(grid):
        non_zero_indices = np.nonzero(row)[0]
        if len(non_zero_indices) == 1:
            seed_rows.append({
                "row_index": i,
                "color": row[non_zero_indices[0]],
                "column_index": non_zero_indices[0]
            })
    return seed_rows

def transform(input_grid):
    """
    Transforms the input grid based on seed rows (rows with a single colored pixel).
    """
    input_grid = np.array(input_grid)  # Ensure input is a NumPy array
    output_grid = np.zeros_like(input_grid)
    seed_rows = find_seed_rows(input_grid)

    # Construct output based on seed row information
    for seed_info in seed_rows:
        row_index = seed_info["row_index"]
        color = seed_info["color"]
        column_index = seed_info["column_index"]
        output_grid[row_index, column_index:] = color

    # fill the regions between the colored pixels
    if (len(seed_rows) > 1):
        num_rows, num_cols = output_grid.shape

        # create the alternating pattern of seed colors
        seed_colors = [sr['color'] for sr in seed_rows]
        seed_cols = [sr['column_index'] for sr in seed_rows]

        for r_idx in range(num_rows):
            if any(output_grid[r_idx]): # if any color in the row
                continue

            # cycle through the color/column pairs from seed_rows
            c_idx = 0
            while c_idx < num_cols:
                for sr_idx in range(len(seed_rows)):
                    start = seed_cols[sr_idx]
                    if c_idx >= start and c_idx < num_cols:
                      output_grid[r_idx, c_idx] = seed_colors[sr_idx]
                    c_idx += 1


    return output_grid