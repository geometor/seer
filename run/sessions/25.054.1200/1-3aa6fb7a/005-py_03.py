import numpy as np

def analyze_example(input_grid, expected_output, transformed_output):
    input_azure_pixels = np.argwhere(input_grid == 8)
    input_blue_pixels = np.argwhere(input_grid == 1)
    expected_blue_pixels = np.argwhere(expected_output == 1)
    transformed_blue_pixels = np.argwhere(transformed_output == 1)
    diff_grid = (expected_output != transformed_output).astype(int)
    diff_pixels = np.argwhere(diff_grid)
    
    analysis = {
        "input_shape": input_grid.shape,
        "input_azure_count": len(input_azure_pixels),
        "input_blue_count": len(input_blue_pixels),
        "expected_blue_count": len(expected_blue_pixels),
        "transformed_blue_count": len(transformed_blue_pixels),
        "diff_pixel_count": len(diff_pixels),
        "diff_pixels": diff_pixels.tolist(),
    }
    return analysis

# Example data - replace with actual data loading
input_grids = [
    np.array([[0, 0, 0, 0, 0, 0, 0],
              [0, 8, 0, 0, 0, 0, 0],
              [0, 8, 8, 0, 0, 0, 0],
              [0, 0, 0, 0, 8, 8, 0],
              [0, 0, 0, 0, 0, 8, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0]]),
    np.array([[0, 0, 0, 0, 8, 8, 0],
              [0, 0, 0, 0, 0, 8, 0],
              [0, 0, 8, 0, 0, 0, 0],
              [0, 0, 8, 8, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 8, 0, 0],
              [0, 0, 0, 8, 8, 0, 0]])
]
expected_outputs = [
    np.array([[0, 0, 0, 0, 0, 0, 0],
              [0, 8, 1, 0, 0, 0, 0],
              [0, 8, 8, 0, 0, 0, 0],
              [0, 0, 0, 0, 8, 8, 0],
              [0, 0, 0, 0, 1, 8, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0]]),
    np.array([[0, 0, 0, 0, 8, 8, 0],
              [0, 0, 0, 0, 1, 8, 0],
              [0, 0, 8, 1, 0, 0, 0],
              [0, 0, 8, 8, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 8, 0, 0],
              [0, 0, 0, 8, 8, 0, 0]])
]
transformed_outputs = [
   np.array([[0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0],
              [0, 8, 8, 0, 0, 0, 0],
              [0, 0, 0, 0, 8, 8, 0],
              [0, 0, 0, 0, 0, 8, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0]]),
    np.array([[0, 0, 0, 0, 1, 8, 0],
              [0, 0, 0, 0, 0, 8, 0],
              [0, 0, 8, 0, 0, 0, 0],
              [0, 0, 8, 8, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 8, 0, 0],
              [0, 0, 0, 8, 8, 0, 0]])
]

for i in range(len(input_grids)):
    analysis = analyze_example(input_grids[i], expected_outputs[i], transformed_outputs[i])
    print(f"Analysis for Example {i+1}:")
    for key, value in analysis.items():
        print(f"  {key}: {value}")