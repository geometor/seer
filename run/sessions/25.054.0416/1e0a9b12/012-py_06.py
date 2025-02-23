"""
1.  **Identify Key Rows:** Find all rows in the input grid that contain any pixel color other than 0 (white) or 4 (yellow).
2.  **Combine Rows (Bottom-Up):** Combine *all* identified key rows. The order of combination is from the bottom row of the input to the top. These combined rows will form the bottom rows of the output grid.
3.  **Place Combined Rows:** Position the combined rows at the *bottom* of the output grid.
4.  **Handle Color 9 (Maroon):** Within each combined row in the output, move any pixel of color 9 (maroon) to the last column of that row.
5.  **Preserve Relative Order:** Maintain the original horizontal order of all other colored pixels within each row.
6.  **Fill Remaining Rows:** Fill any remaining rows at the top of the output grid (above the combined rows) with 0 (white).
"""

import numpy as np

def get_key_rows(grid):
    """Identifies rows that contain colors other than 0 or 4 and returns them."""
    key_rows = []
    for i, row in enumerate(grid):
        if any(pixel != 0 and pixel != 4 for pixel in row):
            key_rows.append(row)
    return key_rows

def transform(input_grid):
    """Transforms the input grid according to the observed rules."""
    output_grid = np.zeros_like(input_grid)
    key_rows = get_key_rows(input_grid)
    
    # Combine and reorder rows (bottom-up).
    num_key_rows = len(key_rows)
    
    combined_rows = []
      
    for i in range(num_key_rows):
       combined_rows.insert(0, key_rows[num_key_rows-1-i])
    
    # apply to output
    output_row_index = output_grid.shape[0] - 1

    for row_index in range(len(combined_rows)-1, -1, -1):
       row = combined_rows[row_index]
       non_zero_pixels = [(i,x) for i, x in enumerate(row) if x !=0]
       
       if non_zero_pixels: # this check avoids the case of combining all zero rows

            if 9 in row:
                # Handle Maroon (9) to last position.
                
                non_zero_pixels_no_maroon = [(i,x) for i, x in enumerate(row) if x !=0 and x!=9]
                
                
                output_grid[output_row_index,output_grid.shape[1]-1] = 9

                current_output_col = 0
                for col, pixel_val in non_zero_pixels_no_maroon:
                    if current_output_col < output_grid.shape[1]-1:
                       output_grid[output_row_index, current_output_col] = pixel_val
                       current_output_col+=1
            
            else:    
               current_output_col = 0
               for col, pixel_val in non_zero_pixels:
                    if current_output_col < output_grid.shape[1]:
                        output_grid[output_row_index, current_output_col] = pixel_val
                        current_output_col+=1
       output_row_index -= 1

    return output_grid