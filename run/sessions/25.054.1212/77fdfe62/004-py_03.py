import numpy as np
from collections import Counter

def analyze_example(example):
    """Analyzes a single example and returns comparison metrics."""
    input_grid = np.array(example["input"])
    expected_grid = np.array(example["expected"])

    shape_status, matches, differences = compare_grids(input_grid, expected_grid)

    input_counts = Counter(input_grid.flatten())
    expected_counts = Counter(expected_grid.flatten())

    return {
        "shape_status": shape_status,
        "matching_pixels": matches,
        "differing_pixels": differences,
        "input_pixel_counts": dict(input_counts),
        "expected_pixel_counts": dict(expected_counts),
    }

def compare_grids(grid1, grid2):
    """Compares two grids and returns the number of matching and differing pixels."""
    if grid1.shape != grid2.shape:
        return "Different Shapes",0,0
        
    matches = np.sum(grid1 == grid2)
    differences = grid1.size - matches
    return "Same Shape", matches, differences


examples = [
    {
        "input": [
            [2, 1, 0, 0, 0, 0, 1, 3],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 0, 8, 0, 0, 1, 0],
            [0, 1, 8, 8, 0, 8, 1, 0],
            [0, 1, 0, 0, 8, 0, 1, 0],
            [0, 1, 8, 0, 8, 8, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [4, 1, 0, 0, 0, 0, 1, 6],
        ],
        "expected": [[0, 2, 0, 0], [2, 2, 0, 3], [0, 0, 6, 0], [4, 0, 6, 6]],
        "transformed": [[2, 2, 0, 3], [2, 2, 0, 0], [0, 0, 6, 6], [4, 0, 6, 6]],
    },
    {
        "input": [
            [9, 1, 0, 0, 1, 4],
            [1, 1, 1, 1, 1, 1],
            [0, 1, 8, 8, 1, 0],
            [0, 1, 8, 0, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [2, 1, 0, 0, 1, 3],
        ],
        "expected": [[9, 4], [2, 0]],
        "transformed": [[9, 9, 0, 4], [9, 9, 0, 0], [0, 0, 3, 3], [2, 0, 3, 3]],
    },
    {
        "input": [
            [6, 1, 0, 0, 0, 0, 1, 2],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 1, 0, 8, 0, 8, 1, 0],
            [0, 1, 8, 8, 8, 0, 1, 0],
            [0, 1, 8, 0, 8, 8, 1, 0],
            [0, 1, 8, 8, 8, 0, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [7, 1, 0, 0, 0, 0, 1, 4],
        ],
        "expected": [[0, 6, 0, 2], [6, 6, 2, 0], [7, 0, 4, 4], [7, 7, 4, 0]],
        "transformed": [[6, 6, 0, 2], [6, 6, 0, 0], [0, 0, 4, 4], [7, 0, 4, 4]],
    },
]

results = [analyze_example(ex) for ex in examples]

for i, result in enumerate(results):
    print(f"Example {i+1}:")
    print(f"  Shape Status: {result['shape_status']}")
    print(f"  Matching Pixels: {result['matching_pixels']}")
    print(f"  Differing Pixels: {result['differing_pixels']}")
    print(f"  Input Pixel Counts: {result['input_pixel_counts']}")
    print(f"  Expected Pixel Counts: {result['expected_pixel_counts']}")
    print("-" * 20)