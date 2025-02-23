"""
1. Count Red Pixels: Count the number of pixels with the value 2 (red) in the input grid.
2. Determine Output Value:
    *   If the count of red pixels is even, the output value is 1.
    *   If the count of red pixels is odd, the output value is 7.
3. Create Output Grid: Create a 1x1 output grid containing the determined output value as a single pixel.
"""

import numpy as np

def transform(input_grid):
    # Count red pixels
    red_count = np.sum(input_grid == 2)

    # Determine output value based on even/odd count
    if red_count % 2 == 0:
        output_value = 1
    else:
        output_value = 7

    # Create 1x1 output grid
    output_grid = np.array([[output_value]])

    return output_grid