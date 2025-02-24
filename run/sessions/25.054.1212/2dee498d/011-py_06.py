import numpy as np

def calculate_metrics(input_grid, expected_output, transformed_output):
    """Calculates metrics comparing expected and transformed outputs."""

    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)

    metrics = {
        "input_shape": input_grid.shape,
        "expected_output_shape": expected_output.shape,
        "transformed_output_shape": transformed_output.shape,
        "match": np.array_equal(expected_output, transformed_output),
        "pixels_off": None,  # Default value, can be more complex
        "size_correct": expected_output.shape == transformed_output.shape,
    }
    if not metrics["match"]:
      num_diff = 0
      h = min(expected_output.shape[0],transformed_output.shape[0])
      w = min(expected_output.shape[1],transformed_output.shape[1])

      for i in range(h):
        for j in range(w):
            if expected_output[i][j] != transformed_output[i][j]:
              num_diff += 1
      metrics["pixels_off"]= num_diff
    else:
       metrics["pixels_off"] = 0

    return metrics
# Example Data (From the prompt)

example1_input = [
    [4, 5, 1, 1, 5, 4, 4, 5, 1],
    [5, 5, 5, 5, 5, 5, 5, 5, 5],
    [1, 5, 4, 4, 5, 1, 1, 5, 4]
]
example1_expected = [
    [4, 5, 1],
    [5, 5, 5],
    [1, 5, 4]
]
example1_transformed = [
    [4, 5, 1, 1],
    [5, 5, 5, 5],
    [1, 5, 4, 4]
]

example2_input = [
    [2, 0, 0, 1, 2, 0, 0, 1, 2, 0, 0, 1],
    [4, 2, 1, 4, 4, 2, 1, 4, 4, 2, 1, 4],
    [4, 1, 2, 4, 4, 1, 2, 4, 4, 1, 2, 4],
    [1, 0, 0, 2, 1, 0, 0, 2, 1, 0, 0, 2]
]
example2_expected = [
    [2, 0, 0, 1],
    [4, 2, 1, 4],
    [4, 1, 2, 4],
    [1, 0, 0, 2]
]
example2_transformed = [
    [2, 0, 0, 1],
    [4, 2, 1, 4],
    [4, 1, 2, 4],
    [1, 0, 0, 2]
]

example3_input = [
    [2, 1, 2, 1, 2, 1],
    [2, 3, 2, 3, 2, 3]
]
example3_expected = [
    [2, 1],
    [2, 3]
]
example3_transformed = [
    [2, 1, 2, 1],
    [2, 3, 2, 3]
]

examples = [
    (example1_input, example1_expected, example1_transformed),
    (example2_input, example2_expected, example2_transformed),
    (example3_input, example3_expected, example3_transformed),
]

for i, (input_grid, expected_output, transformed_output) in enumerate(examples):
    metrics = calculate_metrics(input_grid, expected_output, transformed_output)
    print(f"Example {i+1} Metrics:")
    for key, value in metrics.items():
        print(f"  {key}: {value}")