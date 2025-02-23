import numpy as np
from collections import Counter

def analyze_results(examples):
    """Analyzes the results of the transformation attempts.

    Args:
        examples: A list of dictionaries, each containing 'input', 'expected_output',
                  'transformed_output', 'match', 'pixels_off', 'size_correct',
                  'color_palette_correct', and 'correct_pixel_counts'.
    """

    for i, example in enumerate(examples):
        print(f"## Example {i + 1}:")
        print(f"match: {example['match']}")
        print(f"pixels_off: {example['pixels_off']}")
        print(f"size_correct: {example['size_correct']}")
        print(f"color_palette_correct: {example['color_palette_correct']}")
        print(f"correct_pixel_counts: {example['correct_pixel_counts']}")

        # Detailed pixel-by-pixel comparison
        input_grid = np.array(example['input'])
        expected_grid = np.array(example['expected_output'])
        transformed_grid = np.array(example['transformed_output'])
        
        diff_grid_expected_transformed = expected_grid != transformed_grid
        print("\nDifferences between Expected and Transformed:")
        print(diff_grid_expected_transformed)


        input_color_counts = Counter(input_grid.flatten())
        expected_color_counts = Counter(expected_grid.flatten())
        transformed_color_counts = Counter(transformed_grid.flatten())

        print("\nColor Counts:")
        print(f"  Input: {input_color_counts}")
        print(f"  Expected: {expected_color_counts}")
        print(f"  Transformed: {transformed_color_counts}")


examples = [
    {
        'input': [[2, 2, 2], [2, 1, 8], [2, 8, 8]],
        'expected_output': [[2, 2, 2], [2, 5, 5], [2, 5, 5]],
        'transformed_output': [[2, 2, 2], [2, 1, 5], [5, 5, 8]],
        'match': False,
        'pixels_off': 3,
        'size_correct': True,
        'color_palette_correct': False,
        'correct_pixel_counts': False
    },
   {
        'input': [[1, 1, 1], [8, 1, 3], [8, 2, 2]],
        'expected_output': [[1, 1, 1], [5, 1, 5], [5, 5, 5]],
        'transformed_output': [[1, 1, 1], [5, 1, 3], [8, 5, 2]],
        'match': False,
        'pixels_off': 3,
        'size_correct': True,
        'color_palette_correct': False,
        'correct_pixel_counts': False
    },
    {
        'input': [[2, 2, 2], [8, 8, 2], [2, 2, 2]],
        'expected_output': [[2, 2, 2], [5, 5, 2], [2, 2, 2]],
        'transformed_output': [[2, 2, 2], [5, 8, 5], [2, 5, 2]],
        'match': False,
        'pixels_off': 3,
        'size_correct': True,
        'color_palette_correct': False,
        'correct_pixel_counts': False
    },
    {
        'input': [[3, 3, 8], [4, 4, 4], [8, 1, 1]],
        'expected_output': [[3, 3, 8], [5, 5, 5], [5, 1, 1]],
        'transformed_output': [[3, 3, 8], [5, 4, 5], [8, 1, 1]],
        'match': False,
        'pixels_off': 4,
        'size_correct': True,
        'color_palette_correct': False,
        'correct_pixel_counts': False
    }

]

analyze_results(examples)
