import numpy as np

def analyze_results(examples):
    results = []
    for i, example in enumerate(examples):
        input_grid = np.array(example['input'])
        expected_output = np.array(example['output'])
        
        # get the dimensions
        rows, cols = input_grid.shape

        
        # Check for main diagonal (top-left to bottom-right)
        main_diag_match = True
        for r in range(rows):
            for c in range(cols):
                if r == c:
                    if expected_output[r,c] != 5:
                        main_diag_match = False
                        break
            if not main_diag_match:
                break

        # Check for anti-diagonal (top-right to bottom-left)
        anti_diag_match = True
        for r in range(rows):
            for c in range(cols):
                if r + c == cols -1:
                    if expected_output[r,c] != 5:
                        anti_diag_match = False
                        break
            if not anti_diag_match:
                break

        # Check fill color
        unique_values = np.unique(expected_output)
        fill_color = None
        if len(unique_values) <= 2:
            for color in unique_values:
                if color != 5:
                    fill_color = color
                    break

        results.append({
            'example_number': i + 1,
            'main_diagonal_correct': main_diag_match,
            'anti_diagonal_correct': anti_diag_match,
            'non_diagonal_value': fill_color
            
        })

    return results
examples = [
    {'input': [[2, 2, 2], [3, 2, 3], [3, 3, 3]], 'output': [[5, 0, 0], [0, 5, 0], [0, 0, 5]]},
    {'input': [[3, 3, 3], [4, 2, 2], [4, 4, 2]], 'output': [[0, 0, 5], [0, 5, 0], [5, 0, 0]]},
    {'input': [[4, 4, 4], [4, 4, 4], [4, 4, 4]], 'output': [[5, 5, 5], [0, 0, 0], [0, 0, 0]]},
    {'input': [[3, 3, 3], [3, 3, 3], [3, 3, 3]], 'output': [[5, 5, 5], [0, 0, 0], [0, 0, 0]]},
    {'input': [[4, 4, 4], [4, 4, 4], [3, 3, 3]], 'output': [[5, 0, 0], [0, 5, 0], [0, 0, 5]]}
]
analysis = analyze_results(examples)
print(analysis)