import numpy as np

def grid_from_string(grid_string):
    lines = grid_string.strip().split('\n')
    return np.array([[int(x) for x in line.split()] for line in lines])

def compare_grids(grid1, grid2):
    diff_grid = np.where(grid1 != grid2, 1, 0)
    pixels_off = np.sum(diff_grid)
    return pixels_off, diff_grid

# Example 1 Data
input_grid_ex1_str = """
0 0 0 0 0 0 0
0 8 0 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
"""
expected_output_ex1_str = """
0 0 0 0 0 0 0
0 8 1 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
"""
transformed_output_ex1_str = """
0 0 0 0 0 0 0
0 8 0 0 0 0 0
0 8 8 1 0 0 0
0 0 0 0 8 8 1
0 0 0 0 0 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
"""

input_grid_ex1 = grid_from_string(input_grid_ex1_str)
expected_output_ex1 = grid_from_string(expected_output_ex1_str)
transformed_output_ex1 = grid_from_string(transformed_output_ex1_str)

pixels_off_ex1, diff_grid_ex1 = compare_grids(transformed_output_ex1, expected_output_ex1)

print("Example 1 Diff Grid:")
print(diff_grid_ex1)
print(f"Pixels Off: {pixels_off_ex1}")


# Example 2 Data
input_grid_ex2_str = """
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 8 0 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 0 8 0 0
0 0 0 8 8 0 0
"""
expected_output_ex2_str = """
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 8 1 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 1 8 0 0
0 0 0 8 8 0 0
"""
transformed_output_ex2_str = """
0 0 0 0 8 8 1
0 0 0 0 0 8 0
0 0 8 0 0 0 0
0 0 8 8 1 0 0
0 0 0 0 0 0 0
0 0 0 0 8 1 0
0 0 0 8 8 0 0
"""

input_grid_ex2 = grid_from_string(input_grid_ex2_str)
expected_output_ex2 = grid_from_string(expected_output_ex2_str)
transformed_output_ex2 = grid_from_string(transformed_output_ex2_str)

pixels_off_ex2, diff_grid_ex2 = compare_grids(transformed_output_ex2, expected_output_ex2)

print("\nExample 2 Diff Grid:")
print(diff_grid_ex2)
print(f"Pixels Off: {pixels_off_ex2}")