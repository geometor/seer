import numpy as np

def compare_grids(grid1, grid2):
    """Compares two grids and returns a detailed report."""
    if grid1.shape != grid2.shape:
        return "Grids have different shapes."

    diff = grid1 != grid2
    num_diff = np.sum(diff)
    diff_indices = np.where(diff)

    report = f"Number of differing pixels: {num_diff}\n"
    report += "Locations (row, col) and values (grid1, grid2):\n"
    for r, c in zip(*diff_indices):
        report += f"  ({r}, {c}): ({grid1[r, c]}, {grid2[r, c]})\n"
    return report

# Example data from the prompt (replace with actual data)
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
        "transformed": np.array([
            [1, 1, 2, 5, 0, 0, 0, 5, 0, 0, 0],
            [4, 1, 1, 5, 0, 0, 0, 5, 0, 0, 0],
            [4, 4, 1, 5, 0, 0, 0, 5, 0, 0, 0]
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
        "transformed": np.array([
            [6, 3, 3, 5, 0, 0, 0, 5, 0, 0, 0],
            [6, 3, 3, 5, 0, 0, 0, 5, 0, 0, 0],
            [6, 3, 2, 5, 0, 0, 0, 5, 0, 0, 0]
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
        "transformed": np.array([
            [2, 7, 8, 5, 0, 0, 0, 5, 0, 0, 0],
            [7, 7, 8, 5, 0, 0, 0, 5, 0, 0, 0],
            [8, 8, 8, 5, 0, 0, 0, 5, 0, 0, 0]
        ])
    }
]

for i, example in enumerate(examples):
    print(f"Example {i+1}:")
    print(compare_grids(example["transformed"], example["expected"]))
    print("-" * 20)