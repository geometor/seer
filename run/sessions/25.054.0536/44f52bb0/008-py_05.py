"""
Counts the number of red pixels (value '2') in the input grid.
If the count is 3, the output is 7 (orange).
"""

import numpy as np

def transform(input_grid):
    # Count the number of red pixels (value '2').
    red_count = np.sum(input_grid == 2)

    # Determine the output value based on the red pixel count.
    if red_count == 3:
        output_value = 7
    else:
        output_value = 0  # Default value if the condition is not met
    
    return output_value