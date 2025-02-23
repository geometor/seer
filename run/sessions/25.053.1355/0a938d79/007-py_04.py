# Hypothetical code execution - This would be done externally
results = []
for i, (input_grid, expected_output) in enumerate(zip(train_inputs, train_outputs)):
    transformed_output = transform(input_grid)
    match = np.array_equal(transformed_output, expected_output)
    pixels_off = np.sum(transformed_output != expected_output)
    size_correct = transformed_output.shape == expected_output.shape
    
    # Count matching pixels for each color
    unique_colors = np.unique(np.concatenate((expected_output, transformed_output)))
    correct_pixel_counts = {}
    for color in unique_colors:
        correct_pixel_counts[color] = np.sum((transformed_output == expected_output) & (expected_output == color))

    results.append({
        "example": i + 1,
        "match": match,
        "pixels_off": pixels_off,
        "size_correct": size_correct,
        "correct_pixel_counts": correct_pixel_counts
    })

for result in results:
    print(result)