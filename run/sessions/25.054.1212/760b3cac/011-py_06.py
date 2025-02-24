import numpy as np

def calculate_metrics(input_grid, expected_output, transformed_output):
    """Calculates and prints comparison metrics."""

    match = np.array_equal(expected_output, transformed_output)
    pixels_off = np.sum(expected_output != transformed_output)
    size_correct = expected_output.shape == transformed_output.shape
    color_palette_correct = set(np.unique(transformed_output)) <= set(np.unique(input_grid))

    # Count correct pixel colors
    correct_pixel_counts = True
    for color in set(np.unique(input_grid)):
      if np.sum(expected_output == color) != np.sum(transformed_output == color):
        correct_pixel_counts = False

    print(f"  match: {match}")
    print(f"  pixels_off: {pixels_off}")
    print(f"  size_correct: {size_correct}")
    print(f"  color_palette_correct: {color_palette_correct}")
    print(f"  correct_pixel_counts: {correct_pixel_counts}")
    
# Example data (replace with your actual data)
example1_input = np.array([[0, 0, 0, 8, 0, 8, 0, 0, 0],
                           [0, 0, 0, 0, 8, 8, 0, 0, 0],
                           [0, 0, 0, 0, 0, 8, 0, 0, 0],
                           [0, 0, 0, 4, 0, 0, 0, 0, 0],
                           [0, 0, 0, 4, 4, 4, 0, 0, 0],
                           [0, 0, 0, 0, 4, 0, 0, 0, 0]])
example1_expected = np.array([[8, 0, 8, 8, 0, 8, 0, 0, 0],
                              [8, 8, 0, 0, 8, 8, 0, 0, 0],
                              [8, 0, 0, 0, 0, 8, 0, 0, 0],
                              [0, 0, 0, 4, 0, 0, 0, 0, 0],
                              [0, 0, 0, 4, 4, 4, 0, 0, 0],
                              [0, 0, 0, 0, 4, 0, 0, 0, 0]])
example1_transformed = np.array([[8, 8, 8, 8, 8, 8, 0, 0, 0],
                                 [0, 0, 0, 0, 8, 8, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 8, 0, 0, 0],
                                 [0, 0, 0, 4, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 4, 4, 4, 0, 0, 0],
                                 [0, 0, 0, 0, 4, 0, 0, 0, 0]])

example2_input = np.array([[0, 0, 0, 8, 0, 8, 0, 0, 0],
                           [0, 0, 0, 8, 8, 8, 0, 0, 0],
                           [0, 0, 0, 8, 8, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 4, 0, 0, 0],
                           [0, 0, 0, 4, 4, 4, 0, 0, 0],
                           [0, 0, 0, 0, 4, 0, 0, 0, 0]])
example2_expected = np.array([[0, 0, 0, 8, 0, 8, 8, 0, 8],
                              [0, 0, 0, 8, 8, 8, 8, 8, 8],
                              [0, 0, 0, 8, 8, 0, 0, 8, 8],
                              [0, 0, 0, 0, 0, 4, 0, 0, 0],
                              [0, 0, 0, 4, 4, 4, 0, 0, 0],
                              [0, 0, 0, 0, 4, 0, 0, 0, 0]])
example2_transformed = np.array([[0, 0, 0, 8, 0, 8, 0, 0, 0],
                                 [0, 0, 0, 8, 8, 8, 0, 0, 0],
                                 [0, 0, 0, 8, 8, 0, 0, 0, 0],
                                 [0, 0, 0, 0, 0, 4, 0, 0, 0],
                                 [0, 0, 0, 4, 4, 4, 0, 0, 0],
                                 [0, 0, 0, 0, 4, 0, 0, 0, 0]])

example3_input = np.array([[0, 0, 0, 8, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 8, 8, 0, 0, 0],
                           [0, 0, 0, 8, 0, 0, 0, 0, 0],
                           [0, 0, 0, 4, 0, 0, 0, 0, 0],
                           [0, 0, 0, 4, 4, 4, 0, 0, 0],
                           [0, 0, 0, 0, 4, 0, 0, 0, 0]])
example3_expected = np.array([[0, 0, 8, 8, 0, 0, 0, 0, 0],
                              [8, 8, 0, 0, 8, 8, 0, 0, 0],
                              [0, 0, 8, 8, 0, 0, 0, 0, 0],
                              [0, 0, 0, 4, 0, 0, 0, 0, 0],
                              [0, 0, 0, 4, 4, 4, 0, 0, 0],
                              [0, 0, 0, 0, 4, 0, 0, 0, 0]])
example3_transformed = np.array([[8, 8, 8, 8, 8, 8, 8, 8, 8],
                                 [8, 8, 8, 8, 8, 8, 8, 8, 8],
                                 [8, 8, 8, 8, 8, 8, 8, 8, 8],
                                 [0, 0, 0, 4, 0, 0, 0, 0, 0],
                                 [0, 0, 0, 4, 4, 4, 0, 0, 0],
                                 [0, 0, 0, 0, 4, 0, 0, 0, 0]])

print("Example 1 Metrics:")
calculate_metrics(example1_input, example1_expected, example1_transformed)
print("\nExample 2 Metrics:")
calculate_metrics(example2_input, example2_expected, example2_transformed)
print("\nExample 3 Metrics:")
calculate_metrics(example3_input, example3_expected, example3_transformed)
