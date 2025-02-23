# AboveBelow7 • 006 • refine_coder

---
```python
"""
1.  **Identify Objects:**
    *   Find a contiguous "rectangle" object. A rectangle is defined as a block where the top row is solid, and the sides extend downward. It can have "dips", and isn't necessarily a perfect geometric rectangle. Record color, top-left, and bottom-right coordinates.
    *   Find a contiguous "U-shape" object. A U-shape is defined here as having two vertical columns of equal length, connected by a horizontal base. The connecting base can be any width, but must be complete. The open end of the "U" must point upwards. Record color, top-left, and bottom-right coordinates of its bounding box.
2.  **Handle Missing Objects:**
    *   If either object type isn't found, return the input unchanged.
3.  **Calculate Vertical Offsets:**
    *   Determine the vertical offset (difference in row number) between the top-left corner of the rectangle and the top-left corner of the U-shape.
4.  **Swap Positions by Translation:**
    *   Clear the original positions of both objects in a copy of the input grid.
    *   Redraw the rectangle, translating it *vertically* by the calculated offset. Apply a boundary check - if any translated position is outside the bounds of the grid, adjust the position to fit within bounds.
    *   Redraw the U-shape, translating it *vertically* by the *negative* of the calculated offset. Apply a boundary check - if any translated position is outside the bounds of the grid, adjust the position to fit within bounds.
5. **Output**: Output is the adjusted grid.
"""

import numpy as np

def find_rectangle(grid):
    """Finds a rectangle-like object in the grid."""
    rows, cols = np.where(grid != 0)
    if len(rows) == 0:
        return None

    min_row, max_row = np.min(rows), np.max(rows)
    min_col, max_col = np.min(cols), np.max(cols)

    # Find the most frequent color in the top row. We assume this is the rectangle color.
    top_row_colors = [grid[min_row, c] for c in range(min_col, max_col + 1)]
    if not top_row_colors:
        return None

    from collections import Counter
    color_counts = Counter(top_row_colors)
    color = color_counts.most_common(1)[0][0]  # most common color

    coords = []
    for r in range(min_row, max_row + 1):
        for c in range(min_col, max_col + 1):
            if grid[r,c] == color:
                coords.append((r,c))

    if len(coords) > 0:
       return{
            "name": "rectangle_1",
            "color": color,
            "shape": "rectangle",
            "top_left": (min_row, min_col),
            "bottom_right": (max_row, max_col),
            "coords": coords
        }
    return None
    

def find_u_shape(grid):
    """Finds a U-shape object in the grid."""
    rows, cols = np.where(grid != 0)
    if len(rows) == 0:
        return None

    min_row, max_row = np.min(rows), np.max(rows)
    min_col, max_col = np.min(cols), np.max(cols)
    
    for color in np.unique(grid[rows, cols]): # check each found color
        coords = []
        for r in range(min_row, max_row + 1):
            for c in range(min_col, max_col + 1):
                if grid[r,c] == color:
                    coords.append((r,c))

        # Check for U-shape (opening upwards)
        if len(coords) > 3: # Needs at least 4 for a u-shape
            # find left, right, bottom
            u_rows, u_cols = zip(*coords)  # Unzip coordinates

            left_col = min(u_cols)
            right_col = max(u_cols)
            bottom_row = max(u_rows)
            
            # basic validation for u-shape
            left_count = sum(1 for r, c in coords if c == left_col)
            right_count = sum(1 for r, c in coords if c == right_col)
            bottom_count = sum(1 for r, c in coords if r == bottom_row)

            if left_count >= 2 and right_count >= 2 and bottom_count >= 2 and left_count == right_count: # enforce equal length columns
                # check if base is complete
                base_complete = all(grid[bottom_row,c] == color for c in range(left_col, right_col + 1))
                if base_complete:
                    return{
                        "name": "u_shape_1",
                        "color": color,
                        "shape": "u-shape",
                        "top_left": (min_row, min_col),
                        "bottom_right": (max_row, max_col),
                        "coords": coords
                    }
    return None

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)

    # Identify Objects
    rectangle = find_rectangle(input_grid)
    u_shape = find_u_shape(input_grid)

    # Handle Missing Objects
    if rectangle is None or u_shape is None:
        return output_grid

    # Calculate Vertical Offset
    vertical_offset = u_shape["top_left"][0] - rectangle["top_left"][0]

    # Clear original positions
    for r, c in rectangle["coords"]:
        output_grid[r, c] = 0
    for r, c in u_shape["coords"]:
        output_grid[r, c] = 0

    # Swap Positions by Translation: Rectangle
    for r, c in rectangle["coords"]:
        new_r = r + vertical_offset
        new_r = max(0, min(new_r, output_grid.shape[0] - 1))  # Boundary check and correction
        output_grid[new_r, c] = rectangle["color"]

    # Swap Positions by Translation: U-Shape
    for r, c in u_shape["coords"]:
        new_r = r - vertical_offset
        new_r = max(0, min(new_r, output_grid.shape[0] - 1))  # Boundary check and correction
        output_grid[new_r, c] = u_shape["color"]
        
    return output_grid
```
