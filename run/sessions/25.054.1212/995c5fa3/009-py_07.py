import numpy as np

def analyze_grid(grid, grid_id):
    """Analyzes an input grid and returns a dictionary of properties."""
    analysis = {
        "grid_id": grid_id,
        "rows": len(grid),
        "cols": len(grid[0]) if len(grid) > 0 else 0,
        "color_counts": {},
        "row_patterns": {},
    }

    for color in range(10):
      analysis["color_counts"][color] = np.sum(grid == color)

    for i, row in enumerate(grid):
        analysis["row_patterns"][i] = tuple(row)


    return analysis

# Example data (replace with actual data from the prompt)
examples = [
    {
        "input": np.array([
            [5, 5, 5, 5, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5],
            [5, 5, 5, 5, 0, 5, 0, 0, 5, 0, 0, 5, 5, 0],
            [5, 5, 5, 5, 0, 5, 0, 0, 5, 0, 0, 5, 5, 0],
            [5, 5, 5, 5, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5],
        ]),
        "output": np.array([
            [2, 2, 2],
            [8, 8, 8],
            [3, 3, 3],
        ]),
      "id": "example_1"
    },
    {
        "input": np.array([
            [5, 5, 5, 5, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5],
            [0, 5, 5, 0, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5],
            [0, 5, 5, 0, 0, 5, 0, 0, 5, 0, 5, 5, 5, 5],
            [5, 5, 5, 5, 0, 5, 0, 0, 5, 0, 5, 5, 5, 5],
        ]),
        "output": np.array([
            [3, 3, 3],
            [4, 4, 4],
            [2, 2, 2],
        ]),
      "id": "example_2"

    },
  {
        "input": np.array([
            [5, 5, 5, 5, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5],
            [5, 0, 0, 5, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5],
            [5, 0, 0, 5, 0, 5, 5, 5, 5, 0, 5, 0, 0, 5],
            [5, 5, 5, 5, 0, 5, 5, 5, 5, 0, 5, 0, 0, 5],
        ]),
        "output": np.array([
            [8, 8, 8],
            [2, 2, 2],
            [4, 4, 4],
        ]),
      "id": "example_3"

    },
      {
        "input": np.array([
            [5, 5, 5, 5, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5],
            [5, 5, 5, 5, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5],
            [5, 5, 5, 5, 0, 5, 0, 0, 5, 0, 5, 5, 5, 5],
            [5, 5, 5, 5, 0, 5, 0, 0, 5, 0, 5, 5, 5, 5],
        ]),
        "output": np.array([
            [2, 2, 2],
            [4, 4, 4],
            [2, 2, 2],
        ]),
      "id": "example_4"

    },
]

# Analyze each example
analysis_results = [analyze_grid(ex["input"], ex["id"]) for ex in examples]

# Print the analysis for each example
for result in analysis_results:
    print(result)
