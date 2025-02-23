import numpy as np

# Define the training examples (input and expected output)
training_examples = [
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
    },
]

results = []
for i, example in enumerate(training_examples):

    rows = example["input"].shape[0]
    middle_row_index = rows // 2
    first_row_value = example["expected"][0,0]

    expected_above = []
    expected_below = []

    if rows % 2 != 0:
        if first_row_value == 0:
            expected_above = [0] * middle_row_index
            expected_below = [5] * (rows - middle_row_index)
        elif first_row_value == 5:
            expected_above = [5] * middle_row_index
            expected_below = [0] * (rows - middle_row_index)
    else:
        expected_above = [0] * rows
        expected_below = [] #even

    results.append({
        "example_number": i + 1,
        "rows": rows,
        "middle_row_index": middle_row_index,
        "first_row_value": first_row_value,
        "expected_above":expected_above,
        "expected_below":expected_below
    })
print (results)