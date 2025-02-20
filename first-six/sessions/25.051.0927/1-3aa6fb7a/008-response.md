# 1-3aa6fb7a • 008 • refine_code - CODE

---
```python
"""
Transforms an input grid by placing blue (1) cells adjacent to azure (8) cells based on the shape and orientation of the azure objects.

1. **Identify Azure Objects:** Find all contiguous regions of azure (8) colored cells.
2. **Classify Azure Objects:** Determine if each azure object is a single cell or an "L" shape.
3. **Place Blue Cells:**
   - **Single Cell:** Place a blue cell to the left of the azure cell if the space is empty (0).  If the left side is occupied, place it to the right if that space is empty.
   - **"L" Shape (Variant 1: [[8, 8], [0, 8]]):** Place a blue cell to the top-right of the "L".
   - **"L" Shape (Variant 2: [[8, 8], [8, 0]]):** Place a blue cell to the top-left of the "L".
4. **Avoid Overwrites:** Do not place a blue cell on top of any existing non-zero cell.
"""

import numpy as np

def find_objects(grid, color):
    """Finds objects of a specific color in the grid."""
    objects = []
    visited = set()

    def dfs(row, col):
        """Depth-first search to find contiguous regions."""
        if (row, col) in visited or not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != color:
            return []
        visited.add((row, col))
        region = [(row, col)]
        region.extend(dfs(row + 1, col))
        region.extend(dfs(row - 1, col))
        region.extend(dfs(row, col + 1))
        region.extend(dfs(row, col - 1))
        return region

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == color and (i, j) not in visited:
                objects.append(dfs(i, j))
    return objects

def transform(input_grid):
    """Transforms the input grid according to the described rule."""
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)
    blue_placed = set()  # Keep track of where blue cells have been placed.

    # Iterate through azure objects
    for obj in azure_objects:
        min_row = min(r for r, c in obj)
        min_col = min(c for r, c in obj)
        max_row = max(r for r,c in obj)
        max_col = max(c for r,c in obj)

        # Check for "L" shape:  [[8, 8], [0, 8]]
        if ( (min_row, min_col) in obj and (min_row, min_col + 1) in obj and
             (min_row + 1, min_col) not in obj and (min_row +1, min_col + 1) in obj
             and (min_row-1, min_col+1) not in obj):

            if (min_row-1, min_col+2) not in blue_placed and 0<=min_row-1<output_grid.shape[0] and 0<=min_col+2<output_grid.shape[1] and output_grid[min_row-1, min_col+2] == 0:
              output_grid[min_row-1, min_col + 2] = 1
              blue_placed.add((min_row-1, min_col +2))
              continue #Prioritize

        # Check for "L" shape: [[8, 8], [8, 0]]
        if ( (min_row, min_col) in obj and (min_row, min_col + 1) in obj and
             (min_row + 1, min_col) in obj and (min_row +1, min_col + 1) not in obj
             and (min_row - 1, min_col) not in obj ):

             if (min_row-1, min_col-1) not in blue_placed and 0<=min_row-1<output_grid.shape[0] and 0<=min_col-1<output_grid.shape[1] and output_grid[min_row-1, min_col-1] == 0:
                output_grid[min_row-1, min_col - 1] = 1
                blue_placed.add((min_row-1, min_col-1))
                continue #Prioritize


        # Check for single azure cells
        if len(obj) == 1:
            row, col = obj[0]
            # Check left neighbor, then right neighbor. Prioritize left placement
            if col > 0 and input_grid[row, col - 1] == 0:
                if (row, col - 1) not in blue_placed:
                    output_grid[row, col - 1] = 1
                    blue_placed.add((row, col - 1))
                    continue #Prioritize

            elif col < input_grid.shape[1] - 1 and input_grid[row, col + 1] == 0:
                if (row, col + 1) not in blue_placed:
                    output_grid[row, col + 1] = 1
                    blue_placed.add((row, col + 1))
                    continue #Prioritize

    return output_grid
```

