import numpy as np

def analyze_example(input_grid, expected_output, transformed_output):
    """Analyzes an example and returns metrics."""
    
    match = np.array_equal(expected_output, transformed_output)
    pixels_off = np.sum(expected_output != transformed_output)
    size_correct = expected_output.shape == transformed_output.shape
    
    # Flatten the arrays for easier comparison
    expected_flat = expected_output.flatten()
    transformed_flat = transformed_output.flatten()
    
    # Get unique colors and their counts in expected output
    expected_colors, expected_counts = np.unique(expected_flat, return_counts=True)
    expected_color_counts = dict(zip(expected_colors, expected_counts))
    
    # Get unique colors and their counts in transformed output
    transformed_colors, transformed_counts = np.unique(transformed_flat, return_counts=True)
    transformed_color_counts = dict(zip(transformed_colors, transformed_counts))
    
    color_palette_correct = set(expected_colors) == set(transformed_colors)
    
    #compare counts.
    correct_pixel_counts=True
    for color in expected_color_counts.keys():
       if expected_color_counts[color]!=transformed_color_counts.get(color, -1):
            correct_pixel_counts=False

    return {
        "match": match,
        "pixels_off": pixels_off,
        "size_correct": size_correct,
        "color_palette_correct": color_palette_correct,
        "correct_pixel_counts": correct_pixel_counts,
        "expected_color_counts": expected_color_counts,
        "transformed_color_counts": transformed_color_counts,
    }
def get_grid_from_text(grid_text):
    lines = grid_text.strip().split('\n')
    return np.array([[int(val) for val in line.split()] for line in lines])

# Example Data (as provided in problem)
example1_input = """
0 0 0 0 0 0 0
0 8 0 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
"""
example1_expected = """
0 0 0 0 0 0 0
0 8 1 0 0 0 0
0 8 8 0 0 0 0
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
"""
example1_transformed = """
0 0 0 0 0 0 0
0 1 0 0 0 0 0
0 1 1 0 0 0 0
0 0 0 0 1 1 0
0 0 0 0 0 1 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
"""

example2_input = """
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 8 0 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 0 8 0 0
0 0 0 8 8 0 0
"""
example2_expected = """
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 8 1 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 1 8 0 0
0 0 0 8 8 0 0
"""
example2_transformed = """
0 0 0 0 1 1 0
0 0 0 0 0 1 0
0 0 1 0 0 0 0
0 0 1 1 0 0 0
0 0 0 0 0 0 0
0 0 0 0 1 0 0
0 0 0 1 1 0 0
"""

example1_input_grid = get_grid_from_text(example1_input)
example1_expected_grid = get_grid_from_text(example1_expected)
example1_transformed_grid = get_grid_from_text(example1_transformed)

example2_input_grid = get_grid_from_text(example2_input)
example2_expected_grid = get_grid_from_text(example2_expected)
example2_transformed_grid = get_grid_from_text(example2_transformed)

analysis1 = analyze_example(example1_input_grid, example1_expected_grid, example1_transformed_grid)
analysis2 = analyze_example(example2_input_grid, example2_expected_grid, example2_transformed_grid)

print("Example 1 Analysis:", analysis1)
print("Example 2 Analysis:", analysis2)