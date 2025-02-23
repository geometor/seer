"""
1.  **Identify Objects:** Locate all non-zero pixels (objects) in the input grid.
2.  **Special Rules:**
    *   **Yellow (4) Stacking (Conditional):** IF there are any yellow (4) objects, move them to column 0.  The highest row index where a yellow object can be placed is row 3. Place yellow objects one per row, filling downward from row 3.
3.  **General Rule - Column and Vertical Order Preservation:** All objects *retain their original column index*. Within each column, objects maintain their relative vertical order from the input grid. Objects are shifted down to the *lowest available* rows in their respective columns. "Available" rows are those not occupied by objects placed due to special rules.
"""

import numpy as np

def get_objects(grid):
    objects = []
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] != 0:
                objects.append({"value": grid[r, c], "row": r, "col": c})
    return objects

def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    rows, cols = input_grid.shape

    # get objects
    objects = get_objects(input_grid)

    # separate yellow objects
    yellow_objects = [obj for obj in objects if obj["value"] == 4]
    other_objects = [obj for obj in objects if obj["value"] != 4]

    # ---- Special Rules ----
    # place yellow objects
    yellow_row = 3
    for obj in yellow_objects:
        if yellow_row < rows:
            output_grid[yellow_row, 0] = 4
            yellow_row += 1

    # Determine available rows AFTER special rules
    available_rows = []
    if yellow_objects:
        available_rows = [r for r in range(rows) if r not in range(3, yellow_row)]
    else:
        available_rows = [r for r in range(rows)]


    # ---- General Rule -----
    # place other objects, preserving column and relative order
    objects_by_column = {}
    for obj in other_objects:
        col = obj["col"]
        if col not in objects_by_column:
            objects_by_column[col] = []
        objects_by_column[col].append(obj)

    for col in sorted(objects_by_column.keys()):
        objects_by_column[col].sort(key=lambda x: x["row"])  # Sort by original row
        row_index = len(available_rows) - 1  # start at the lowest available row

        for obj in objects_by_column[col]:
            if row_index >= 0:
                output_grid[available_rows[row_index], obj["col"]] = obj["value"]
                row_index -= 1

    return output_grid