import numpy as np
from collections import Counter

def analyze_results(input_grid, expected_output, transformed_output):
    """
    Analyzes the differences between the expected and transformed outputs.
    """
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)

    match = np.array_equal(expected_output, transformed_output)
    pixels_off = None
    size_correct = False
    color_palette_correct = False
    correct_pixel_counts = False

    if not match:
        pixels_off = np.where(expected_output != transformed_output)

    if expected_output.shape == transformed_output.shape:
        size_correct = True

    expected_colors = Counter(expected_output.flatten())
    transformed_colors = Counter(transformed_output.flatten())
    if expected_colors.keys() == transformed_colors.keys():
        color_palette_correct = True

    if size_correct and expected_colors == transformed_colors:
        correct_pixel_counts = True


    return {
        'match': match,
        'pixels_off': pixels_off,
        'size_correct': size_correct,
        'color_palette_correct': color_palette_correct,
        'correct_pixel_counts': correct_pixel_counts,
    }

# Example data (replace with your actual data)
examples = [
    {
        'input': [[0, 5, 0, 0, 0, 0, 0, 0, 0],
                  [2, 2, 0, 5, 1, 0, 5, 2, 2],
                  [0, 0, 0, 0, 5, 0, 0, 0, 0]],
        'expected': [[0, 2, 1, 1, 0, 0, 0],
                     [2, 2, 0, 1, 2, 2, 2],
                     [0, 0, 0, 0, 0, 0, 0]],
        'transformed': [[0, 1, 0, 0, 0, 0, 0, 0, 0],
                      [2, 2, 0, 1, 0, 0, 1, 2, 2],
                      [0, 0, 0, 0, 1, 0, 0, 0, 0]]
    },
   {
        'input': [[0, 0, 0, 5, 1, 5, 0, 0, 0, 0, 0],
                  [2, 2, 0, 0, 0, 0, 0, 0, 3, 3, 3],
                  [0, 5, 0, 0, 0, 0, 0, 5, 3, 0, 0]],
        'expected': [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [2, 2, 0, 0, 0, 0, 3, 3, 3],
                     [0, 2, 1, 1, 1, 3, 3, 0, 0]],
        'transformed': [[0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                        [2, 2, 0, 0, 0, 0, 0, 0, 3, 3, 3],
                        [0, 1, 0, 0, 0, 0, 0, 1, 3, 0, 0]]
    },
    {
        'input': [[0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0],
                  [2, 2, 2, 0, 5, 8, 8, 0, 0, 0, 0],
                  [0, 0, 5, 0, 0, 0, 0, 0, 5, 6, 6]],
        'expected': [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [2, 2, 2, 0, 0, 8, 6, 6, 6],
                     [0, 0, 2, 8, 8, 8, 0, 0, 0]],
        'transformed': [[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [2, 2, 2, 0, 1, 8, 8, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 1, 6, 6]]
    },
    {
        'input': [[0, 1, 5, 0, 0, 0, 0, 0, 2, 2, 0],
                  [1, 1, 0, 0, 5, 2, 0, 5, 2, 0, 0],
                  [0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0]],
        'expected': [[0, 1, 1, 2, 2, 0, 2, 2],
                     [1, 1, 0, 0, 2, 2, 2, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0]],
        'transformed': [[0, 0, 1, 0, 0, 0, 0, 0, 2, 2, 0],
                        [0, 0, 0, 0, 1, 2, 0, 1, 2, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
    }
]

for i, example in enumerate(examples):
    results = analyze_results(example['input'], example['expected'], example['transformed'])
    print(f"Example {i+1}:")
    print(f"  Match: {results['match']}")
    print(f"  Pixels Off (Indices): {results['pixels_off']}")
    print(f"  Size Correct: {results['size_correct']}")
    print(f"  Color Palette Correct: {results['color_palette_correct']}")
    print(f"  Correct Pixel Counts: {results['correct_pixel_counts']}")
    print("-" * 20)