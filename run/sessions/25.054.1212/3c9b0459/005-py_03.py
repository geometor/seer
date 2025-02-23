import numpy as np

def transpose(grid):
  """Transposes a 2D grid represented as a list of lists."""
  return np.array(grid).T.tolist()

# Example 1
input1 = [[2, 2, 1], [2, 1, 2], [2, 8, 1]]
expected1 = [[1, 8, 2], [2, 1, 2], [1, 2, 2]]
transposed1 = transpose(input1)
print(f"Example 1 Transposed:\n{transposed1}")
match1 = transposed1 == expected1
print(f"Example 1 Match: {match1}")

# Example 2
input2 = [[9, 2, 4], [2, 4, 4], [2, 9, 2]]
expected2 = [[2, 9, 2], [4, 4, 2], [4, 2, 9]]
transposed2 = transpose(input2)
print(f"Example 2 Transposed:\n{transposed2}")
match2 = transposed2 == expected2
print(f"Example 2 Match: {match2}")

# Example 3
input3 = [[8, 8, 8], [5, 5, 8], [8, 5, 5]]
expected3 = [[5, 5, 8], [8, 5, 5], [8, 8, 8]]
transposed3 = transpose(input3)
print(f"Example 3 Transposed:\n{transposed3}")
match3 = transposed3 == expected3
print(f"Example 3 Match: {match3}")

# Example 4
input4 = [[3, 2, 9], [9, 9, 9], [2, 3, 3]]
expected4 = [[3, 3, 2], [9, 9, 9], [9, 2, 3]]
transposed4 = transpose(input4)
print(f"Example 4 Transposed:\n{transposed4}")
match4 = transposed4 == expected4
print(f"Example 4 Match: {match4}")
