# AboveBelow1 • 011 • refine_dreamer

---
Here's an analysis of the provided information and a plan to refine the solution:

**General Assessment:**

The initial code correctly identifies the need to preserve the top three rows and blank subsequent rows. It also introduces a crucial exception: preserving the first horizontal line encountered below the top three rows.  However, the code fails in Example 1 and Example 3 because it stops processing further rows *after* encountering the first horizontal line. It needs to blank all rows *below* that preserved horizontal line. Example 2 works correctly only because there are no other rows below the identified horizontal line. The core issue is the premature termination of the blanking process after finding a horizontal line. We need to blank all rows *after* the horizontal line is copied.

**Strategy:**

1.  **Refine Horizontal Line Detection:** The `is_horizontal_line` function is correct and should be kept.
2.  **Modify Blanking Logic:** Instead of stopping the loop after copying the horizontal line, the loop should continue, but *all* subsequent rows should be set to 0. The `found_horizontal_line` flag controls when the blanking starts.

**Metrics and Observations (YAML):**

```yaml
examples:
  - id: 1
    input_shape: [11, 12]
    output_shape: [11, 12]
    match: False
    pixels_off: 4
    notes: >
      The code failed to blank the rows *after* the horizontal line. The 4
      pixels that don't match are due to keeping rows that should be blanked
      (specifically, the yellow and black pixels in rows 8-10. Row 3 is
      correctly kept, and all subsequent rows are incorrectly kept)
    objects:
      - type: horizontal_line
        color: yellow
        row_index: 2
      - type: horizontal_line
        color: red
        row_index: 6
      - type: horizontal_line_like
        color: yellow
        row_index: 8
      - type: horizontal_line_like
        color: yellow
        row_index: 9
      - type: horizontal_line_like
        color: yellow
        row_index: 10

  - id: 2
    input_shape: [10, 16]
    output_shape: [10, 16]
    match: True
    pixels_off: 0
    notes: >
      The code works correctly because the horizontal line is followed only by
      rows that are already blank (or should remain blank).
    objects:
      - type: horizontal_line
        color: green
        row_index: 2

  - id: 3
    input_shape: [9, 16]
    output_shape: [9, 16]
    match: False
    pixels_off: 8
    notes: >
      The horizontal line at row 3 is preserved correctly, but rows after it are not blanked.
      The pixels on row 4 that should be blanked are not.
    objects:
      - type: horizontal_line
        color: grey
        row_index: 3

```

**Natural Language Program:**

1.  **Copy Top Rows:** Copy the first three rows (rows 0, 1, and 2) of the input grid to the output grid without modification.
2.  **Find Horizontal Line:** Starting from row 3, search for the first horizontal line. A horizontal line is defined as a row where all pixels have the same non-zero color.
3.  **Preserve Horizontal Line (if found):** If a horizontal line is found, copy that entire row from the input grid to the corresponding row in the output grid.
4.  **Blank Subsequent Rows:**  All rows *below* the first three rows, are set to 0 (white).
5. **Blank Rows After Horizontal Line (if present)**: All rows below the copied horizontal line are set to all 0 (white).

