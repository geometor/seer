import numpy as np

def count_colors(grid):
    """Counts the occurrences of each color in the grid."""
    unique, counts = np.unique(grid, return_counts=True)
    return dict(zip(unique, counts))

def analyze_example(input_grid, expected_output, transformed_output):
    """Analyzes an example and returns relevant metrics."""
    metrics = {}
    metrics["match"] = np.array_equal(expected_output, transformed_output)
    metrics["pixels_off"] = np.sum(expected_output != transformed_output)
    metrics["size_correct"] = expected_output.shape == transformed_output.shape
    metrics["input_colors"] = count_colors(input_grid)
    metrics["expected_colors"] = count_colors(expected_output)
    metrics["transformed_colors"] = count_colors(transformed_output)
    return metrics

# Example grids and outputs would be defined here, then:
# example_metrics = analyze_example(input_grid, expected_output, transformed_output)
# print(example_metrics)