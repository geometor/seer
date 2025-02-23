import numpy as np

input_grid = np.array([
    [0, 0, 0, 1, 0],
    [0, 3, 0, 0, 0],
    [0, 3, 0, 1, 2],
    [6, 0, 0, 0, 0],
    [0, 3, 0, 0, 0]
])

output_grid = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0],
    [0, 3, 0, 1, 0],
    [6, 3, 0, 1, 2]
])

input_objects = []
output_objects = []

for i in range(input_grid.shape[0]):
    for j in range(input_grid.shape[1]):
        if input_grid[i, j] != 0:
            input_objects.append({
                "value": input_grid[i, j],
                "row": i,
                "col": j
            })
        if output_grid[i,j] != 0:
            output_objects.append({
                "value": output_grid[i, j],
                "row": i,
                "col": j
            })


print("Input Objects:")
print(input_objects)
print("Output Objects:")
print(output_objects)
