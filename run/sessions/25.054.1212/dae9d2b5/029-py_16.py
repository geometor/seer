import numpy as np

def get_grid_string(grid):
    return '\n'.join(' '.join(map(str, row)) for row in grid)
    
def analyze_example(input_grid, expected_output, transformed_output):
    """Analyzes a single example and provides detailed metrics."""

    results = {}
    results["match"] = expected_output == transformed_output
    results["pixels_off"] = sum(1 for a, b in zip(np.array(expected_output).flatten(), np.array(transformed_output).flatten()) if a != b)
    results["size_correct"] = np.array(expected_output).shape == (3,3)
    results["color_palette_correct"] = all(pixel in [0, 6] for row in transformed_output for pixel in row)
    
    expected_counts = {}
    transformed_counts = {}
    for i in range(10):
        expected_counts[i] = sum(row.count(i) for row in expected_output)
        transformed_counts[i] = sum(row.count(i) for row in transformed_output)
    
    results["correct_pixel_counts"] = expected_counts == transformed_counts

    
    print(f"Input:\n{get_grid_string(input_grid)}")
    print(f"Expected Output:\n{get_grid_string(expected_output)}")
    print(f"Transformed Output:\n{get_grid_string(transformed_output)}")
    print(results)
    return results
    

# Example usage with the provided test cases (assuming you have them defined)
test_cases = [
    ([[4, 4, 0, 3, 3, 0], [4, 0, 0, 3, 0, 0], [0, 0, 0, 0, 0, 3]],
     [[6, 6, 0], [6, 0, 0], [0, 0, 6]],
     [[0, 6, 6], [0, 0, 6], [0, 0, 0]]),
    ([[4, 0, 4, 3, 3, 0], [4, 0, 0, 3, 0, 0], [0, 0, 4, 3, 0, 0]],
     [[6, 6, 6], [6, 0, 0], [6, 0, 6]],
     [[0, 6, 6], [0, 0, 0], [6, 0, 6]]),
    ([[0, 0, 4, 0, 3, 0], [0, 4, 4, 3, 0, 3], [4, 4, 0, 0, 0, 3]],
     [[0, 6, 6], [6, 6, 6], [6, 6, 6]],
     [[6, 0, 0], [6, 6, 0], [0, 6, 6]]),
    ([[4, 4, 0, 3, 0, 0], [0, 0, 0, 0, 0, 3], [4, 0, 0, 0, 0, 0]],
     [[6, 6, 0], [0, 0, 6], [6, 0, 0]],
     [[6, 0, 6], [0, 0, 6], [0, 0, 0]]),
    ([[0, 0, 0, 0, 3, 0], [4, 0, 0, 0, 0, 0], [0, 0, 4, 3, 3, 0]],
     [[0, 6, 0], [6, 0, 0], [6, 6, 6]],
     [[0, 6, 0], [0, 0, 0], [6, 0, 0]])
]

for i, (input_grid, expected_output, transformed_output) in enumerate(test_cases):
        print(f"Analyzing Example {i+1}:")
        analyze_example(input_grid, expected_output, transformed_output)
        print("-" * 20)