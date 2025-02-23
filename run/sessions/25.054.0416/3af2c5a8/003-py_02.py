import numpy as np

def describe_grid(grid):
    """Provides a textual description of the grid's contents."""
    height, width = grid.shape
    description = f"Grid dimensions: {height}x{width}\n"
    unique, counts = np.unique(grid, return_counts=True)
    color_counts = dict(zip(unique, counts))
    for color, count in color_counts.items():
        description += f"Color {color}: {count} pixels\n"
    return description

def analyze_example(input_grid, expected_output, transformed_output):
    """Analyzes a single example and returns a report."""

    report = "--- Example Analysis ---\n"
    report += "\nInput Grid:\n"
    report += describe_grid(input_grid)
    report += "\nExpected Output Grid:\n"
    report += describe_grid(expected_output)
    report += "\nTransformed Output Grid:\n"
    report += describe_grid(transformed_output)
    report += "\nComparison:\n"

    match = np.array_equal(expected_output, transformed_output)
    report += f"Match: {match}\n"

    if not match:
        diff = expected_output - transformed_output
        pixels_off = np.count_nonzero(diff)
        report += f"Pixels Off: {pixels_off}\n"
        
        # compare sizes
        expected_height, expected_width = expected_output.shape
        transformed_height, transformed_width = transformed_output.shape
        
        size_correct = expected_height == transformed_height and expected_width == transformed_width
        
        report += f"Size Correct: {size_correct}\n"
    
    return report

# Example Data (from the prompt)
example1_input = np.array([[0, 0, 8, 0], [0, 8, 0, 8], [0, 0, 8, 0]])
example1_expected = np.array([[0, 0, 8, 0, 0, 8, 0, 0], [0, 8, 0, 8, 8, 0, 8, 0], [0, 0, 8, 0, 0, 8, 0, 0], [0, 0, 8, 0, 0, 8, 0, 0], [0, 8, 0, 8, 8, 0, 8, 0], [0, 0, 8, 0, 0, 8, 0, 0]])
example1_transformed = np.array([[0, 0, 8, 0, 0, 0, 8, 0], [0, 8, 0, 8, 0, 8, 0, 8], [0, 0, 8, 0, 0, 0, 8, 0], [0, 0, 8, 0, 0, 0, 8, 0], [0, 8, 0, 8, 0, 8, 0, 8], [0, 0, 8, 0, 0, 0, 8, 0]])

example2_input = np.array([[0, 0, 3, 3], [0, 3, 0, 3], [3, 3, 3, 0]])
example2_expected = np.array([[0, 0, 3, 3, 3, 3, 0, 0], [0, 3, 0, 3, 3, 0, 3, 0], [3, 3, 3, 0, 0, 3, 3, 3], [3, 3, 3, 0, 0, 3, 3, 3], [0, 3, 0, 3, 3, 0, 3, 0], [0, 0, 3, 3, 3, 3, 0, 0]])
example2_transformed = np.array([[0, 0, 3, 3, 0, 0, 3, 3], [0, 3, 0, 3, 0, 3, 0, 3], [3, 3, 3, 0, 3, 3, 3, 0], [0, 0, 3, 3, 0, 0, 3, 3], [0, 3, 0, 3, 0, 3, 0, 3], [3, 3, 3, 0, 3, 3, 3, 0]])

example3_input = np.array([[3, 3, 3, 3], [3, 0, 0, 0], [3, 0, 0, 0]])
example3_expected = np.array([[3, 3, 3, 3, 3, 3, 3, 3], [3, 0, 0, 0, 0, 0, 0, 3], [3, 0, 0, 0, 0, 0, 0, 3], [3, 0, 0, 0, 0, 0, 0, 3], [3, 0, 0, 0, 0, 0, 0, 3], [3, 3, 3, 3, 3, 3, 3, 3]])
example3_transformed = np.array([[3, 3, 3, 3, 3, 3, 3, 3], [3, 0, 0, 0, 3, 0, 0, 0], [3, 0, 0, 0, 3, 0, 0, 0], [3, 3, 3, 3, 3, 3, 3, 3], [3, 0, 0, 0, 3, 0, 0, 0], [3, 0, 0, 0, 3, 0, 0, 0]])

# Analyze all examples
print(analyze_example(example1_input, example1_expected, example1_transformed))
print(analyze_example(example2_input, example2_expected, example2_transformed))
print(analyze_example(example3_input, example3_expected, example3_transformed))