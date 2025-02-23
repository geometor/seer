"""
The output grid represents a condensed version of the input, selecting a representative row of largest objects of each color from input.

Transformation Rule:
1. Identify the largest object of each unique color in the input grid.
2. Find the bounding box that encloses the largest object for each color.
3. Extract the first row of each bounding box, taking only the first 3 pixels.
4. Assemble the output grid with these rows, maintaining the order of colors corresponding to the sizes of the objects, largest to smallest.
"""

import numpy as np
from collections import Counter

def get_objects(grid):
    """Finds contiguous objects in a grid."""
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def get_neighbors(r, c):
        neighbors = []
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < grid.shape[0] and 0 <= nc < grid.shape[1]:
                neighbors.append((nr, nc))
        return neighbors

    def dfs(row, col, color):
        if visited[row, col] or grid[row, col] != color:
            return []
        visited[row, col] = True
        object_pixels = [(row, col)]
        for r, c in get_neighbors(row, col):
            object_pixels.extend(dfs(r, c, color))
        return object_pixels

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if not visited[row, col]:
                color = grid[row, col]
                object_pixels = dfs(row, col, color)
                if object_pixels:
                    objects.append({
                        'color': color,
                        'pixels': object_pixels,
                        'size': len(object_pixels)
                    })
    return objects

def get_bounding_box(pixels):
    """Calculates the bounding box of a set of pixels."""
    min_row = min(p[0] for p in pixels)
    max_row = max(p[0] for p in pixels)
    min_col = min(p[1] for p in pixels)
    max_col = max(p[1] for p in pixels)
    return min_row, max_row, min_col, max_col

def transform(input_grid):
    """Transforms the input grid according to the specified rule."""

    # Find objects in the input grid
    objects = get_objects(input_grid)

    # Find the largest object for each color
    largest_objects = {}
    for obj in objects:
        color = obj['color']
        if color not in largest_objects or obj['size'] > largest_objects[color]['size']:
            largest_objects[color] = obj

    # Sort largest objects by size in descending order
    sorted_largest_objects = sorted(largest_objects.values(), key=lambda x: x['size'], reverse=True)
    
    # Initialize the output grid
    output_grid = np.zeros((len(sorted_largest_objects), 3), dtype=int)

    # Extract the first row of the bounding box for each largest object
    for i, obj in enumerate(sorted_largest_objects):
        min_row, max_row, min_col, max_col = get_bounding_box(obj['pixels'])
        first_row = input_grid[min_row, min_col:min_col + 3]
        
        # Pad with zeros if the row has fewer than 3 pixels
        if len(first_row) < 3:
          padding = np.zeros(3-len(first_row), dtype=int)
          first_row = np.concatenate((first_row, padding))

        output_grid[i, :] = first_row

    return output_grid