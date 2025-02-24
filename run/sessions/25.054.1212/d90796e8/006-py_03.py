"""
1.  Iterate through each row of the input grid.
2.  Identify sequences of *adjacent* cells within the row that meet *all* these criteria:
    *   The cell's value is not 0 (white).
    *   The cell's value is not 5 (grey).
    *   The cell's value is different from its immediate neighbor(s) within the sequence.
3.  Calculate Sum:** For each identified sequence:
    *   Sum the values of all cells in the sequence.  If value 2 is involved, multiple by 2.
4.  Leftmost Placement:** Replace the value of the *leftmost* cell in the sequence with the calculated sum.
5.  Zeroing:** Set the values of *all other* cells within that identified sequence to 0.
6.  Isolated Cell Handling**: Any non-zero, non-grey cell that is *not* part of an adjacent sequence (as defined in step 2) is set to 0 in the output.
7.  Copy Unchanged:** All cells that are not part of an identified sequence (i.e., 0 (white) or 5 (grey) cells) are copied directly from the input to the output without modification.
"""

import numpy as np

def transform(input_grid):
    # initialize output_grid as a copy of input
    output_grid = np.copy(input_grid)
    rows, cols = input_grid.shape

    # Iterate through each row
    for r in range(rows):
        colored_indices = []
        for c in range(cols):
            if input_grid[r, c] != 0 and input_grid[r, c] != 5:
                colored_indices.append(c)

        # process the colored cells
        if len(colored_indices) > 0:
          
          summed_indices = []
          sum_val = 0
          i = 0
          while i < len(colored_indices):
            current_val = input_grid[r, colored_indices[i]]
            current_sum = current_val
            current_sequence = [colored_indices[i]]
            
            j = i + 1
            while j < len(colored_indices):
                next_val = input_grid[r, colored_indices[j]]
                if next_val != current_val:
                    current_sum += next_val
                    current_sequence.append(colored_indices[j])
                    j += 1

                else:
                    break

            
            if len(current_sequence) > 1: # adjacent and different
                if 2 in [input_grid[r,x] for x in current_sequence]:
                      current_sum = 0
                      for x in current_sequence:
                        if input_grid[r,x] == 2:
                            current_sum = current_sum + (input_grid[r,x] * 3)
                        else:
                            current_sum += input_grid[r,x]
                output_grid[r, current_sequence[0]] = current_sum
                for k in range(1, len(current_sequence)):
                  output_grid[r, current_sequence[k]] = 0

            elif len(current_sequence) == 1:
                output_grid[r, current_sequence[0]] = 0

            i = j


    return output_grid