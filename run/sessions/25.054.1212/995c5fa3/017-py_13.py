import numpy as np

def analyze_example(input_grid, expected_output, example_num):
    """Analyzes a single example and reports on white pixel presence and output colors."""

    has_white_col_4 = 0 in input_grid[:, 4] if input_grid.shape[1] > 4 else False
    has_white_col_8 = 0 in input_grid[:, 8] if input_grid.shape[1] > 8 else False
    has_white_col_9 = 0 in input_grid[:, 9] if input_grid.shape[1] > 9 else False

    output_row_0_color = expected_output[0, 0]
    output_row_1_color = expected_output[1, 0]
    output_row_2_color = expected_output[2, 0]
    
    # convert to int
    has_white_col_4 = int(has_white_col_4)
    has_white_col_8 = int(has_white_col_8)
    has_white_col_9 = int(has_white_col_9)

    print(f"Example {example_num}:")
    print(f"  Input Grid Shape: {input_grid.shape}")
    print(f"  White in Input Col 4?: {has_white_col_4}")
    print(f"  White in Input Col 8?: {has_white_col_8}")
    print(f"  White in Input Col 9?: {has_white_col_9}")
    print(f"  Output Row 0 Color: {output_row_0_color}")
    print(f"  Output Row 1 Color: {output_row_1_color}")
    print(f"  Output Row 2 Color: {output_row_2_color}")
    print("-" * 20)
    return (has_white_col_4, has_white_col_8, has_white_col_9, output_row_0_color,
        output_row_1_color,output_row_2_color)

# Provided example data (replace with your actual data loading)
examples = [
    (np.array([[5, 5, 5, 5, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5],
               [5, 5, 5, 5, 0, 5, 0, 0, 5, 0, 0, 5, 5, 0],
               [5, 5, 5, 5, 0, 5, 0, 0, 5, 0, 0, 5, 5, 0],
               [5, 5, 5, 5, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5]]),
     np.array([[2, 2, 2],
               [8, 8, 8],
               [3, 3, 3]])),
    (np.array([[5, 5, 5, 5, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5],
               [0, 5, 5, 0, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5],
               [0, 5, 5, 0, 0, 5, 0, 0, 5, 0, 5, 5, 5, 5],
               [5, 5, 5, 5, 0, 5, 0, 0, 5, 0, 5, 5, 5, 5]]),
     np.array([[3, 3, 3],
               [4, 4, 4],
               [2, 2, 2]])),
    (np.array([[5, 5, 5, 5, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5],
               [5, 0, 0, 5, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5],
               [5, 0, 0, 5, 0, 5, 5, 5, 5, 0, 5, 0, 0, 5],
               [5, 5, 5, 5, 0, 5, 5, 5, 5, 0, 5, 0, 0, 5]]),
     np.array([[8, 8, 8],
               [2, 2, 2],
               [4, 4, 4]])),
    (np.array([[5, 5, 5, 5, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5],
               [5, 5, 5, 5, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5],
               [5, 5, 5, 5, 0, 5, 0, 0, 5, 0, 5, 5, 5, 5],
               [5, 5, 5, 5, 0, 5, 0, 0, 5, 0, 5, 5, 5, 5]]),
     np.array([[2, 2, 2],
               [4, 4, 4],
               [2, 2, 2]])),
]
results = []
for i, (input_grid, expected_output) in enumerate(examples):
   results.append(analyze_example(input_grid, expected_output, i + 1))

# analyze the results
col_4 = [x[0] for x in results]
col_8 = [x[1] for x in results]
col_9 = [x[2] for x in results]
row_0 = [x[3] for x in results]
row_1 = [x[4] for x in results]
row_2 = [x[5] for x in results]

print(f"col_4 results: {col_4}")
print(f"col_8 results: {col_8}")
print(f"col_9 results: {col_9}")
print(f"row_0 results: {row_0}")
print(f"row_1 results: {row_1}")
print(f"row_2 results: {row_2}")