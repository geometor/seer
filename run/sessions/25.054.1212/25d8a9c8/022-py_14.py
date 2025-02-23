import numpy as np

def report_grid(grid, name):
    report = f"{name}:\n"
    report += str(grid) + '\n'
    report += f'shape: {grid.shape}\n'
    unique, counts = np.unique(grid, return_counts=True)
    report += f'pixel counts: {dict(zip(unique, counts))}\n'
    return report

# Example data (from the prompt)
examples = [
    {
        "input": np.array([[4, 4, 4], [2, 3, 2], [2, 3, 3]]),
        "expected": np.array([[5, 5, 5], [0, 0, 0], [0, 0, 0]]),
    },
     {
        "input": np.array([[7, 3, 3], [6, 6, 6], [3, 7, 7]]),
        "expected": np.array([[0, 0, 0], [5, 5, 5], [0, 0, 0]]),
    },
    {
        "input": np.array([[2, 9, 2], [4, 4, 4], [9, 9, 9]]),
        "expected": np.array([[0, 0, 0], [5, 5, 5], [5, 5, 5]]),
    },
    {
        "input": np.array([[2, 2, 4], [2, 2, 4], [1, 1, 1]]),
        "expected": np.array([[0, 0, 0], [0, 0, 0], [5, 5, 5]]),
    }
]

reports = []
for i, example in enumerate(examples):
  reports.append(f'Example {i+1}:')
  reports.append(report_grid(example['input'], 'Input'))
  reports.append(report_grid(example['expected'], 'Expected Output'))
  reports.append("-----")

for report in reports:
    print(report)