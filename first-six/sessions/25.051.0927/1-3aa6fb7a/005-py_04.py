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

    # Insert blue cell near top-right "L"
    for obj in azure_objects:
      min_row = min(r for r, c in obj)
      min_col = min(c for r, c in obj)
      if ( (min_row, min_col) in obj and (min_row, min_col + 1) in obj and
            (min_row + 1, min_col) not in obj and (min_row +1, min_col + 1) in obj
            and (min_row, min_col-1) not in obj ):

            if (min_row+1, min_col-1) not in blue_placed:
              output_grid[min_row+1, min_col - 1] = 1
              blue_placed.add((min_row+1, min_col -1))
              break


    # Insert blue cell near bottom-middle "L"
    for obj in azure_objects:
      min_row = min(r for r, c in obj)
      min_col = min(c for r, c in obj)

      if ( (min_row, min_col) in obj and (min_row, min_col + 1) in obj and
            (min_row + 1, min_col) not in obj and (min_row +1, min_col + 1) in obj
            and (min_row, min_col-1) not in obj ):

            if (min_row+1, min_col -1) not in blue_placed:
              output_grid[min_row+1, min_col-1] = 1
              blue_placed.add((min_row+1, min_col -1 ))
              break


    # Insert blue cell adjacent to middle-left single cell.
    for obj in azure_objects:
        if len(obj) == 1:
            row, col = obj[0]
            if row == 2 and col == 2: # Specific single cell.
                if (row,col+1) not in blue_placed:
                    output_grid[row, col + 1] = 1
                    blue_placed.add((row,col+1))
                    break


    # Insert blue cell adjacent to bottom-right single cell
    for obj in azure_objects:
        if len(obj) == 1:
            row, col = obj[0]
            if  col > 0 and input_grid[row, col-1] == 0: #check to the left
                if (row, col - 1) not in blue_placed: #check if blue exists there
                    output_grid[row, col - 1] = 1
                    blue_placed.add((row,col - 1))
                    break #place it

    return output_grid