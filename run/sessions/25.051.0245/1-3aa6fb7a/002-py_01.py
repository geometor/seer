"""
For each connected component of color 8 in the input grid:
1. Identify all cells that form the connected component of color 8.
2. For each cell in this component, count the number of its neighbors (up, down, left, right) that are also part of the same component.
3. Determine the "end points" of the component. An "end point" is a cell that has exactly one neighbor within the same color 8 component.
4. Find the "top-most end point" among all identified end points. This is the end point with the minimum row index. If there's a tie in row indices, choose the one with the minimum column index.
5. Find the "bottom-most end point" among all identified end points. This is the end point with the maximum row index. If there's a tie in row indices, choose the one with the minimum column index.
6. In the output grid, place a color 1 (blue) cell immediately to the right of the "top-most end point".
7. In the output grid, place a color 1 (blue) cell immediately to the left of the "bottom-most end point".
8. If a grid cell is not modified by steps 6 or 7, it retains its original color from the input grid.
"""

import numpy as np

def get_neighbors(grid, r, c):
    """ Get valid neighbors of a cell. """
    rows, cols = grid.shape
    neighbors = []
    if r > 0:
        neighbors.append((r - 1, c))
    if r < rows - 1:
        neighbors.append((r + 1, c))
    if c > 0:
        neighbors.append((r, c - 1))
    if c < cols - 1:
        neighbors.append((r, c + 1))
    return neighbors

def find_connected_components(grid, color):
    """ Find all connected components of a given color. """
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    components = []

    def dfs(r, c, current_component):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
                visited[r, c] or grid[r, c] != color):
            return
        visited[r, c] = True
        current_component.append((r, c))
        for nr, nc in get_neighbors(grid, r, c):
            dfs(nr, nc, current_component)

    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == color and not visited[r, c]:
                current_component = []
                dfs(r, c, current_component)
                components.append(current_component)
    return components

def find_end_points(grid, component):
    """ Find end points in a component. """
    end_points = []
    for r, c in component:
        neighbors = get_neighbors(grid, r, c)
        count = 0
        for nr, nc in neighbors:
            if (nr, nc) in component:
                count += 1
        if count == 1:
            end_points.append((r, c))
    return end_points

def find_top_most_end_point(end_points):
    """ Find the top-most end point. """
    return min(end_points, key=lambda x: (x[0], x[1]))

def find_bottom_most_end_point(end_points):
    """ Find the bottom-most end point. """
    return max(end_points, key=lambda x: (x[0], x[1]))

def transform(input_grid):
    """ Transform the input grid according to the specified rules. """
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    components = find_connected_components(input_grid, 8)

    for component in components:
        end_points = find_end_points(input_grid, component)
        if end_points:
            top_most = find_top_most_end_point(end_points)
            bottom_most = find_bottom_most_end_point(end_points)

            # Place color 1 to the right of top-most
            if top_most[1] + 1 < output_grid.shape[1]:
                output_grid[top_most[0], top_most[1] + 1] = 1

            # Place color 1 to the left of bottom-most
            if bottom_most[1] - 1 >= 0:
                output_grid[bottom_most[0], bottom_most[1] - 1] = 1

    return output_grid