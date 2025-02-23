import numpy as np

def analyze_example(input_grid, expected_output):
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)

    input_colors = np.unique(input_grid)
    output_colors = np.unique(expected_output)
    
    input_color_counts = {color: np.sum(input_grid == color) for color in input_colors}
    output_color_counts = {color: np.sum(expected_output == color) for color in output_colors}
    
    rotated_input = np.rot90(input_grid, k=-1) #rotate clockwise
    
    diff_with_rotation = np.sum(rotated_input != expected_output)
    
    print(f"  Input Colors: {input_colors}")
    print(f"  Output Colors: {output_colors}")
    print(f"  Input Color Counts: {input_color_counts}")
    print(f"  Output Color Counts: {output_color_counts}")
    print(f"  Differences after rotation: {diff_with_rotation}")

print("Example 1:")
analyze_example([[9, 0, 0], [9, 9, 9], [9, 9, 9]], [[0, 9, 9], [0, 9, 9], [9, 9, 9]])

print("\nExample 2:")
analyze_example([[0, 6, 6], [6, 0, 0], [6, 6, 0]], [[6, 0, 0], [6, 0, 6], [6, 0, 6]])

print("\nExample 3:")
analyze_example([[0, 0, 9], [0, 0, 9], [9, 9, 9]], [[9, 9, 9], [0, 0, 9], [0, 0, 9]])

print("\nExample 4:")
analyze_example([[2, 0, 2], [0, 0, 2], [0, 2, 2]], [[2, 2, 2], [0, 0, 2], [2, 0, 0]])
