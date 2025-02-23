import numpy as np

def analyze_examples(examples):
    results = []
    for i, example in enumerate(examples):
        input_grid = np.array(example['input'])
        expected_output = np.array(example['output'])

        # get rows per color
        input_rows = {}
        expected_rows = {}
        for color in np.unique(input_grid):
            input_rows[color] = np.all(input_grid == color, axis = 1).sum()
        for color in np.unique(expected_output):
            expected_rows[color] = np.all(expected_output == color, axis=1).sum()
            
        results.append({
            'example': i + 1,
            'input_rows': input_rows,
            'expected_rows': expected_rows
        })
    return results
examples = [
    {
        'input': [[0, 0, 5], [0, 5, 0], [5, 0, 0]],
        'output': [[3, 3, 3], [4, 4, 4], [2, 2, 2]]
    },
    {
        'input': [[0, 0, 5], [0, 0, 5], [0, 0, 5]],
        'output': [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
    },
    {
        'input': [[5, 0, 0], [0, 5, 0], [5, 0, 0]],
        'output': [[2, 2, 2], [4, 4, 4], [2, 2, 2]]
    },
    {
       'input': [[0, 5, 0], [0, 0, 5], [0, 5, 0]],
        'output': [[4, 4, 4], [3, 3, 3], [4, 4, 4]]
    }
]
analysis = analyze_examples(examples)
print(analysis)