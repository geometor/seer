example_prompt = """
**example_{{ example_num }}**

**input**
{{ input_grid }}

**output**
{{ output_grid }}

images:

"""

example_instructions = """
above is a pair of example input and output grids 

- document your initial observations and impressions. 
  begin with a verbal description of your perception of the elements of the grids - objects, colors, relationships, and if possible, the transformation rule
- use `code_execution` to examine the grid information and verify the
  assumptions about size, colors, objects, and transformations. 

- focus your analysis on aspects like:

    - Counting the occurrences of each color.
    - How to identify the coordinates of pixels that have changed color or position.
    - Determining if the dimensions of the grid have changed.
    - Analyzing the count, size, shape, and relative positions of objects (contiguous
      blocks of the same color).

- the code you use in code_execution may not be carried forward on following prompts, be
  sure to have the code print your findings in the output
- use what you learn to develop a natural language program of the
  transformation rule.
- review your findings and try to determine the natural language description of
  the transformation rule. How does the information captured in the YAML block
  inform your understanding of the transformation?

use a yaml block to capture details (examples):

```yaml
input:
  width: X
  height: Y
  colors:
    - N: (count)
  objects:
    - size, position and color - desc
```

```yaml
differences:
  cells_changed: N
  colors_changed: desc
  transformation:
    - speculate on transformation rules
```

final step - provide a thorough natural language program
to tell another intelligent entity how to transform the input grid into the
output grid

You will examine and analyze the example grids

For each example pair, your goal is to derive a natural language description of
the transformation rule that explains how the input is changed to produce the
output. This "natural language program" should describe the steps or logic
involved in the transformation. 

the natural language program should be sufficient for an intelligent agent to
perform the operation of generating an output grid from the input, without the
benefit of seeing the examples. So be sure that the provide 

- context for understanding the input grid (objects, organization and important colors)
  particularly context for how to identify the 'objects'
- process for initializing the output grid (copy from input or set size and
  fill)
- describe the color palette to be used in the output
- describe how to determine which pixels should change in the output

For example, it might state: 

- copy input to working output
- identify sets of pixels in blue (1) rectangles in working grid
- identify to largest rectangle
- set the largest rectangle's pixels to red (2)

But remember - any information that describe the story of the transformations is
desired. Be flexible and creative. 

"""

examples_summary_prompt = """
**examples summary**
"""

examples_summary_instructions = """
This is your chance to review what you have learned from the examples

- summarize your observations to explain the transformation of the input to output
- use code_execution to re-investigate properties, patterns and differences in the grids to confirm your predictions
- generate your final step by step natural language program

Consider the following in this phase:

- **Confidence Assessment:** How confident are you in your derived transformation rule?
- **Alternative Scenarios:** Did you consider any alternative transformation rules? If so, why did you choose the current one?
- **Justification:** Briefly explain how your chosen transformation rule leads to the predicted output grid for the test case.

## Ruminate Phase
During this phase, you should review all examples presented and your findings
and do your best to validate your natural language program.

consider what you have learned from all the examples provided. This is a crucial phase for identifying consistent patterns and formulating a general rule.

Your primary objective is to review the natural language program you've
developed

Actively compare the findings from the analysis of each example pair. Identify elements that remain consistent across transformations (invariants) and elements that change.

Formulate multiple hypotheses about the underlying transformation rule that explains the observed input-output relationships.

Use `code_execution` to evaluate and test the proposed transformation stories against all examples. Focus on validating your hypotheses by checking if the predicted output based on your rule matches the actual output for each example. Consider these aspects in your validation:

- Does the rule apply consistently across all examples?
- Are there any exceptions or inconsistencies?
- Can the rule be generalized or does it need to be more specific?

If inconsistencies arise, revisit your analysis of the individual examples and refine your hypotheses. The process of understanding the transformation rule is iterative.

Our goal is to arrive at a natural language program that describes the transformation. This program should be a concise and accurate description of the general rule governing the input-to-output transformation.
"""

test_input_prompt = """
**test**

**input**
{{ input_grid }}

**observations**
"""

test_input_instructions = """
using the knowledge you have gathered from the previous examples
and the step by step natural language program
we want to build the test output grid

- initial the output grid
  copy input grid or set size
- set pixels in the output grid as described in the program
- use code_execution to validate the output - correct configuration of objects
  and attributes
- make final adjustments
  review properties of this grid and compare with examples, 
  paying attention to similarities and differences in size, colors, and object arrangements.
- submit final output grid

"""


init_working_grid_instructions  = """
use function_call to initialize the working output grid:

- initialize_output_from_input: good when examples show few differences between
  input and output
- initialize_output_by_size: create a fresh grid from size and color
"""

show_working_grid_prompt = """
**review working grid{{ example_num }}**

**input**
{{ input_grid }}

**output**
{{ output_grid }}

**observations**
"""

show_working_grid_instructions = """
- take a moment to review that the changes in the working output grid are in keeping with the rule
- use code_execution to investigate properties
"""

next_action_instructions = """
in this task you will make a function call 
to set pixels on the grid to achieve the solution

after you update the grid you will be presented with a copy to review

- set_pixel: update one pixel at a time
- set_range: update a rectangular subset of pixel
- set_floodfill: update a contiguous region with a new color
- submit: when the working grid meets your criteria call submit to check you solution

please call only one function per round so you can review the working grid
"""

