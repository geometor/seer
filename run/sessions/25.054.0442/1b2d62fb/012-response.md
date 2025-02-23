# 1b2d62fb • 012 • refine_coder

---
```python
"""
1.  **Find Blue Stripe:** Locate a vertical column in the input grid that consists entirely of blue (1) pixels. If no such column exists, return an empty grid that is the same dimensions as the input.

2.  **Record Stripe Index:** Note the column index (x-coordinate) of this blue stripe.

3.  **Extract Column:** Extract all pixel values from the input grid at the recorded column index.

4.  **Conditional Replacement:** For *each* blue pixel in the *extracted column*:
    *   Check its immediate neighbors (up, down, left, and right) in the *original input grid*.
    *   If *any* of these neighbors are a color other than blue (1) or white (0), replace the blue pixel in the extracted column with azure (8).
    *   If all neighbors are blue or white, leave the blue pixel unchanged.

5.  **Create Output Grid:**
     *   Start with an empty grid with a width of 1 and height of the original input
     *   Insert the extracted, and potentially transformed, central column.

6. **Replicate Column - Left**
    * Check the column immediately to the left of the blue stripe. If the column contains a pixel that is neither blue (1) or white (0), insert a copy of the central column to the left.

7. **Replicate Column - Right**
    * Check the column immediately to the right of the blue stripe. If the column contains a pixel that is neither blue (1) or white (0), insert a copy of the central column to the right.

8. **Pad Output:** If the output has width of 1 (only the central column), pad both sides with a single column of zeros.
"""

import numpy as np

def find_vertical_stripe(grid, color):
    """Finds the index of a vertical stripe of the specified color."""
    height, width = grid.shape
    for x in range(width):
        is_stripe = True
        for y in range(height):
            if grid[y, x] != color:
                is_stripe = False
                break
        if is_stripe:
            return x
    return -1

def get_neighbors(grid, row, col):
    """Gets the colors of the immediate neighbors of a pixel."""
    height, width = grid.shape
    neighbors = []
    if row > 0:
        neighbors.append(grid[row - 1, col])  # Top
    if row < height - 1:
        neighbors.append(grid[row + 1, col])  # Bottom
    if col > 0:
        neighbors.append(grid[row, col - 1])  # Left
    if col < width - 1:
        neighbors.append(grid[row, col + 1])  # Right
    return neighbors

def transform(input_grid):
    # 1. Find the Blue Stripe and its index.
    blue_stripe_index = find_vertical_stripe(input_grid, 1)
    height, width = input_grid.shape

    # 2. If no blue stripe is found, return an empty grid with input size
    if blue_stripe_index == -1:
        return np.zeros_like(input_grid)

    # 3. Extract Column
    extracted_column = input_grid[:, blue_stripe_index]

    # 4. Conditional Replacement
    transformed_column = extracted_column.copy()
    for i, pixel in enumerate(extracted_column):
        if pixel == 1:
            neighbors = get_neighbors(input_grid, i, blue_stripe_index)
            if any(neighbor not in [0, 1] for neighbor in neighbors):
                transformed_column[i] = 8

    # 5. Create Output Grid (start with width 1)
    output_grid = np.zeros((height, 1), dtype=int)
    output_grid[:, 0] = transformed_column

    # 6. Replicate Column - Left
    if blue_stripe_index > 0:
      left_column = input_grid[:, blue_stripe_index-1]
      if any(pixel not in [0,1] for pixel in left_column):
        output_grid = np.insert(output_grid, 0, transformed_column, axis=1)
    
    # 7. Replicate Column - Right
    if blue_stripe_index < width -1:
      right_column = input_grid[:, blue_stripe_index + 1]
      if any(pixel not in [0,1] for pixel in right_column):
        output_grid = np.insert(output_grid, output_grid.shape[1], transformed_column, axis=1)

    # 8. Pad with white (0) if no columns added
    if output_grid.shape[1] == 1:
      output_grid = np.pad(output_grid, ((0,0),(1,1)), constant_values=0)

    return output_grid
```
