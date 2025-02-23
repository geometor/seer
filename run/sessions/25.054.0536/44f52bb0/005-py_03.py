import numpy as np

def is_fully_connected(grid, red_pixels):
    """
    Checks if a set of red pixels in a grid are fully connected.
    """
    if not red_pixels:
        return True  # No red pixels, vacuously true

    visited = set()
    queue = [red_pixels[0]]
    visited.add(red_pixels[0])

    while queue:
        r, c = queue.pop(0)
        # Check neighbors (up, down, left, right)
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if (nr, nc) in red_pixels and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc))
    print(f"visited: {visited}")
    print(f"red_pixels: {red_pixels}")

    return len(visited) == len(red_pixels)

def get_red_pixel_groups(grid):
    """
    find the groups of connected red pixels
    """
    red_pixels = []
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r,c] == 2:
                red_pixels.append((r,c))

    groups = []
    ungrouped = red_pixels[:]

    while ungrouped:
        group = set()
        to_process = [ungrouped.pop(0)]
        group.add(to_process[0])
        while to_process:
            r, c = to_process.pop()
            # Check neighbors (up, down, left, right)
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) in ungrouped:
                    ungrouped.remove((nr,nc))
                    to_process.append((nr,nc))
                    group.add((nr,nc))
        groups.append(group)
    return groups
            

# Example grids (from the prompt)
grids = [
    np.array([[2, 0, 2], [0, 2, 0], [2, 0, 2]]),  # Example 1
    np.array([[2, 0, 0], [2, 0, 0], [0, 2, 0]]),  # Example 2
    np.array([[2, 0, 2], [2, 0, 2], [2, 0, 2]]),  # Example 3
    np.array([[0, 0, 0], [2, 0, 2], [0, 0, 0]]),  # Example 4
    np.array([[2, 2, 0], [0, 2, 2], [0, 0, 0]]),  # Example 5
    np.array([[2, 2, 0], [0, 2, 0], [0, 0, 0]]),  # Example 6
]

expected_outputs = [1, 7, 1, 1, 7, 7]

for i, grid in enumerate(grids):
    print(f"Example {i + 1}:")
    red_pixels = []
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            if grid[r, c] == 2:
                red_pixels.append((r, c))
    fully_connected = is_fully_connected(grid, red_pixels)
    groups = get_red_pixel_groups(grid)
    print(f"Number of groups {len(groups)}")
    print(f"Fully connected: {fully_connected}\n")
