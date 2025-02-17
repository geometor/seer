import numpy as np

def get_objects(grid):
    """
    Finds contiguous regions of the same color in a grid.
    """
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(r, c, color, obj):
        if (r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or
                visited[r, c] or grid[r, c] != color):
            return
        visited[r, c] = True
        obj.append((r, c))
        dfs(r + 1, c, color, obj)
        dfs(r - 1, c, color, obj)
        dfs(r, c + 1, color, obj)
        dfs(r, c - 1, color, obj)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if not visited[r, c] and grid[r, c] != 0:
                obj = []
                dfs(r, c, grid[r, c], obj)
                objects.append(obj)
    return objects

def split_object_by_contiguity(obj, grid):
    """
    Splits the object into parts based on contiguity.
    """
    single_contiguous_parts = []
    other_parts = []

    for r, c in obj:
        neighbors = 0
        # Check adjacent cells (not diagonally)
        if (r + 1, c) in obj: neighbors += 1
        if (r - 1, c) in obj: neighbors += 1
        if (r, c + 1) in obj: neighbors += 1
        if (r, c - 1) in obj: neighbors += 1

        # If a position as only a single vertical connection with
        # neighbors, it goes into single_contiguous_vertical
        is_single_vertical = False
        if neighbors <= 2:
            if ((r+1,c) in obj and (r-1,c) in obj) and not ((r,c+1) in obj or (r,c-1) in obj):
                is_single_vertical = True
            elif neighbors == 1 and ( (r+1, c) in obj or (r-1,c) in obj):
                is_single_vertical = True


        if is_single_vertical:
            single_contiguous_parts.append((r, c))
        else:
            other_parts.append((r, c))
    return single_contiguous_parts, other_parts

def transform(input_grid):
    """
    Transforms the input grid according to the described rule.
    """

    output_grid = np.copy(input_grid)
    objects = get_objects(input_grid)

    for obj in objects:
        if input_grid[obj[0]] == 5:  # Assuming color 5 is the object to modify
            single_parts, other_parts = split_object_by_contiguity(obj, input_grid)

            for r, c in single_parts:
                output_grid[r, c] = 2  # Recolor single contiguous parts to 2

            for r, c in other_parts:
                output_grid[r, c] = 8 # Recolor other parts to 8

    return output_grid