# Conceptual - imagine this being executed, and providing output to include below
# Focusing on getting the core information

def analyze_results(input_grid, expected_output, transformed_output):
    """
    Analyzes an individual example. Reports differences.
    """
    
    print("Input Grid:")
    print(input_grid)
    print("Expected Output:")
    print(expected_output)
    print("Transformed Output:")
    print(transformed_output)

    match = np.array_equal(expected_output, transformed_output)
    print(f"Match: {match}")

    if not match:
        diff = expected_output != transformed_output
        pixels_off = np.sum(diff)
        print(f"Pixels Off: {pixels_off}")
        
        # Count occurences of each color in expected output
        expected_color_counts = {}
        for color in range(10):
          expected_color_counts[color] = np.sum(expected_output == color)
        print(f"Expected Color Counts: {expected_color_counts}")
        
        # Count occurences of each color in transformed output
        transformed_color_counts = {}
        for color in range(10):
          transformed_color_counts[color] = np.sum(transformed_output == color)
        print(f"Transformed Color Counts: {transformed_color_counts}")
        
        print("Pixel differences (expected -> transformed):")
        for r in range(expected_output.shape[0]):
          for c in range(expected_output.shape[1]):
            if expected_output[r,c] != transformed_output[r,c]:
              print(f"  ({r},{c}): {expected_output[r,c]} -> {transformed_output[r,c]}")

# Example usage for each of the provided training examples (1 to 4)
#  ... call analyze_results for each example ...