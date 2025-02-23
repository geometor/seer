import numpy as np

def detail_report(input_grid, expected_grid, transformed_grid):
    input_np = np.array(input_grid)
    expected_np = np.array(expected_grid)
    transformed_np = np.array(transformed_grid)
    
    print("Input Grid:")
    print(input_np)
    print("\nExpected Grid:")
    print(expected_np)
    print("\nTransformed Grid:")
    print(transformed_np)

    print("\nDifferences (Expected - Transformed):")
    diff = expected_np - transformed_np
    print(diff)
    
    print("\nNumber of mismatched pixels:", np.sum(diff != 0))

    
    for row in range(expected_np.shape[0]):
      print(f'row {row}: expected {expected_np[row,:]}  transformed {transformed_np[row,:]}')

examples = [
    {
        "input": [[2, 2, 1], [1, 5, 1], [5, 2, 2]],
        "expected": [[2, 1, 5], [2, 5, 2], [1, 1, 2]],
        "transformed": [[5, 1, 2], [2, 5, 2], [2, 1, 1]]
    },
    {
        "input": [[2, 2, 5], [6, 2, 2], [5, 5, 5]],
        "expected": [[2, 6, 5], [2, 2, 5], [5, 2, 5]],
        "transformed": [[5, 6, 2], [5, 2, 2], [5, 2, 5]]
    },
    {
        "input": [[9, 9, 5], [5, 5, 8], [5, 8, 9]],
        "expected": [[9, 5, 5], [9, 5, 8], [5, 8, 9]],
        "transformed": [[5, 5, 9], [8, 5, 9], [9, 8, 5]]
    },
    {
        "input": [[2, 6, 6], [2, 1, 1], [2, 6, 2]],
        "expected": [[2, 2, 2], [6, 1, 6], [6, 1, 2]],
        "transformed": [[2, 2, 2], [6, 1, 6], [2, 1, 6]]
    }
]

for i, example in enumerate(examples):
    print(f"\n--- Example {i+1} ---")
    detail_report(example["input"], example["expected"], example["transformed"])
