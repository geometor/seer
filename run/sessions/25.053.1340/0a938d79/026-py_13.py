"""
1.  **Identify Key Rows:** Scan the input grid row by row. Identify rows that contain *exactly one* non-zero pixel. Note the color of that pixel and the row index.

2.  **Replicate and Insert:** For each identified row:
    *   Create multiple copies of a new row, where *all* pixels in the new row are of the color found in the original, key, row.
    *   The number of replicated rows should match the height of the original image.
    *  Insert the new replicated rows in blocks maintaining the order they were found in the original input.

3. **Assemble output:** The result of inserting the replicated rows is the final output grid.
"""

import numpy as np

def _find_key_rows(grid):
    """Finds rows with exactly one non-zero pixel and returns their indices and colors."""
    key_rows = []
    for i, row in enumerate(grid):
        non_zero_pixels = [x for x in row if x != 0]
        if len(non_zero_pixels) == 1:
            key_rows.append((i, non_zero_pixels[0]))
    return key_rows

def _replicate_row(color, width, count):
    """Creates multiple ('count') copies of a row filled with the given color."""
    return [[color] * width for _ in range(count)]
    

def transform(input_grid):
    """Transforms the input grid according to the described rule."""

    input_grid = np.array(input_grid)
    height, width = input_grid.shape
    output_grid = []

    # Find key rows (rows with exactly one non-zero pixel).
    key_rows = _find_key_rows(input_grid)

    # For each key row, replicate and insert.
    for _, color in key_rows:
        replicated_rows = _replicate_row(color, width, height)
        output_grid.extend(replicated_rows)
    
    return np.array(output_grid)