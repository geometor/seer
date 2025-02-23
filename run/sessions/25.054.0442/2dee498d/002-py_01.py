"""
The transformation extracts a subgrid from the input. The subgrid consists of the odd columns (first, third, fifth, etc ) of the input. The rows appear to be identical from input to output.

1.  Iterate through the input grid.
2.  Select every other colum.
3.  Construct a new output grid.
4.  Populate the output with the selected columns.
"""

import numpy as np

def transform(input_grid):
    # Construct a new output grid by selecting every other column.
    output_grid = []
    for row in input_grid:
      new_row = []
      for i in range(len(row)):
        if (i+1) % 2 != 0: # check if is odd (first, third, etc)
          new_row.append(row[i])
      output_grid.append(new_row)

    return output_grid