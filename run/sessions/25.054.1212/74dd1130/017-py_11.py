import numpy as np

def analyze_rows(input_grid, output_grid):
    """Analyzes the relationship between rows in input and output grids."""
    input_rows = [tuple(row) for row in input_grid]
    output_rows = [tuple(row) for row in output_grid]
    row_mapping = {}
    for i, in_row in enumerate(input_rows):
        if in_row in output_rows:
            out_indices = [j for j, out_row in enumerate(output_rows) if out_row == in_row]
            row_mapping[i] = out_indices
        else:
            row_mapping[i] = []  # Row not found in output
    return row_mapping

def calculate_metrics(input_grid, expected_output, transformed_output):
     #convert to numpy arrays
    input_grid_np = np.array(input_grid)
    expected_output_np = np.array(expected_output)
    transformed_output_np = np.array(transformed_output)
    
    pixels_off = np.sum(expected_output_np != transformed_output_np)
    size_correct = input_grid_np.shape == expected_output_np.shape == transformed_output_np.shape
    color_palette_correct = np.all(np.isin(transformed_output_np, np.unique(np.concatenate((input_grid_np.flatten(), expected_output_np.flatten())))))

    unique_input_colors = np.unique(input_grid_np)
    input_counts = {int(color): np.count_nonzero(input_grid_np == color) for color in unique_input_colors}
    unique_expected_colors = np.unique(expected_output_np)
    expected_counts = {int(color): np.count_nonzero(expected_output_np == color) for color in unique_expected_colors}
    unique_transformed_colors = np.unique(transformed_output_np)
    transformed_counts = {int(color): np.count_nonzero(transformed_output_np == color) for color in unique_transformed_colors}

    correct_pixel_counts = (input_counts == expected_counts) and (expected_counts == transformed_counts)
    row_mapping_in_to_out = analyze_rows(input_grid_np, expected_output_np)
    row_mapping_in_to_transformed = analyze_rows(input_grid_np, transformed_output_np)
    
    return {
        'pixels_off': int(pixels_off),
        'size_correct': bool(size_correct),
        'color_palette_correct': bool(color_palette_correct),
        'correct_pixel_counts': bool(correct_pixel_counts),
        'row_mapping_in_to_out': row_mapping_in_to_out,
        'row_mapping_in_to_transformed': row_mapping_in_to_transformed,
        'input_counts': input_counts,
        'expected_counts': expected_counts,
        'transformed_counts': transformed_counts
    }

examples = [
    {
        'input': [[2, 1, 1], [1, 5, 1], [5, 2, 2]],
        'expected': [[2, 1, 5], [2, 5, 2], [1, 1, 2]],
        'transformed': [[1, 1, 2], [1, 5, 1], [2, 2, 5]]
    },
    {
        'input': [[2, 6, 5], [6, 2, 2], [5, 5, 5]],
        'expected': [[2, 6, 5], [2, 2, 5], [5, 2, 5]],
        'transformed': [[6, 5, 2], [2, 2, 6], [5, 5, 5]]
    },
    {
        'input': [[9, 5, 5], [5, 5, 8], [5, 8, 9]],
        'expected': [[9, 5, 5], [9, 5, 8], [5, 8, 9]],
        'transformed': [[5, 5, 9], [8, 5, 5], [9, 8, 5]]
    },
    {
        'input': [[2, 2, 6], [2, 1, 1], [2, 6, 2]],
        'expected': [[2, 2, 2], [6, 1, 6], [6, 1, 2]],
        'transformed': [[2, 6, 2], [1, 1, 2], [2, 6, 2]]
    }
]

for i, example in enumerate(examples):
    metrics = calculate_metrics(example['input'], example['expected'], example['transformed'])
    print(f"Example {i+1}:")
    print(f"  Metrics: {metrics}")
    print("---")
