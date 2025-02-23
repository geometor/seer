"""
1.  **Locate Target Region:** Scan the input grid to identify the smallest rectangular region containing *all* non-zero (non-black) colored pixels. This region is defined by the minimum and maximum row and column indices that contain any non-zero pixel.
2.  **Extract Region:** Copy the pixel values within the identified rectangular region.
3.  **Create Output Grid:** Create an output grid with the exact dimensions (height and width) of the extracted region.
4. **Arrange:** Maintain the position of non-zero pixels from the input and set all other values to zero.
5.  **Output:** Return the extracted output grid.
"""

import numpy as np

def find_target_region(grid):
    """Finds the smallest rectangular region containing all non-zero pixels."""
    rows, cols = grid.shape
    non_zero_rows = []
    non_zero_cols = []

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != 0:
                non_zero_rows.append(r)
                non_zero_cols.append(c)

    if not non_zero_rows:  # No non-zero pixels found
        return None, None, None, None

    top_row = min(non_zero_rows)
    bottom_row = max(non_zero_rows)
    left_col = min(non_zero_cols)
    right_col = max(non_zero_cols)

    return top_row, bottom_row, left_col, right_col

def transform(input_grid):
    """Transforms the input grid by extracting the smallest bounding box of non-zero pixels."""
    # Convert input to numpy array
    input_grid = np.array(input_grid)

    # Find the target region
    top_row, bottom_row, left_col, right_col = find_target_region(input_grid)

    if top_row is None:  # Handle case where no region is found
        return []

    # Extract the region
    extracted_region = input_grid[top_row:bottom_row+1, left_col:right_col+1]
    
    # Create output grid filled with zeros and same shape
    output_grid = np.zeros_like(extracted_region)

    # Iterate through extract_region
    rows, cols = extracted_region.shape
    for r in range(rows):
      for c in range(cols):
        # Copy only non-zero
        if extracted_region[r,c] != 0:
          output_grid[r,c] = extracted_region[r,c]


    return output_grid.tolist()