import numpy as np

def analyze_example(input_grid, expected_output, transformed_output):
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)

    pixels_off = np.sum(expected_output != transformed_output)
    size_correct = input_grid.shape[0] == 5 and input_grid.shape[1] == 5 and expected_output.shape[0] == 3 and expected_output.shape[1] == 3
    unique_input_colors = np.unique(input_grid)
    unique_expected_colors = np.unique(expected_output)
    
    color_palette_correct = all([c in [0,1,2,3,4,5,6,7,8,9] for c in unique_input_colors]) and all([c in [0,1,2,3,4,5,6,7,8,9] for c in unique_expected_colors])

    input_counts = {c: np.sum(input_grid == c) for c in unique_input_colors}
    expected_counts = {c: np.sum(expected_output == c) for c in unique_expected_colors}
    correct_pixel_counts = all([input_counts.get(c,0) == expected_counts.get(c, 0) for c in unique_input_colors])

    print(f"""
pixels_off: {pixels_off}
size_correct: {size_correct}
color_palette_correct: {color_palette_correct}
correct_pixel_counts: {correct_pixel_counts}
unique_input_colors: {unique_input_colors}
unique_expected_colors: {unique_expected_colors}
""")

examples = [
    ([[2, 0, 0, 0, 0], [0, 2, 0, 0, 2], [2, 0, 0, 2, 0], [0, 0, 0, 2, 2], [0, 0, 2, 2, 0]],
     [[5, 5, 5], [0, 5, 0], [0, 5, 0]],
     [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),

    ([[0, 0, 0, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 1, 1], [0, 1, 0, 1, 0], [0, 0, 0, 0, 1]],
     [[0, 5, 0], [5, 5, 5], [0, 5, 0]],
     [[5, 5, 5], [5, 5, 5], [5, 5, 5]]),

    ([[3, 0, 0, 0, 0], [0, 0, 0, 3, 3], [0, 3, 3, 0, 0], [0, 3, 0, 3, 0], [3, 0, 3, 3, 0]],
     [[0, 0, 5], [0, 0, 5], [5, 5, 5]],
     [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),

    ([[1, 0, 1, 0, 0], [1, 0, 0, 1, 1], [1, 1, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]],
     [[0, 5, 0], [5, 5, 5], [0, 5, 0]],
     [[5, 5, 5], [5, 5, 5], [5, 5, 5]]),

    ([[2, 0, 2, 0, 2], [2, 0, 0, 0, 2], [2, 2, 0, 0, 0], [2, 0, 0, 2, 2], [2, 2, 2, 0, 2]],
     [[5, 5, 5], [0, 5, 0], [0, 5, 0]],
     [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),

    ([[0, 2, 0, 2, 0], [0, 2, 2, 2, 0], [0, 2, 2, 0, 2], [2, 2, 2, 0, 0], [0, 0, 2, 0, 2]],
     [[5, 5, 5], [0, 5, 0], [0, 5, 0]],
     [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),

    ([[0, 3, 0, 3, 0], [3, 3, 0, 0, 0], [0, 3, 0, 0, 0], [0, 0, 3, 0, 0], [3, 3, 3, 0, 0]],
     [[0, 0, 5], [0, 0, 5], [5, 5, 5]],
     [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
]
for i, example in enumerate(examples):
    print(f"Example {i+1}:")
    analyze_example(example[0], example[1], example[2])
