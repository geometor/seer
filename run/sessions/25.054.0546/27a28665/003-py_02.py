def analyze_example(input_grid, output_grid):
    import numpy as np

    input_array = np.array(input_grid)
    rows, cols = input_array.shape
    white_pixels = np.sum(input_array == 0)
    non_white_pixels = np.sum(input_array != 0)
    output_value = output_grid[0][0]

    main_diagonal_pixels = []
    anti_diagonal_pixels = []
    for i in range(min(rows, cols)):
        main_diagonal_pixels.append(input_array[i, i])
        anti_diagonal_pixels.append(input_array[i, cols - 1 - i])

    main_diag_counts = {}
    anti_diag_counts = {}
    for i in range(10): #check counts for all colors
        main_diag_counts[i] = main_diagonal_pixels.count(i)
        anti_diag_counts[i] = anti_diagonal_pixels.count(i)


    analysis = {
        "rows": rows,
        "cols": cols,
        "white_pixels": int(white_pixels),
        "non_white_pixels": int(non_white_pixels),
        "output_value": int(output_value),
        "main_diagonal_pixels": [int(x) for x in main_diagonal_pixels], #convert to standard python int
        "anti_diagonal_pixels": [int(x) for x in anti_diagonal_pixels],
        "main_diag_counts": {k: int(v) for k, v in main_diag_counts.items()}, #all to int for json
        "anti_diag_counts": {k: int(v) for k, v in anti_diag_counts.items()},
    }
    return analysis

# Example Usage with the provided examples (converted to list format):

examples = [
    ([[5, 5, 0], [5, 0, 5], [0, 5, 0]], [[1]]),
    ([[8, 0, 8], [0, 8, 0], [8, 0, 8]], [[2]]),
    ([[5, 0, 5], [0, 5, 0], [5, 0, 5]], [[2]]),
    ([[0, 1, 1], [0, 1, 1], [1, 0, 0]], [[3]]),
    ([[0, 8, 8], [0, 8, 8], [8, 0, 0]], [[3]]),
    ([[4, 4, 0], [4, 0, 4], [0, 4, 0]], [[1]]),
    ([[0, 5, 0], [5, 5, 5], [0, 5, 0]], [[6]]),
]

analysis_results = []
for input_grid, output_grid in examples:
    analysis_results.append(analyze_example(input_grid, output_grid))

import json #for pretty printing
print(json.dumps(analysis_results, indent=2))