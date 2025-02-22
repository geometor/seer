"""
The transformation rule involves identifying azure (8) objects and changing the color of specific azure pixels within each object's line segments to blue (1). The selection of the pixel to change depends on segment orientation:

1.  **Object Identification:** Find all distinct azure objects (connected components) in the input grid.
2.  **Segment Identification:** For each azure object, identify all horizontal and vertical line segments.
3.  **Segment Transformation - Vertical:** Within each vertical line segment, change the second azure pixel from the top to blue.
4.  **Segment Transformation - Horizontal:** Within each horizontal line segment, change the second azure pixel from the left to blue.
5.  **Output:** The output grid is a copy of the input grid with the identified pixel color changes.
"""

import numpy as np

def find_objects(grid):
    """
    Identifies distinct objects in the grid.  Assumes background is color 0.
    Returns a list of objects, where each object is a list of (row, col) coordinates.
    """
    objects = []
    visited = set()
    rows, cols = grid.shape

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c, current_object, color):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(r + dr, c + dc, current_object, color)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != 0 and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object, grid[r,c])
                objects.append(current_object)
    return objects

def find_segments(obj):
    """
    Identifies horizontal and vertical line segments within an object.
    Returns a tuple of two lists: (vertical_segments, horizontal_segments)
    Each segment is a list of (row, col) coordinates.
    """
    vertical_segments = []
    horizontal_segments = []

    # Find vertical segments
    cols = sorted(list(set([c for r, c in obj])))
    for col in cols:
        segment = sorted([(r, c) for r, c in obj if c == col])
        if len(segment) > 1:
            vertical_segments.append(segment)

    # Find horizontal segments
    rows = sorted(list(set([r for r, c in obj])))
    for row in rows:
        segment = sorted([(r, c) for r, c in obj if r == row])
        if len(segment) > 1:
            horizontal_segments.append(segment)

    return vertical_segments, horizontal_segments

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    objects = find_objects(input_grid)

    # change output pixels
    for obj in objects:
        # Process only azure objects
        if any(input_grid[r, c] != 8 for r, c in obj):
            continue

        vertical_segments, horizontal_segments = find_segments(obj)

        # Transform vertical segments
        for segment in vertical_segments:
            if len(segment) >= 2:
                r, c = segment[1]  # Second from the top
                output_grid[r, c] = 1

        # Transform horizontal segments
        for segment in horizontal_segments:
            if len(segment) >= 2:
                r, c = segment[1]  # Second from the left
                output_grid[r, c] = 1

    return output_grid