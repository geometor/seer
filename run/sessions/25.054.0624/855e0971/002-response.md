# 855e0971 • 002 • example_1 • investigate_coder

---
```python
"""
1.  **Identify Bands:** Divide the input grid into three horizontal bands based on color: gray (top), yellow (middle), and azure (bottom).

2.  **Locate White Pixels:** Within the yellow and azure bands, identify the locations of the white (0) pixels.

3.  **Replicate in Yellow Band:** For each white pixel in the *yellow* band, replicate it vertically downwards within the yellow band. Keep the original white pixel, creating copies in every row of the band in the same column.

4. **Replicate in Azure Band:** For each white pixel in the *azure* band, replicate it vertically downwards within the azure band. Keep the original white pixel, creating copies in every row of the band in the same column.

5. **Assemble:** The grey top band does not change. Combine the (unchanged) top grey band, and transformed yellow and azure bands. This forms the output grid.
"""

import numpy as np

def find_bands(grid):
    # Find rows where the color changes
    color_changes = []
    for i in range(1, grid.shape[0]):
        if not np.array_equal(grid[i], grid[i-1]):
            color_changes.append(i)

    # Extract bands based on color changes. Assume at least 3
    bands = []
    bands.append((grid[0,0], 0, color_changes[0])) # (color, start_row, end_row)
    bands.append((grid[color_changes[0], 0], color_changes[0], color_changes[1]))
    bands.append((grid[color_changes[1], 0], color_changes[1], grid.shape[0]))

    return bands

def transform(input_grid):
    # Initialize output grid as a copy of the input
    output_grid = np.copy(input_grid)
    bands = find_bands(input_grid)

    # Iterate through each band
    for color, start_row, end_row in bands:
       #skip the grey pixels
        if color == 5:
            continue

        # Find white pixels in the current band
        white_pixel_cols = []
        for c in range(input_grid.shape[1]):
            if any(input_grid[start_row:end_row, c] == 0):
              if input_grid[start_row:end_row,c][0] == 0:
                white_pixel_cols.append(c)

        # Replicate white pixels vertically within the band
        for col in white_pixel_cols:
            for row in range(start_row, end_row):
                output_grid[row, col] = 0

    return output_grid
```
