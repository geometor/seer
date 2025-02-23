# db93a21d • 016 • refine_coder

---
```python
"""
1.  **Identify Rectangles:** Find all maroon (9) colored rectangles in the input grid. Record their positions (top-left corner coordinates), widths, and heights.
2.  **Create Green Outline:** For the top-left most rectangle, construct a 1 pixel thick green (3) outline around the maroon rectangle.
3. **Create a complex outline:** For the rectangle at the right, create a 1-pixel green outline on its top, and 3-pixel on its right.
4.  **Create Blue Outline:** Create an outline for the largest rectangle using blue, there is a gap of 1-pixel between the blue outline and the shape. The blue shape is one pixel thick.
5.  **Create Green Filling:** Starting from the top left corner, fill every white region with green until it connects with any other color.
"""

import numpy as np

def find_rectangles(grid, color):
    rectangles = []
    visited = np.zeros_like(grid, dtype=bool)
    rows, cols = grid.shape
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and not visited[r, c]:
                width = 0
                height = 0
                # Find width
                for i in range(c, cols):
                    if grid[r, i] == color:
                        width += 1
                        visited[r, i] = True
                    else:
                        break
                # Find height
                for j in range(r + 1, rows):
                    if all(grid[j, c:c+width] == color):
                        for i in range(c, c + width):
                            visited[j, i] = True  # fixed missing
                        height += 1
                    else:
                        break
                rectangles.append((r, c, width, height + 1)) #  height was off by one.
    return rectangles

def outline_rectangle_pixels(grid, r, c, width, height, color, thickness=1):
    # Top
    for i in range(c, c + width):
        for t in range(thickness):
            if r - 1 - t >= 0:
                grid[r-1-t, i] = color

    # Bottom
    for i in range(c, c + width):
        for t in range(thickness):
            if r + height + t < grid.shape[0]:
                grid[r + height + t, i] = color

    # Left
    for i in range(r, r + height):
        for t in range(thickness):
            if c - 1 - t >= 0:
                grid[i, c - 1 - t] = color
    # Right
    for i in range(r, r + height):
        for t in range(thickness):
          if c + width + t < grid.shape[1]:
            grid[i, c + width + t] = color

def outline_rectangle_complex_pixels(grid, r, c, width, height, color_top, thickness_top, color_right, thickness_right):
    # Top
    for i in range(c, c + width):
        for t in range(thickness_top):
            if r - 1 -t >= 0:
                grid[r - 1 - t, i] = color_top
    # Right
    for i in range(r, r + height):
        for t in range(thickness_right):
            if c + width + t < grid.shape[1]:
              grid[i, c + width + t] = color_right


def outline_rectangle_with_gap_pixels(grid, r, c, width, height, color, gap=1):
   # Top
    for i in range(c, c + width):
        if r - 1 - gap >= 0 and grid[r-1-gap, i] == 0 :
            grid[r - 1 - gap, i] = color

    # Bottom
    for i in range(c, c + width):
        if r + height + gap < grid.shape[0] and grid[r+height+gap, i] == 0:
            grid[r + height + gap, i] = color

    # Left
    for i in range(r, r + height):
        if c - 1 - gap >= 0 and grid[i, c-1-gap] == 0:
            grid[i, c - 1 - gap] = color

    # Right
    for i in range(r, r + height):
        if c + width + gap < grid.shape[1] and grid[i, c+width+gap] == 0:
            grid[i, c + width + gap] = color

def flood_fill_with_boundary(grid, r, c, target_color, replacement_color):
    if r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or grid[r, c] != target_color:
        return
    grid[r, c] = replacement_color
    flood_fill_with_boundary(grid, r + 1, c, target_color, replacement_color)
    flood_fill_with_boundary(grid, r - 1, c, target_color, replacement_color)
    flood_fill_with_boundary(grid, r, c + 1, target_color, replacement_color)
    flood_fill_with_boundary(grid, r, c - 1, target_color, replacement_color)

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # identify rectangles
    rectangles = find_rectangles(input_grid, 9)

    # sort by top-left (r, c)
    rectangles_top_left = sorted(rectangles, key=lambda x: (x[0], x[1]))

    # sort for largest
    rectangles_largest = sorted(rectangles, key=lambda x: x[2] * x[3], reverse=True)

    # sort by most right
    rectangles_right = sorted(rectangles, key=lambda x: x[1], reverse=True)

    # create outlines
    if len(rectangles_top_left) >= 1:
        outline_rectangle_pixels(output_grid, rectangles_top_left[0][0], rectangles_top_left[0][1], rectangles_top_left[0][2], rectangles_top_left[0][3], 3)  # green

    if len(rectangles_right) >= 1:
        outline_rectangle_complex_pixels(output_grid, rectangles_right[0][0], rectangles_right[0][1], rectangles_right[0][2], rectangles_right[0][3], 3, 1, 3, 3) # green complex

    if len(rectangles_largest) >= 1:
      outline_rectangle_with_gap_pixels(output_grid, rectangles_largest[0][0], rectangles_largest[0][1], rectangles_largest[0][2], rectangles_largest[0][3], 1, 1) #blue

    # create filling
    flood_fill_with_boundary(output_grid, 0, 0, 0, 3)

    return output_grid
```
