import numpy as np

def analyze_grid_diff(input_grid, expected_output, transformed_output):
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    
    # Handle potential errors and size mismatches
    if transformed_output is None:
        print("Transformed output is None (likely due to an error).")
        return
    
    if expected_output.shape != transformed_output.shape:
      print(f"size mismatch, expected: {expected_output.shape}, got: {transformed_output.shape}")
      return
    
    diff = expected_output != transformed_output
    pixels_off = np.sum(diff)
    print(f"Pixels Off: {pixels_off}")
    print(f"Size Correct: {expected_output.shape == transformed_output.shape}")
    print(f"Color Palette Correct: {set(np.unique(input_grid)) <= set(np.unique(expected_output))}")  #check subsets

    input_colors = dict(zip(*np.unique(input_grid, return_counts=True)))
    expected_colors = dict(zip(*np.unique(expected_output, return_counts=True)))
    transformed_colors = dict(zip(*np.unique(transformed_output, return_counts=True)))

    print(f"Input Colors: {input_colors}")
    print(f"Expected Colors: {expected_colors}")
    print(f"Transformed Colors: {transformed_colors}")


# Example 1
input_grid1 = [[2, 0, 0], [0, 0, 0], [0, 0, 2]]
expected_output1 = [[2, 0, 8, 2, 0, 8], [8, 0, 8, 8, 0, 8], [8, 0, 2, 8, 0, 2], [2, 0, 8, 2, 0, 8], [8, 0, 8, 8, 0, 8], [8, 0, 2, 8, 0, 2]]
transformed_output1 = [[2, 8, 0, 8, 0, 8], [8, 8, 8, 8, 8, 8], [0, 8, 0, 8, 0, 8], [8, 8, 8, 8, 8, 8], [0, 8, 0, 8, 2, 8], [8, 8, 8, 8, 8, 8]]

print("Example 1 Analysis:")
analyze_grid_diff(input_grid1, expected_output1, transformed_output1)


# Example 2
input_grid2 = [[0, 5, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [5, 0, 0, 0, 0, 5], [0, 0, 0, 0, 0, 0]]
expected_output2 = [[8, 5, 0, 0, 0, 8, 8, 5, 0, 0, 0, 8], [8, 8, 0, 0, 0, 8, 8, 8, 0, 0, 0, 8], [8, 8, 0, 0, 0, 8, 8, 8, 0, 0, 0, 8], [8, 8, 0, 0, 0, 8, 8, 8, 0, 0, 0, 8], [5, 8, 0, 0, 0, 5, 5, 8, 0, 0, 0, 5], [8, 8, 0, 0, 0, 8, 8, 8, 0, 0, 0, 8], [8, 5, 0, 0, 0, 8, 8, 5, 0, 0, 0, 8], [8, 8, 0, 0, 0, 8, 8, 8, 0, 0, 0, 8], [8, 8, 0, 0, 0, 8, 8, 8, 0, 0, 0, 8], [8, 8, 0, 0, 0, 8, 8, 8, 0, 0, 0, 8], [5, 8, 0, 0, 0, 5, 5, 8, 0, 0, 0, 5], [8, 8, 0, 0, 0, 8, 8, 8, 0, 0, 0, 8]]
transformed_output2 = None  # Due to the error

print("\nExample 2 Analysis:")
analyze_grid_diff(input_grid2, expected_output2, transformed_output2)


# Example 3
input_grid3 = [[0, 4], [0, 0]]
expected_output3 = [[0, 4, 0, 4], [0, 8, 0, 8], [0, 4, 0, 4], [0, 8, 0, 8]]
transformed_output3 = [[0, 8, 4, 8], [8, 8, 8, 8], [0, 8, 0, 8], [8, 8, 8, 8]]

print("\nExample 3 Analysis:")
analyze_grid_diff(input_grid3, expected_output3, transformed_output3)
