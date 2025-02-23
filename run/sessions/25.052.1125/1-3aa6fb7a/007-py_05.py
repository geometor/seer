import numpy as np

def find_objects(grid, color):
    objects = []
    visited = set()

    def dfs(r, c, current_object):
        if (r, c) in visited or r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, current_object)
        dfs(r, c - 1, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def transform(input_grid):
    output_grid = np.copy(input_grid)
    azure_objects = find_objects(input_grid, 8)

    for obj in azure_objects:
        obj.sort(key=lambda x: (x[0], x[1]))
        rows = [cell[0] for cell in obj]
        cols = [cell[1] for cell in obj]

        if len(set(cols)) == 1 and len(obj) > 1:  # Vertical Line
            top_cell = obj[0]
            if top_cell[1] + 1 < output_grid.shape[1]: # Boundary Check
              output_grid[top_cell[0], top_cell[1] + 1] = 1

        elif len(set(rows)) == 1 and len(obj) > 1:  # Horizontal Line
            right_cell = obj[-1]
            if right_cell[1] - 1 >= 0:  # Boundary check
                output_grid[right_cell[0], right_cell[1] - 1] = 1

        elif len(obj) == 3: # L-shape
            # Find corner
            row_counts = {}
            col_counts = {}
            for r in rows:
                row_counts[r] = row_counts.get(r,0) + 1
            for c in cols:
                col_counts[c] = col_counts.get(c,0) + 1

            corner_row = [r for r, count in row_counts.items() if count > 1][0]
            corner_col = [c for c, count in col_counts.items() if count > 1][0]
            
            # Determine corner direction and check boundaries
            if corner_row > min(rows) and corner_row -1 >= 0:
              output_grid[corner_row - 1, corner_col] = 1

    return output_grid