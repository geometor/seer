"""
1.  **Identify Objects:** Locate all non-zero pixels (objects) within the input grid.
2.  **Column Preservation:**  Each object *retains its original column index* in the output grid.
3. **Yellow Stack:** The Yellow (4) objects move to the highest available row index for column index 0, one per row, starting at row index 3 and filling rows below.
4.  **Object Ordering - Vertical Shift:** Other objects keep their column and shift down to the lowest available rows, but their *relative vertical order is preserved*. If two objects start in the same column, the object higher in the input will remain higher in the output within the "available" rows. Available means rows that aren't occupied after the yellows have been stacked.
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

    # place yellow objects
    yellow_row = 3
    for obj in yellow_objects:
        if yellow_row < rows:
          output_grid[yellow_row, 0] = 4
          yellow_row += 1

    # place other objects, preserving column and relative order
    available_rows = [r for r in range(rows) if r not in range(3, yellow_row)]
    objects_by_column = {}
    for obj in other_objects:
        col = obj["col"]
        if col not in objects_by_column:
            objects_by_column[col] = []
        objects_by_column[col].append(obj)

    for col in sorted(objects_by_column.keys()):
        objects_by_column[col].sort(key=lambda x: x["row"])  # Sort by original row
        row_index = len(available_rows)-1 # start at the lowest available row index

        for obj in objects_by_column[col]:
            if row_index >=0:
                output_grid[available_rows[row_index], obj["col"]] = obj["value"]
                row_index -= 1


    return output_grid