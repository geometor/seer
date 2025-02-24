import numpy as np

def analyze_grid(grid):
    height, width = grid.shape
    unique_colors = np.unique(grid)
    color_counts = {color: np.count_nonzero(grid == color) for color in unique_colors}
    return {
        'height': height,
        'width': width,
        'unique_colors': unique_colors.tolist(),
        'color_counts': color_counts,
    }

# Example Grids (from the problem description)
grids = {
    "example_1_input": np.array([[0,1,0],[1,1,0],[0,1,0],[0,1,1],[0,1,0],[1,1,0]]),
    "example_1_expected": np.array([[0,2,0],[2,2,0],[0,2,0],[0,2,2],[0,2,0],[2,2,0],[0,2,0],[0,2,2],[0,2,0]]),
    "example_1_transformed": np.array([[0,2,0],[2,2,0],[0,2,0],[0,2,2],[0,2,0],[2,2,0],[0,2,0],[2,2,0],[0,2,0]]),
    "example_2_input": np.array([[0,1,0],[1,0,1],[0,1,0],[1,0,1],[0,1,0],[1,0,1]]),
    "example_2_expected": np.array([[0,2,0],[2,0,2],[0,2,0],[2,0,2],[0,2,0],[2,0,2],[0,2,0],[2,0,2],[0,2,0]]),
    "example_2_transformed": np.array([[0,2,0],[2,0,2],[0,2,0],[2,0,2],[0,2,0],[2,0,2],[0,2,0],[2,0,2],[0,2,0]]),
    "example_3_input": np.array([[0,1,0],[1,1,0],[0,1,0],[0,1,0],[1,1,0],[0,1,0]]),
    "example_3_expected": np.array([[0,2,0],[2,2,0],[0,2,0],[0,2,0],[2,2,0],[0,2,0],[0,2,0],[2,2,0],[0,2,0]]),
    "example_3_transformed": np.array([[0,2,0],[2,2,0],[0,2,0],[0,2,0],[2,2,0],[0,2,0],[0,2,0],[2,2,0],[0,2,0]]),
}

for key, grid in grids.items():
  analysis = analyze_grid(grid)
  print(f"{key}:")
  print(analysis)