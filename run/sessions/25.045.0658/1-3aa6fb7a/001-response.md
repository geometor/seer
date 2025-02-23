# 25.045.0658 • 1-3aa6fb7a • 001 Response

---

*text:*

**Natural Language Program:**

The transformation rule is as follows:
For every cell in the input grid, we check its current color.
If the cell is white (color 0), we then examine its four immediate neighbors (up, down, left, right).
If at least one of these neighboring cells is azure (color 8), we change the color of the current cell to blue (color 1) in the output grid.
If none of the neighboring cells are azure (color 8), the cell remains white (color 0) in the output grid.
If the cell is already azure (color 8), it remains azure (color 8) in the output grid, and is not modified.
Cells of any other color are also not modified. In this specific example, only colors 0 and 8 are present in the input, and colors 0, 1, and 8 in the output.

**YAML Block:**

```yaml
task_context: "Grid transformation based on neighbor color"
transformation_rule: "For each white cell, if any adjacent cell is azure, change the cell to blue."
objects:
  - type: "cell"
    properties:
      color: ["white", "azure", "blue"]
      position: "grid coordinates"
  - type: "neighbor"
    relation: "adjacent to"
actions:
  - action_type: "check_neighbor_color"
    target_object: "cell"
    neighbor_type: "adjacent"
    condition_color: "azure"
  - action_type: "change_color"
    target_object: "cell"
    new_color: "blue"
    condition: "adjacent azure neighbor exists and cell is white"
```
