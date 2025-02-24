import numpy as np

def analyze_results(input_grids, expected_outputs, transformed_outputs):
    """Analyzes the results of the transformation.

    Args:
        input_grids: List of input grids.
        expected_outputs: List of expected output grids.
        transformed_outputs: List of transformed output grids.

    Returns:
        A dictionary containing analysis results.
    """

    analysis = {}
    for i in range(len(input_grids)):
        input_grid = input_grids[i]
        expected_output = expected_outputs[i]
        transformed_output = transformed_outputs[i]

        # Find indices of blue pixels in input
        blue_pixels = np.where(input_grid == 1)
        blue_x_coords = blue_pixels[1]
        last_blue_x = blue_x_coords[-1] if blue_x_coords.size > 0 else -1

        example_key = f"example_{i+1}"
        analysis[example_key] = {
            "match": np.array_equal(expected_output, transformed_output),
            "pixels_off": np.sum(expected_output != transformed_output),
            "last_blue_x": last_blue_x,
            "expected_output_row2_x": np.where(expected_output[1,:] == 2)[0].tolist() # find the x coordinates that are red in the second row
        }
    return analysis

# Recreate the inputs and outputs. You'd typically load these.
input_grids = [
    np.array([[0, 0, 0], [1, 0, 0], [0, 0, 0]]),
    np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
    np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
    np.array([[0, 1, 0], [0, 0, 1], [0, 0, 0]]),
    np.array([[0, 0, 1], [0, 0, 0], [0, 0, 0]]),
    np.array([[1, 1, 0], [0, 0, 0], [1, 0, 0]]),
    np.array([[0, 1, 0], [1, 1, 0], [0, 0, 0]]),
    np.array([[1, 1, 0], [0, 0, 0], [1, 0, 1]]),
    np.array([[0, 1, 0], [1, 1, 0], [1, 0, 0]]),
    np.array([[1, 0, 0], [0, 0, 1], [0, 1, 1]]),
]

expected_outputs = [
    np.array([[2, 0, 0], [0, 0, 0], [0, 0, 0]]),
    np.array([[2, 2, 0], [0, 0, 0], [0, 0, 0]]),
    np.array([[2, 2, 0], [0, 0, 0], [0, 0, 0]]),
    np.array([[2, 2, 0], [0, 0, 0], [0, 0, 0]]),
    np.array([[2, 0, 0], [0, 0, 0], [0, 0, 0]]),
    np.array([[2, 2, 2], [0, 0, 0], [0, 0, 0]]),
    np.array([[2, 2, 2], [0, 0, 0], [0, 0, 0]]),
    np.array([[2, 2, 2], [0, 2, 0], [0, 0, 0]]),
    np.array([[2, 2, 2], [0, 2, 0], [0, 0, 0]]),
    np.array([[2, 2, 2], [0, 2, 0], [0, 0, 0]]),
]

transformed_outputs = [
    np.array([[2, 0, 0], [0, 0, 0], [0, 0, 0]]),
    np.array([[2, 2, 0], [0, 0, 0], [0, 0, 0]]),
    np.array([[2, 2, 0], [0, 0, 0], [0, 0, 0]]),
    np.array([[2, 2, 0], [0, 0, 0], [0, 0, 0]]),
    np.array([[2, 0, 0], [0, 0, 0], [0, 0, 0]]),
    np.array([[2, 2, 2], [0, 0, 0], [0, 0, 0]]),
    np.array([[2, 2, 2], [0, 0, 0], [0, 0, 0]]),
    np.array([[2, 2, 2], [0, 0, 0], [0, 0, 0]]),
    np.array([[2, 2, 2], [0, 0, 0], [0, 0, 0]]),
    np.array([[2, 2, 2], [0, 0, 0], [0, 0, 0]]),
]

analysis = analyze_results(input_grids, expected_outputs, transformed_outputs)
print(analysis)
