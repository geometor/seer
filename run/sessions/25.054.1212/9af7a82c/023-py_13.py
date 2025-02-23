import numpy as np

def analyze_examples(examples):
    for i, example in enumerate(examples):
        input_grid = np.array(example['input'])
        expected_output = np.array(example['output'])
        transformed_output = example['transformed_output']


        input_rows, input_cols = input_grid.shape
        output_rows, output_cols = expected_output.shape

        print(f"Example {i+1}:")
        print(f"  Input shape: {input_grid.shape}")
        print(f"  Expected Output shape: {expected_output.shape}")
        print(f"  Transformed shape {transformed_output.shape}")

        # Check column reversal (with the last-to-first swap)
        reversed_cols_correct = True
        for j in range(input_cols):
          if not np.array_equal(input_grid[:, input_cols - 1 - j], expected_output[:input_rows, j]):
                if j == 0:
                    continue # allow last column
                else:
                    reversed_cols_correct = False
                    break

        print(f"  Columns reversed (with last-to-first): {reversed_cols_correct}")

        # check if expected first row is the same as input first row:
        print(f"  first row same {np.array_equal(expected_output[0,:], input_grid[0,::-1])}")


examples = [
    {
        'input': [[2, 2, 1], [2, 3, 1], [1, 1, 1]],
        'output': [[1, 2, 3], [1, 2, 0], [1, 2, 0], [1, 0, 0], [1, 0, 0]],
        'transformed_output': [[2, 2, 1], [2, 3, 1], [1, 1, 1], [2, 0, 0], [0, 0, 0]]
    },
    {
        'input': [[3, 1, 1, 4], [2, 2, 2, 4], [4, 4, 4, 4]],
        'output': [[4, 2, 1, 3], [4, 2, 1, 0], [4, 2, 0, 0], [4, 0, 0, 0], [4, 0, 0, 0], [4, 0, 0, 0]],
       'transformed_output': [[3, 1, 1, 4], [2, 2, 2, 4], [4, 4, 4, 4], [3, 0, 0, 0], [0, 0, 0, 0]]

    },
    {
        'input': [[8, 8, 2], [3, 8, 8], [3, 3, 4], [3, 3, 4]],
        'output': [[3, 8, 4, 2], [3, 8, 4, 0], [3, 8, 0, 0], [3, 8, 0, 0], [3, 0, 0, 0]],
        'transformed_output': [[8, 8, 2], [3, 8, 8], [3, 3, 4], [3, 3, 4], [8, 0, 0], [0, 0, 0], [0, 0, 0]]
    },
    {
        'input': [[1, 1, 1], [2, 2, 1], [2, 8, 1], [2, 8, 1]],
        'output': [[1, 2, 8], [1, 2, 8], [1, 2, 0], [1, 2, 0], [1, 0, 0], [1, 0, 0]],
        'transformed_output': [[1, 1, 1], [2, 2, 1], [2, 8, 1], [2, 8, 1], [1, 0, 0], [0, 0, 0], [0, 0, 0]]
    }
]

analyze_examples(examples)