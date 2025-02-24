# bc1d5164 • 020 • example_4 • investigate_coder

---
```python
"""
1.  **Identify** all pixels with the color yellow (value 4) in the input grid.
2.  **Determine** the bounding box that encompasses all yellow pixels. Or, determine maximum and minimum row/column.
3. **Create** a new output grid with dimensions that, relatively speaking, capture the yellow pixels in a minimal bounding box.
4. **Map** the positions of the identified yellow pixels from the input grid to the output grid. Preserve position *relative to the minimal bounding box.*
5.  **Fill** all other cells in the output grid with the color white (value 0). Essentially, the bounding box created in (2.) is fit into 3x3 grid.
"""

import numpy as np

def get_yellow_pixels(grid):
    # find coordinates of yellow pixels
    yellow_pixels = []
    for row_index, row in enumerate(grid):
        for col_index, pixel in enumerate(row):
            if pixel == 4:
                yellow_pixels.append((row_index, col_index))
    return yellow_pixels

def transform(input_grid):
    """Transforms the input grid by extracting yellow pixels and placing them in a 3x3 grid."""

    # Convert input to numpy array
    input_grid = np.array(input_grid)
    
    # 1. Identify all yellow pixels.
    yellow_pixels = get_yellow_pixels(input_grid)

    # 2. Determine the bounding box (min/max row/col).
    if not yellow_pixels:  # Handle the case where there are no yellow pixels
        return np.zeros((3, 3), dtype=int)

    min_row, min_col = yellow_pixels[0]
    max_row, max_col = yellow_pixels[0]

    for row, col in yellow_pixels:
        min_row = min(min_row, row)
        max_row = max(max_row, row)
        min_col = min(min_col, col)
        max_col = max(max_col, col)

    # 3. Create a 3x3 output grid initialized with white (0).
    output_grid = np.zeros((3, 3), dtype=int)

    # 4. Map yellow pixel positions to the output grid.
    for row, col in yellow_pixels:
        # Normalize row and col positions to the range [0, 2]
        norm_row = int(((row - min_row) / (max_row - min_row)) * 2) if (max_row - min_row) > 0 else 0
        norm_col = int(((col - min_col) / (max_col - min_col)) * 2) if (max_col - min_col) > 0 else 0

        # Place the yellow pixel in output
        output_grid[norm_row, norm_col] = 4

    # 5. Output grid is already filled with 0s (white).
    return output_grid
```
