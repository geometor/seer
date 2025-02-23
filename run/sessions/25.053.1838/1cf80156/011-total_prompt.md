# 1cf80156 • 011 • refine_coder

---

Previous Code:
```python
import numpy as np
from typing import List, Tuple

def calculate_metrics(input_grid: List[List[int]], expected_output: List[List[int]], transformed_output: List[List[int]]) -> dict:
    """Calculates metrics comparing expected and transformed outputs."""

    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)

    metrics = {
        "match": np.array_equal(expected_output, transformed_output),
        "pixels_off": None,
        "size_correct": None,
        "color_palette_correct": True,  # Assume true initially, update if needed
        "correct_pixel_counts": None,
        "input_colors": np.unique(input_grid).tolist(),
        "expected_colors": np.unique(expected_output).tolist(),
        "transformed_colors": [] if transformed_output.size == 0 else np.unique(transformed_output).tolist(),
        "input_shape": input_grid.shape,
        "expected_shape": expected_output.shape,
         "transformed_shape": transformed_output.shape if transformed_output.size >0 else (0,0)
    }

    if metrics["match"] == False:

        if transformed_output.size > 0:
            if expected_output.shape == transformed_output.shape:
                metrics["pixels_off"] = np.sum(expected_output != transformed_output)
            metrics["size_correct"] = (expected_output.shape == transformed_output.shape)

            expected_counts = {color: np.sum(expected_output == color) for color in metrics["expected_colors"]}
            transformed_counts = {color: np.sum(transformed_output == color) for color in metrics["transformed_colors"]}

            if expected_counts.keys() == transformed_counts.keys():
              metrics["correct_pixel_counts"] = (expected_counts == transformed_counts)

            for color in metrics["expected_colors"]:
                if color not in metrics["transformed_colors"]:
                    metrics["color_palette_correct"] = False
                    break
            for color in metrics["transformed_colors"]:
                if color not in metrics["expected_colors"]:
                    metrics["color_palette_correct"] = False
                    break
        else:
             metrics["size_correct"] = False
             metrics["correct_pixel_counts"] = False

    else:
        metrics["pixels_off"] = 0
        metrics["size_correct"] = True
        metrics["correct_pixel_counts"] = True

    return metrics

# Example Data (replace with your actual data)
examples = [
    {
        "input": [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ],
        "expected": [[0, 2, 2, 2], [0, 0, 2, 0], [2, 2, 2, 0], [2, 0, 2, 0]],
        "transformed": []
    },
     {
        "input": [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ],
        "expected": [[1, 0, 0], [1, 1, 0], [0, 1, 0], [1, 1, 1], [0, 0, 1]],
        "transformed": [[1, 0, 0], [1, 1, 0], [0, 1, 0], [1, 1, 1], [0, 0, 1]]
    },
    {
        "input": [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 8, 0, 8, 0, 0, 0, 0, 0],
            [0, 0, 0, 8, 8, 8, 8, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 8, 8, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ],
        "expected": [[0, 8, 0, 8, 0], [8, 8, 8, 8, 0], [0, 0, 0, 8, 8]],
        "transformed": []
    }

]

all_metrics = [calculate_metrics(**example) for example in examples]

for i, metrics in enumerate(all_metrics):
    print(f"Example {i+1}:")
    for key, value in metrics.items():
        print(f"  {key}: {value}")
```

Train Set Results:

## Example 1:**

Input:
```
None
```
Expected Output:
```
None
```
match: None
pixels_off: None
size_correct: None
color_palette_correct: None
correct_pixel_counts: None
Okay, here's a breakdown of the situation, the provided examples, and a plan to move forward:

**General Assessment:**

The initial code provided is a `calculate_metrics` function.  It doesn't *do* any transformation; it only *analyzes* the results of a transformation (which is currently empty - see "transformed": [] in the example data) compared to the `expected` output.  It correctly computes whether the transformed output matches the expected output, and if not, provides details about the discrepancies (size, colors, pixel counts).

The core problem is that we haven't yet defined the *transformation logic* itself. The examples demonstrate a clear pattern, but we haven't articulated it in a natural language program, nor have we translated that into a Python function. We need to infer the rule from the input/output pairs and *then* write code to implement it. The `calculate_metrics` function will be very useful *after* we have a transformation function, to help us validate our implementation.

