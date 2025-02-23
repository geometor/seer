# 1-3aa6fb7a • 005 • example_2 - NLP

---
Okay, let's analyze the transformation between the input and output grids.

**YAML Observation:**

```yaml
observations:
  input_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: scattered segments
        positions:
          - (0,4), (0,5)  # Horizontal line segment
          - (1,5) # Single pixel
          - (2,2) # Single pixel
          - (3,2), (3,3) # Horizontal line segment
          - (5,4) # Single Pixel
          - (6,3), (6,4) # Horizontal line segment
      - color: 0 (white)
        shape: background
        positions: fills the remaining cells
  output_grid:
    size: 7x7
    objects:
      - color: 8 (azure)
        shape: same as input
        positions: same as input
      - color: 1 (blue)
        shape: single cells
        positions:
          - (1,4)   # Left to the segment (0,4)
          - (2,3)   # Right to the segment (2,2)
          - (5,3)  # Left to the segment (5,4)

      - color: 0 (white)
        shape: background
        positions: fills the remaining cells

```

**Natural Language Program (Transformation Rule):**

1.  **Identify Objects:** In the input grid, we have color 8 (azure) pixels.

2.  **Observe Changes:** We see in the output that azure pixels maintained as is. And, a new blue pixel (color 1) can appear immediately to the left or the right of an azure pixel, only once for an azure pixel.

3. **Describe the Rule:**
    - Scan the input grid from the upper shape to the lower shape.
    - For each azure shape, identify their right-adjacent and left-adjacent position, in order.
    - If a position doesn't have any colored pixel, add a new pixel by drawing at these positions with blue(color 1).

```python
"""
The transformation rule is as follows:
1. Identify all azure (color 8) pixels in the input grid.
2. For each identified pixel, check its immediate left or right. If it is empty, then place a blue (color 1) there.
"""

import numpy as np

def find_pixels(grid, color):
    """
    Find pixels of specified color.
    """
    pixels = []
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color:
                pixels.append((r, c))
    return pixels

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule:
    1. Find all pixels of azure color.
    2. Add one blue pixel at the left or the right of each of these pixels
    """
    # Initialize output grid as a copy of the input grid
    output_grid = np.copy(input_grid)

    # Find all pixels of color 8 (azure)
    azure_pixels = find_pixels(input_grid, 8)

    # For each azure pixel, place a blue pixel (color 1) to the left or right
    for pixel in azure_pixels:
        r, c = pixel
        if c - 1 >= 0 and output_grid[r, c - 1] == 0 :  # Check left side
            output_grid[r, c - 1] = 1
            continue
        if c + 1 < output_grid.shape[1] and output_grid[r, c+1] == 0:  # Check right side and bounds
            output_grid[r, c + 1] = 1


    return output_grid
```

