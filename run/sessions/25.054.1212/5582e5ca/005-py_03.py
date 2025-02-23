import numpy as np

def analyze_example(input_str, output_str):
    input_grid = np.array([list(map(int, row.split())) for row in input_str.split('\n')])
    output_grid = np.array([list(map(int, row.split())) for row in output_str.split('\n')])

    input_height, input_width = input_grid.shape
    output_height, output_width = output_grid.shape
    
    input_colors = np.unique(input_grid)
    output_colors = np.unique(output_grid)

    metrics = {
        'input_dims': (input_height, input_width),
        'output_dims': (output_height, output_width),
        'input_colors': input_colors.tolist(),
        'output_colors': output_colors.tolist(),
        'top_left_input': input_grid[0,0].item()
    }
    return metrics

# Example data from the prompt
examples = [
    {
        "input": "4 4 8\n6 4 3\n6 3 0",
        "output": "4 4 4\n4 4 4\n4 4 4"
    },
    {
        "input": "6 8 9\n1 8 1\n9 4 9",
        "output": "9 9 9\n9 9 9\n9 9 9"
    },
    {
        "input": "4 6 9\n6 4 1\n8 8 6",
        "output": "6 6 6\n6 6 6\n6 6 6"
    }
]

for i, example in enumerate(examples):
  metrics = analyze_example(example['input'], example['output'])
  print(f"Example {i+1} Metrics:")
  print(metrics)