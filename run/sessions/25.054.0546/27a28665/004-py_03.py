import numpy as np

def transform(input_grid):
    input_array = np.array(input_grid)
    rows, cols = input_array.shape

    # Rule derived from the first example pair:
    count = 0
    if rows == cols:  # Only consider square grids
        main_diag = [input_array[i, i] for i in range(rows)]
        anti_diag = [input_array[i, cols - 1 - i] for i in range(rows)]

        main_diag_non_white = [x for x in main_diag if x != 0]
        anti_diag_non_white = [x for x in anti_diag if x != 0]

        if main_diag_non_white == anti_diag_non_white and len(main_diag_non_white) > 0:
              count = 1
        else:
            if len(main_diag_non_white) > 0 or len(anti_diag_non_white) > 0:
              count = 2
    if len(main_diag_non_white) == 0 and len(anti_diag_non_white) == 0:
      count = 0

    return [[count]]

examples = [
    ([[5, 5, 0], [5, 0, 5], [0, 5, 0]], [[1]]),
    ([[8, 0, 8], [0, 8, 0], [8, 0, 8]], [[2]]),
    ([[5, 0, 5], [0, 5, 0], [5, 0, 5]], [[2]]),
    ([[0, 1, 1], [0, 1, 1], [1, 0, 0]], [[3]]),
    ([[0, 8, 8], [0, 8, 8], [8, 0, 0]], [[3]]),
    ([[4, 4, 0], [4, 0, 4], [0, 4, 0]], [[1]]),
    ([[0, 5, 0], [5, 5, 5], [0, 5, 0]], [[6]]),
]

# Test against all examples
results = []
for input_grid, expected_output in examples:
    output = transform(input_grid)
    match = output == expected_output
    results.append({
        "input": input_grid,
        "expected_output": expected_output,
        "actual_output": output,
        "match": match
    })

import json
print(json.dumps(results, indent=2))
