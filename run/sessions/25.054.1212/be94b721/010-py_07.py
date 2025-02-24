import numpy as np
from typing import List, Dict, Tuple

def find_objects(grid: np.ndarray) -> List[Dict]:
    """
    Identifies contiguous regions of non-zero pixels as objects.

    Args:
        grid: The input grid (2D numpy array).

    Returns:
        A list of dictionaries, where each dictionary represents an object
        and contains its color, pixels, bounding box, and centroid.
    """
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(row, col, color, pixels):
        if (row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1]
                or visited[row, col] or grid[row, col] != color):
            return
        visited[row, col] = True
        pixels.append((row, col))
        dfs(row + 1, col, color, pixels)
        dfs(row - 1, col, color, pixels)
        dfs(row, col + 1, color, pixels)
        dfs(row, col - 1, color, pixels)

    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] != 0 and not visited[row, col]:
                color = grid[row, col]
                pixels = []
                dfs(row, col, color, pixels)
                if pixels:
                    min_row = min(p[0] for p in pixels)
                    max_row = max(p[0] for p in pixels)
                    min_col = min(p[1] for p in pixels)
                    max_col = max(p[1] for p in pixels)
                    bbox = (min_row, min_col, max_row, max_col)
                    centroid = ((min_row + max_row) // 2, (min_col + max_col) // 2)
                    objects.append({
                        'color': color,
                        'pixels': pixels,
                        'bbox': bbox,
                        'centroid': centroid
                    })
    return objects

def get_object_dimensions(pixels: List[Tuple[int, int]]) -> Tuple[int, int]:
    """Calculates the dimensions (width, height) of an object."""
    min_row = min(p[0] for p in pixels)
    max_row = max(p[0] for p in pixels)
    min_col = min(p[1] for p in pixels)
    max_col = max(p[1] for p in pixels)
    return (max_row - min_row + 1, max_col - min_col + 1)

def analyze_example(example):
    input_grid = np.array(example['input'])
    expected_output = np.array(example['output'])

    input_objects = find_objects(input_grid)
    output_objects = find_objects(expected_output) #Analyze the objects in expected output too
    
    input_analysis = []
    for obj in input_objects:
        dims = get_object_dimensions(obj['pixels'])
        input_analysis.append({
            'color': obj['color'],
            'dimensions': dims,
            'bbox': obj['bbox'],
            'centroid': obj['centroid']
        })

    output_analysis = []
    for obj in output_objects:
        dims = get_object_dimensions(obj['pixels'])
        output_analysis.append({
            'color': obj['color'],
            'dimensions': dims,
            'bbox': obj['bbox'],
            'centroid': obj['centroid']
        })


    return {
        'input_objects': input_analysis,
        'output_objects': output_analysis,
        'input_grid_shape': input_grid.shape,
        'output_grid_shape': expected_output.shape
    }


def analyze_all_examples(examples):
    all_results = [analyze_example(ex) for ex in examples]
    return all_results

# Assuming 'example_data' is a list of dictionaries, each with 'input' and 'output'
# example_data = [...]  # Your actual example data would go here
# analysis_results = analyze_all_examples(example_data)
# print(analysis_results)

# Example of further analysis (within the code execution environment):
#for i, result in enumerate(analysis_results):
#    print(f"Example {i+1}:")
#    print(f"  Input objects: {result['input_objects']}")
#    print(f"  Output Objects: {result['output_objects']}")
#    print(f" Input shape: {result['input_grid_shape']}")
#    print(f" Output shape: {result['output_grid_shape']}")