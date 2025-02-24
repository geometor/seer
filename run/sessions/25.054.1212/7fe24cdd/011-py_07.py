import numpy as np

# Example 1
input_grid1 = np.array([[8, 5, 0], [8, 5, 3], [0, 3, 2]])
expected_output1 = np.array([[8, 5, 0, 0, 8, 8], [8, 5, 3, 3, 5, 5], [0, 3, 2, 2, 3, 0], [0, 3, 2, 2, 3, 0], [5, 5, 3, 3, 5, 8], [8, 8, 0, 0, 5, 8]])
transformed_output1 = transform(input_grid1)
pixels_off1 = np.sum(expected_output1 != transformed_output1)
print(f"Example 1 Pixels Off: {pixels_off1}")

# Example 2
input_grid2 = np.array([[3, 8, 2], [3, 2, 2], [8, 5, 2]])
expected_output2 = np.array([[3, 8, 2, 2, 8, 3], [3, 2, 2, 2, 2, 3], [8, 5, 2, 2, 5, 8], [8, 5, 2, 2, 5, 8], [3, 2, 2, 2, 2, 3], [3, 8, 2, 2, 8, 3]])
transformed_output2 = transform(input_grid2)
pixels_off2 = np.sum(expected_output2 != transformed_output2)
print(f"Example 2 Pixels Off: {pixels_off2}")

# Example 3
input_grid3 = np.array([[0, 3, 0], [6, 6, 6], [0, 3, 0]])
expected_output3 = np.array([[0, 3, 0, 0, 3, 0], [6, 6, 6, 6, 6, 6], [0, 3, 0, 0, 3, 0], [0, 3, 0, 0, 3, 0], [6, 6, 6, 6, 6, 6], [0, 3, 0, 0, 3, 0]])
transformed_output3 = transform(input_grid3)
pixels_off3 = np.sum(expected_output3 != transformed_output3)
print(f"Example 3 Pixels Off: {pixels_off3}")
