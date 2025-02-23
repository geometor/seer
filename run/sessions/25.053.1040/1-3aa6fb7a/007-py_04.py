import numpy as np

# Example 1
input1 = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 0, 0, 0],
    [0, 8, 8, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
])
expected1 = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 8, 1, 0, 0, 0, 0],
    [0, 8, 8, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 1, 8, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
])
transformed1 = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 0, 0, 0],
    [0, 8, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
])

# Example 2
input2 = np.array([
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 0, 8, 0],
    [0, 0, 8, 0, 0, 0, 0],
    [0, 0, 8, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 8, 8, 0, 0]
])
expected2 = np.array([
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 1, 8, 0],
    [0, 0, 8, 1, 0, 0, 0],
    [0, 0, 8, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 8, 0, 0],
    [0, 0, 0, 8, 8, 0, 0]
])
transformed2 = np.array([
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 8, 0, 0, 0, 0],
    [0, 0, 8, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 8, 8, 0, 0]
])

def compare_grids(grid1, grid2):
  """Compares two grids and returns a detailed report."""
  if grid1.shape != grid2.shape:
    return "Shapes are different"

  diff = grid1 != grid2
  num_diff = np.sum(diff)
  diff_indices = np.where(diff)
  diff_values1 = grid1[diff_indices]
  diff_values2 = grid2[diff_indices]

  report = {
      "num_differences": int(num_diff),
      "differences": []
  }
  for i in range(num_diff):
    report["differences"].append({
        "location": (int(diff_indices[0][i]), int(diff_indices[1][i])),
        "value_in_grid1": int(diff_values1[i]),
        "value_in_grid2": int(diff_values2[i])
    })

  return report

report1 = compare_grids(expected1, transformed1)
report2 = compare_grids(expected2, transformed2)

print("Comparison Report for Example 1:")
print(report1)
print("\nComparison Report for Example 2:")
print(report2)