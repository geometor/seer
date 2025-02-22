import numpy as np

def transform(input_grid):
    """
    Transforms the input grid according to the specified rule.
    """
    output_grid = np.copy(input_grid)
    rows, cols = output_grid.shape

    # Find all 'L' shapes
    l_shapes = []
    for r in range(rows - 1):
        for c in range(cols - 1):
            if output_grid[r, c] == 8:
                # Check for all 4 L-shape orientations
                if output_grid[r + 1, c] == 8 and output_grid[r, c + 1] == 8:  # _|
                    l_shapes.append(((r, c), (r + 1, c), (r, c + 1), "top_left", (r, c+1) ))
                if output_grid[r + 1, c] == 8 and output_grid[r + 1, c + 1] == 8:  # |_
                    l_shapes.append(((r, c), (r + 1, c), (r + 1, c + 1), "top_right", (r+1,c+1)))
                if output_grid[r, c + 1] == 8 and output_grid[r + 1, c + 1] == 8:  # -|
                    l_shapes.append(((r, c), (r, c + 1), (r + 1, c + 1), "bottom_left",(r,c)))
                if output_grid[r, c] == 8 and output_grid[r-1,c] == 8 and output_grid[r,c+1] ==8:
                    l_shapes.append(((r,c),(r-1,c), (r,c+1),"top_left_rev", (r,c+1))) # reverse L
                if output_grid[r,c] == 8 and output_grid[r-1,c] == 8 and output_grid[r-1,c-1]==8:
                    l_shapes.append(((r,c), (r-1,c),(r-1,c-1),"top_right_rev", (r-1,c-1)))
                if output_grid[r,c] == 8 and output_grid[r,c-1] == 8 and output_grid[r-1,c]==8:
                    l_shapes.append(((r,c),(r,c-1),(r-1,c), "bottom_left_rev",(r,c-1)))

    # Determine top-left-most and bottom-right-most L shapes
    if l_shapes:

        # Sort the list of tuples by the sum of row index
        sorted_by_row = sorted(l_shapes, key=lambda x: x[0][0] )
        top_left_most = sorted_by_row[0]
        bottom_right_most = sorted_by_row[-1]
        #print(top_left_most, bottom_right_most)

        #Apply the blue color.
        if "top" in top_left_most[3]:

          r,c = top_left_most[4]
          if c+1 < cols:
              output_grid[r,c+1] = 1

        if "bottom" in bottom_right_most[3]:

          r,c = bottom_right_most[4]

          if c-1 >= 0:
            output_grid[r, c - 1] = 1


    return output_grid