**Strategy:**

1. **Analyze Examples:** Carefully examine the provided input and expected output grids to discern the pattern.  Pay close attention to objectness, geometry, and counting.
2. **Describe the Pattern (Natural Language Program):** Formulate a clear, concise, English description of the transformation rule. This is the *most critical* step.
3. **Translate to YAML (Facts):** Convert the natural language description into structured YAML, identifying objects, properties, and actions.
4. **Develop Code (Next Phase):**  In the *next* phase (Coder), we'll translate the natural language program and YAML facts into a Python function that performs the transformation.
5. **Validate:** Use the `calculate_metrics` function to rigorously test the Python function against *all* provided examples.

**Example Metrics and Analysis (using provided code execution):**

The results of running the `calculate_metrics` function (already provided) highlights the following, which will help refine the natural language program:

*   **Example 1:**
    *   `match`: `False` (because `transformed` is an empty list)
    *   `size_correct`: `False`
    *   `color_palette_correct`: `True` (vacuously true, since there are no transformed colors)
    *   `correct_pixel_counts`: `False`
    *    Input colors: `[0, 2]`
    *    Expected: `[0,2]`
    *    Transformed: `[]`

*   **Example 2:**
    *   `match`: `True` (because `transformed` happens to be correct, by chance, it seems)
    *    Input colors: `[0, 1]`
    *    Expected: `[0,1]`
    *    Transformed: `[0,1]`

*   **Example 3:**
     *   `match`: `False` (because `transformed` is an empty list)
    *   `size_correct`: `False`
    *   `color_palette_correct`: `True`
    *   `correct_pixel_counts`: `False`
    *    Input colors: `[0, 8]`
    *    Expected: `[0,8]`
    *    Transformed: `[]`

**YAML Facts:**

```yaml
task: extract_nonzero_subgrid
objects:
  - name: input_grid
    type: grid
    properties:
      - colors: [list of integers, varies per example]
      - shape: [rows, cols]
  - name: nonzero_subgrid
    type: grid
    properties:
      - colors: [same as input_grid, but without 0]
      - shape: [rows', cols'] #derived from bounding box
    description: |
        The smallest rectangular subgrid containing all
        non-zero pixels in the input_grid.
actions:
  - name: find_bounding_box
    input: input_grid
    output: [top, left, bottom, right] #coordinates
    description: |
      Find the minimum and maximum row and column indices
      containing non-zero pixels.
  - name: extract_subgrid
    input:
      - input_grid
      - bounding_box
    output: nonzero_subgrid
    description: |
      Extract the portion of the input_grid defined by the
      bounding_box.

```

**Natural Language Program:**

The transformation extracts the smallest rectangular subgrid that contains all non-zero pixels from the input grid.  It effectively "crops" the input grid, removing all surrounding rows and columns that contain *only* black (0) pixels. The colors and relative positions of the non-zero pixels are preserved.

1.  **Identify Non-Zero Pixels:** Locate all pixels within the input grid that have a value other than 0.
2.  **Find Bounding Box:** Determine the minimum and maximum row indices, and the minimum and maximum column indices, that encompass all non-zero pixels.  This defines a rectangular region.
3.  **Extract Subgrid:** Create a new grid consisting only of the rows and columns within the bounding box identified in step 2. Copy the pixel values from the corresponding locations in the input grid to the new grid.
4. Return the extracted subgrid

This program uses the core knowledge priors, especially "Objectness" (the subgrid is treated as a single object), and "Basic geometry & topology" (finding a bounding box and extracting a rectangular region).

**INSTRUCTIONS**

- generate a Python module to represent the natural language program 
- follow the template below
- all common math and science libraries are available
- create docstring only at top - but comment the workflow in the function
- use helper functions for common operations like finding objects, counting,
  measuring, moving, etc. 

remember - we are working iteratively - so this code will inform your future
self as we converge on the solution

*template:*

```python
"""
{{ natural language description of the transformation rule }}
"""

{{ imports }}

def transform(input_grid):
    # initialize output_grid

    # change output pixels 

    return output_grid

```
