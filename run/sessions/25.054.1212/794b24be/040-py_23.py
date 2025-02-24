import numpy as np

def analyze_examples(examples):
    results = []
    for i, example in enumerate(examples):
        input_grid = np.array(example['input'])
        expected_output = np.array(example['output'])
        transformed_output = np.array(example['transformed_output'])

        # Find blue pixels in the input
        blue_pixels = np.where(input_grid == 1)
        blue_count = len(blue_pixels[0])
        
        #find bounding box around the blue pixels
        if blue_count > 0:
            min_row, min_col = np.min(blue_pixels, axis=1)
            max_row, max_col = np.max(blue_pixels, axis=1)
            bounding_box = ((min_row, min_col), (max_row, max_col))
        else:
            bounding_box = None

        # Find red pixels in expected
        red_pixels_expected = np.where(expected_output == 2)
        red_count_expected = len(red_pixels_expected[0])
        
        red_pixels_transformed = np.where(transformed_output == 2)
        red_count_transformed = len(red_pixels_transformed[0])

        results.append({
            'example_num': i + 1,
            'blue_count': blue_count,
            'bounding_box': bounding_box,
            'red_count_expected': red_count_expected,
            'red_count_transformed' : red_count_transformed,
            'output_shape' : expected_output.shape
        })

    return results

examples = [
    {'input': [[0, 0, 0], [1, 0, 0], [0, 0, 0]], 'output': [[2, 0, 0], [0, 0, 0], [0, 0, 0]], 'transformed_output': [[0, 0, 0], [2, 0, 0], [0, 0, 0]]},
    {'input': [[0, 1, 0], [1, 0, 0], [0, 0, 0]], 'output': [[2, 2, 0], [0, 0, 0], [0, 0, 0]], 'transformed_output': [[0, 2, 0], [2, 0, 0], [0, 0, 0]]},
    {'input': [[0, 0, 1], [0, 0, 0], [1, 0, 0]], 'output': [[2, 2, 0], [0, 0, 0], [0, 0, 0]], 'transformed_output': [[0, 0, 2], [0, 0, 0], [2, 0, 0]]},
    {'input': [[0, 1, 0], [0, 0, 1], [0, 0, 0]], 'output': [[2, 2, 0], [0, 0, 0], [0, 0, 0]], 'transformed_output': [[0, 2, 0], [0, 0, 2], [0, 0, 0]]},
    {'input': [[0, 0, 1], [0, 0, 0], [0, 0, 0]], 'output': [[2, 0, 0], [0, 0, 0], [0, 0, 0]], 'transformed_output': [[0, 0, 2], [0, 0, 0], [0, 0, 0]]},
    {'input': [[1, 1, 0], [0, 0, 0], [1, 0, 0]], 'output': [[2, 2, 2], [0, 0, 0], [0, 0, 0]], 'transformed_output': [[2, 2, 0], [0, 0, 0], [2, 0, 0]]},
    {'input': [[0, 1, 0], [1, 1, 0], [0, 0, 0]], 'output': [[2, 2, 2], [0, 0, 0], [0, 0, 0]], 'transformed_output': [[0, 2, 0], [2, 2, 0], [0, 0, 0]]},
    {'input': [[1, 1, 0], [0, 0, 0], [1, 0, 1]], 'output': [[2, 2, 2], [0, 2, 0], [0, 0, 0]], 'transformed_output': [[2, 2, 0], [0, 0, 0], [2, 0, 2]]},
    {'input': [[0, 1, 0], [1, 1, 0], [1, 0, 0]], 'output': [[2, 2, 2], [0, 2, 0], [0, 0, 0]], 'transformed_output': [[0, 2, 0], [2, 2, 0], [2, 0, 0]]},
    {'input': [[1, 0, 0], [0, 0, 1], [0, 1, 1]], 'output': [[2, 2, 2], [0, 2, 0], [0, 0, 0]], 'transformed_output': [[2, 0, 0], [0, 0, 2], [0, 2, 2]]}
]

analysis_results = analyze_examples(examples)
print(analysis_results)