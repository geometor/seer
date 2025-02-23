import numpy as np

def analyze_example(input_grid, expected_output, transformed_output):
    """Analyzes an example and provides detailed metrics."""

    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)


    print(f"  Input Grid:\n{input_grid}")
    print(f"  Expected Output:\n{expected_output}")
    print(f"  Transformed Output:\n{transformed_output}")


    match = np.array_equal(expected_output, transformed_output)
    pixels_off = np.sum(expected_output != transformed_output)
    size_correct = input_grid.shape == expected_output.shape == transformed_output.shape
    color_palette_correct = set(input_grid.flatten()) == set(expected_output.flatten()) == set(transformed_output.flatten())

    def pixel_counts(grid):
        counts = {}
        for val in np.unique(grid):
            counts[val] = np.sum(grid == val)
        return counts

    correct_pixel_counts = pixel_counts(expected_output) == pixel_counts(transformed_output)

    print(f"  Match: {match}")
    print(f"  Pixels Off: {pixels_off}")
    print(f"  Size Correct: {size_correct}")
    print(f"  Color Palette Correct: {color_palette_correct}")
    print(f"  Correct Pixel Counts: {correct_pixel_counts}")
    print("-" * 20)

# Example Data
examples = [
    {
        "input": [[0, 2, 2], [0, 2, 2], [2, 0, 0]],
        "expected": [[0, 2, 2], [0, 2, 2], [1, 0, 0]],
        "transformed": [[0, 2, 2], [0, 2, 1], [2, 0, 0]],
    },
    {
        "input": [[2, 2, 2, 0], [0, 2, 0, 0], [0, 0, 0, 2], [0, 2, 0, 0]],
        "expected": [[2, 2, 2, 0], [0, 2, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]],
        "transformed": [[2, 2, 2, 0], [0, 2, 0, 0], [0, 0, 0, 2], [0, 2, 0, 0]],
    },
    {
        "input": [[2, 2, 0, 0], [0, 2, 0, 0], [2, 2, 0, 2], [0, 0, 0, 0], [0, 2, 2, 2]],
        "expected": [[2, 2, 0, 0], [0, 2, 0, 0], [2, 2, 0, 1], [0, 0, 0, 0], [0, 2, 2, 2]],
        "transformed": [[1, 2, 0, 0], [0, 2, 0, 0], [1, 2, 0, 2], [0, 0, 0, 0], [0, 2, 2, 2]],
    },
    {
        "input": [[2, 2, 0], [2, 0, 2], [0, 2, 0]],
        "expected": [[2, 2, 0], [2, 0, 1], [0, 1, 0]],
        "transformed": [[2, 2, 0], [2, 0, 1], [0, 1, 0]],
    },
]

for i, example in enumerate(examples):
    print(f"Example {i + 1}:")
    analyze_example(example["input"], example["expected"], example["transformed"])