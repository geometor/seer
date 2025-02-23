import numpy as np

# Define a function to collect properties of a grid
def grid_properties(grid):
    unique_colors = np.unique(grid)
    color_counts = {color: np.sum(grid == color) for color in unique_colors}
    rows, cols = grid.shape
    return {
        'shape': (rows, cols),
        'unique_colors': unique_colors.tolist(),
        'color_counts': color_counts,
    }

# expected outputs
expected_outputs = [
    np.array([[3, 3, 3], [4, 4, 4], [2, 2, 2]]),
    np.array([[3, 3, 3], [3, 3, 3], [3, 3, 3]]),
    np.array([[2, 2, 2], [4, 4, 4], [2, 2, 2]]),
    np.array([[4, 4, 4], [3, 3, 3], [4, 4, 4]]),
]

# Collect properties
example_props = []
for i, output in enumerate(expected_outputs):
    props = grid_properties(output)
    example_props.append(
      {
        'example': i+1,
        'props': props
      }
    )

print(example_props)
