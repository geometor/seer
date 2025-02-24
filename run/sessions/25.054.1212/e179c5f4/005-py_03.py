import numpy as np

def transform(input_grid):
    # Initialize output grid with the same dimensions as the input grid.
    rows = len(input_grid)
    cols = len(input_grid[0])
    output_grid = np.zeros((rows, cols), dtype=int)

    # Apply a more complex pattern based on observations, not a simple checkerboard.
    # This is a placeholder for the actual, still-to-be-determined logic.
    # We're trying a pattern that might capture runs of 8s and 1s.
    for i in range(rows):
        for j in range(cols):
            if i < rows and j < cols:
                if (i // 2 ) % 2 == 0:
                    if(j//2) % 2 == 0:
                        output_grid[i][j] = 8
                    else:
                        output_grid[i][j] = 1
                else:
                    if(j//2) % 2 == 0:
                        output_grid[i][j] = 1
                    else:
                        output_grid[i][j] = 8
    return output_grid

# Example inputs (as strings for easier handling)
input_grids_str = [
    "0 0\n0 0\n0 0\n0 0\n0 0\n0 0\n0 0\n0 0\n0 0\n1 0",
    "0 0 0\n0 0 0\n0 0 0\n0 0 0\n0 0 0\n0 0 0\n0 0 0\n0 0 0\n0 0 0\n1 0 0",
    "0 0 0 0\n0 0 0 0\n0 0 0 0\n0 0 0 0\n0 0 0 0\n0 0 0 0\n0 0 0 0\n0 0 0 0\n0 0 0 0\n1 0 0 0"
]

# Expected outputs (as strings)
expected_outputs_str = [
    "8 1\n1 8\n8 1\n1 8\n8 1\n1 8\n8 1\n1 8\n8 1\n1 8",
    "8 1 8\n1 8 8\n8 1 8\n8 8 1\n8 1 8\n1 8 8\n8 1 8\n8 8 1\n8 1 8\n1 8 8",
    "8 8 8 1\n8 8 1 8\n8 1 8 8\n1 8 8 8\n8 1 8 8\n8 8 1 8\n8 8 8 1\n8 8 1 8\n8 1 8 8\n1 8 8 8"
]

# Convert string inputs to numpy arrays
input_grids = [np.array([list(map(int, row.split())) for row in grid_str.split('\n')]) for grid_str in input_grids_str]
expected_outputs = [np.array([list(map(int, row.split())) for row in grid_str.split('\n')]) for grid_str in expected_outputs_str]

# Transform the input grids
transformed_outputs = [transform(grid) for grid in input_grids]

# Compare and report
for i, (expected, transformed) in enumerate(zip(expected_outputs, transformed_outputs)):
    match = np.array_equal(expected, transformed)
    pixels_off = np.sum(expected != transformed)
    size_correct = expected.shape == transformed.shape
    unique_expected, counts_expected = np.unique(expected, return_counts=True)
    unique_transformed, counts_transformed = np.unique(transformed, return_counts=True)

    color_palette_correct = set(unique_expected) == set(unique_transformed)
   
    correct_pixel_counts = False
    if color_palette_correct:
        correct_pixel_counts = all([counts_expected[i]==counts_transformed[i] for i,_ in enumerate(unique_expected)])

    print(f"Example {i+1}:")
    print(f"match: {match}")
    print(f"pixels_off: {pixels_off}")
    print(f"size_correct: {size_correct}")
    print(f"color_palette_correct: {color_palette_correct}")
    print(f"correct_pixel_counts: {correct_pixel_counts}")

    print(f"{transformed=}")
    print(f"{expected=}")    
    print("-" * 20)