"""
1.  **Identify Objects:** Locate all contiguous blocks of non-zero pixels in the input grid. Each block is an object.
2.  **Blue Object Removal (Green Rule):** If a blue object is *directly adjacent* to a green object, remove the blue object.
3.  **Blue Object Removal (Yellow Rule):** If a blue object is to the *immediate right* of a yellow object, remove the blue object.
4.  **Yellow Expansion:** If a blue object is removed due to the "Yellow Rule" (step 3), the yellow object that caused the removal grows downwards by two pixels.
5. **Azure and Yellow Combination:** When a yellow object and azure object are adjacent, vertically or horizontally, the yellow object turns to azure and grows downward by one pixel.
6. **Green Growth next to Red:** If an object is red, then the objects to its immediate left, grow or turn green.
7. **Magenta Transofmration:** If a magenta is below azure, it transform into a 3x1 green, growing down.
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

def is_directly_adjacent(obj1_pixels, obj2_pixels):
    """Checks if two sets of pixels are directly adjacent (not diagonal)."""
    for r1, c1 in obj1_pixels:
        for r2, c2 in obj2_pixels:
            if (abs(r1 - r2) + abs(c1 - c2)) == 1:
                return True
    return False

def is_immediately_right_of(obj1_pixels, obj2_pixels):
    """Checks if obj1 is immediately to the right of obj2."""
    for r1, c1 in obj1_pixels:
        for r2, c2 in obj2_pixels:
            if c1 == c2 + 1 and r1 == r2:
                return True
    return False

def is_below(obj1_pixels, obj2_pixels):
    """Checks if obj1 is below obj2"""
    for r1, c1 in obj1_pixels:
        for r2, c2 in obj2_pixels:
            if r1 > r2:
                return True

    return False


def transform(input_grid):
    # Initialize output_grid as a copy of the input grid
    output_grid = np.copy(input_grid)
    objects = find_objects(input_grid)

    # Apply rules iteratively.  Some rules modify the grid, so we need to
    # re-find objects after each major rule application.

    # Blue Object Removal (Green Rule)
    objects = find_objects(output_grid)
    for color, obj_pixels in objects:
        if color == 1:  # Blue
            for other_color, other_obj_pixels in objects:
                if other_color == 3 and is_directly_adjacent(obj_pixels, other_obj_pixels):
                    for r, c in obj_pixels:
                        output_grid[r, c] = 0

    # Blue Object Removal (Yellow Rule) and Yellow Expansion
    objects = find_objects(output_grid)
    for color, obj_pixels in objects:
        if color == 1: # Blue
            for other_color, other_obj_pixels in objects:
                if other_color == 4 and is_immediately_right_of(obj_pixels, other_obj_pixels):
                    for r, c in obj_pixels:
                        output_grid[r,c] = 0
                    # grow yellow
                    max_row = max(r for r, c in other_obj_pixels)
                    min_col = min(c for r, c in other_obj_pixels)
                    max_col = max(c for r, c in other_obj_pixels)
                    if max_row + 2 < output_grid.shape[0]:
                        for col in range(min_col, max_col+1):
                            output_grid[max_row+1, col] = 4
                            output_grid[max_row+2, col] = 4

     # Azure and Yellow Combination
    objects = find_objects(output_grid)
    for color, obj_pixels in objects:
        if color == 4: #yellow
            for other_color, other_obj_pixels in objects:
                if other_color == 8 and is_directly_adjacent(obj_pixels, other_obj_pixels):
                    # turn yellow to azure
                    for r, c in obj_pixels:
                        output_grid[r,c] = 8
                    # grow azure down one
                    max_row = max(r for r, c in other_obj_pixels)
                    min_col = min(c for r, c in other_obj_pixels)
                    max_col = max(c for r, c in other_obj_pixels)

                    if max_row + 1 < output_grid.shape[0]:
                         for col in range(min_col, max_col + 1):
                            output_grid[max_row+1, col] = 8


    # Green Growth Next to Red
    objects = find_objects(output_grid)
    for color, obj_pixels in objects:
        if color == 2: # red
            for r, c in obj_pixels:
                if c - 1 >= 0:
                    output_grid[r, c-1] = 3

    # Magenta Transformation

    objects = find_objects(output_grid)
    for color, obj_pixels in objects:
        if color == 6: # magenta
             for other_color, other_obj_pixels in objects:
                if other_color == 8 and is_below(obj_pixels, other_obj_pixels):
                    min_row = min(r for r, c in obj_pixels)
                    max_row = max(r for r, c in obj_pixels)
                    min_col = min(c for r, c in obj_pixels)
                    max_col = max(c for r, c in obj_pixels)
                    # clear magenta
                    for r, c in obj_pixels:
                        output_grid[r,c] = 0
                    # make 3x1 green
                    if max_row < output_grid.shape[0]:
                        for col in range(min_col, min_col+3):
                            if col < output_grid.shape[1]:
                                output_grid[min_row,col] = 3



    return output_grid