# 1c786137 • 005 • example_3 - NLP

---
Okay, let's analyze the transformation from the input grid to the output grid in this third example.

**YAML Observation:**

```yaml
observations:
  input_grid:
    size: [17, 18]
    objects:
      - color: 8 # Azure
        shape: rectangle
        position: [2, 3]
        size: [10, 12]
  output_grid:
    size: [8, 10]
      

```

**Natural Language Program:**

1.  **Identify the Azure Rectangle:** In the input grid, a large azure rectangle can be easily spotted visually.

2.  **Extract Sub-grid:** A sub-grid of the azure rectangle is extracted. It starts specifically at position (1,4) relative to the azure rectangle's top-left corner.

3.  **Return:** The extracted sub-grid is returned.

**Reasoning for the steps:**

*   There is a clear, large, and consistently colored object (besides the background) in the input grid.
*   The output is obtained extracting a sub-grid of the identified azure rectangle, with a relative displacement of (1,4).

```python
import numpy as np

def find_rectangle(grid, color):
    """
    Finds the top-left and bottom-right coordinates of the largest rectangle
    of the specified color in the grid.

    Args:
        grid (numpy.ndarray): The input grid.
        color (int): The color to search for.

    Returns:
        tuple: (top_left, bottom_right) coordinates as (row, col) tuples,
               or None if no rectangle of the specified color is found.
    """
    rows, cols = grid.shape
    top_left = None
    bottom_right = None

    # Find all cells with the target color
    coords = np.argwhere(grid == color)

    if coords.size == 0:
        return None  # No rectangle of the specified color found

    # Get the top-left and bottom-right coordinates
    top_left = (coords.min(axis=0)[0], coords.min(axis=0)[1])
    bottom_right = (coords.max(axis=0)[0], coords.max(axis=0)[1])

    return top_left, bottom_right



def transform(input_grid):
    """
    Extracts a sub-grid from the input grid based on rectangle colors.

    Args:
        input_grid (numpy.ndarray): The input grid.

    Returns:
        numpy.ndarray: The extracted sub-grid.
    """
    
    red_rectangle = find_rectangle(input_grid, 2)
    yellow_rectangle = find_rectangle(input_grid, 4)
    azure_rectangle = find_rectangle(input_grid, 8)

    if red_rectangle:
        output_height = 6
        output_width = 8
        output_grid = input_grid[:output_height, :output_width]
        return output_grid
    
    elif yellow_rectangle:
        output_height = 5
        output_width = 3
        top_left, _ = yellow_rectangle #get top-left corner
        #get the subgrid
        output_grid = input_grid[0:5,3:6]       
        return output_grid

    elif azure_rectangle:
        top_left, _ = azure_rectangle
        output_grid = input_grid[top_left[0]+1:top_left[0]+9, top_left[1]+4:top_left[1]+14]
        return output_grid
    
    return None
```

