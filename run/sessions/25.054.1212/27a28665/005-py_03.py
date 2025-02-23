import numpy as np

def analyze_examples(examples):
    results = []
    for i, example in enumerate(examples):
        input_grid = np.array(example['input'])
        output_grid = np.array(example['output'])
        transformed_grid = transform(example['input']) #using previous transform function.

        # Basic Metrics
        input_non_zero = np.count_nonzero(input_grid)
        output_value = output_grid[0, 0]
        transformed_value = transformed_grid[0, 0]
        distinct_colors = len(np.unique(input_grid[input_grid != 0]))
        match = np.array_equal(output_grid, transformed_grid)

        # Color repetition count
        repetition_count = 0
        colors = np.unique(input_grid[input_grid != 0])
        for color in colors:
            color_count = np.count_nonzero(input_grid == color)
            if color_count > 1:
              repetition_count += color_count
        
        # Main Diagonal
        main_diag = np.diag(input_grid)
        main_diag_count = np.count_nonzero(main_diag)
        main_diag_unique = len(np.unique(main_diag[main_diag != 0]))

        # Anti-Diagonal
        anti_diag = np.diag(np.fliplr(input_grid))
        anti_diag_count = np.count_nonzero(anti_diag)
        anti_diag_unique = len(np.unique(anti_diag[anti_diag != 0]))

        results.append({
            'example': i + 1,
            'input_non_zero': input_non_zero,
            'output_value': output_value,
            'transformed_value': transformed_value,
            'distinct_colors': distinct_colors,
            'repetition_count': repetition_count,
            'main_diag_count': main_diag_count,
            'main_diag_unique': main_diag_unique,
            'anti_diag_count': anti_diag_count,
            'anti_diag_unique': anti_diag_unique,            
            'match': match
        })
    return results

examples = [
    {'input': [[5, 5, 0], [5, 0, 5], [0, 5, 0]], 'output': [[1]]},
    {'input': [[8, 0, 8], [0, 8, 0], [8, 0, 8]], 'output': [[2]]},
    {'input': [[5, 0, 5], [0, 5, 0], [5, 0, 5]], 'output': [[2]]},
    {'input': [[0, 1, 1], [0, 1, 1], [1, 0, 0]], 'output': [[3]]},
    {'input': [[0, 8, 8], [0, 8, 8], [8, 0, 0]], 'output': [[3]]},
    {'input': [[4, 4, 0], [4, 0, 4], [0, 4, 0]], 'output': [[1]]},
    {'input': [[0, 5, 0], [5, 5, 5], [0, 5, 0]], 'output': [[6]]}
]

analysis = analyze_examples(examples)

for result in analysis:
    print(result)