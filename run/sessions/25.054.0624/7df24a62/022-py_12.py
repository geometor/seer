import numpy as np

def analyze_results(input_grid, expected_output, transformed_output):
    """
    Analyzes an individual example. Reports differences.
    """

    print("Input Grid:")
    print(input_grid)
    print("Expected Output:")
    print(expected_output)
    print("Transformed Output:")
    print(transformed_output)

    match = np.array_equal(expected_output, transformed_output)
    print(f"Match: {match}")

    if not match:
        diff = expected_output != transformed_output
        pixels_off = np.sum(diff)
        print(f"Pixels Off: {pixels_off}")

        # Count occurrences of each color in expected output
        expected_color_counts = {}
        for color in range(10):
            expected_color_counts[color] = np.sum(expected_output == color)
        print(f"Expected Color Counts: {expected_color_counts}")

        # Count occurrences of each color in transformed output
        transformed_color_counts = {}
        for color in range(10):
            transformed_color_counts[color] = np.sum(transformed_output == color)
        print(f"Transformed Color Counts: {transformed_color_counts}")

        print("Pixel differences (expected -> transformed):")
        for r in range(expected_output.shape[0]):
            for c in range(expected_output.shape[1]):
                if expected_output[r, c] != transformed_output[r, c]:
                    print(f"  ({r},{c}): {expected_output[r,c]} -> {transformed_output[r,c]}")

# Example usage (replace with actual data from the task)
# Assuming a simple transform function for now:  copy input to output
def transform(input_grid):
  return input_grid.copy()

task_data = {  # place holder, will replace with actual task
    "train": [
        {
            "input": np.array([[1, 1], [1, 1]]),
            "output": np.array([[1, 1], [1, 1]]),
        },
        {
            "input": np.array([[2, 2], [2, 2]]),
            "output": np.array([[2, 2, 2], [2, 2, 2]]),
        },
                {
            "input": np.array([[3, 3], [3, 3]]),
            "output": np.array([[3, 3, 3, 3], [3, 3, 3, 3]]),
        },
    ]
}

for i, example in enumerate(task_data["train"]):
    print(f"\n--- Example {i+1} ---")
    transformed_output = transform(example["input"])
    analyze_results(example["input"], example["output"], transformed_output)
