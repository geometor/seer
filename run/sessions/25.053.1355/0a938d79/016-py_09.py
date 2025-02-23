"""
1.  **Identify Objects:** Find all the non-zero pixels in the input grid. Each of these is considered an "object". Note their color and initial position.

2.  **Determine the Axis of Extension**:
    *   If all objects are in one row, then the axis of extension is `column`.
    *   If all objects are in one column, then the axis of extension is `row`.
    *   Otherwise, if there is an initial pattern in rows, extend by `row`, else if the pattern is in columns, extend by `column`

3.  **Identify the Color Pattern**:
    *   Create an ordered list of the unique colors, this establishes the replication pattern.
    *   If the objects span multiple rows and/or columns, consider their initial relative positions to maintain the pattern during extension.

4.  **Extend the Pattern:**
    *   **Horizontal Extension (Column Axis):** For each object, extend its color horizontally along its row, creating copies to the left and right, maintaining the original pattern spacing and order with other colors. The pattern is continued to the edge of the grid.
    *   **Vertical Extension (Row Axis):** For each object, extend its color vertically along its column, creating copies above and below, maintaining the original pattern spacing and order with other colors. The pattern is continued to the edge of the grid.

5.  **Maintain Relative Positions**: When extending, if objects had initial relative positions (e.g., color A was two columns to the left of color B), ensure this relative positioning is maintained during the extension.
"""

import numpy as np

def find_objects(grid):
    """Finds all unique non-zero colored pixels and their positions."""
    objects = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] != 0:
                objects.append((grid[i, j], (i, j)))
    # remove duplicate color entries
    unique_objects = []
    seen_colors = set()
    for color, pos in objects:
        if color not in seen_colors:
            unique_objects.append((color, pos))
            seen_colors.add(color)

    return unique_objects

def determine_axis(objects):
    """Determines the axis of replication (row or column)."""
    if not objects:
        return "row"  # Default to row if no objects

    rows = set()
    cols = set()
    for _, (row, col) in objects:
        rows.add(row)
        cols.add(col)

    if len(rows) == 1:
        return "column"
    elif len(cols) == 1:
        return "row"
    else:
        # Check for an initial row or column pattern
        row_diffs = []
        col_diffs = []

        if len(objects) > 1:
             # Sort objects by row and then by column
            objects.sort(key=lambda x: (x[1][0], x[1][1]))

            for i in range(len(objects) - 1):
                row_diffs.append(objects[i+1][1][0] - objects[i][1][0])
                col_diffs.append(objects[i+1][1][1] - objects[i][1][1])

            if all(c == 0 for c in col_diffs):
                return "row" # Pattern in rows
            elif all(r == 0 for r in row_diffs):
                return "column" # Pattern in columns
        return "row"

def extend_pattern(grid, objects, axis):
    """Extends the pattern horizontally or vertically."""
    output_grid = np.zeros_like(grid)
    
    if axis == "column":
        # Horizontal extension
        for color, (row, col) in objects:
            output_grid[row, :] = color
            
            # Get all object of same row
            row_objects = [obj for obj in objects if obj[1][0] == row]
            row_objects.sort(key=lambda x: x[1][1]) # sort by column
            
            if len(row_objects) > 1:
                # extend between each object
                for i in range(len(row_objects)-1):
                    color1, (_, col1) = row_objects[i]
                    color2, (_, col2) = row_objects[i+1]
                    
                    for j in range(col1+1, col2):
                        output_grid[row, j] = color2 if (j - col1) % 2 == 1 else color1

                
                first_color = row_objects[0][0]
                last_color = row_objects[-1][0]
                
                _, first_col = row_objects[0][1]
                _, last_col = row_objects[-1][1]
                
                # extend to the edges
                color = first_color
                for j in range(first_col -1, -1, -1):
                    color = (last_color if color == first_color else first_color) if len(row_objects) > 1 else color
                    output_grid[row, j] = color

                color = last_color
                for j in range(last_col + 1, grid.shape[1]):
                    color = (first_color if color == last_color else last_color) if len(row_objects) > 1 else color
                    output_grid[row, j] = color

    elif axis == "row":
        # Vertical extension
        for color, (row, col) in objects:
            output_grid[:, col] = color

            # Get all object of same column
            col_objects = [obj for obj in objects if obj[1][1] == col]
            col_objects.sort(key=lambda x: x[1][0]) # sort by row
            if len(col_objects) > 1:

                # extend between each objects
                for i in range(len(col_objects)-1):
                    color1, (row1, _) = col_objects[i]
                    color2, (row2, _) = col_objects[i+1]

                    for i in range(row1 + 1, row2):
                        output_grid[i, col] = color2 if (i - row1) % 2 == 1 else color1

                first_color = col_objects[0][0]
                last_color = col_objects[-1][0]
                
                first_row,_ = col_objects[0][1]
                last_row, _ = col_objects[-1][1]

                # extend to the edge
                color = first_color
                for i in range(first_row - 1, -1, -1):
                    color = (last_color if color == first_color else first_color) if len(col_objects) > 1 else color
                    output_grid[i, col] = color

                color = last_color
                for i in range(last_row + 1, grid.shape[0]):
                    color = (first_color if color == last_color else last_color) if len(col_objects) > 1 else color
                    output_grid[i, col] = color

    return output_grid

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)

    # Find all non-zero colored pixels (objects)
    objects = find_objects(input_grid)

    if not objects:
        return output_grid

    # Determine the axis of replication
    axis = determine_axis(objects)

    # Extend pattern
    output_grid = extend_pattern(input_grid, objects, axis)

    return output_grid