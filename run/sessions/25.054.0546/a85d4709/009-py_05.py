import numpy as np

def analyze_examples(examples):
    results = []
    for i, (input_grid, expected_output) in enumerate(examples):
        input_grid = np.array(input_grid)
        expected_output = np.array(expected_output)

        # Find positions of '5' in the input grid
        gray_positions = np.argwhere(input_grid == 5)

        # Basic metrics
        input_shape = input_grid.shape
        output_shape = expected_output.shape
        unique_input_values = np.unique(input_grid)
        unique_output_values = np.unique(expected_output)
        
        output_values_at_five = []
        if gray_positions.size > 0:
          for pos in gray_positions:
            output_values_at_five.append(expected_output[pos[0],pos[1]])
        else:
          output_values_at_five = None


        result = {
            'example_number': i + 1,
            'input_shape': input_shape,
            'output_shape': output_shape,
            'unique_input_values': unique_input_values.tolist(),
            'unique_output_values': unique_output_values.tolist(),
            'gray_positions': gray_positions.tolist(),
            'output_values_where_input_is_five':output_values_at_five
        }
        results.append(result)
    return results

examples = [
    ([[0, 0, 5], [0, 5, 0], [5, 0, 0]], [[3, 3, 3], [4, 4, 4], [2, 2, 2]]),
    ([[0, 0, 5], [0, 0, 5], [0, 0, 5]], [[3, 3, 3], [3, 3, 3], [3, 3, 3]]),
    ([[5, 0, 0], [0, 5, 0], [5, 0, 0]], [[2, 2, 2], [4, 4, 4], [2, 2, 2]]),
    ([[0, 5, 0], [0, 0, 5], [0, 5, 0]], [[4, 4, 4], [3, 3, 3], [4, 4, 4]]),
]

analysis_results = analyze_examples(examples)

for result in analysis_results:
    print(result)
