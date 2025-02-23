"""
The transformation rule is: Find the cell immediately to the left of the top-left corner cell of each azure object. Change the color of that cell to blue (color 1).
"""

import numpy as np

def transform(input_grid):
    input_grid = np.array(input_grid)
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape
    processed = set()

    # Iterate through the grid to find azure objects
    for i in range(rows):
        for j in range(cols):
            if input_grid[i, j] == 8 and (i,j) not in processed:
                #find top-left
                top_i, top_j = i,j
                
                q = [(top_i, top_j)]
                visited = set()
                visited.add((top_i, top_j))
                
                while len(q)>0:
                  cur_i, cur_j = q.pop()
                  processed.add((cur_i,cur_j))

                  if cur_i<top_i or (cur_i==top_i and cur_j < top_j):
                      top_i, top_j = cur_i, cur_j
                      
                  neighbors = [(cur_i - 1, cur_j), (cur_i + 1, cur_j), (cur_i, cur_j - 1), (cur_i, cur_j + 1)]
                  for ni,nj in neighbors:
                      if 0<=ni<rows and 0<=nj<cols and input_grid[ni,nj]==8 and (ni,nj) not in visited:
                          q.append((ni,nj))
                          visited.add((ni,nj))

                #change the left neighbor to blue
                if top_j - 1 >= 0:
                  output_grid[top_i, top_j - 1] = 1

    return output_grid.tolist()


if __name__ == '__main__':
    input_grid = [
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 0, 8, 0],
        [0, 0, 8, 0, 0, 0, 0],
        [0, 0, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 8, 8, 0, 0]
    ]
    expected_output = [
        [0, 0, 0, 0, 8, 8, 0],
        [0, 0, 0, 0, 1, 8, 0],
        [0, 0, 8, 1, 0, 0, 0],
        [0, 0, 8, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 8, 0, 0],
        [0, 0, 0, 8, 8, 0, 0]
    ]

    transformed_grid = transform(input_grid)

    if transformed_grid == expected_output:
        print("Transformation Successful!")
    else:
        print("Transformation Failed!")
        print("Expected Output:\n", expected_output)
        print("Transformed Output:\n", transformed_grid)
        
    assert transformed_grid == expected_output