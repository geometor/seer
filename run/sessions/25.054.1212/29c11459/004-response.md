# 29c11459 • 004 • refine_coder

---
```python
"""
1.  **Identify Target Row:** Examine each row of the input grid. Find a row that contains at least two pixels of different colors, excluding black(0).
2.  **Locate Distinct-Colored Pixels:** On the identified row, find the two distinct-colored pixels that are furthest apart (i.e., the leftmost and rightmost of different colors on that row).
3. **Determine center column:** The center column will the x value of `(grid_width - 1) / 2`
4.  **Connect Left to Center:**  Change all pixels between the leftmost pixel and the center column (exclusive) to the color of the leftmost pixel.
5.  **Connect Center to Right:** Change all pixels between the center column (exclusive) and the rightmost pixel to the color of the rightmost pixel.
6.  **Place Gray Pixel:** Place a gray (5) pixel at the center column of the target row.
7. **Output:** Return the changed grid
"""

import numpy as np

def find_distinct_colored_pixels(row):
    """Finds the leftmost and rightmost distinct colored (non-zero) pixels in a row."""
    colored_pixels = [(i, color) for i, color in enumerate(row) if color != 0]
    if len(colored_pixels) < 2:
        return None, None, None, None  # Not enough distinct colors

    # Sort by color to easily find distinct ones
    colored_pixels.sort(key=lambda x: x[1])

    leftmost = colored_pixels[0]
    rightmost = colored_pixels[-1]

    # Ensure they are actually distinct
    if leftmost[1] == rightmost[1]:
      distinct = []
      current_color = leftmost[1]
      distinct.append(leftmost)
      for i in range(1,len(colored_pixels)):
          if colored_pixels[i][1] != current_color:
            distinct.append(colored_pixels[i])
            break
      if (len(distinct) < 2):
        return None, None, None, None
      else:
        leftmost = distinct[0]
        rightmost = distinct[1]
        
    #find the true leftmost and rightmost
    if (leftmost[0] > rightmost[0]):
      leftmost, rightmost = rightmost, leftmost


    return leftmost[0], leftmost[1], rightmost[0], rightmost[1]

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    center_col = (cols - 1) // 2

    for row_index in range(rows):
      row = input_grid[row_index]
      left_col, left_color, right_col, right_color = find_distinct_colored_pixels(row)

      if left_col is not None:
          # Connect Left to Center
          for col in range(left_col, center_col):
              output_grid[row_index, col] = left_color

          # Connect Center to Right
          for col in range(center_col + 1, right_col + 1):
              output_grid[row_index, col] = right_color

          # Place Gray Pixel
          output_grid[row_index, center_col] = 5
          break  # Stop after the first row with distinct colors is processed

    return output_grid
```
