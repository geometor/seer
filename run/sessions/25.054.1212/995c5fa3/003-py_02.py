import numpy as np

def analyze_results(input_grid, expected_output, transformed_output):
    input_grid = np.array(input_grid)
    expected_output = np.array(expected_output)
    transformed_output = np.array(transformed_output)

    print(f"Input shape: {input_grid.shape}")
    print(f"Expected output shape: {expected_output.shape}")
    print(f"Transformed output shape: {transformed_output.shape}")

    match = np.array_equal(expected_output, transformed_output)
    print(f"Match: {match}")

    if not match:
        pixels_off = np.sum(expected_output != transformed_output)
        print(f"Pixels off: {pixels_off}")

        unique_expected, counts_expected = np.unique(expected_output, return_counts=True)
        unique_transformed, counts_transformed = np.unique(transformed_output, return_counts=True)

        print("Expected Pixel Counts:", dict(zip(unique_expected, counts_expected)))
        print("Transformed Pixel Counts:", dict(zip(unique_transformed, counts_transformed)))

# Example Data (replace with actual data from each example)
examples = [
    {
      "input": [
            [5, 5, 5, 5, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5],
            [5, 5, 5, 5, 0, 5, 0, 0, 5, 0, 0, 5, 5, 0],
            [5, 5, 5, 5, 0, 5, 0, 0, 5, 0, 0, 5, 5, 0],
            [5, 5, 5, 5, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5]
      ],
      "expected": [
            [2, 2, 2],
            [8, 8, 8],
            [3, 3, 3]
      ],
      "transformed": [
        [0, 8, 8],
        [0, 8, 8],
        [0, 0, 0]
      ]
    },
     {
      "input": [
            [5, 5, 5, 5, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5],
            [0, 5, 5, 0, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5],
            [0, 5, 5, 0, 0, 5, 0, 0, 5, 0, 5, 5, 5, 5],
            [5, 5, 5, 5, 0, 5, 0, 0, 5, 0, 5, 5, 5, 5]
      ],
      "expected": [
            [3, 3, 3],
            [4, 4, 4],
            [2, 2, 2]
      ],
      "transformed":[
            [8, 8, 0],
            [8, 8, 0],
            [0, 0, 0]
          ]

    },
    {
      "input":[
            [5, 5, 5, 5, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5],
            [5, 0, 0, 5, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5],
            [5, 0, 0, 5, 0, 5, 5, 5, 5, 0, 5, 0, 0, 5],
            [5, 5, 5, 5, 0, 5, 5, 5, 5, 0, 5, 0, 0, 5]
      ],
      "expected":[
            [8, 8, 8],
            [2, 2, 2],
            [4, 4, 4]
      ],
       "transformed":[
            [8, 8, 0],
            [0, 8, 8],
            [0, 0, 0]
        ]
    },
    {
        "input": [
            [5, 5, 5, 5, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5],
            [5, 5, 5, 5, 0, 5, 5, 5, 5, 0, 5, 5, 5, 5],
            [5, 5, 5, 5, 0, 5, 0, 0, 5, 0, 5, 5, 5, 5],
            [5, 5, 5, 5, 0, 5, 0, 0, 5, 0, 5, 5, 5, 5]
        ],
        "expected":[
            [2, 2, 2],
            [4, 4, 4],
            [2, 2, 2]
          ],
        "transformed":[
            [0, 8, 8],
            [0, 0, 0],
            [0, 0, 0]
      ]
    }

]

for i, example in enumerate(examples):
    print(f"\n--- Example {i + 1} ---")
    analyze_results(example["input"], example["expected"], example["transformed"])