def analyze_results(examples):
    results = []
    for i, example in enumerate(examples):
        input_grid = example['input']
        expected_output = example['output']
        transformed_output = transform(np.array(input_grid))

        #pixel diff
        diff = np.array(expected_output) - transformed_output
        pixels_off = np.count_nonzero(diff)

        #Size correct
        size_correct = diff.shape == (0,0)

        #Correct color palette
        output_colors = set(np.unique(expected_output))
        transform_colors = set(np.unique(transformed_output))
        color_palette_correct = output_colors.issubset(transform_colors)


        #Correct Pixel Count
        from collections import Counter
        expected_counts = Counter(np.array(expected_output).flatten())
        transformed_counts = Counter(transformed_output.flatten())
        correct_pixel_counts = expected_counts == transformed_counts

        results.append({
            'example_number': i + 1,
            'pixels_off': pixels_off,
            'size_correct': size_correct,
            'color_palette_correct':color_palette_correct,
            'correct_pixel_counts':correct_pixel_counts
        })
    return results

examples = [
    {
        'input': [[0, 0, 6], [0, 4, 0], [3, 0, 0]],
        'output': [[0, 0, 6], [0, 4, 6], [3, 4, 6]]
    },
    {
        'input': [[0, 2, 0], [7, 0, 8], [0, 0, 0]],
        'output': [[0, 2, 0], [7, 2, 8], [7, 2, 8]]
    },
    {
        'input': [[4, 0, 0], [0, 2, 0], [0, 0, 0]],
        'output': [[4, 0, 0], [4, 2, 0], [4, 2, 0]]
    }
]

analysis = analyze_results(examples)
print(analysis)