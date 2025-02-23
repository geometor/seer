# 2-0ca9ddb6 • 003 • example_2 - NLP

---
**General Assessment:**

The second example follows the same general pattern as the first, reinforcing the rules related to red (2) and blue (1) pixels. Additionally, this example introduces a new color, azure (8), which appears unaffected by the transformation. This confirms the initial hypothesis of a local, color-specific operation. The presence of the azure pixel helps to solidify the idea that only red and blue pixels trigger changes in the output, while other colors remain unchanged.

**Strategy:**

1.  **Verify Existing Rules:** Re-confirm the red and blue pixel rules identified in the first example, ensuring they apply correctly here.
2.  **Incorporate New Color (Azure):**  Observe that the azure pixel remains unchanged, which indicates that the transformation is color-selective.
3.  **Refine Rule (if necessary):**  The rules from the previous analysis should be sufficient, but this example serves as additional validation.
4.   **Document:** Capture observations in the YAML block.
5.   **Provide Natural Language Program**: Describe the transformation precisely.

**Metrics and Observations (Pre-Code):**

*   **Input Grid Size:** 9x9
*   **Output Grid Size:** 9x9
*   **Input Colors:** 0 (white), 1 (blue), 2 (red), 8 (azure)
*   **Output Colors:** 0 (white), 1 (blue), 2 (red), 4 (yellow), 7 (orange), 8 (azure)
*   There are two red pixels, located at (2, 6) and (7, 1).  Yellow pixels appear adjacent (above, below and sides) to them in the output.
*   There are two blue pixels at (3, 2) and (6, 6). Orange pixels surround them in the output, in orthogonal directions only.
*  The azure (8) pixel at (0,3) remains the same.

**YAML Facts:**



```yaml
input:
  grid_size: [9, 9]
  objects:
    - color: 8  # Azure
      position: [0, 3]
      shape: single_pixel
    - color: 2  # Red
      positions: [[2, 6], [7, 1]]
      shape: single_pixel
    - color: 1  # Blue
      positions: [[3, 2], [6, 6]]
      shape: single_pixel

output:
  grid_size: [9, 9]
  objects:
    - color: 8  # Azure
      position: [0, 3]
      shape: single_pixel
    - color: 2  # Red
      positions: [[2, 6], [7, 1]]
      shape: single_pixel
    - color: 4 # Yellow
      positions: [[1,5],[1,7],[3,5],[3,7],[6,0],[6,2],[8,0],[8,2]]
      shape: single_pixel
    - color: 1  # Blue
      positions: [[3, 2], [6, 6]]
      shape: single_pixel
    - color: 7  # Orange
      positions: [[2,2],[3,1],[3,3],[4,2],[5,6],[6,5],[6,7],[7,6]]
      shape: single_pixel

```



**Natural Language Program:**

1.  **Red Pixel Rule:** For every red pixel in the input, maintain its position and color in the output. Additionally, introduce yellow pixels to its immediate, non-diagonal neighbors (above, below, left, and right) if these neighboring positions exist within the grid boundaries and are occupied by white pixels in the input grid.

2.  **Blue Pixel Rule:** For every blue pixel in the input, maintain its position and color in the output. Additionally, change the color of its immediate, non-diagonal neighbors (above, below, left, and right) to orange if these neighboring positions exist within the grid boundaries and are occupied by white pixels in the input grid.

3.  **Other Colors:** Pixels of any color other than red or blue remain unchanged in their position and color from the input to the output grid.


```python
"""
Transforms an input grid based on the location of red and blue pixels.

1.  **Red Pixel Rule:** For every red pixel in the input, keep it as is in output and add yellow pixels directly above and below if those adjacent spots exist within the grid boundary and contains white pixel.

2.  **Blue Pixel Rule:** For every blue pixel in the input, keep it as is in output and change the directly adjacent area, if any, into orange color (above, below, left, right, but *not* diagonals), if those adjacent spots exist within the grid boundary and are white.

3.   **Other Colors:** Pixels of any color other than red or blue remain unchanged in their position and color from input to the output.
"""

import numpy as np

def get_pixel(grid, r, c):
    if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
        return grid[r][c]
    else:
        return None
    
def set_pixel(grid, r, c, value):
   if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
        grid[r][c] = value
   
def transform(input_grid):
    # initialize output_grid as a copy of the input
    output_grid = np.copy(input_grid)
    rows = len(input_grid)
    cols = len(input_grid[0])

    # Iterate through each cell of the input_grid
    for r in range(rows):
        for c in range(cols):
            # Red pixel rule
            if input_grid[r][c] == 2:  # Red pixel found
                #output_grid[r][c] = 2 # keep the red pixel (this is redundant as output is copy)
                # Add yellow above and below if within bounds
                if r > 0 and input_grid[r-1][c] == 0 :
                    output_grid[r - 1][c] = 4  # Yellow
                if r < rows - 1 and input_grid[r+1][c] == 0:
                    output_grid[r + 1][c] = 4  # Yellow
                if c > 0 and input_grid[r][c-1] == 0:
                    output_grid[r][c-1] = 4
                if c < cols -1 and input_grid[r][c+1] == 0:
                    output_grid[r][c+1] = 4

            # Blue pixel rule
            elif input_grid[r][c] == 1:  # Blue pixel found
                # output_grid[r][c] = 1 # keep the blue pixel (this is redundant as output is copy)
                # Change adjacent cells to orange if within bounds
                if r > 0 and input_grid[r-1][c] == 0:
                    output_grid[r - 1][c] = 7  # Orange
                if r < rows - 1 and input_grid[r+1][c] == 0:
                    output_grid[r + 1][c] = 7  # Orange
                if c > 0 and input_grid[r][c-1] == 0:
                    output_grid[r][c - 1] = 7  # Orange
                if c < cols - 1 and input_grid[r][c+1] == 0:
                    output_grid[r][c + 1] = 7  # Orange

    return output_grid
```
