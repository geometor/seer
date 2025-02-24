import numpy as np

def compare_grids(grid1, grid2):
    """Compares two grids and returns the number of matching and differing pixels."""
    grid1 = np.array(grid1)
    grid2 = np.array(grid2)
    if grid1.shape != grid2.shape:
        return "Different Shapes",0,0
        
    matches = np.sum(grid1 == grid2)
    differences = grid1.size - matches
    return "Same Shape", matches, differences

# Example Data (from the prompt)
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

for i, example in enumerate(examples):
  shape_status, matching_pixels, differing_pixels = compare_grids(example["expected"], example["transformed"])
  print(f"Example {i+1}: Shape Status: {shape_status}, Matching Pixels: {matching_pixels}, Differing Pixels: {differing_pixels}")
