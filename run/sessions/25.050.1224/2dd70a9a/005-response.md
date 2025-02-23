# 2dd70a9a • 005 • example_3 - NLP

---
Okay, let's analyze this third input/output pair, keeping in mind the previously developed rule and checking for any necessary adjustments.

**Observations and Documentation (YAML)**

```yaml
input_grid:
  size: 15x15
  objects:
    - color: 8 (azure)
      shape: scattered single cells and small clusters
      notes: Acts as a boundary and seed for green expansion.
    - color: 0 (white)
      shape: background
      notes: Fills most of the empty space.
    - color: 2 (red)
      shape: 1x2 block
      position: (9, 1) and (9, 2)
      notes: Remains static.
    - color: 3 (green)
      shape: two adjacent cells
      position: (5, 1) and (5, 2)
      notes: Agents for transformation.

output_grid:
  size: 15x15
  objects:
    - color: 8 (azure)
      notes: Unchanged.
    - color: 0 (white)
      notes: Unchanged.
    - color: 2 (red)
      notes: Unchanged.
    - color: 3 (green)
      shape: Horizontal segments.
      notes: Multiple expansions, each triggered by nearby azure and previous green positions.

```

**Determining the Transformation Rule (Natural Language Program)**

1.  **Static Objects:** The red cells (color 2) and azure cells (color 8) remain in their initial configurations.

2.  **Green Object Identification:** The two adjacent green cells (color 3) at (5, 1) and (5, 2) are the initial agents.

3.  **Expansion Procedure Refinement:**
    *   Calculate the average row index of the initial green pair: (5 + 5) / 2 = 5.
    *   Find the closest azure cell (seed) *to the right* on this row (or the closest if no azure to the right). The closest is at (5, 8).
    *   Expand green from this seed to the *left* until an azure cell or the grid boundary is hit.
    *   The next expansions are a bit different. It seems new expansions don't just come from *pairs* of green cells, but from *any* green cells, and the expansion row can also be determined using an azure cell as reference. The next "seed" appears to be at (7,7) and (8,7), with row (6+9)/2.
    *   In row 6, we have a new expansion to the left. In row 9, to the right.

4. **Revised Expansion Summary**
The expansion algorithm is better explained as follows:
   - Locate existing green objects.
   - Compute average row indices between pairs of color 3 objects, or between color 3 objects and the closest color 8 to its right if only one object 3 is present.
   - Use the closest azure seed *to the right* of the initial object 3 in that row (or simply the closest seed if no azure cells on that side)
   - Expand from the azure seed to the left or to the right (or both) until reaching a border, or another color 8.

```python
import numpy as np

def get_object_positions(grid, color):
    """Finds the positions of all cells with a specific color."""
    return np.array(np.where(grid == color)).T

def find_closest_azure_seed(grid, row, start_col, direction):
    """
    Finds the closest azure cell in the specified row, starting from a given column and searching in a given direction.
    
    Args:
        grid: The input grid.
        row: The row to search.
        start_col: start searching from this column
        direction: 1 for right, -1 for left.

    Returns: The position of the closest azure, or None.
    """

    if direction != 1 and direction != -1:
        raise Exception("direction must be -1 (left) or +1 (right)")

    azure_positions = get_object_positions(grid, 8)
    
    if len(azure_positions) == 0 :
        return None

    azure_in_row = [pos for pos in azure_positions if pos[0] == row]
    if not azure_in_row:
        return None
    
    if direction == 1: # search to the right
      
      valid_azure = [pos for pos in azure_in_row if pos[1] > start_col]

      if len(valid_azure) == 0: # no azure on the right, search closest
          return min(azure_in_row, key=lambda pos: abs(pos[1] - start_col), default=None)

      return min(valid_azure, key=lambda pos: abs(pos[1] - start_col), default=None)

    else: # search to the left
      valid_azure = [pos for pos in azure_in_row if pos[1] < start_col]

      if len(valid_azure) == 0:  # no azure on the left, search closest
            return min(azure_in_row, key=lambda pos: abs(pos[1] - start_col), default=None)
      
      return min(valid_azure, key=lambda pos: abs(pos[1] - start_col), default = None)

def transform(input_grid):
    """Transforms the input grid according to the final rule."""
    output_grid = np.copy(input_grid)
    
    # 1. Keep red and azure cells unchanged
    
    # 2 & 3. Green expansion
    green_positions = list(get_object_positions(input_grid, 3)) # Convert to list for easier manipulation
    
    
    processed_greens = []

    while len(green_positions) > 0:

      current_green = green_positions.pop(0) # Take one green as reference
      
      if (current_green[0],current_green[1]) in processed_greens: # already used
          continue
      
      # calculate average row with another green or azure
      
      if len(green_positions) > 0: # exist other green
            other_green = min(green_positions, key=lambda pos: abs(pos[0] - current_green[0]) +  abs(pos[1] - current_green[1])) # closest one
            expansion_row = int(np.mean([current_green[0], other_green[0]]))
            
            #seed to the right
            seed = find_closest_azure_seed(input_grid, expansion_row, current_green[1], direction = 1)
            
      else:  # no other green
        expansion_row = current_green[0]
        seed = find_closest_azure_seed(input_grid, expansion_row, current_green[1], direction = 1)

      
      if seed is not None: # apply expansion

        if expansion_row == current_green[0]: # same line
          # expand to the left
          col = seed[1] - 1
          while col >= 0 and input_grid[expansion_row, col] != 8:
                output_grid[expansion_row, col] = 3
                col -= 1

        else: # different line

          # expand to the right
          col = seed[1] + 1
          while col < input_grid.shape[1] and input_grid[expansion_row, col] != 8:
            output_grid[expansion_row, col] = 3
            col += 1

      processed_greens.append((current_green[0],current_green[1]))
      if 'other_green' in locals():
        processed_greens.append((other_green[0],other_green[1]))



    return output_grid
```

