def analyze_example(input_grid, output_grid):
    input_grid = np.array(input_grid)
    output_grid = np.array(output_grid)

    changed_pixels = []
    for r in range(input_grid.shape[0]):
        for c in range(input_grid.shape[1]):
            if input_grid[r,c] != output_grid[r,c]:
                changed_pixels.append( ((r,c), input_grid[r,c], output_grid[r,c]) )

    input_objects = {}
    output_objects = {}

    #very simplistic object detection - contiguous same color
    def get_objects(grid, obj_dict):
        visited = set()
        def dfs(r, c, color, obj_id):
            if (r, c) in visited or r < 0 or r >= grid.shape[0] or c < 0 or c >= grid.shape[1] or grid[r,c] != color:
                return
            visited.add((r,c))
            obj_dict[obj_id].append((r,c))
            dfs(r+1, c, color, obj_id)
            dfs(r-1, c, color, obj_id)
            dfs(r, c+1, color, obj_id)
            dfs(r, c-1, color, obj_id)

        obj_id = 0
        for r in range(grid.shape[0]):
            for c in range(grid.shape[1]):
                if (r,c) not in visited and grid[r,c]!=0:
                    obj_dict[obj_id] = []
                    dfs(r, c, grid[r,c], obj_id)
                    obj_id += 1

    get_objects(input_grid, input_objects)
    get_objects(output_grid, output_objects)
    

    print(f"  Changed Pixels: {changed_pixels}")
    print(f"  Input Shape: {input_grid.shape}")
    print(f"  Output Shape: {output_grid.shape}")
    print(f"  Input Objects: {input_objects}")
    print(f"  Output Objects: {output_objects}")

print("Example 1:")
analyze_example([
    [0, 2, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 0, 0],
    [1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 5, 5, 5, 5, 5, 5],
    [0, 0, 0, 0, 0, 0, 0],
    [6, 6, 6, 6, 6, 0, 0],
    [0, 0, 0, 4, 4, 4, 4],
    [0, 0, 0, 0, 0, 0, 0],
    [8, 8, 8, 8, 8, 8, 8]
], [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 2, 2],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 0, 6, 6, 6, 6, 6],
    [0, 0, 0, 4, 4, 4, 4],
    [0, 5, 5, 5, 5, 5, 5],
    [8, 8, 8, 8, 8, 8, 8]
])

print("\nExample 2:")
analyze_example([
    [0, 0, 0, 1],
    [0, 0, 0, 0],
    [2, 2, 2, 0],
    [0, 0, 0, 0],
    [0, 3, 3, 0],
    [0, 0, 0, 0],
    [8, 8, 8, 8]
], [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 3, 3],
    [0, 2, 2, 2],
    [8, 8, 8, 8]
])

print("\nExample 3:")
analyze_example([
    [2, 2, 0],
    [0, 4, 0],
    [8, 8, 8]
], [
    [0, 0, 4],
    [0, 2, 2],
    [8, 8, 8]
])