"""
1.  **Identify Objects:** Treat each contiguous block of non-zero pixels of the same color as an object.
2.  **Horizontal Replication and Mirroring:** For each row containing a non-zero pixel, replicate the non-zero pixels horizontally across the entire row. If there are multiple distinct objects, alternate their colors. Mirror the object on the edge of the row to the opposite edge.
3. **Row Filling:** Fill the spaces between replicated objects with the same pattern of colors in the original objects on that row.
4. **Row Duplication:** Duplicate rows with the outermost objects (e.g. row 2 and 18 in example 3).
"""

import numpy as np

def get_objects(grid):
    """Identifies objects (non-white pixels) and their locations."""
    objects = []
    for r in range(grid.shape[0]):
        row_objects = []
        for c in range(grid.shape[1]):
            if grid[r, c] != 0:
                row_objects.append((r, c, grid[r, c]))
        if row_objects:
            objects.append(row_objects)
    return objects


def transform(input_grid):
    # initialize output_grid
    output_grid = np.zeros_like(input_grid)
    
    # Identify Objects on each row
    objects_by_row = get_objects(input_grid)

    # Iterate through rows with objects
    for row_objects in objects_by_row:
        row = row_objects[0][0]  # Get the row number
        row_colors = [obj[2] for obj in row_objects]  # original object colors
        
        # Horizontal replication
        for col in range(output_grid.shape[1]):
          output_grid[row, col] = row_colors[col % len(row_colors)]

        # Mirror outer object
        first_object_col = row_objects[0][1]
        last_object_col = row_objects[-1][1]
        if first_object_col==last_object_col:
          output_grid[row,0] = input_grid[row,first_object_col]
          output_grid[row,-1] = input_grid[row,first_object_col]
        else:
          output_grid[row,0] = input_grid[row, last_object_col]
          output_grid[row,-1] = input_grid[row, first_object_col]

    # duplicate outer filled rows
    outer_rows=[]
    for r in range(input_grid.shape[0]):
      if np.any(input_grid[r]!=0):
        outer_rows.append(r)
    if len(outer_rows)>0:
      first_row = outer_rows[0]
      last_row = outer_rows[-1]
      for r in range(input_grid.shape[0]):
        if np.any(output_grid[r]!=0):
          if r==first_row:
            for i in range(r):
              output_grid[i,:] = output_grid[r,:]
          if r==last_row:
            for i in range(r+1,input_grid.shape[0]):
              output_grid[i,:] = output_grid[r,:]
    
    return output_grid