# 2-0ca9ddb6 • 003 • example_2 - NLP

---
**Natural Language Program: Transformation Rule**

1. **Initialization:** Create a new output grid that is initially identical to the input grid.
2. **Iterate through Input Grid:** Examine each cell in the input grid, row by row, and column by column.
3. **Identify Red Pixels:** If a cell in the input grid contains the color red (color code 2):
    - Consider its horizontal, vertical, and diagonal neighbors (all 8 neighbors).
    - For each neighbor position, check if the corresponding cell in the *input* grid is white (color code 0).
    - If a neighbor cell in the input grid is white, change the color of the same neighbor cell in the *output* grid to yellow (color code 4).
4. **Identify Blue Pixels:** If a cell in the input grid contains the color blue (color code 1):
    - Consider its horizontal, vertical, and diagonal neighbors (all 8 neighbors).
    - For each neighbor position, check if the corresponding cell in the *input* grid is white (color code 0).
    - If a neighbor cell in the input grid is white, change the color of the same neighbor cell in the *output* grid to orange (color code 7).
5. **Maintain Original Pixels:** The original red and blue pixels in the input grid remain unchanged in the output grid. All other pixels that are not neighbors of red or blue pixels (or whose neighbors in input were not white) also remain unchanged from the input to the output grid.
6. **Unaffected Pixels:** Pixels of other colors, such as azure (color code 8) in this example, are not part of the transformation logic and remain unchanged in the output.
7. **Output:** The resulting output grid after processing all red and blue pixels in the input grid is the final transformed grid.

**YAML Block: Object Observation and Documentation**

```yaml
task_context: "Grid transformation based on color proximity, applying different border colors for red and blue objects."
objects:
  - type: "pixel"
    color: "red"
    color_code: 2
    behavior: "Generates yellow border in all 8 directions on empty (white) spaces."
  - type: "pixel"
    color: "blue"
    color_code: 1
    behavior: "Generates orange border in all 8 directions on empty (white) spaces."
  - type: "pixel"
    color: "azure"
    color_code: 8
    behavior: "Unaffected by transformation, remains unchanged."
predicates:
  - "is_red": "Checks if a pixel is red (color code 2)."
  - "is_blue": "Checks if a pixel is blue (color code 1)."
  - "is_white": "Checks if a pixel is white (color code 0)."
  - "is_neighbor": "Checks if a position is any of the 8 neighbors (horizontal, vertical, or diagonal)."
actions:
  - "create_yellow_border": "Sets all neighbors to yellow if input neighbor is white and the central pixel is red."
  - "create_orange_border": "Sets all neighbors to orange if input neighbor is white and the central pixel is blue."
transformation_rule: "For each red pixel, create a yellow border in all directions on white input neighbors. For each blue pixel, create an orange border in all directions on white input neighbors. Azure pixels and their neighbors are unaffected."
```
