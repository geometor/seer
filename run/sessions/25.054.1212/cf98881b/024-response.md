# cf98881b • 024 • refine_coder

---
```python
"""
1.  **Selection:** Iterate through the input grid. Select all pixels with a value of 0, 1, 4, or 9.
2. **Collection**: Collect these selected pixels into a list, preserving input order from left to right and top to bottom
3. **Bounding Box:** Find the largest contiguous block of selected pixels, where contiguous means adjacent vertically and horizontally. From the training examples, the shape of this contiguous block is always 4x4.
4.  **Output:** Create the output grid of size 4 x 4, populating with the selected pixels.
"""

import numpy as np

def transform(input_grid):
    # Convert input_grid to a NumPy array
    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    
    # 1. Selection & 2. Collection
    selected_pixels = []
    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] in [0, 1, 4, 9]:
                selected_pixels.append(input_grid[r, c])

    # 3. Bounding Box (Implicitly handled by reshaping to 4x4)
    # 4. Output (Create a 4x4 output grid)
    output_grid = np.zeros((4, 4), dtype=int)
    
    # Populate the output grid. If there are fewer than 16 selected pixels, 
    # the remaining cells will remain 0 (as initialized).
    for i in range(min(16, len(selected_pixels))):
        row = i // 4
        col = i % 4
        output_grid[row, col] = selected_pixels[i]

    return output_grid
```
