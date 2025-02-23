"""
1.  **Identify Objects:** Examine the input grid and identify all contiguous regions of the same color as distinct objects.
2.  **Targeted Color Removal:** Remove *all* objects of a specific color, with exceptions based on the structure and location of the objects.
    *   If the *targeted* color is yellow (4), remove all yellow (4) objects.
    *   If the *targeted* color is magenta (6), remove all magenta (6) objects.
    *   If the *targeted* color is blue (1):
        *   Keep blue (1) objects if they form a contiguous region at the top of the grid.
        *   Remove all other blue (1) objects.
3.  **Output:** Create an output grid of the same dimensions as the input, containing only the objects not removed in the previous step. All other pixels should be black (0).
"""

import numpy as np
from typing import List, Tuple

def find_objects(grid: np.ndarray) -> List[Tuple[int, List[Tuple[int, int]]]]:
    """
    Identifies contiguous objects of the same color in a grid.

    Args:
        grid: A 2D numpy array representing the grid.

    Returns:
        A list of tuples.  Each tuple contains:
          - The color of the object.
          - A list of (row, col) coordinates representing the object's pixels.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def dfs(row, col, color, object_pixels):
        if (row, col) in visited or not (0 <= row < rows and 0 <= col < cols) or grid[row, col] != color:
            return
        visited.add((row, col))
        object_pixels.append((row, col))
        dfs(row + 1, col, color, object_pixels)
        dfs(row - 1, col, color, object_pixels)
        dfs(row, col + 1, color, object_pixels)
        dfs(row, col - 1, color, object_pixels)

    for row in range(rows):
        for col in range(cols):
            if (row, col) not in visited and grid[row, col] != 0:
                color = grid[row, col]
                object_pixels = []
                dfs(row, col, color, object_pixels)
                objects.append((color, object_pixels))
    return objects

def get_target_color(grid: np.ndarray, objects:List[Tuple[int, List[Tuple[int, int]]]]) -> int:
    """
    Determines target color for removal - most common non-black color.
    Handles edge cases of 0 and single non-black color cases.

    Args:
        grid: grid to analyze.
        objects: object list, as produced by find_objects

    Returns:
        Target color integer, 0 if no target is found
    """
    color_counts = {}
    rows, cols = grid.shape
    
    # edge cases:
    # all black
    if len(objects) == 0:
        return 0

    # single color, other than black
    colors = set([color for color, _ in objects])
    if len(colors) == 1:
        return colors.pop()
    
    # multiple colors - find most common
    for color, pixels in objects:
        if color != 0:  # Exclude black
            color_counts[color] = color_counts.get(color, 0) + len(pixels)
    
    if not color_counts: # only black
        return 0
    
    return max(color_counts, key=color_counts.get)


def transform(input_grid: List[List[int]]) -> List[List[int]]:
    """
    Transforms the input grid according to the rules.
    """
    grid = np.array(input_grid)
    rows, cols = grid.shape
    output_grid = np.zeros_like(grid)

    # Find objects
    objects = find_objects(grid)
    
    # Determine target color - most common non-black
    target_color = get_target_color(grid, objects)
    
    # special case for blue (1)
    if target_color == 1:
        for color, pixels in objects:
            if color == 1:
                # check contiguity and top location
                contiguous_top = False
                if pixels:
                    min_row = min(row for row, _ in pixels)
                    # consider top if any part of object is at top
                    if min_row == 0:
                        # build grid to use find_objects to check contiguity
                        temp_grid = np.zeros_like(grid)
                        for r, c in pixels:
                            temp_grid[r,c] = 1
                        blue_objects = find_objects(temp_grid)
                        # if only one object, it's contigious!
                        if len(blue_objects) == 1:
                            contiguous_top = True

                if contiguous_top:  # keep object
                    for row, col in pixels:
                         output_grid[row, col] = color
            # all other colors copied to output
            elif color != 0:
                for row, col in pixels:
                    output_grid[row, col] = color
    else: # not blue
        for color, pixels in objects:
            if color != target_color and color != 0:  # Keep if not target color and not black
                for row, col in pixels:
                    output_grid[row, col] = color

    return output_grid.tolist()