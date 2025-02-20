# 1-3aa6fb7a • 003 • example_2 - NLP

---
**Natural Language Program:**

The task is to modify the input grid by identifying connected regions of azure color (color 8) and adding a blue cell (color 1) adjacent to each region. The placement of the blue cell depends on whether the azure region is "left-leaning" or "right-leaning" based on its shape.

Here's the step-by-step transformation rule:

1.  **Identify Azure Regions:** Find all connected components of cells with color 8 in the input grid. Each connected component is considered an independent azure region.
2.  **Analyze Each Region:** For each identified azure region, perform the following steps:
    a. **Determine Bounding Box:** Find the smallest rectangle that encloses the azure region. This is defined by the minimum row (min\_r), minimum column (min\_c), maximum row (max\_r), and maximum column (max\_c) indices of the cells in the region.
    b. **Calculate Centroid Column:** Calculate the average column index of all cells in the azure region.
    c. **Calculate Bounding Box Center Column:** Calculate the average of the minimum column (min\_c) and maximum column (max\_c) of the bounding box.
    d. **Compare Centroid Column and Bounding Box Center Column:**
        - **If the Centroid Column is greater than the Bounding Box Center Column:** The region is considered "right-leaning". Place a blue cell (color 1) at the position with row index equal to the minimum row of the bounding box (min\_r) and column index equal to the minimum column of the bounding box (min\_c).
        - **If the Centroid Column is less than or equal to the Bounding Box Center Column:** The region is considered "left-leaning" or centered. Place a blue cell (color 1) at the position with row index equal to the minimum row of the bounding box (min\_r) and column index immediately to the right of the maximum column of the bounding box (max\_c + 1).
    e. **Preserve Azure Region:** Ensure that the azure region itself remains unchanged in the output grid.
3.  **Maintain Background:** All cells in the input grid that are not part of any azure region and are not modified by step 2.d, remain white (color 0) in the output grid.

This process is applied independently to each connected azure region in the input grid to produce the final output grid.

**YAML Block:**

```yaml
task_context: "grid transformation"
transformation_rule: "add blue cell adjacent to azure regions based on shape lean"
objects:
  - azure_region:
      color: 8
      properties:
        - bounding_box
        - centroid_column
        - bounding_box_center_column
        - lean_direction: ["left", "right"]
  - blue_cell:
      color: 1
      action: "add adjacent to azure region"
predicates:
  - is_connected: "cells of same color are adjacent"
  - is_right_leaning: "centroid_column > bounding_box_center_column"
  - is_left_or_centered_leaning: "centroid_column <= bounding_box_center_column"
actions:
  - identify_azure_regions: "find all connected components of color 8"
  - calculate_bounding_box: "find min/max row/col of region"
  - calculate_centroid_column: "average column index of region cells"
  - calculate_bounding_box_center_column: "average min/max column of bounding box"
  - compare_columns: "centroid_column vs bounding_box_center_column"
  - place_blue_cell_left: "at (min_r, min_c) if right-leaning"
  - place_blue_cell_right: "at (min_r, max_c + 1) if left/centered-leaning"
  - preserve_azure_region: "keep azure cells unchanged"
  - maintain_background: "keep non-azure and non-modified cells as white"
```
