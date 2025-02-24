# 1fad071e • 014 • example_3 • investigate_coder

---
```python
"""
1. Divide the input grid vertically into regions of three columns each.
2. Within each region, separately sum the number of red (2) pixels vertically in each column.
3. Within each region, identify the column which had the highest count from step 2.
4. If there is a tie between columns, choose the left most column, and set that column to 1 (blue) in output. All other columns are assigned 0 (white).
5. Combine all the results to produce a final output 1xN.
6. Count the occurence of each sum obtained in step 2 *across all regions*.
7. If any of the obtained sums equal the total number of regions, it means that the sum appeared in every group. Create an output pixel and assign 1 (blue).
8. If no sums occurred in all regions, create an output pixel and assign 0 (white).
9. Concatenate the pixels generated in step 5, 7 and 8.
"""

import numpy as np

def transform(input_grid):
    """Transforms the input grid according to the described rules."""

    input_grid = np.array(input_grid)
    rows, cols = input_grid.shape
    region_width = 3
    num_regions = (cols + region_width - 1) // region_width  # Calculate the number of regions
    output_grid = []

    # Step 1 & 2: Divide into regions and sum red pixels in each column.
    region_max_counts = []
    for i in range(num_regions):
        start_col = i * region_width
        end_col = min((i + 1) * region_width, cols)
        region = input_grid[:, start_col:end_col]
        
        red_counts = []
        for col in range(region.shape[1]):
          red_counts.append(np.sum(region[:,col] == 2))
        
        region_max_counts.append(red_counts)

    # Step 3 & 4 & 5: Find max count in each region and create a blue pixel.
    for red_counts in region_max_counts:
      if(len(red_counts) > 0):
        max_count = max(red_counts)
        max_index = red_counts.index(max_count)

        # Create the 1xN output
        output_grid.append(1)
      else:
        output_grid.append(0) #If no reds, append 0

    # Step 6 & 7 & 8: Count occurrences of sums and add blue/white pixels.
    all_counts = []
    for red_counts in region_max_counts:
      for count in red_counts:
        all_counts.append(count)

    counts_across_regions = {}
    for count in all_counts:
      if count in counts_across_regions:
          counts_across_regions[count] += 1
      else:
          counts_across_regions[count] = 1

    all_region_match_found = False
    for count, num_occurrences in counts_across_regions.items():
        if num_occurrences == num_regions:
            output_grid.append(1)
            all_region_match_found = True

    if not all_region_match_found:
      output_grid.append(0)

    return output_grid
```
