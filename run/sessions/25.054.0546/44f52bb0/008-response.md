# 44f52bb0 • 008 • example_2 • investigate_coder

---
```python
"""
1.  **Identify**: Locate all pixels in the input grid with the value 2 (red).
2.  **Count**: Count the number of these red pixels.
3. **Assign**: If the count of red pixels in the Input grid equals 3, the output will be assigned to the color 7 (orange).
"""

import numpy as np

def count_pixels_of_color(grid, color):
    """Counts the number of pixels of a specified color in the grid."""
    return np.sum(grid == color)

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""

    # Count the number of red (2) pixels.
    red_pixel_count = count_pixels_of_color(input_grid, 2)

    # Assign output based on count
    if red_pixel_count == 3:
       output = 7
    else:
       output = 0

    return output
```
