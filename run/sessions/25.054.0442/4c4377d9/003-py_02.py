import numpy as np

def analyze_results(input_grid, expected_output, transformed_output):
    incorrect_pixels = []
    if transformed_output.shape != expected_output.shape:
        print("Shapes are different, cannot compare pixels.")
        return incorrect_pixels

    for row in range(expected_output.shape[0]):
        for col in range(expected_output.shape[1]):
            if expected_output[row, col] != transformed_output[row, col]:
                incorrect_pixels.append({
                    'location': (row, col),
                    'expected': expected_output[row, col],
                    'transformed': transformed_output[row, col]
                })
    return incorrect_pixels


# Example Data (from the prompt)
examples = [
    {
        "input": np.array([[9, 9, 5, 9], [5, 5, 9, 9], [9, 5, 9, 9]]),
        "expected": np.array([[9, 5, 9, 9], [5, 5, 9, 9], [9, 9, 5, 9], [9, 9, 5, 9], [5, 5, 9, 9], [9, 5, 9, 9]]),
        "transformed": np.array([[9, 9, 5, 9], [9, 5, 9, 9], [9, 9, 5, 9], [9, 9, 5, 5], [9, 5, 9, 9], [5, 5, 9, 9]])
    },
    {
        "input": np.array([[4, 1, 1, 4], [1, 1, 1, 1], [4, 4, 4, 1]]),
        "expected": np.array([[4, 4, 4, 1], [1, 1, 1, 1], [4, 1, 1, 4], [4, 1, 1, 4], [1, 1, 1, 1], [4, 4, 4, 1]]),
        "transformed": np.array([[4, 1, 1, 4], [4, 4, 4, 1], [4, 1, 1, 4], [1, 1, 1, 1], [4, 4, 4, 1], [1, 1, 1, 1]])
    },
    {
        "input": np.array([[9, 4, 9, 4], [9, 9, 4, 4], [4, 4, 4, 4]]),
        "expected": np.array([[4, 4, 4, 4], [9, 9, 4, 4], [9, 4, 9, 4], [9, 4, 9, 4], [9, 9, 4, 4], [4, 4, 4, 4]]),
        "transformed": np.array([[9, 4, 9, 4], [4, 4, 4, 4], [9, 4, 9, 4], [5, 5, 4, 4], [4, 4, 4, 4], [9, 9, 4, 4]])
    },
    {
        "input": np.array([[3, 3, 5, 5], [3, 5, 5, 3], [5, 5, 3, 3]]),
        "expected": np.array([[5, 5, 3, 3], [3, 5, 5, 3], [3, 3, 5, 5], [3, 3, 5, 5], [3, 5, 5, 3], [5, 5, 3, 3]]),
        "transformed": np.array([[3, 3, 5, 5], [5, 5, 3, 3], [3, 3, 5, 5], [3, 9, 9, 3], [5, 5, 3, 3], [3, 5, 5, 3]])
    }
]

for i, example in enumerate(examples):
    incorrect_pixels = analyze_results(example["input"], example["expected"], example["transformed"])
    print(f"Example {i+1}:")
    print(f"  Incorrect Pixels: {len(incorrect_pixels)}")
    for pixel_data in incorrect_pixels:
        print(f"    Location: {pixel_data['location']}, Expected: {pixel_data['expected']}, Transformed: {pixel_data['transformed']}")
