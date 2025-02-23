import numpy as np

def analyze_example(input_grid, expected_output):
    """Analyzes a single example and returns relevant metrics."""
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)

    # Find the most frequent non-black color
    unique_colors, counts = np.unique(input_grid, return_counts=True)
    color_counts = dict(zip(unique_colors, counts))
    
    # Remove black (0) from consideration
    if 0 in color_counts:
        del color_counts[0]

    predominant_color = max(color_counts, key=color_counts.get, default=0)
    predominant_count = color_counts.get(predominant_color, 0)

    expected_color = None
    expected_count = 0
    
    if expected_output.size > 0:
          expected_color = expected_output.flatten()[0]
          expected_count = expected_output.size
    
    return {
        'input_shape': input_grid.shape,
        'expected_shape': expected_output.shape,
        'predominant_color_input': predominant_color,
        'predominant_color_count': predominant_count,
        'expected_color': expected_color,
        'expected_count': expected_count
    }

# Example data (from the prompt)
examples = [
    ([[0, 0, 0], [1, 0, 0], [0, 1, 0]], [[1, 1]]),
    ([[0, 2, 0], [2, 0, 0], [0, 2, 0]], [[2, 2, 2]]),
    ([[0, 7, 0], [0, 0, 0], [0, 0, 0]], [[7]]),
    ([[0, 8, 0], [8, 8, 0], [8, 0, 0]], [[8, 8, 8, 8]]),
]

# Analyze each example
for i, (input_grid, expected_output) in enumerate(examples):
    analysis = analyze_example(input_grid, expected_output)
    print(f"Example {i+1}:")
    for key, value in analysis.items():
        print(f"  {key}: {value}")