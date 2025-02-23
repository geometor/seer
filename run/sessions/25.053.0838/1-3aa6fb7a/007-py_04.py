import numpy as np

# Previous code (from Example 1 analysis - reproduced here for completeness)
def get_objects(grid, color):
    objects = []
    visited = np.zeros_like(grid, dtype=bool)

    def dfs(r, c, current_object):
        if (r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or
                visited[r, c] or grid[r, c] != color):
            return
        visited[r, c] = True
        current_object.append((r, c))
        dfs(r + 1, c, current_object)
        dfs(r - 1, c, current_object)
        dfs(r, c + 1, c, current_object)
        dfs(r, c - 1, current_object)

    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == color and not visited[r, c]:
                current_object = []
                dfs(r, c, current_object)
                objects.append(current_object)
    return objects

def get_adjacent_pixels(grid, object_pixels, adj_color):
    adjacent = []
    for r, c in object_pixels:
        neighbors = [
            (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)
        ]
        for nr, nc in neighbors:
            if (0 <= nr < grid.shape[0] and 0 <= nc < grid.shape[1] and
                    grid[nr, nc] == adj_color):
                adjacent.append((nr, nc))
    # remove duplicates
    adjacent = list(dict.fromkeys(adjacent))
    return adjacent

def get_top_left_adjacent(grid, object_pixels, adj_color):
    adjacent_pixels = get_adjacent_pixels(grid, object_pixels, adj_color)
    if not adjacent_pixels:
        return None
    # find top-most, then left-most
    adjacent_pixels.sort()
    return adjacent_pixels[0]

def transform(input_grid):
    # initialize output_grid
    output_grid = np.copy(input_grid)
    # Identify azure objects
    azure_objects = get_objects(input_grid, 8)
    # find adjacent white pixels and change the color
    for obj in azure_objects:
      adjacent_white = get_top_left_adjacent(input_grid, obj, 0)
      if adjacent_white:
        output_grid[adjacent_white] = 1

    return output_grid

# New Input
input_grid_2 = np.array([
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 0, 8, 0],
    [0, 0, 8, 0, 0, 0, 0],
    [0, 0, 8, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 8, 8, 0, 0]
])

output_grid_2 = np.array([  # provided expected output
    [0, 0, 0, 0, 8, 8, 0],
    [0, 0, 0, 0, 1, 8, 0],
    [0, 0, 8, 1, 0, 0, 0],
    [0, 0, 8, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 8, 0, 0],
    [0, 0, 0, 8, 8, 0, 0]
])

predicted_output_grid_2 = transform(input_grid_2)
print(f'{predicted_output_grid_2=}')
print(f'{output_grid_2=}') # the correct answer, for comparison
comparison = predicted_output_grid_2 == output_grid_2
print(f'{comparison.all()=}')


azure_objects_input = get_objects(input_grid_2, 8)
white_pixels_adjacent_to_azure_input = []
for obj in azure_objects_input:
    white_pixels_adjacent_to_azure_input.extend(get_adjacent_pixels(input_grid_2, obj, 0))

print(f'{azure_objects_input=}')
print(f'{len(azure_objects_input)=}')
print(f'{white_pixels_adjacent_to_azure_input=}')
