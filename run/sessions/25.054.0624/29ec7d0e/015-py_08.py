import numpy as np
from typing import List, Tuple

def find_connected_component(grid, start_row, start_col, visited):
    """
    Finds the connected component starting from a given seed pixel using Depth-First Search (DFS).
    """
    rows, cols = grid.shape
    component = []
    color = grid[start_row,start_col]

    def dfs(row, col):
        if (
            row < 0
            or row >= rows
            or col < 0
            or col >= cols
            or visited[row, col]
            or grid[row,col] != color
        ):
            return

        visited[row, col] = True
        component.append((row, col))

        # Explore adjacent cells (including diagonals)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                dfs(row + dr, col + dc)

    dfs(start_row, start_col)
    return component

def analyze_example(input_grid):
    """Analyzes a single input grid."""
    rows, cols = input_grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    white_pixel_count = 0
    components = []

    for r in range(rows):
        for c in range(cols):
            if input_grid[r, c] == 0 and not visited[r,c]:
                component = find_connected_component(input_grid, r, c, visited)
                components.append(component)
            if input_grid[r,c] == 0:
                white_pixel_count +=1

    component_sizes = [len(comp) for comp in components]
    print(f"  White pixel count: {white_pixel_count}")
    print(f"  Number of white components: {len(components)}")
    print(f"  White component sizes: {component_sizes}")
    # bounding box info
    for i, component in enumerate(components):
        min_row = min(p[0] for p in component)
        max_row = max(p[0] for p in component)
        min_col = min(p[1] for p in component)
        max_col = max(p[1] for p in component)
        print(f"  Component {i+1} bounding box: ({min_row}, {min_col}) - ({max_row}, {max_col})")


