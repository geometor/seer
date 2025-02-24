import numpy as np

def analyze_differences(expected, actual):
    """Analyzes differences between expected and actual grids."""

    if expected.shape != actual.shape:
        return "Shapes differ"

    diff = expected != actual
    col_diffs = np.any(diff, axis=0)
    row_diffs = np.any(diff, axis=1)

    diff_indices = np.where(diff)

    return {
        "differing_columns": np.where(col_diffs)[0].tolist(),
        "differing_rows": np.where(row_diffs)[0].tolist(),
        "first_diff": diff_indices[0][0], diff_indices[1][0]

    }

# Example usage (replace with actual data from previous runs):
examples = [
    {
        "input": np.array([
            [1, 1, 2, 5, 0, 0, 0, 5, 0, 0, 0],
            [4, 1, 1, 5, 0, 0, 0, 5, 0, 0, 0],
            [4, 4, 1, 5, 0, 0, 0, 5, 0, 0, 0]
        ]),
        "expected": np.array([
            [1, 1, 2, 5, 4, 4, 1, 5, 1, 4, 4],
            [4, 1, 1, 5, 4, 1, 1, 5, 1, 1, 4],
            [4, 4, 1, 5, 1, 1, 2, 5, 2, 1, 1]
        ]),
        "actual": np.array([
            [1, 1, 2, 5, 5, 5, 5, 5, 0, 0, 0],
            [4, 1, 1, 5, 5, 5, 5, 5, 0, 0, 0],
            [4, 4, 1, 5, 5, 5, 5, 5, 0, 0, 0]
        ])
    },
     {
        "input": np.array([
            [6, 3, 3, 5, 0, 0, 0, 5, 0, 0, 0],
            [6, 3, 3, 5, 0, 0, 0, 5, 0, 0, 0],
            [6, 3, 2, 5, 0, 0, 0, 5, 0, 0, 0]
        ]),
        "expected": np.array([
            [6, 3, 3, 5, 6, 6, 6, 5, 2, 3, 6],
            [6, 3, 3, 5, 3, 3, 3, 5, 3, 3, 6],
            [6, 3, 2, 5, 2, 3, 3, 5, 3, 3, 6]
        ]),
        "actual": np.array([
            [6, 3, 3, 5, 5, 5, 5, 5, 0, 0, 0],
            [6, 3, 3, 5, 5, 5, 5, 5, 0, 0, 0],
            [6, 3, 2, 5, 5, 5, 5, 5, 0, 0, 0]
        ])
    },
     {
        "input": np.array([
            [2, 7, 8, 5, 0, 0, 0, 5, 0, 0, 0],
            [7, 7, 8, 5, 0, 0, 0, 5, 0, 0, 0],
            [8, 8, 8, 5, 0, 0, 0, 5, 0, 0, 0]
        ]),
        "expected": np.array([
            [2, 7, 8, 5, 8, 7, 2, 5, 8, 8, 8],
            [7, 7, 8, 5, 8, 7, 7, 5, 8, 7, 7],
            [8, 8, 8, 5, 8, 8, 8, 5, 8, 7, 2]
        ]),
        "actual": np.array([
            [2, 7, 8, 5, 5, 5, 5, 5, 0, 0, 0],
            [7, 7, 8, 5, 5, 5, 5, 5, 0, 0, 0],
            [8, 8, 8, 5, 5, 5, 5, 5, 0, 0, 0]
        ])
    }
]

for i, example in enumerate(examples):
    analysis = analyze_differences(example["expected"], example["actual"])
    print(f"Example {i+1}:")
    print(analysis)
    print("-" * 20)