# 1-3aa6fb7a • 001 • example_1 - NLP

---
Okay, let's analyze the transformation between the input and output grids.

**Observations**

First, let's describe the input and output grids in terms of objects and their properties:

**Input Grid:**

*   There are two azure (8) colored objects.
*   The first object is an L-shape composed of three cells in the top-left.
*    The second object is an inverted-L shape composed of three cells in the bottom right.

**Output Grid:**

*   There are two azure (8) colored objects (same as input).
*    There are two new single-celled blue (1) object appearing "inside" the original azure objects, one on the left branch of each L.

**Transformation Rule (Natural Language Program)**

Here's a step-by-step description of the transformation:

1.  **Identify Azure Objects:** Locate all azure (8) colored objects in the input grid.

2.  **Analyze Shape:** For each azure object, check their shape. In this case they all form either L or inverted L.

3.  **Insert Blue Pixel:** For an azure object, select its leftmost vertical segment. Add a blue pixel (1) to the right of that segment.

**Summary of differences**

The transformation rule places a blue pixel beside the left side of each azure L.

