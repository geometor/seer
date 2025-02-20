# 6-0520fde7 • 005 • example_2 - NLP

---
Okay, let's analyze the transformation from the input grid to the output grid.

**YAML Block: Observations**

```yaml
input_grid:
  size: (3, 7)
  objects:
    blue:
      - shape: irregular
        positions: [(0, 0), (0, 1), (0,5), (1, 2), (1, 4), (1, 5), (1, 6), (2,0), (2,1), (2,5)]
    gray:
      - shape: irregular
        positions: [(0, 3), (1, 3), (2, 3)]
output_grid:
  size: (3, 3)
  objects:
    red:
      - shape: single cell
        positions: [(0, 1), (1,2), (2,1)]
```

**Natural Language Program**

1.  **Identify Objects:** In the input grid, we observe two distinct colored objects: blue (1) and gray (5).

2.  **Focus Object:** The key to the transformation seems to be the gray object.

3.  **Center Extraction:** The output grid is a 3x3 extraction centered around the gray (5) colored cells in the input. However, not all gray cells are treated equally. The transformation centers on the vertically-middle gray cell (1,3).

4.  **Color Change:** The central gray cell (1, 3) in the input grid becomes red (2) in the output grid. In addition, immediate vertical neighbors of the selected gray cell also change to `2` if present in the selected 3x3 area. All other cells in a new 3x3 grid centered on the central gray position become white(0).

**Step-by-step transformation description:**

1. Locate the vertical middle gray cell, if multiple gray columns exist, pick the horizontal middle one.
2. Create 3x3 sub-grid centered vertically in the input grid and horizontally on the selected gray position.
3. Change the centered cell into `2`.
4. Check the immediate vertical neighbors of the selected gray cell. If inside the selected area, set them to `2`.
5. Fill the rest of the cells in the extracted 3x3 sub-grid with `0`.

```python
"""
Transforms the input grid by extracting a 3x3 sub-grid centered around the vertically middle gray cell,
changing the central cell to red (2), and setting all other cells in the sub-grid to white (0).
"""

import numpy as np

def get_gray_positions(grid):
    # return the positions of gray cells (5) in the grid
    return np.array(np.where(grid == 5)).T

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """
    input_grid = np.array(input_grid)
    gray_positions = get_gray_positions(input_grid)
    
    # Check if gray cells exist
    if len(gray_positions) == 0:
        # Return a default 3x3 grid filled with 0, but ideally, handle the error
        return np.zeros((3, 3), dtype=int)
        
    # Find the vertically middle gray cell
    gray_positions = gray_positions[gray_positions[:, 0].argsort()] #sort by y
    middle_gray_y = gray_positions[len(gray_positions) // 2,0]

    middle_gray_positions = gray_positions[gray_positions[:,0]==middle_gray_y]
    middle_gray_positions = middle_gray_positions[middle_gray_positions[:, 1].argsort()] #sort by x
    
    center_x = middle_gray_positions[len(middle_gray_positions)//2,1]
    center_y = middle_gray_y
    
    # Initialize the output grid with zeros
    output_grid = np.zeros((3, 3), dtype=int)

    # Calculate the boundaries for extraction, ensuring we stay within bounds
    y_start = max(0, center_y - 1)
    y_end = min(input_grid.shape[0], center_y + 2)
    x_start = max(0, center_x - 1)
    x_end = min(input_grid.shape[1], center_x + 2)

    # Extract the subgrid.
    subgrid = input_grid[y_start:y_end, x_start:x_end]
    
    
    # Determine center in output_grid
    out_center_y = min(1,center_y)
    out_center_x = min(1, center_x)

    # change center to 2
    output_grid[out_center_y, out_center_x] = 2

    # Check immediate vertical neighbors
    if center_y > 0 and input_grid[center_y-1, center_x] == 5:
      if center_y-1 >= y_start:
        output_grid[out_center_y-1, out_center_x] = 2
    if center_y < input_grid.shape[0]-1 and input_grid[center_y+1, center_x] == 5:
      if center_y+1 < y_end:
        output_grid[out_center_y+1, out_center_x] = 2
        

    return output_grid
```

