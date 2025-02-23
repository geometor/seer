# 0a938d79 • 004 • refine_coder

---
```python
"""
1.  **Identify Source Rows:** Scan each row of the input grid. A row is a "source row" if it contains at least one non-zero (non-white) pixel.

2.  **Replicate Horizontally:** For each source row, replicate its pattern of non-zero pixels across the *entire* row. Any zero-value pixels between non-zero pixels in the source row should remain zero.  The output for this row will now have solid stripes of color corresponding to the non-zero pixels in the input.

3. **Stack Rows:** Create the output grid by stacking the source rows from top to bottom. If a row between two source rows does not contain any source colors, the row from above is copied down until a new source row is encountered.

4. **Handle Edge Cases** If a source row contains only `0` - all white - then it has no effect.
"""

import numpy as np

def _find_source_rows(grid):
    """Identifies and returns a list of row indices that contain at least one non-zero pixel."""
    source_rows = []
    for i, row in enumerate(grid):
        if any(pixel != 0 for pixel in row):
            source_rows.append(i)
    return source_rows

def _replicate_row_horizontally(row):
    """Replicates the non-zero pixels of a row across the entire row."""
    new_row = np.array(row)  # create a copy to modify
    non_zero_indices = np.where(new_row != 0)[0]

    for i in range(len(new_row)):
      if new_row[i] == 0:
        closest_index = -1
        min_dist = float('inf')
        for nz_idx in non_zero_indices:
          dist = abs(nz_idx - i)
          if dist < min_dist:
              min_dist = dist
              closest_index = nz_idx
        if closest_index != -1:
           new_row[i] = new_row[closest_index]
    return new_row.tolist()

def transform(input_grid):
    # initialize output_grid
    input_grid = np.array(input_grid)
    output_grid = np.zeros_like(input_grid)
    
    # Find source rows
    source_row_indices = _find_source_rows(input_grid)

    # Replicate and stack rows
    last_filled_row = None
    for y in range(input_grid.shape[0]):
        if y in source_row_indices:
            # replicate current source row
            output_grid[y, :] = _replicate_row_horizontally(input_grid[y, :])
            last_filled_row = output_grid[y,:]
        elif last_filled_row is not None:
            # fill from above
            output_grid[y,:] = last_filled_row

    return output_grid.tolist()
```
