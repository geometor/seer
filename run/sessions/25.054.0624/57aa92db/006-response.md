# 57aa92db • 006 • refine_coder

---
```python
"""
1.  **Object Identification:** Identify all contiguous blocks of non-black pixels in the input grid. Each block is an object, defined by its color and pixel coordinates.

2.  **Blue Removal (Yellow Rule):**
    *   IF a *blue* pixel is IMMEDIATELY to the RIGHT of a *yellow* pixel (same row, column + 1), THEN remove the *blue* pixel (change to black).

3.  **Yellow Expansion:**
    *   IF a *blue* pixel was removed due to the "Yellow Rule" (step 2), THEN the *yellow* object that caused the removal grows downwards by two pixels. The growth extends from the bottom-most row of the original yellow object, maintaining the original yellow object's column span.

4.  **Blue Removal (Green Rule):**
    *   IF a *blue* pixel is directly adjacent (horizontally or vertically, NOT diagonally) to a *green* pixel, THEN remove the *blue* pixel.

5.  **Azure and Yellow Combination:**
    *    IF a *yellow* object is directly adjacent (horizontally or vertically) to an *azure* object, THEN transform the *yellow* object into an *azure* object AND extend the original *azure* object downwards by one pixel.  The growth extends from the bottom-most row of the *original* azure object and maintains the original azure object's column span.

6.  **Green Growth next to Red:**
    *   IF a pixel is *red*, THEN the pixels immediately to its left are *green*.

7.  **Magenta Transformation**
    *   IF a *magenta* object is directly *below* an *azure* object, transform the *magenta* object into a 3x1 *green* object, aligned at the top-left with the original *magenta* object. The green object is one pixel wide and three pixels high.

8. **Order of execution:**
It is likely this sequence will need to be executed in this order to prevent objects from interfering with each other. For instance, removing the blue next to the yellow before growing the yellow.
The Magenta Transformation must occur after the Azure and Yellow combination.
"""

import numpy as np

def find_objects(grid):
    """Finds contiguous objects in a grid."""
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, color, obj):
        """Depth-first search to find contiguous pixels of the same color."""
        if (
            row < 0
            or row >= grid.shape[0]
            or col < 0
            or col >= grid.shape[1]
            or visited[row, col]
            or grid[row, col] != color
        ):
            return
        visited[row, col] = True
        obj.append((row, col))
        dfs(row + 1, col, color, obj)
        dfs(row - 1, col, color, obj)
        dfs(row, col + 1, color, obj)
        dfs(row, col - 1, color, obj)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if not visited[row, col] and grid[row, col] != 0:
                obj = []
                dfs(row, col, grid[row, col], obj)
                objects.append((grid[row, col], obj))  # Store color and object pixels
    return objects

def is_immediately_right_of(pixel1, pixel2):
    """Checks if pixel1 is immediately to the right of pixel2."""
    r1, c1 = pixel1
    r2, c2 = pixel2
    return c1 == c2 + 1 and r1 == r2

def is_adjacent(pixel1, pixel2):
    """Checks if pixel1 is directly adjacent to pixel2 (not diagonal)."""
    r1, c1 = pixel1
    r2, c2 = pixel2
    return (abs(r1 - r2) + abs(c1 - c2)) == 1

def is_below(pixel1, pixel2):
    r1, c1 = pixel1
    r2, c2 = pixel2

    return r1 > r2

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Apply rules in the specified order
    objects = find_objects(output_grid)

    # Blue Removal (Yellow Rule) and Yellow Expansion
    for color1, obj1_pixels in objects:
        if color1 == 1: # Blue
            for color2, obj2_pixels in objects:
                if color2 == 4: # Yellow
                    for p1 in obj1_pixels:
                        for p2 in obj2_pixels:
                            if is_immediately_right_of(p1,p2):
                                # Remove Blue pixel
                                output_grid[p1] = 0
                                # Grow yellow downwards
                                max_yellow_row = max(r for r, c in obj2_pixels)
                                yellow_cols = [c for r, c in obj2_pixels if r == max_yellow_row] # only operate off the bottom
                                
                                if max_yellow_row + 2 < output_grid.shape[0]:
                                    for col in yellow_cols:
                                        output_grid[max_yellow_row + 1, col] = 4
                                        output_grid[max_yellow_row + 2, col] = 4
                                break # yellow only operates once

    # Blue Removal (Green Rule)
    objects = find_objects(output_grid)  # Refresh objects after modifications
    for color1, obj1_pixels in objects:
        if color1 == 1:  # Blue
            for color2, obj2_pixels in objects:
                if color2 == 3:  # Green
                    for p1 in obj1_pixels:
                        for p2 in obj2_pixels:
                            if is_adjacent(p1, p2):
                                output_grid[p1] = 0  # Remove blue pixel
                                break  # Move to the next blue pixel
                        else:
                            continue
                        break

   # Azure and Yellow Combination
    objects = find_objects(output_grid)
    for color1, obj1_pixels in objects:
        if color1 == 4:  # Yellow
            for color2, obj2_pixels in objects:
                if color2 == 8:  # Azure
                    for p1 in obj1_pixels:
                        for p2 in obj2_pixels:
                            if is_adjacent(p1, p2):
                                # Transform Yellow to Azure
                                output_grid[p1] = 8
                                # Extend *original* Azure down
                                max_azure_row = max(r for r, _ in obj2_pixels) # operate of original azure
                                azure_cols = [ c for r, c in obj2_pixels if r == max_azure_row] # only grow based on bottom

                                if max_azure_row + 1 < output_grid.shape[0]:
                                    for col in azure_cols:
                                        output_grid[max_azure_row + 1, col] = 8
                                break
                        else:
                            continue
                        break

    # Green Growth next to Red
    objects = find_objects(output_grid) # refresh
    for color, obj_pixels in objects:
        if color == 2:  # Red
            for r, c in obj_pixels:
                if c - 1 >= 0:
                    output_grid[r, c - 1] = 3

    # Magenta Transformation
    objects = find_objects(output_grid)  # Refresh objects
    for color1, obj1_pixels in objects:
        if color1 == 6:  # Magenta
            for color2, obj2_pixels in objects:
                if color2 == 8:  # Azure
                    for p1 in obj1_pixels:
                        for p2 in obj2_pixels:
                            if is_below(p1, p2):
                                # Transform Magenta to 3x1 Green
                                min_row = min(r for r, c in obj1_pixels)
                                min_col = min(c for r, c in obj1_pixels)
                                # clear magenta
                                for r,c in obj1_pixels:
                                    output_grid[r,c] = 0

                                # make 3x1 green
                                for i in range(3):
                                    if min_row + i < output_grid.shape[0] and min_col < output_grid.shape[1]:
                                        output_grid[min_row + i, min_col] = 3
                                break # only transform once
                        else:
                            continue
                        break

    return output_grid
```
