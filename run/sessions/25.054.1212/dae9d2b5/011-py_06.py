import pandas as pd
import numpy as np

# Input and expected output data for all examples
data = {
    'example': [1, 2, 3, 4, 5],
    'input': [
        np.array([[4, 4, 0, 3, 3, 0], [4, 0, 0, 3, 0, 0], [0, 0, 0, 0, 0, 3]]),
        np.array([[4, 0, 4, 3, 3, 0], [4, 0, 0, 3, 0, 0], [0, 0, 4, 3, 0, 0]]),
        np.array([[0, 0, 4, 0, 3, 0], [0, 4, 4, 3, 0, 3], [4, 4, 0, 0, 0, 3]]),
        np.array([[4, 4, 0, 3, 0, 0], [0, 0, 0, 0, 0, 3], [4, 0, 0, 0, 0, 0]]),
        np.array([[0, 0, 0, 0, 3, 0], [4, 0, 0, 0, 0, 0], [0, 0, 4, 3, 3, 0]])
    ],
    'expected_output': [
        np.array([[6, 6, 0], [6, 0, 0], [0, 0, 6]]),
        np.array([[6, 6, 6], [6, 0, 0], [6, 0, 6]]),
        np.array([[0, 6, 6], [6, 6, 6], [6, 6, 6]]),
        np.array([[6, 6, 0], [0, 0, 6], [6, 0, 0]]),
        np.array([[0, 6, 0], [6, 0, 0], [6, 6, 6]])
    ]
}

# Previous transform function (for reference)
def transform_previous(input_grid):
    output_grid = np.zeros((3, 3), dtype=int)
    for out_col in range(3):
        in_col1 = out_col * 2
        in_col2 = out_col * 2 + 1
        for row in range(3):
            if (input_grid[row, in_col1] != 0) or (input_grid[row, in_col2] != 0):
                output_grid[row, out_col] = 6
    return output_grid

# Create DataFrame to store the report data
report = pd.DataFrame(data)

# Apply the *previous* transform function and check matching
report['transformed_output'] = report['input'].apply(transform_previous)
report['match'] = report.apply(lambda row: np.array_equal(row['expected_output'], row['transformed_output']), axis=1)

# Calculate differences
def calculate_differences(expected, transformed):
    if not np.array_equal(expected,transformed):
        return np.sum(expected != transformed)
    else: return 0

report['pixels_off'] = report.apply(lambda row: calculate_differences(row['expected_output'], row['transformed_output']), axis=1)
report['size_correct'] = report.apply(lambda row: row['expected_output'].shape == row['transformed_output'].shape, axis=1)

# check color palette
def check_color_palette(expected, transformed):
    exp_colors = np.unique(expected)
    trans_colors = np.unique(transformed)
    if len(exp_colors) != len(trans_colors): return False
    return np.all(np.isin(exp_colors,trans_colors))

report['color_palette_correct'] = report.apply(lambda row: check_color_palette(row['expected_output'], row['transformed_output']), axis=1)

# calculate correct pixel counts
def check_pixel_counts(expected, transformed):
        exp_value_counts = pd.Series(expected.flatten()).value_counts()
        trans_value_counts = pd.Series(transformed.flatten()).value_counts()
        return exp_value_counts.equals(trans_value_counts)

report['correct_pixel_counts'] = report.apply(lambda row: check_pixel_counts(row['expected_output'], row['transformed_output']), axis=1)

print(report.drop(['input','expected_output','transformed_output'], axis=1))