# ed36ccf7 • 018 • refine_coder

---
```python
"""
Identify objects in the grid. If the object is an "L" shape, rotate the "L" shape 90 degrees clockwise. If the object is a diagonal, do nothing.
"""

import numpy as np

def get_objects(grid):
    """
    Extracts non-zero objects from the grid.
    Returns a list of objects, where each object is a tuple of (coordinates, color).
    """
    objects = []
    visited = set()
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c, current_object, color):
        if (r, c) in visited or r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        dfs(r + 1, c, current_object, color)
        dfs(r - 1, c, current_object, color)
        dfs(r, c + 1, current_object, color)
        dfs(r, c - 1, current_object, color)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0 and (r, c) not in visited:
                current_object = []
                color = grid[r][c]
                dfs(r, c, current_object, color)
                objects.append((current_object, color))
    return objects

def rotate_point_around_center(point, rows, cols):
    """Rotates a point 90 degrees clockwise around the center of the grid."""
    r, c = point
    center_r = (rows - 1) / 2.0
    center_c = (cols - 1) / 2.0
    new_r = c - center_c + center_r
    new_c = -(r - center_r) + center_c
    return int(round(new_r)), int(round(new_c))

def is_L_shape(coords, rows, cols):
    """Checks if the coordinates form an L shape (regular or mirrored)."""
    if len(coords) != 3:
        return False

    coords_np = np.array(coords)
    diffs = np.diff(coords_np, axis=0)

    if len(diffs) < 2:
      return False
    
    if (diffs[0][0] == 0 or diffs[0][1] == 0) and (diffs[1][0] == 0 or diffs[1][1] == 0) :
        if (diffs[0][0] == 0 and diffs[1][1] == 0) or (diffs[0][1] == 0 and diffs[1][0] == 0):
           return True

    return False

def classify_l_shape(coords, rows, cols):
    """
    Classifies the orientation of an L-shape.
    Returns a string representing the orientation.
    """
    if not is_L_shape(coords, rows, cols):
        return "not_l"

    # Find the "corner" of the L
    corner = None
    for i in range(len(coords)):
        count = 0
        for j in range(len(coords)):
            if i != j:
                if abs(coords[i][0] - coords[j][0]) + abs(coords[i][1] - coords[j][1]) == 1:
                    count += 1
        if count == 2:
            corner = coords[i]
            break

    # Find the two points that are not the corner
    other_points = [p for p in coords if p != corner]

    # Determine the orientation based on the relative positions of the other points
    if other_points[0][0] == other_points[1][0]:  # Vertical leg
        if other_points[0][1] < corner[1]:
            if other_points[0][0] < corner[0]:
                return "upright" # upright
            else:
                return "rotated_180"
        else: # other_points[0][1] > corner[1]:
            if other_points[0][0] < corner[0]:
                return "rotated_270"  # L
            else:
                return "mirrored_horizontal"

    elif other_points[0][1] == other_points[1][1]:  # Horizontal leg
        if other_points[0][0] < corner[0]:
            if other_points[0][1] < corner[1]:
                return "rotated_90"
            else:
                return "mirrored_vertical"
        else:
            if other_points[0][1] < corner[1]:
                return "mirrored_270"
            else:
                return "mirrored_180" # mirrored and rotated
            
    return "unknown"  # Should not reach here for valid L-shapes

def rotate_l_shape(coords, rows, cols, l_type):
    """
    Rotates an L-shape 90 degrees clockwise, taking into account its specific orientation.
    """

    # helper maps for rotations
    rotation_map = {
        "upright": "rotated_90",
        "rotated_90": "rotated_180",
        "rotated_180": "rotated_270",
        "rotated_270": "upright",
        "mirrored_horizontal": "mirrored_90",
        "mirrored_90": "mirrored_180",
        "mirrored_180":"mirrored_270",
        "mirrored_270": "mirrored_horizontal",
        "mirrored_vertical": "mirrored_270",  # Adjust as needed
        "mirrored_270": "rotated_180",     # Adjust as needed
    }
    
    new_l_type = rotation_map[l_type]

    if new_l_type == "upright":
      # find top left and build from there
      min_r = min(c[0] for c in coords)
      min_c = min(c[1] for c in coords)
      return [(min_r,min_c), (min_r+1, min_c), (min_r+2, min_c), (min_r+2, min_c+1)]
    elif new_l_type == "rotated_90":
      min_r = min(c[0] for c in coords)
      min_c = min(c[1] for c in coords)
      return [(min_r, min_c), (min_r, min_c+1), (min_r, min_c+2), (min_r-1,min_c+2)]
    elif new_l_type == "rotated_180":
        min_r = min(c[0] for c in coords)
        min_c = min(c[1] for c in coords)
        # find the top-right
        return [(min_r+2, min_c+1), (min_r, min_c+1), (min_r+1, min_c+1), (min_r, min_c)]
    elif new_l_type == "rotated_270":
      # find bottom-right, and build
      max_r = max(c[0] for c in coords)
      max_c = max(c[1] for c in coords)
      return [(max_r, max_c), (max_r, max_c-1), (max_r, max_c-2), (max_r+1, max_c-2)]
    elif new_l_type == "mirrored_horizontal":
        min_r = min(c[0] for c in coords)
        max_c = max(c[1] for c in coords)
        return [(min_r, max_c), (min_r+1, max_c), (min_r+2, max_c), (min_r+2, max_c-1)]
    elif new_l_type == "mirrored_90":
        min_r = min(c[0] for c in coords)
        max_c = max(c[1] for c in coords)
        return [(min_r, max_c), (min_r-1, max_c), (min_r-2, max_c), (min_r - 2, max_c-1)]
    elif new_l_type == "mirrored_180":
        min_r = min(c[0] for c in coords)
        min_c = min(c[1] for c in coords)
        return [(min_r,min_c), (min_r+1, min_c), (min_r+2, min_c), (min_r,min_c+1)] # check
    elif new_l_type == "mirrored_270":
        max_r = max(c[0] for c in coords)
        min_c = min(c[1] for c in coords)
        return [(max_r,min_c), (max_r-1, min_c), (max_r - 2, min_c), (max_r-2, min_c+1)]
    elif new_l_type == "mirrored_vertical":
        max_r = max(c[0] for c in coords)
        max_c = max(c[1] for c in coords)
        return [(max_r, max_c), (max_r, max_c -1), (max_r, max_c - 2), (max_r-1, max_c-2)]

    # return original if not mapped
    return coords

def is_diagonal(coords, rows, cols):
    """Checks if the coordinates form a diagonal and returns its type ("main" or "anti")."""
    if len(coords) != rows:
      return False

    coords_set = set(coords)

    # Check for main diagonal
    is_main_diagonal = all((i, i) in coords_set for i in range(rows))
    if is_main_diagonal:
        return "main"

    # check for anti diagonal
    is_anti_diagonal = all((i, cols - 1 - i) in coords_set for i in range(rows))
    if is_anti_diagonal:
        return "anti"

    return False

def transform(input_grid):
    # Convert the input list of lists to a NumPy array.
    input_np = np.array(input_grid)
    rows, cols = input_np.shape

    # Get objects
    objects = get_objects(input_np)

    # initialize output grid
    output_np = np.zeros_like(input_np)

    for coords, color in objects:
        if is_L_shape(coords, rows, cols):
            # Classify and rotate L shape
            l_type = classify_l_shape(coords, rows, cols)
            new_coords = rotate_l_shape(coords, rows, cols, l_type)
            for r, c in new_coords:
                if 0 <= r < rows and 0 <= c < cols:
                    output_np[r, c] = color
        elif is_diagonal(coords, rows, cols):
          # diagonals don't change
            for r, c in coords:
              output_np[r,c] = color
        else:
          # everything else stays put
          for r, c in coords:
            output_np[r,c] = color

    # Convert the NumPy array back to a list of lists.
    output_grid = output_np.tolist()

    return output_grid
```
