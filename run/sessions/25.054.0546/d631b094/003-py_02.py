import numpy as np

# Function to analyze a single example
def analyze_example(input_grid, expected_output, transformed_output, example_num, stage):
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    
    metrics = {
        "example": example_num,
        "stage": stage,
        "input_shape": input_grid.shape,
        "expected_output_shape": expected_output.shape,
        "transformed_output_shape": transformed_output.shape if transformed_output.size > 0 else (0, 0),
        "input_colors": np.unique(input_grid).tolist(),
        "expected_output_colors": np.unique(expected_output).tolist(),
        "transformed_output_colors": np.unique(transformed_output).tolist() if transformed_output.size > 0 else [],
        "match": np.array_equal(expected_output, transformed_output)
     }
    
    non_white_input_colors = [c for c in metrics["input_colors"] if c != 0]
    non_white_expected_output_colors = [c for c in metrics["expected_output_colors"] if c != 0]

    if len(non_white_input_colors) == 1:
        metrics["input_has_single_non_white_color"] = True
        metrics["count_of_non_white_pixels"] = np.count_nonzero(input_grid == non_white_input_colors[0])
    else:
       metrics["input_has_single_non_white_color"] = False
       metrics["count_of_non_white_pixels"] = 0
        
    if len(non_white_expected_output_colors) ==1:
        metrics["expected_has_single_non_white_color"] = True
        metrics["expected_count"] = np.count_nonzero(expected_output == non_white_expected_output_colors[0])
    else:
        metrics["expected_has_single_non_white_color"] = False
        metrics["expected_count"] = 0

    return metrics

# Example Data (reformatted for easier processing)

example_data = [
    {
        "input": [[0, 0, 0], [1, 0, 0], [0, 1, 0]],
        "expected": [[1, 1]],
        "transformed": [[1, 1]]
    },
     {
        "input": [[0, 2, 0], [2, 0, 0], [0, 2, 0]],
        "expected": [[2, 2, 2]],
        "transformed": []
    },
    {
        "input": [[0, 7, 0], [0, 0, 0], [0, 0, 0]],
        "expected": [[7]],
        "transformed": []
    },
    {
        "input": [[0, 8, 0], [8, 8, 0], [8, 0, 0]],
        "expected": [[8, 8, 8, 8]],
        "transformed": []
    }
]

# Analyze all examples
all_metrics = [analyze_example(ex["input"], ex["expected"], np.array(ex["transformed"]), i + 1, "train") for i, ex in enumerate(example_data)]


# Print out the metrics
for metrics in all_metrics:
    print(metrics)