# Load the example grids (replace with your actual data loading)
example_inputs = [
    np.array([
        [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 3, 0, 0, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3],
        [1, 3, 5, 0, 0, 1, 3, 5, 2, 4, 0, 0, 5, 2, 4, 1, 3, 5],
        [1, 4, 2, 5, 3, 1, 4, 2, 5, 3, 0, 0, 2, 5, 3, 1, 4, 2],
        [1, 5, 4, 3, 2, 1, 0, 0, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4],
        [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
        [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 0, 0, 0, 5, 1, 2, 3],
        [1, 3, 5, 2, 4, 1, 3, 5, 2, 4, 1, 3, 5, 2, 4, 1, 3, 5],
        [1, 4, 2, 5, 3, 1, 4, 2, 5, 3, 1, 4, 2, 5, 3, 1, 4, 2],
        [1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4],
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3],
        [0, 0, 0, 0, 4, 1, 3, 5, 2, 4, 1, 3, 5, 2, 4, 1, 3, 5],
        [1, 4, 2, 5, 3, 1, 4, 2, 5, 3, 1, 4, 2, 5, 3, 1, 4, 2],
        [1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5, 4],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3],
        [1, 3, 5, 2, 4, 1, 3, 5, 2, 4, 1, 3, 5, 2, 4, 1, 3, 5],
    ]),
    np.array([
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 3, 4, 5, 6, 1, 0, 0, 0, 5, 6, 1, 2, 3, 4, 5, 6],
        [1, 3, 5, 1, 3, 5, 1, 0, 0, 0, 3, 5, 1, 3, 5, 1, 3, 5],
        [1, 4, 1, 4, 1, 4, 1, 0, 0, 0, 1, 4, 1, 4, 1, 4, 1, 4],
        [1, 5, 3, 1, 5, 3, 1, 5, 3, 1, 5, 0, 0, 0, 3, 1, 5, 3],
        [1, 6, 5, 0, 0, 0, 0, 6, 5, 4, 3, 0, 0, 0, 5, 4, 3, 2],
        [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 3, 0, 0, 0, 0, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6],
        [1, 3, 5, 1, 3, 5, 1, 3, 5, 1, 3, 5, 1, 3, 5, 1, 3, 5],
        [1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4],
        [1, 5, 3, 1, 5, 3, 1, 5, 3, 1, 5, 3, 1, 5, 3, 1, 5, 3],
        [1, 6, 5, 4, 3, 2, 1, 0, 0, 0, 3, 2, 0, 0, 0, 0, 3, 2],
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1],
        [1, 2, 3, 4, 5, 6, 1, 0, 0, 0, 5, 6, 0, 0, 0, 0, 5, 6],
        [1, 3, 5, 1, 3, 5, 1, 3, 5, 1, 3, 5, 1, 3, 5, 1, 3, 5],
        [1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4],
        [1, 5, 3, 1, 5, 3, 1, 5, 3, 1, 5, 3, 1, 5, 3, 1, 5, 3],
        [1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2],
    ]),
    np.array([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4],
        [1, 3, 5, 7, 2, 4, 6, 1, 3, 5, 7, 2, 0, 0, 0, 0, 5, 7],
        [1, 4, 7, 3, 6, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3],
        [1, 5, 2, 6, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 6],
        [1, 0, 0, 2, 7, 5, 0, 0, 0, 0, 2, 7, 0, 0, 0, 0, 4, 2],
        [1, 0, 0, 5, 4, 3, 0, 0, 0, 0, 5, 4, 3, 0, 0, 0, 6, 5],
        [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4],
        [1, 3, 5, 7, 2, 4, 6, 1, 3, 5, 7, 2, 4, 6, 1, 3, 5, 7],
        [1, 4, 7, 3, 6, 2, 5, 1, 4, 7, 3, 6, 2, 5, 1, 4, 7, 3],
        [1, 5, 2, 6, 3, 7, 4, 1, 5, 2, 6, 3, 7, 4, 1, 5, 2, 6],
        [1, 6, 4, 2, 7, 5, 3, 1, 6, 4, 2, 7, 5, 3, 1, 6, 4, 2],
        [1, 7, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1, 7, 6, 5],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4],
        [1, 3, 5, 7, 2, 4, 6, 1, 3, 5, 7, 2, 4, 6, 1, 3, 5, 7],
        [1, 4, 7, 3, 6, 2, 5, 1, 4, 7, 3, 6, 2, 5, 1, 4, 7, 3],
    ]),
    np.array([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2],
        [1, 3, 5, 7, 1, 3, 5, 7, 1, 3, 5, 7, 1, 3, 5, 7, 1, 3],
        [1, 4, 7, 2, 5, 8, 3, 6, 1, 4, 7, 2, 5, 8, 0, 0, 1, 4],
        [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 0, 0, 1, 5],
        [1, 6, 3, 8, 5, 2, 7, 4, 1, 6, 3, 8, 5, 2, 0, 0, 1, 6],
        [1, 7, 5, 3, 1, 7, 5, 3, 1, 7, 5, 3, 1, 7, 5, 3, 1, 7],
        [1, 8, 7, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 1, 8],
        [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 3, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2],
        [1, 3, 5, 7, 0, 0, 0, 0, 1, 3, 5, 7, 1, 3, 5, 7, 1, 3],
        [1, 4, 7, 2, 5, 8, 3, 6, 1, 4, 7, 2, 5, 8, 3, 6, 1, 4],
        [1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5],
        [1, 6, 3, 8, 5, 2, 0, 0, 1, 6, 3, 8, 5, 2, 7, 4, 1, 6],
        [1, 7, 5, 3, 1, 7, 0, 0, 1, 7, 5, 3, 1, 7, 5, 3, 1, 7],
        [1, 8, 7, 6, 0, 0, 3, 2, 1, 8, 7, 6, 5, 4, 3, 2, 1, 8],
        [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2],
    ]),
]

for i, input_grid in enumerate(example_inputs):
    print(f"Example Input {i+1}:")
    analyze_example(input_grid)
    print("-" * 20)