# 6aa20dc0 • 008 • example_2 • investigate_coder

---
```python
"""
Transforms an input grid by expanding colored shapes based on their adjacency to other shapes.

1. **Identify Objects:** Locate all contiguous regions of non-yellow pixels. These are the "colored shapes." Each shape is identified by its unique color (1, 2, or 6).

2. **Detect Contact Points:** For each colored shape, examine its perimeter (both side-by-side and diagonal neighbors). Identify any pixels where different colored shapes are adjacent.

3. **Conditional Expansion - Blue (1):** If a blue shape touches another blue shape, do not expand the blue shape at that adjacency. If a blue shape touches shapes of a *different* color, then fill all adjacent yellow cells in the *entire grid* with the same color and value as the original colored shape.

4. **Conditional Expansion - Red (2):** If a red shape touches other shapes of a *different* color, then extend a single continuous perimeter of the red shape around the the touching shape.

5. **Conditional Expansion - Magenta (6):** If a magenta shape touches shapes of a *different* color, then fill any immediately adjacent yellow cells with the color of the magenta shape.

6. **Background:** All remaining pixels retain their original yellow (4) color.

"""

import numpy as np

def get_objects(grid):
    """
    Finds all contiguous regions of non-yellow pixels, identifying them as distinct objects.
    """
    objects = {}
    visited = np.zeros_like(grid, dtype=bool)
    rows, cols = grid.shape

    def dfs(r, c, color, obj_id):
        if (r < 0 or r >= rows or c < 0 or c >= cols or visited[r, c] or grid[r, c] != color):
            return
        visited[r, c] = True
        objects[obj_id]['pixels'].append((r, c))
        dfs(r + 1, c, color, obj_id)
        dfs(r - 1, c, color, obj_id)
        dfs(r, c + 1, color, obj_id)
        dfs(r, c - 1, color, obj_id)
        dfs(r + 1, c + 1, color, obj_id)
        dfs(r - 1, c - 1, color, obj_id)
        dfs(r + 1, c - 1, color, obj_id)
        dfs(r - 1, c + 1, color, obj_id)


    obj_id_counter = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] != 4 and not visited[r, c]:
                objects[obj_id_counter] = {'color': grid[r, c], 'pixels': []}
                dfs(r, c, grid[r, c], obj_id_counter)
                obj_id_counter += 1
    return objects

def get_neighbors(grid, r, c):
    """Returns a list of (row, col) tuples for all 8 neighbors of a pixel."""
    rows, cols = grid.shape
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            nr, nc = r + i, c + j
            if 0 <= nr < rows and 0 <= nc < cols:
                neighbors.append((nr, nc))
    return neighbors

def expand_blue(grid, output_grid, objects):
   """Expands blue shapes based on the contact with different colored shapes."""
   for obj_id, obj_data in objects.items():
       if obj_data['color'] == 1:  # Blue object
           for r, c in obj_data['pixels']:
               neighbors = get_neighbors(grid, r, c)
               for nr, nc in neighbors:
                  if grid[nr,nc] != 4 and grid[nr,nc] != 1:
                     for r_out in range(output_grid.shape[0]):
                        for c_out in range(output_grid.shape[1]):
                           if output_grid[r_out, c_out] == 4:
                              for nr_out, nc_out in get_neighbors(output_grid, r_out, c_out):
                                 if (nr_out, nc_out) in obj_data['pixels']:
                                      output_grid[r_out,c_out] = 1

def expand_red(grid, output_grid, objects):

    for obj_id, obj_data in objects.items():
        if obj_data['color'] == 2:  # Red object
            for r, c in obj_data['pixels']:
                neighbors = get_neighbors(grid, r, c)
                for nr, nc in neighbors:
                    if grid[nr, nc] != 4 and grid[nr, nc] != 2:
                        #find contiguous shape
                        output_grid[r,c] = 2
                        target_obj = None
                        for other_id, other_data in objects.items():
                           if (nr,nc) in other_data['pixels']:
                              target_obj = other_data
                              break
                        #extend perimeter
                        if target_obj:
                            for tr, tc in target_obj['pixels']:
                                 target_neighbors = get_neighbors(grid, tr, tc)
                                 for tnr, tnc in target_neighbors:
                                    if grid[tnr,tnc] == 4:
                                        output_grid[tnr, tnc] = 2
                                        break


def expand_magenta(grid, output_grid, objects):
    """Expands magenta shapes by filling immediately adjacent yellow cells."""
    for obj_id, obj_data in objects.items():
        if obj_data['color'] == 6:  # Magenta object
            for r, c in obj_data['pixels']:
                neighbors = get_neighbors(grid, r, c)
                for nr, nc in neighbors:
                    if grid[nr, nc] == 4:  # Adjacent to yellow
                        output_grid[nr, nc] = 6


def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    objects = get_objects(input_grid)
    expand_blue(input_grid, output_grid, objects)
    expand_red(input_grid, output_grid, objects)
    expand_magenta(input_grid, output_grid, objects)


    return output_grid
```
