import numpy as np

def analyze_example(input_grid, expected_output, transformed_output):
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)

    metrics = {
        "input_colors": list(np.unique(input_grid)),
        "output_colors": list(np.unique(expected_output)),
        "transformed_colors": list(np.unique(transformed_output)),
        "input_color_counts": {int(color): int(count) for color, count in zip(*np.unique(input_grid, return_counts=True))},
        "output_color_counts": {int(color): int(count) for color, count in zip(*np.unique(expected_output, return_counts=True))},
        "transformed_color_counts": {int(color): int(count) for color, count in zip(*np.unique(transformed_output, return_counts=True))},
        "pixels_off": np.sum(expected_output != transformed_output),
    }
    return metrics
# Example usage (using the provided examples as lists):

examples = [
   {
        "input": [[9, 0, 0], [9, 9, 9], [9, 9, 9]],
        "expected": [[0, 9, 9], [0, 9, 9], [9, 9, 9]],
        "transformed": [[0, 0, 0], [9, 9, 0], [9, 9, 9]],
    },
    {
        "input": [[0, 6, 6], [6, 0, 0], [6, 6, 0]],
        "expected": [[6, 0, 0], [6, 0, 6], [6, 0, 6]],
        "transformed": [[6, 6, 6], [6, 0, 6], [6, 6, 6]],
    },
    {
        "input": [[0, 0, 9], [0, 0, 9], [9, 9, 9]],
        "expected": [[9, 9, 9], [0, 0, 9], [0, 0, 9]],
        "transformed": [[0, 0, 9], [0, 0, 9], [0, 9, 9]],
    },
    {
        "input": [[2, 0, 2], [0, 0, 2], [0, 2, 2]],
        "expected": [[2, 2, 2], [0, 0, 2], [2, 0, 0]],
        "transformed": [[0, 0, 2], [0, 0, 2], [0, 2, 2]],
    },
]
for i, example in enumerate(examples):
    print(f"Example {i+1}:")
    metrics = analyze_example(example["input"], example["expected"], example["transformed"])
    for key, value in metrics.items():
        print(f"  {key}: {value}")
