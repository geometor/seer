from collections import Counter

def calculate_metrics(input_grid, expected_output, transformed_output):
    """Calculates evaluation metrics for a single example."""
    metrics = {
        "match": np.array_equal(expected_output, transformed_output),
        "pixels_off": np.sum(expected_output != transformed_output),
        "size_correct": expected_output.shape == transformed_output.shape,
        "color_palette_correct": set(np.unique(expected_output)) == set(np.unique(transformed_output)),
        "correct_pixel_counts": Counter(expected_output.flatten()) == Counter(transformed_output.flatten()),
    }
    return metrics

input_grids = [
    np.array([[4, 4, 4], [2, 3, 2], [2, 3, 3]]),
    np.array([[7, 3, 3], [6, 6, 6], [3, 7, 7]]),
    np.array([[2, 9, 2], [4, 4, 4], [9, 9, 9]]),
    np.array([[2, 2, 4], [2, 2, 4], [1, 1, 1]]),
]
expected_outputs = [
    np.array([[5, 5, 5], [0, 0, 0], [0, 0, 0]]),
    np.array([[0, 0, 0], [5, 5, 5], [0, 0, 0]]),
    np.array([[0, 0, 0], [5, 5, 5], [5, 5, 5]]),
    np.array([[0, 0, 0], [0, 0, 0], [5, 5, 5]]),
]
transformed_outputs = [
    np.array([[5, 5, 5], [0, 3, 0], [0, 3, 3]]),
    np.array([[7, 3, 3], [6, 6, 6], [3, 7, 7]]),
    np.array([[0, 5, 0], [5, 5, 5], [5, 5, 5]]),
    np.array([[0, 0, 5], [0, 0, 5], [1, 1, 1]]),
]

for i, (inp, exp, trans) in enumerate(zip(input_grids, expected_outputs, transformed_outputs)):
  metrics = calculate_metrics(inp, exp, trans)
  print(f"Example {i+1}:")
  print(metrics)

def get_color_changes(input_grid, output_grid):
  """
  Identifies color changes between the input and output grids.

  Args:
    input_grid: A NumPy array representing the input grid.
    output_grid: A NumPy array representing the output grid.

  Returns:
    A dictionary where keys are the original colors and values are the
    colors they change to.
  """

  color_changes = {}
  for i in range(input_grid.shape[0]):
      for j in range(input_grid.shape[1]):
          input_color = input_grid[i, j]
          output_color = output_grid[i, j]
          if input_color != output_color:
              color_changes[input_color] = output_color
  return color_changes

for i, (inp, exp) in enumerate(zip(input_grids, expected_outputs)):
    print(f"color changes example: {i+1}")
    print(get_color_changes(inp,exp))
