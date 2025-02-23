import numpy as np

def analyze_results(example_inputs, example_outputs, transform_func):
    results = []
    for i, (input_grid, expected_output) in enumerate(zip(example_inputs, example_outputs)):
        transformed_grid = transform_func(input_grid)
        diff_pixels = np.sum(transformed_grid != expected_output)
        
        input_colors = np.unique(input_grid[input_grid != 0])
        output_colors = np.unique(expected_output[expected_output != 0])
        transformed_colors = np.unique(transformed_grid[transformed_grid != 0])

        results.append({
            "example": i + 1,
            "pixels_off": diff_pixels,
            "input_colors": input_colors.tolist(),
            "output_colors": output_colors.tolist(),
            "transformed_colors": transformed_colors.tolist(),
            "input_shape": input_grid.shape,
            "output_shape": expected_output.shape,
            "transformed_shape": transformed_grid.shape,
            "same_size": input_grid.shape == expected_output.shape == transformed_grid.shape,
            "same_colors": np.array_equal(np.sort(input_colors), np.sort(output_colors))

        })
    return results

# Call the analysis function with your existing data.
analysis_results = analyze_results(example_inputs, example_outputs, transform)

# Print the results in a readable format.
for result in analysis_results:
    print(f"Example {result['example']}:")
    print(f"  Pixels Off: {result['pixels_off']}")
    print(f"  Input Colors: {result['input_colors']}")
    print(f"  Output Colors: {result['output_colors']}")
    print(f"  Transformed Colors: {result['transformed_colors']}")
    print(f"  Input Shape: {result['input_shape']}")
    print(f"  Output Shape: {result['output_shape']}")
    print(f"  Transformed Shape: {result['transformed_shape']}")
    print(f"  Same Size: {result['same_size']}")
    print(f"  Same Colors: {result['same_colors']}")

    print("-" * 20)