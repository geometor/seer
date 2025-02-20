# 1-3aa6fb7a • 003 • example_2 - NLP

---
Okay, let's analyze the transformation between the input and output grids in the second example.

**YAML Observation:**

```yaml
input_grid:
  size: 7x7
  objects:
    - color: 8 (azure)
      shape: Disconnected segments. Two horizontal 1x2 lines and two vertical 2x1 lines.
      positions:
        - [0,4], [0,5] # Horizontal line 1
        - [1,5]       # segment of Horizontal line 1        
        - [2,2], [3,2] # Vertical line 1
        - [3,3]       # segment of Vertical Line 1
        - [5,4]       # Vertical line 2
        - [6,3], [6,4]       # Horizontal line 2

    - color: 0 (white)
      shape: background
      position: everywhere else

output_grid:
  size: 7x7
  objects:
    - color: 8 (azure)
      shape: Disconnected segments.  Two horizontal 1x2 lines and two vertical 2x1 lines.
      positions:
        - [0,4], [0,5] # Horizontal line 1
        - [1,5]       # segment of Horizontal line 1
        - [2,2], [3,2] # Vertical line 1
        - [3,3]       # segment of Vertical Line 1        
        - [5,4]       # Vertical line 2
        - [6,3], [6,4]       # Horizontal line 2
    - color: 1 (blue)
      shape: Single pixel
      positions:
        - [1,4] # left of Horizontal line 1
        - [2,3] # right of Vertical line 1
        - [5,3] # left of the top of vertical line 2

    - color: 0 (white)
      shape: background
      position: everywhere else
```

**Natural Language Program (Step-by-step transformation):**

1.  **Identify Objects:**  The input grid has azure (8) colored objects, and the white (0) background. The azure objects are disconnected segments.

2.  **Detect Change:**  New blue (1) pixels appear in the output grid.

3.  **Locate Blue Pixel Positions and Transformation Rule:**
    *   A blue pixel is added to the *immediate left* of the *topmost* horizontal line of azure color.
    *   A blue pixel is added to the *immediate right* of the *topmost* vertical line of azure color.
    *   A blue pixel is added to the *immediate left* of the *top* of the next (or second to top if more than one at the same level) vertical line.
    *  The azure (8) elements and the white (0) background remain unchanged.

The example shows that we have a more complex rule. We must consider a hierarchy among the lines. We look for horizontal and vertical lines, and then find the topmost line. It is not the bottommost, but the *topmost* horizontal and vertical lines of color 8.
When we find a collision (more than one vertical segment starting on the same row) we choose the next highest vertical segment.

```python
"""
Transformation Rule:
The azure (8) objects remain unchanged.
A blue (1) pixel is added to the immediate left of the topmost horizontal azure line.
A blue (1) pixel is added to the immediate right of the topmost vertical azure line.
A blue (1) pixel is added to the immediate left of the top of the next vertical line.

"""

import numpy as np

def find_topmost_horizontal_line(grid, color):
    """Finds the topmost horizontal line of a given color."""
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols - 1):
            if grid[r, c] == color and grid[r, c+1] == color:
                return r, c
    return None

def find_topmost_vertical_lines(grid, color):
    """Finds the topmost vertical lines of a given color, handling duplicates."""
    rows, cols = grid.shape
    vertical_lines = []
    for c in range(cols):
        for r in range(rows - 1):
            if grid[r, c] == color and grid[r+1, c] == color:
                vertical_lines.append((r, c))
    # Sort by row and then by column to handle duplicates, returning distinct lines
    vertical_lines = sorted(set(vertical_lines), key=lambda x: (x[0], x[1]))
    return vertical_lines
    

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""
    output_grid = np.copy(input_grid)

    # Find the topmost horizontal line of color 8
    top_horizontal = find_topmost_horizontal_line(output_grid, 8)
    if top_horizontal:
        r, c = top_horizontal
        # Add a blue pixel (1) to the left
        if c > 0:
            output_grid[r, c - 1] = 1

    # Find the topmost vertical lines of color 8
    top_verticals = find_topmost_vertical_lines(output_grid, 8)
    if top_verticals:
      if len(top_verticals) >= 1:
        # Add a blue pixel (1) to the right of the first (topmost) line
        r,c = top_verticals[0]
        if c+1 < output_grid.shape[1]:
          output_grid[r, c + 1] = 1
      if len(top_verticals) >= 2:  #check there is enough vertical lines
        # Add a blue pixel (1) to the left of the second (next topmost)
        r,c = top_verticals[1]
        if c > 0:
          output_grid[r,c-1] = 1


    return output_grid
```

