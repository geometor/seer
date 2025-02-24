def count_connected_components(grid, color):
    """
    Counts the number of distinct connected components of a given color in the grid.
    Uses Depth First Search.
    """
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    count = 0

    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols or visited[row, col] or grid[row, col] != color:
            return
        visited[row, col] = True
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and not visited[r, c]:
                dfs(r, c)
                count += 1
    return count
