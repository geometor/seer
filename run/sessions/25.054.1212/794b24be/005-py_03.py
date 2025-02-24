import numpy as np

def analyze_results(input_grid, expected_output, transformed_output):
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)
    
    metrics = {
        "input_shape": input_grid.shape,
        "expected_output_shape": expected_output.shape,
        "transformed_output_shape": transformed_output.shape,
        "shapes_match": expected_output.shape == transformed_output.shape,
        "pixel_match": np.array_equal(expected_output, transformed_output),
        "pixels_off": None, #Calculate later after size adjustment
        "blue_pixels_count": np.sum(input_grid == 1),
        "red_pixels_count_expected": np.sum(expected_output == 2),
        "red_pixels_count_transformed": np.sum(transformed_output == 2)
    }
    if metrics['shapes_match'] == True:
        metrics["pixels_off"] = int(np.sum(expected_output != transformed_output))

    return metrics

#Example Usage:
examples = [
    {
        "input": [[0, 0, 0], [1, 0, 0], [0, 0, 0]],
        "expected": [[0, 0, 0], [2, 0, 0], [0, 0, 0]],
        "transformed": [[2]]
    },
    {
        "input": [[0, 1, 0], [1, 0, 0], [0, 0, 0]],
        "expected": [[0, 2, 0], [2, 0, 0], [0, 0, 0]],
        "transformed": [[0, 2], [2, 0]]
    },
    {
        "input": [[0, 0, 1], [0, 0, 0], [1, 0, 0]],
        "expected": [[0, 0, 2], [0, 0, 0], [2, 0, 0]],
        "transformed": [[0, 0, 2], [0, 0, 0], [2, 0, 0]]
    },
    {
        "input": [[0, 1, 0], [0, 0, 1], [0, 0, 0]],
        "expected": [[0, 2, 0], [0, 0, 2], [0, 0, 0]],
        "transformed": [[2, 0], [0, 2]]
    },
    {
        "input": [[0, 0, 1], [0, 0, 0], [0, 0, 0]],
        "expected": [[0, 0, 2], [0, 0, 0], [0, 0, 0]],
        "transformed": [[2]]
    },
    {
        "input": [[1, 1, 0], [0, 0, 0], [1, 0, 0]],
        "expected": [[2, 2, 0], [0, 0, 0], [2, 0, 0]],
        "transformed": [[2, 2], [0, 0], [2, 0]]
    },
    {
        "input": [[0, 1, 0], [1, 1, 0], [0, 0, 0]],
        "expected": [[0, 2, 0], [2, 2, 0], [0, 0, 0]],
        "transformed": [[0, 2], [2, 2]]
    },
    {
        "input": [[1, 1, 0], [0, 0, 0], [1, 0, 1]],
        "expected": [[2, 2, 0], [0, 0, 0], [2, 0, 2]],
        "transformed": [[2, 2, 0], [0, 0, 0], [2, 0, 2]]
    },
    {
        "input": [[0, 1, 0], [1, 1, 0], [1, 0, 0]],
        "expected": [[0, 2, 0], [2, 2, 0], [2, 0, 0]],
        "transformed": [[0, 2], [2, 2], [2, 0]]
    },
    {
        "input": [[1, 0, 0], [0, 0, 1], [0, 1, 1]],
        "expected": [[2, 0, 0], [0, 0, 2], [0, 2, 2]],
        "transformed": [[2, 0, 0], [0, 0, 2], [0, 2, 2]]
    }
]

for i, example in enumerate(examples):
    print(f"Example {i+1}:")
    metrics = analyze_results(example["input"], example["expected"], example["transformed"])
    for key, value in metrics.items():
        print(f"  {key}: {value}")