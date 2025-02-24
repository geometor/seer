import numpy as np

def analyze_example(input_str, expected_output_str, transformed_output_str):
    input_grid = np.array([list(map(int, row.split())) for row in input_str.split('\n')])
    expected_grid = np.array([list(map(int, row.split())) for row in expected_output_str.split('\n')])
    transformed_grid = np.array([list(map(int, row.split())) for row in transformed_output_str.split('\n')])

    diff = expected_grid - transformed_grid
    pixels_off = np.count_nonzero(diff)

    match = np.array_equal(expected_grid, transformed_grid)
    size_correct = input_grid.shape == expected_grid.shape
    unique_expected, counts_expected = np.unique(expected_grid, return_counts=True)
    unique_transformed, counts_transformed = np.unique(transformed_grid, return_counts=True)
    
    
    color_palette_correct = np.array_equal(np.sort(unique_expected), np.sort([0,1]))

    correct_pixel_counts = np.array_equal(counts_expected, counts_transformed)
    
    print(f"Match: {match}")
    print(f"Pixels Off: {pixels_off}")
    print(f"Size Correct: {size_correct}")
    print(f"Color Palette Correct: {color_palette_correct}")
    print(f"Correct Pixel Counts: {correct_pixel_counts}")
    if not correct_pixel_counts:
        print(f"  Expected Counts: {dict(zip(unique_expected, counts_expected))}")
        print(f"  Transformed Counts: {dict(zip(unique_transformed, counts_transformed))}")
        
# Example 1:
print("Example 1:")

input_str_1 = """
0 0
0 0
0 0
0 0
0 0
0 0
0 0
0 0
0 0
1 0
"""
expected_output_str_1 = """
0 1
1 0
0 1
1 0
0 1
1 0
0 1
1 0
0 1
1 0
"""
transformed_output_str_1 = """
0 1
1 0
0 1
1 0
0 1
1 0
0 1
1 0
0 1
1 0
"""

analyze_example(input_str_1, expected_output_str_1, transformed_output_str_1)

print("\nExample 2:")
input_str_2 = """
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
1 0 0
"""
expected_output_str_2 = """
0 1 0
1 0 0
0 1 0
0 0 1
0 1 0
1 0 0
0 1 0
0 0 1
0 1 0
1 0 0
"""
transformed_output_str_2 = """
0 1 0
1 0 1
0 1 0
1 0 1
0 1 0
1 0 1
0 1 0
1 0 1
0 1 0
1 0 1
"""
analyze_example(input_str_2, expected_output_str_2, transformed_output_str_2)


print("\nExample 3:")
input_str_3 = """
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
1 0 0 0
"""
expected_output_str_3 = """
0 0 0 1
0 0 1 0
0 1 0 0
1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
0 0 1 0
0 1 0 0
1 0 0 0
"""
transformed_output_str_3 = """
0 1 0 1
1 0 1 0
0 1 0 1
1 0 1 0
0 1 0 1
1 0 1 0
0 1 0 1
1 0 1 0
0 1 0 1
1 0 1 0
"""

analyze_example(input_str_3, expected_output_str_3, transformed_output_str_3)
