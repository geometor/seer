        output_grid[y-1, x] = 4  # Above
        output_grid[y+1, x] = 4  # Below
        output_grid[y, x-1] = 4  # Left
        output_grid[y, x+1] = 4  # Right