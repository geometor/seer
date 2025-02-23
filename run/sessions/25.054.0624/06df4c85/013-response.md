# 06df4c85 • 013 • example_3 • investigate_dreamer

---
Okay, here's my analysis of the provided input-output example pair:

**Perception of Elements:**

The input and output grids consist of colored pixels (represented by numbers 0-9). The dominant colors are yellow (4), white (0), green (3), and red (2).  There are distinct horizontal bands of solid yellow (4) pixels. Within these yellow bands are "islands" of other colors, primarily green (3) and red (2), that seem to be undergoing some kind of transformation.

**YAML Block - Facts:**



```yaml
objects:
  - type: grid
    properties:
      dimensions: 23x23
      colors: [0, 2, 3, 4] # white, red, green, yellow
  - type: horizontal_band
    properties:
      color: 4 # yellow
      height: 3
  - type: island
    properties:
      colors: [2, 3] #red, green
      shape: rectangular
      size: 2x2
      location: within horizontal_band
actions:
  - type: color_propagation
    description: Green and Red islands expand within their horizontal band.
    constraints:
        - propagation_direction: horizontal
        - stays_within_yellow_band: true
        - color-specific behavior:
```



**Natural Language Program:**

1.  **Identify Horizontal Bands:** Locate the horizontal bands of solid yellow (4) pixels. These bands are three pixels high.

2.  **Identify Islands:** Within each yellow band, identify "islands" of green (3) and red (2) pixels. These islands are 2x2 blocks.

3.  **Propagate Colors (Conditional):**
    *   If an island is green (3): Expand the green color horizontally to the left and right *within* the yellow band. The expansion fills the entire width of the yellow band, replacing any white (0) pixels, only if there is an existing green island withing the yellow row.
    *   If an island is red (2): Expand the red color horizontally to the left and right *within* the yellow band, in place of white pixels (0), only if there is an existing red island. Furthermore, if the row immediately above has green, do not replace yellow with red.

4.  **No Change Outside Bands:** Pixels outside the identified yellow bands remain unchanged.
The rows that don't contain any Green or Red colored pixels are not affected.

