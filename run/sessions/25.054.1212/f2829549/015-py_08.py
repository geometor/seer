import numpy as np
from collections import Counter

def object_counts(grid):
    """Counts contiguous objects of the same color in a grid."""
    rows, cols = grid.shape
    visited = np.zeros((rows, cols), dtype=bool)
    counts = Counter()

    def dfs(r, c, color):
        if (
            r < 0
            or r >= rows
            or c < 0
            or c >= cols
            or visited[r, c]
            or grid[r, c] != color
        ):
            return 0
        visited[r, c] = True
        return (
            1
            + dfs(r + 1, c, color)
            + dfs(r - 1, c, color)
            + dfs(r, c + 1, color)
            + dfs(r, c - 1, color)
        )
    
    for r in range(rows) :
        for c in range(cols) :
            if not visited[r,c] :
                color = grid[r,c]
                size = dfs(r,c,color)
                if size > 0 :
                    counts[(color,size)] += 1
    return counts

# example usage (assuming grid definitions from the prompt):
grid_strings = [
    """
7 7 0 1 5 0 0
7 0 0 1 5 0 0
0 0 0 1 5 0 5
0 0 0 1 5 5 0
""",
    """
7 7 0 1 5 0 0
0 0 0 1 0 0 0
7 7 0 1 5 0 0
0 7 7 1 5 5 0
""",
    """
0 7 7 1 5 0 0
0 0 7 1 0 5 5
0 7 0 1 5 5 0
0 0 7 1 0 0 0
""",
    """
7 0 7 1 5 5 0
7 7 0 1 5 5 5
0 7 0 1 0 0 0
0 0 0 1 5 0 5
""",
    """
7 0 0 1 0 5 0
0 0 7 1 5 0 0
0 0 0 1 5 5 5
7 7 7 1 5 5 5
"""
]

expected_output_strings = [
    """
0 0 3
0 3 3
0 3 0
0 0 3
""",
    """
0 0 3
3 3 3
0 0 3
0 0 0
""",
    """
0 0 0
3 0 0
0 0 3
3 3 0
""",
    """
0 0 0
0 0 0
3 0 3
0 3 0
""",
    """
0 0 3
0 3 0
0 0 0
0 0 0
"""
]
grids = [np.fromstring(grid_str.strip(), dtype=int, sep=' ').reshape(len(grid_str.split('\n')), -1) for grid_str in grid_strings]
expected_outputs = [np.fromstring(out_str.strip(), dtype=int, sep=' ').reshape(len(out_str.split('\n')), -1) for out_str in expected_output_strings]

for i, (grid, expected_output) in enumerate(zip(grids, expected_outputs)):
    input_counts = object_counts(grid)
    output_counts = object_counts(expected_output)
    print(f"Example {i+1}:")
    print("Input Object Counts:", input_counts)
    print("Output Object Counts:", output_counts)
    print("------")
