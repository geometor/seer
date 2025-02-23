# 855e0971 • 004 • refine_coder

---
```python
"""
1.  **Identify Bands:** Divide the input grid into horizontal bands based on color changes. The number of bands and their colors can vary.

2.  **Find White Pixel Columns:** Iterate through all rows *except* those belonging to the top band (which often remains unchanged, though its color isn't consistently grey). For each row, identify the *columns* that contain white (0) pixels.

3.  **Replicate in Non-Top Bands:** For *every* row that is *not* in the top band, set the pixel to white (0) in *all* columns identified in step 2.

4.  **Assemble Output:** Combine all rows. The final output will consist of the (potentially unchanged) top band, followed by the modified lower bands where the white pixels have been replicated downwards within their respective column across all non-grey band rows.
"""

import numpy as np

def transform(input_grid):
    # Initialize output grid as a copy of the input
    output_grid = np.copy(input_grid)
    
    # 1. Identify Bands (implicitly done by iterating rows)
    
    # 2. Find White Pixel Columns (in non-top bands)
    white_pixel_columns = set()
    for r in range(input_grid.shape[0]):
        for c in range(input_grid.shape[1]):
            if input_grid[r, c] == 0:
                white_pixel_columns.add(c)

    # Find the first band
    first_band_end_row = 0
    for i in range(1, input_grid.shape[0]):
        if not np.array_equal(input_grid[i], input_grid[0]):
            first_band_end_row = i
            break
    else: #the entire input grid is a single band
        first_band_end_row = input_grid.shape[0]
    
    # 3. Replicate in Non-Top Bands
    for r in range(first_band_end_row, output_grid.shape[0]):
        for c in white_pixel_columns:
            output_grid[r, c] = 0
            
    #Special Case: If the entire input grid is one band, and we have any white pixels.
    if first_band_end_row == input_grid.shape[0] and len(white_pixel_columns) > 0:
        for r in range(input_grid.shape[0]):
            for c in white_pixel_columns:
               if input_grid[r,c] != 0:
                   first_non_white_row = r
                   break
            else:
               continue
            break
        for r in range(first_non_white_row, output_grid.shape[0]):
            for c in white_pixel_columns:
                output_grid[r,c] = 0

    return output_grid
```
