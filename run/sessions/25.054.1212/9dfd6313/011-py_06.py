import numpy as np

def analyze_results(input_grid, expected_output, transformed_output):
    match = np.array_equal(expected_output, transformed_output)
    pixels_off = np.sum(expected_output != transformed_output)
    size_correct = input_grid.shape == expected_output.shape == transformed_output.shape
    
    # Check for color palette correctness
    unique_input_colors = set(np.unique(input_grid))
    unique_expected_colors = set(np.unique(expected_output))
    unique_transformed_colors = set(np.unique(transformed_output))
    
    color_palette_correct = (unique_input_colors == unique_expected_colors) and (unique_expected_colors == unique_transformed_colors)
    
    # Check if the number of pixels of each color is the same
    correct_pixel_counts = True
    for color in unique_input_colors:
        if np.sum(input_grid == color) != np.sum(transformed_output == color) or np.sum(input_grid == color) != np.sum(expected_output == color):
            correct_pixel_counts = False
            break

    return {
        "match": match,
        "pixels_off": pixels_off,
        "size_correct": size_correct,
        "color_palette_correct": color_palette_correct,
        "correct_pixel_counts": correct_pixel_counts,
    }


# Example Data (replace with your actual data)
example_data = [
    {
        "input": np.array([[5, 0, 0], [3, 5, 0], [0, 0, 5]]),
        "expected": np.array([[5, 3, 0], [0, 5, 0], [0, 0, 5]]),
        "transformed": np.array([[5, 0, 0], [3, 5, 0], [0, 0, 5]])
    },
        {
        "input": np.array([[5, 0, 0, 0], [0, 5, 0, 0], [6, 0, 5, 0], [6, 0, 4, 5]]),
        "expected": np.array([[5, 0, 6, 6], [0, 5, 0, 0], [0, 0, 5, 4], [0, 0, 0, 5]]),
        "transformed": np.array([[5, 0, 6, 6], [0, 5, 0, 0], [6, 0, 5, 4], [6, 4, 0, 5]])
    },
    {
        "input": np.array([[5, 0, 0, 0, 0], [0, 5, 0, 0, 0], [8, 8, 5, 0, 0], [0, 2, 0, 5, 0], [0, 2, 0, 1, 5]]),
        "expected": np.array([[5, 0, 8, 0, 0], [0, 5, 8, 2, 2], [0, 0, 5, 0, 0], [0, 0, 0, 5, 1], [0, 0, 0, 0, 5]]),
        "transformed": np.array([[5, 0, 0, 0, 0], [0, 5, 0, 0, 0], [8, 8, 5, 0, 0], [2, 0, 0, 5, 0], [2, 1, 0, 0, 5]])
    }
]

for i, example in enumerate(example_data):
  analysis = analyze_results(example["input"], example["expected"], example["transformed"])
  print(f"Example {i+1}:")
  for k,v in analysis.items():
    print(f"\t{k}: {v}")
