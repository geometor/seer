# 1-3aa6fb7a • 003 • example_2 - NLP

---
Okay, let's analyze the transformation between the input and output grids in this second example.

**YAML Description of Observations**

```yaml
input_grid:
  objects:
    - color: 8 (azure)
      shape: L-shape (composed of 3 cells)
      position: (0,4) # Top-left cell of the object
    - color: 8 (azure)
      shape: L-shape (composed of 3 cells)
      position: (2,2) # Top-left cell of the object
    - color: 8 (azure)
      shape: L-shape (composed of 3 cells)
      position: (5,3)
  background:
    color: 0 (white)

output_grid:
 objects:
    - color: 8 (azure)
      shape: L-shape (composed of 3 cells)
      position: (0,4) # Top-left cell of the object
    - color: 1 (blue)
      shape: single cell
      position: (1,4)
    - color: 8 (azure)
      shape: L-shape (composed of 3 cells)
      position: (2,2) # Top-left cell of the object
    - color: 1 (blue)
      shape: single cell
      position: (2,3)
       - color: 8 (azure)
      shape: L-shape (composed of 3 cells)
      position: (5,3)
    - color: 1 (blue)
      shape: single cell
      position: (5,3)
  background:
    color: 0 (white)
```

**Natural Language Program: Step-by-Step Transformation**

1.  **Identify Objects:** In the input grid, we can identify three distinct L-shaped objects of color 8 (azure).

2.  **Detect Change:** One cell of color 1 (blue) has been added. The position is connected to the top right side, to each of the L-shaped object of the input.

3. **Transformation Rule:** It fills with color 1 the cell at north-east position, considering the most western cell of each azure shape.

