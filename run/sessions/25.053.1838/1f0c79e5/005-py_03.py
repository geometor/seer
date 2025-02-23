import numpy as np
from typing import Tuple

def analyze_example(input_grid: np.ndarray, expected_output: np.ndarray, transformed_output: np.ndarray) -> dict:
    """Analyzes a single example and returns relevant metrics."""

    def get_object_details(grid: np.ndarray) -> Tuple[np.ndarray, Tuple[int, int], int, int]:
        """Extracts object details (mask, top-left, width, height) from a grid."""
        non_zero_pixels = np.argwhere(grid != 0)
        if len(non_zero_pixels) == 0:
            return np.array([]), (-1, -1), 0, 0
        min_row, min_col = non_zero_pixels.min(axis=0)
        max_row, max_col = non_zero_pixels.max(axis=0)
        obj = grid[min_row:max_row+1, min_col:max_col+1]
        return obj, (min_row, min_col), obj.shape[1], obj.shape[0]

    input_obj, input_top_left, input_width, input_height = get_object_details(input_grid)
    expected_obj, expected_top_left, expected_width, expected_height = get_object_details(expected_output)
    _, _, transformed_width, transformed_height = get_object_details(transformed_output)


    analysis = {
        "input_object_present": input_obj.size > 0,
        "input_object_top_left": input_top_left,
        "input_object_width": input_width,
        "input_object_height": input_height,
        "input_object_area": np.sum(input_grid != 0),
        "expected_output_width": expected_width,
        "expected_output_height": expected_height,
        "expected_output_area": np.sum(expected_output != 0),
        "transformed_output_width": transformed_width,
        "transformed_output_height": transformed_height,
        "transformed_output_area": np.sum(transformed_output != 0),
        "match": np.array_equal(expected_output, transformed_output),
        "pixels_off": np.sum(expected_output != transformed_output),
        "size_correct": (expected_width, expected_height) == (transformed_width, transformed_height),

        "input_color_counts":  {str(color): int(count) for color, count in zip(*np.unique(input_grid, return_counts=True))},
        "expected_color_counts": {str(color): int(count) for color, count in zip(*np.unique(expected_output, return_counts=True))},
        "transformed_color_counts": {str(color): int(count) for color, count in zip(*np.unique(transformed_output, return_counts=True))},
    }

    analysis["color_palette_correct"] = (
        set(analysis["expected_color_counts"].keys()) - {"0"} ==  # Exclude background color '0'
        set(analysis["transformed_color_counts"].keys()) - {"0"}
    )
    analysis["correct_pixel_counts"] = analysis["expected_color_counts"] == analysis["transformed_color_counts"]
    return analysis


# Example data (replace with your actual data)
input_grids = [
    np.array([[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,4,2,0,0,0,0,0],[0,0,4,4,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]),
    np.array([[0,0,0,0,0,0,0,0,0],[0,0,3,3,0,0,0,0,0],[0,0,3,2,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]),
    np.array([[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,6,2,0,0,0,0],[0,0,0,2,6,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]),
    np.array([[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,2,2,0,0,0,0],[0,0,0,2,7,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]])
]

expected_outputs = [
    np.array([[0,0,0,0,0,0,4,4,4],[0,0,0,0,0,4,4,4,0],[0,0,0,0,4,4,4,0,0],[0,0,0,4,4,4,0,0,0],[0,0,4,4,4,0,0,0,0],[0,0,4,4,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]),
    np.array([[0,0,0,0,0,0,0,0,0],[0,0,3,3,0,0,0,0,0],[0,0,3,3,3,0,0,0,0],[0,0,0,3,3,3,0,0,0],[0,0,0,0,3,3,3,0,0],[0,0,0,0,0,3,3,3,0],[0,0,0,0,0,0,3,3,3],[0,0,0,0,0,0,0,3,3],[0,0,0,0,0,0,0,0,3]]),
    np.array([[0,0,0,0,0,0,6,6,6],[0,0,0,0,0,6,6,6,0],[0,0,0,0,6,6,6,0,0],[0,0,0,6,6,6,0,0,0],[0,0,6,6,6,0,0,0,0],[0,6,6,6,0,0,0,0,0],[6,6,6,0,0,0,0,0,0],[6,6,0,0,0,0,0,0,0],[6,0,0,0,0,0,0,0,0]]),
    np.array([[7,7,0,0,0,0,7,7,7],[7,7,7,0,0,7,7,7,0],[0,7,7,7,7,7,7,0,0],[0,0,7,7,7,7,0,0,0],[0,0,7,7,7,0,0,0,0],[0,7,7,7,0,0,0,0,0],[7,7,7,0,0,0,0,0,0],[7,7,0,0,0,0,0,0,0],[7,0,0,0,0,0,0,0,0]])
]

transformed_outputs = [
    np.array([[4,2,4,4,0,0,0,0,0],[4,4,4,2,0,0,0,0,0],[4,4,4,4,0,0,0,0,0],[4,2,4,2,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]),
    np.array([[3,3,3,3,0,0,0,0,0],[3,2,2,3,0,0,0,0,0],[3,3,3,3,0,0,0,0,0],[2,3,2,3,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]),
    np.array([[6,2,2,6,0,0,0,0,0],[2,6,6,2,0,0,0,0,0],[2,6,2,6,0,0,0,0,0],[6,2,6,2,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]),
    np.array([[2,2,2,2,0,0,0,0,0],[2,7,7,2,0,0,0,0,0],[2,2,2,2,0,0,0,0,0],[7,2,7,2,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]])
]

for i in range(len(input_grids)):
    analysis = analyze_example(input_grids[i], expected_outputs[i], transformed_outputs[i])
    print(f"Example {i+1}:")
    for key, value in analysis.items():
        print(f"  {key}: {value}")