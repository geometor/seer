# Hypothetical code_execution - not actually runnable here
import numpy as np

def analyze_results(input_grid, expected_output, transformed_output):
    """
    Analyzes the results of the transformation.
    """
    metrics = {}

    metrics["input_grid_shape"] = input_grid.shape
    metrics["expected_shape"] = expected_output.shape
    metrics["transformed_shape"] = transformed_output.shape
    metrics["shape_match"] = input_grid.shape == expected_output.shape == transformed_output.shape

    metrics["input_colors"] = np.unique(input_grid).tolist()
    metrics["expected_colors"] = np.unique(expected_output).tolist()
    metrics["transformed_colors"] = np.unique(transformed_output).tolist()
    metrics["color_palette_match"] = set(metrics["input_colors"]) == set(metrics["expected_colors"])

    metrics["pixel_count_diff"] = np.sum(expected_output != transformed_output) #pixels_off value provided

    input_red_count = np.sum(input_grid == 2)
    transformed_red_count = np.sum(transformed_output == 2)
    expected_red_count = np.sum(expected_output == 2)
    metrics['red_pixel_check'] = (input_red_count == transformed_red_count == expected_red_count)
    return metrics

# Example 1 Data (already provided)
example1_input = np.array([[2, 0, 0, 0, 0],
                          [0, 0, 0, 2, 0],
                          [0, 0, 0, 0, 0],
                          [0, 6, 0, 0, 0],
                          [0, 0, 0, 0, 0]])
example1_expected = np.array([[2, 1, 1, 1, 1],
                             [1, 1, 1, 2, 1],
                             [0, 0, 1, 1, 1],
                             [0, 6, 0, 0, 0],
                             [0, 0, 0, 0, 0]])
example1_transformed = np.array([[2, 0, 0, 0, 0],
                                [0, 0, 0, 2, 0],
                                [0, 0, 0, 0, 0],
                                [0, 6, 0, 0, 0],
                                [0, 0, 0, 0, 0]]) # Initial, incorrect transformation

# Example 2 Data (From ARC Task Data)
example2_input = np.array([[0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 2, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 6, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 2, 0],
                          [0, 0, 0, 0, 0, 0, 0]])
example2_expected = np.array([[0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 2, 0, 0, 0],
                             [0, 0, 0, 1, 0, 0, 0],
                             [0, 6, 1, 1, 1, 0, 0],
                             [0, 0, 0, 1, 0, 0, 0],
                             [0, 0, 0, 1, 0, 2, 0],
                             [0, 0, 0, 0, 0, 0, 0]])
example2_transformed = np.array([[0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 2, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0],
                                [0, 6, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 2, 0],
                                [0, 0, 0, 0, 0, 0, 0]]) # Placeholder - repeat of input

# Example 3 Data (From ARC Task Data)
example3_input = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 2, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 6, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0]])
example3_expected = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 2, 0, 0, 0, 0],
                             [0, 0, 0, 0, 1, 0, 0, 0, 0],
                             [0, 0, 0, 0, 1, 0, 0, 0, 0],
                             [0, 0, 0, 0, 1, 0, 0, 6, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0]])
example3_transformed = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 2, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 6, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0]]) # Placeholder - repeat of input


results = []
results.append(analyze_results(example1_input, example1_expected, example1_transformed))
results.append(analyze_results(example2_input, example2_expected, example2_transformed))
results.append(analyze_results(example3_input, example3_expected, example3_transformed))

for i, res in enumerate(results):
    print(f"--- Example {i+1} ---")
    for k, v in res.items():
        print(f"{k}: {v}")
