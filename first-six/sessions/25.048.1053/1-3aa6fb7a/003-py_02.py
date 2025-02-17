import numpy as np

def find_l_shapes(grid, color):
    """
    Finds L-shaped objects of a specific color in the grid.
    Returns a list of corner coordinates.
    """
    objects = []
    visited = set()

    def is_valid(r, c):
        return 0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]

    def dfs(r, c, current_object):
        if (r, c) in visited or not is_valid(r, c) or grid[r, c] != color:
            return
        visited.add((r, c))
        current_object.append((r, c))

        neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for nr, nc in neighbors:
            dfs(nr, nc, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and (r, c) not in visited:
                current_object = []
                dfs(r, c, current_object)
                if len(current_object) >= 3: #L shapes have at least 3 pixels
                    # Find the corner
                    rows, cols = zip(*current_object)
                    # Count occurrences of each row and col
                    row_counts = {}
                    col_counts = {}

                    for row in rows:
                        row_counts[row] = row_counts.get(row, 0) + 1
                    for col in cols:
                        col_counts[col] = col_counts.get(col, 0) + 1

                    # Corner will have a row and col that occur more than once
                    corner = None
                    for r, c in current_object:
                       if row_counts[r] >1 and col_counts[c] > 1:
                          corner = (r,c)
                          break
                    if corner is not None:
                        objects.append(corner)
    return objects

def transform(input_grid):
    """
    Transforms the input grid by finding L-shaped objects of color 8,
    and changing their corner pixel color to 1.
    """
    output_grid = np.copy(input_grid)
    l_shapes = find_l_shapes(input_grid, 8)

    # Change the color of the identified corners
    for r, c in l_shapes:
        output_grid[r, c] = 1

    return output_grid