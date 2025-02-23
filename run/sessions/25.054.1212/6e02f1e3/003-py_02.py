import numpy as np

def analyze_example(input_grid, expected_output, transformed_output):
    """Analyzes an example and provides metrics."""

    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)

    match = np.array_equal(expected_output, transformed_output)
    pixels_off = np.sum(expected_output != transformed_output)
    size_correct = input_grid.shape == expected_output.shape
    color_palette_correct = set(np.unique(input_grid)) <= set(range(10)) and set(np.unique(expected_output)) <= set(range(10))

    unique_expected, counts_expected = np.unique(expected_output, return_counts=True)
    unique_transformed, counts_transformed = np.unique(transformed_output, return_counts=True)

    correct_pixel_counts = True
    for color, count in zip(unique_expected, counts_expected):
        if color not in unique_transformed or counts_transformed[np.where(unique_transformed == color)[0][0]] != count:
            correct_pixel_counts = False
            break

    print(f"Match: {match}")
    print(f"Pixels Off: {pixels_off}")
    print(f"Size Correct: {size_correct}")
    print(f"Color Palette Correct: {color_palette_correct}")
    print(f"Correct Pixel Counts: {correct_pixel_counts}")
    print("-" * 20)

# Example Data (as lists for easier processing)
examples = [
    {
        "input": [[2, 2, 2], [3, 2, 3], [3, 3, 3]],
        "expected": [[5, 0, 5], [0, 5, 0], [0, 0, 5]],
        "transformed": [[5, 0, 5], [0, 5, 0], [5, 0, 5]]
    },
    {
        "input": [[3, 3, 3], [4, 2, 2], [4, 4, 2]],
        "expected": [[5, 0, 5], [0, 5, 0], [5, 0, 0]],
        "transformed": [[5, 0, 5], [0, 5, 0], [5, 0, 5]]
    },
    {
        "input": [[4, 4, 4], [4, 4, 4], [4, 4, 4]],
        "expected": [[5, 5, 5], [0, 0, 0], [0, 0, 0]],
        "transformed": [[5, 0, 5], [0, 5, 0], [5, 0, 5]]
    },
    {
        "input": [[3, 3, 3], [3, 3, 3], [3, 3, 3]],
        "expected": [[5, 5, 5], [0, 0, 0], [0, 0, 0]],
        "transformed": [[5, 0, 5], [0, 5, 0], [5, 0, 5]]
    },
    {
        "input": [[4, 4, 4], [4, 4, 4], [3, 3, 3]],
        "expected": [[5, 0, 5], [0, 5, 0], [0, 0, 5]],
        "transformed": [[5, 0, 5], [0, 5, 0], [5, 0, 5]]
    }
]

for i, example in enumerate(examples):
    print(f"Example {i+1}:")
    analyze_example(example["input"], example["expected"], example["transformed"])
