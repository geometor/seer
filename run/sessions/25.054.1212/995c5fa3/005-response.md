# 995c5fa3 • 005 • refine_coder

---
```python
"""
The input grid (14x4) is divided into three regions by the vertical white (0) columns.
Each region contributes a row to the output grid (3x3).
Within each region, the position of white (0) pixels in a specific sub-region
determines the color of the output row. The sub-region considered for white
pixel analysis seems to be between the vertical white columns. We can express
this region programmatically as columns 5-8 (inclusive) in the first and second
vertical white separators, and 10-13 (inclusive) in the second and third white
vertical separators.

The color of the output row seems to be determined as:
- 2 (red): If a white pixel is in the 2nd or 4th position in the sub-region.
- 8 (azure): if a white pixel is in the 1st position in the sub-region.
- 3 (green): If a white pixel is in the 3rd position and no white in the first of
              the sub-region.
- 4 (yellow): If a white pixel is in the 2nd position, and no white in the first
             of the sub-region.

"""

import numpy as np

def get_region_color(region):
    # Analyze the region (columns 5-8 and 10-13) for white pixel positions.
    color = 0  # Default color

    # Extract the relevant sub-region based on provided examples.
    if region.shape[1] >= 4: # check shape
      sub_region = region[:,:4]

      # Check for white pixel positions and determine the color.
      if np.any(sub_region[0, 0] == 0):
        color = 8
      elif np.any(sub_region[0, 1] == 0): #and not np.any(sub_region[0,0] == 0):
        color = 2
      elif np.any(sub_region[0, 2] == 0):
        color = 3
      elif np.any(sub_region[0, 3] == 0):
        color = 2
      elif np.any(sub_region[1, 0] == 0):
        color = 3
      elif np.any(sub_region[1,1] == 0):
        color = 4
      elif np.any(sub_region[1, 2] == 0): # and not np.any(sub_region[0,0] == 0):
          color = 4
      elif np.any(sub_region[1, 3] == 0):
        color = 2
      elif np.any(sub_region[2, 0] == 0) :
        color = 8
      elif np.any(sub_region[2, 1] == 0):
        color = 2
      elif np.any(sub_region[2, 2] == 0):
        color = 4
      elif np.any(sub_region[2, 3] == 0):
        color = 4

    return color

def transform(input_grid):
    # Initialize the output grid.
    output_grid = np.zeros((3, 3), dtype=int)
    input_grid = np.array(input_grid)

    # Define the regions of interest (between vertical white columns).
    region1 = input_grid[:, 5:9]
    region2 = input_grid[:, 9:13]
    region3 = input_grid[:, 9:14] #not used

    # Determine the color for each row of the output grid.
    output_grid[0, :] = get_region_color(region1)
    output_grid[1, :] = get_region_color(region2)

    region3 = input_grid[2:, 10:14] # check third line for region.
    output_grid[2,:] = get_region_color(region3)

    return output_grid
```
