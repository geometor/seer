# db93a21d • 018 • refine_coder

---
```python
"""
1.  **Find Rectangles:** Locate all maroon (9) colored rectangles within the input grid.
2.  **Top-Left Outline:** Create a 1-pixel thick green (3) outline around the rectangle whose top-left corner is closest to the top-left corner of the grid.
3.  **Right Rectangle Complex Outline:** Create a 1-pixel green outline only on the top, and create a 3-pixel green outline only on the right of the rectangle. Prioritize the rectangle furthest to the right.
4.  **Largest Rectangle Gapped Outline:** Identify the largest maroon rectangle (by area). Create a 1-pixel thick blue (1) outline around it, maintaining a 1-pixel gap between the outline and the rectangle.
5.  **Conditional Flood Fill:** Starting from the top-left corner (0, 0) of the grid, flood fill the white (0) regions with green (3). Stop the flood fill when encountering any pixel that is blue (1), green (3), or maroon (9).
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
                            visited[j, i] = True
                        height += 1
                    else:
                        break
                rectangles.append((r, c, width, height + 1))
    return rectangles

def outline_top_left_rectangle(grid, rectangles, color):
    if not rectangles:
        return
    top_left_rectangle = min(rectangles, key=lambda x: (x[0], x[1]))
    r, c, width, height = top_left_rectangle
    # Top
    for i in range(c, c + width):
        if r - 1 >= 0:
            grid[r-1, i] = color
    # Bottom
    for i in range(c, c + width):
        if r + height < grid.shape[0]:
            grid[r + height, i] = color
    # Left
    for i in range(r, r + height):
        if c - 1 >= 0:
            grid[i, c - 1] = color
    # Right
    for i in range(r, r + height):
      if c + width < grid.shape[1]:
        grid[i, c + width] = color

def outline_right_rectangle_complex(grid, rectangles, color_top, thickness_top, color_right, thickness_right):
    if not rectangles:
        return
    right_rectangle = max(rectangles, key=lambda x: x[1])
    r, c, width, height = right_rectangle

    # Top outline
    for i in range(c, c + width):
        for t in range(thickness_top):
            if r - 1 - t >= 0:
                grid[r - 1 - t, i] = color_top

    # Right outline
    for i in range(r, r + height):
        for t in range(thickness_right):
            if c + width + t < grid.shape[1]:
                grid[i, c + width + t] = color_right


def outline_largest_rectangle_gapped(grid, rectangles, color, gap):
    if not rectangles:
      return
    largest_rectangle = max(rectangles, key=lambda x: x[2] * x[3])
    r, c, width, height = largest_rectangle

    # Iterate over the potential outline area with the gap
    for i in range(r - gap - 1, r + height + gap + 1):
        for j in range(c - gap - 1, c + width + gap + 1):
            # Check bounds
            if 0 <= i < grid.shape[0] and 0 <= j < grid.shape[1]:
                # Check if it's on the outline perimeter
                if (i == r - gap - 1 or i == r + height + gap or
                    j == c - gap - 1 or j == c + width + gap):
                    # Ensure it's not inside the rectangle and not immediately adjacent
                    if not (r <= i < r + height and c <= j < c + width):

                        grid[i,j] = color



def conditional_flood_fill(grid, r, c, target_color, replacement_color, boundary_colors):
    if r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or grid[r, c] != target_color or grid[r,c] in boundary_colors:
        return
    grid[r, c] = replacement_color
    conditional_flood_fill(grid, r + 1, c, target_color, replacement_color, boundary_colors)
    conditional_flood_fill(grid, r - 1, c, target_color, replacement_color, boundary_colors)
    conditional_flood_fill(grid, r, c + 1, target_color, replacement_color, boundary_colors)
    conditional_flood_fill(grid, r, c - 1, target_color, replacement_color, boundary_colors)


def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Find Rectangles
    rectangles = find_rectangles(output_grid, 9)

    # Top-Left Outline
    outline_top_left_rectangle(output_grid, rectangles, 3)

    # Right Rectangle Complex Outline
    outline_right_rectangle_complex(output_grid, rectangles, 3, 1, 3, 3)

    # Largest Rectangle Gapped Outline
    outline_largest_rectangle_gapped(output_grid, rectangles, 1, 1)

    # Conditional Flood Fill
    conditional_flood_fill(output_grid, 0, 0, 0, 3, [1, 3, 9])

    return output_grid
```
