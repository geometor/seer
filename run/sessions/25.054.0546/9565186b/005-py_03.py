def analyze_example(input_grid, expected_output, transformed_output):
    """Analyzes a single example and returns relevant metrics."""
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)

    match = np.array_equal(expected_output, transformed_output)
    pixels_off = np.sum(expected_output != transformed_output)
    size_correct = input_grid.shape == expected_output.shape
    unique_input_colors = set(input_grid.flatten())
    unique_expected_colors = set(expected_output.flatten())
    unique_transformed_colors = set(transformed_output.flatten())

    # check if colors in transformed are a subset of those in expected
    color_palette_correct = unique_transformed_colors.issubset(unique_expected_colors)

    # count pixels of each color
    input_counts = {color: np.sum(input_grid == color) for color in unique_input_colors}
    expected_counts = {color: np.sum(expected_output == color) for color in unique_expected_colors}
    transformed_counts = {color: np.sum(transformed_output == color) for color in unique_transformed_colors}
    correct_pixel_counts = all([transformed_counts.get(c,0) == expected_counts.get(c,0) for c in unique_expected_colors])
    
    return {
        "match": match,
        "pixels_off": pixels_off,
        "size_correct": size_correct,
        "color_palette_correct": color_palette_correct,
        "correct_pixel_counts": correct_pixel_counts,
        "unique_input_colors": unique_input_colors,
        "unique_expected_colors": unique_expected_colors,
        "unique_transformed_colors": unique_transformed_colors,
        "input_color_counts": input_counts,
        "expected_color_counts": expected_counts,
        "transformed_color_counts": transformed_counts
    }

# Example Data - recreating data structures from prompt
example1_input = [[2, 2, 2], [2, 1, 8], [2, 8, 8]]
example1_expected = [[2, 2, 2], [2, 5, 5], [2, 5, 5]]
example1_transformed = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]

example2_input = [[1, 1, 1], [8, 1, 3], [8, 2, 2]]
example2_expected = [[1, 1, 1], [5, 1, 5], [5, 5, 5]]
example2_transformed = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]

example3_input = [[2, 2, 2], [8, 8, 2], [2, 2, 2]]
example3_expected = [[2, 2, 2], [5, 5, 2], [2, 2, 2]]
example3_transformed = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]

example4_input = [[3, 3, 8], [4, 4, 4], [8, 1, 1]]
example4_expected = [[5, 5, 5], [4, 4, 4], [5, 5, 5]]
example4_transformed = [[5, 5, 5], [4, 4, 4], [5, 5, 5]]

examples = [
   (example1_input, example1_expected, example1_transformed),
   (example2_input, example2_expected, example2_transformed),
   (example3_input, example3_expected, example3_transformed),
   (example4_input, example4_expected, example4_transformed)
]

analysis_results = [analyze_example(*example) for example in examples]

# print in readable format
for i, result in enumerate(analysis_results):
  print (f"Analysis of Example {i+1}")
  for k,v in result.items():
    print (f"  {k}: {v}")