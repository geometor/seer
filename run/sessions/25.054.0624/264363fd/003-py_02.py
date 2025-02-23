import numpy as np

def calculate_metrics(input_grid, expected_output, transformed_output):
    if transformed_output is None:
        return {
            'match': "ERROR",
            'pixels_off': None,
            'size_correct': None,
            'color_palette_correct': None,
            'correct_pixel_counts': None,
        }
    match = np.array_equal(expected_output, transformed_output)
    pixels_off = None if match else np.sum(expected_output != transformed_output)
    size_correct = expected_output.shape == transformed_output.shape
    
    expected_colors = set(np.unique(expected_output))
    transformed_colors = set(np.unique(transformed_output))
    color_palette_correct = expected_colors == transformed_colors

    expected_counts = {color: np.sum(expected_output == color) for color in expected_colors}
    transformed_counts = {color: np.sum(transformed_output == color) for color in transformed_colors}
    correct_pixel_counts = expected_counts == transformed_counts
    
    return {
        'match': match,
        'pixels_off': pixels_off,
        'size_correct': size_correct,
        'color_palette_correct': color_palette_correct,
        'correct_pixel_counts': correct_pixel_counts,
    }
#dummy data
input_grid = np.zeros((3,3))
expected_output = np.zeros((3,3))
transformed_output = np.zeros((3,3))
metrics = calculate_metrics(input_grid, expected_output, transformed_output)
print (metrics)
