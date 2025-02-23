import numpy as np

def compare_grids(expected_grid, actual_grid):
    """
    Compares two grids and returns a list of mismatched pixel details.
    """
    mismatches = []
    expected_np = np.array(expected_grid)
    actual_np = np.array(actual_grid)

    rows, cols = expected_np.shape
    for row in range(rows):
        for col in range(cols):
            if expected_np[row, col] != actual_np[row, col]:
                mismatches.append((row, col, int(expected_np[row, col]), int(actual_np[row, col])))
    return mismatches

# Example Data (as provided in the prompt)
examples = [
    {
        "input": [[9, 0, 0], [9, 9, 9], [9, 9, 9]],
        "expected": [[0, 9, 9], [0, 9, 9], [9, 9, 9]],
        "transformed": [[9, 9, 9], [9, 9, 9], [9, 9, 9]],
        "match": False,
        "pixels_off": 2,
        "size_correct": True,
        "color_palette_correct": True,
        "correct_pixel_counts": False
    },
    {
        "input": [[0, 6, 6], [0, 0, 0], [6, 6, 0]],
        "expected": [[6, 0, 0], [6, 0, 6], [6, 0, 6]],
        "transformed": [[6, 0, 0], [6, 0, 6], [0, 0, 6]],
        "match": False,
        "pixels_off": 1,
        "size_correct": True,
        "color_palette_correct": True,
        "correct_pixel_counts": False
    },
    {
        "input": [[0, 0, 9], [0, 0, 9], [9, 9, 9]],
        "expected": [[9, 9, 9], [0, 0, 9], [0, 0, 9]],
        "transformed": [[9, 9, 9], [9, 0, 9], [9, 9, 9]],
        "match": False,
        "pixels_off": 3,
        "size_correct": True,
        "color_palette_correct": True,
        "correct_pixel_counts": False
    },
    {
        "input": [[2, 0, 0], [0, 0, 2], [0, 2, 2]],
        "expected": [[2, 2, 2], [0, 0, 2], [2, 0, 0]],
        "transformed": [[0, 2, 2], [2, 0, 2], [2, 2, 0]],
        "match": False,
        "pixels_off": 3,
        "size_correct": True,
        "color_palette_correct": True,
        "correct_pixel_counts": False
    }
]

# Calculate and add detailed pixel comparisons
for example in examples:
    example["detailed_pixel_comparison"] = compare_grids(example["expected"], example["transformed"])

# Print the results
for i, example in enumerate(examples):
    print(f"Example {i+1}:")
    for key, value in example.items():
        print(f"  {key}: {value}")
    print("-" * 20)