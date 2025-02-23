import numpy as np

def calculate_metrics(input_grid, expected_output, transformed_output):
    """Calculates and prints metrics for a single example."""

    match = np.array_equal(expected_output, transformed_output)
    pixels_off = np.sum(expected_output != transformed_output)
    size_correct = expected_output.shape == transformed_output.shape
    # Compare color palettes, ignoring order and duplicates
    color_palette_correct = set(np.unique(expected_output)) == set(np.unique(transformed_output))
    
    expected_counts = {color: np.sum(expected_output == color) for color in np.unique(expected_output)}
    transformed_counts = {color: np.sum(transformed_output == color) for color in np.unique(transformed_output)}

    correct_pixel_counts = expected_counts == transformed_counts


    print(f"  match: {match}")
    print(f"  pixels_off: {pixels_off}")
    print(f"  size_correct: {size_correct}")
    print(f"  color_palette_correct: {color_palette_correct}")
    print(f"  correct_pixel_counts: {correct_pixel_counts}")

    if not match:
        print(" Discrepancies:")
        for x in range(expected_output.shape[0]):
            for y in range(expected_output.shape[1]):
                if expected_output[x,y] != transformed_output[x,y]:
                    print(f"    Pixel at ({x},{y}): Expected {expected_output[x,y]}, Got {transformed_output[x,y]}")
                    
# Example Data (recreated for completeness) - replace with your actual data loading
examples = [
    {
        "input": np.array([[4, 4, 4], [2, 3, 2], [2, 3, 3]]),
        "expected": np.array([[5, 5, 5], [0, 0, 0], [0, 0, 0]]),
        "transformed": np.array([[5, 5, 5], [0, 0, 0], [0, 0, 0]]),
    },
    {
        "input": np.array([[7, 3, 3], [6, 6, 6], [3, 7, 7]]),
        "expected": np.array([[0, 0, 0], [5, 5, 5], [0, 0, 0]]),
        "transformed": np.array([[0, 0, 0], [5, 5, 5], [0, 0, 0]]),
    },
    {
        "input": np.array([[2, 9, 2], [4, 4, 4], [9, 9, 9]]),
        "expected": np.array([[0, 5, 0], [5, 5, 5], [5, 5, 5]]),
        "transformed": np.array([[0, 0, 0], [5, 5, 5], [0, 0, 0]]),
    },
    {
        "input": np.array([[2, 2, 4], [2, 2, 4], [1, 1, 1]]),
        "expected": np.array([[0, 0, 5], [0, 0, 5], [5, 5, 5]]),
        "transformed": np.array([[0, 0, 5], [0, 0, 5], [5, 5, 5]]),
    },
]

for i, example in enumerate(examples):
    print(f"Example {i+1}:")
    calculate_metrics(example["input"], example["expected"], example["transformed"])
