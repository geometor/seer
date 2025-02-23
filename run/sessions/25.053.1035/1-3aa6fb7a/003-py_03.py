input_str = """
0 0 0 0 8 8 0
0 0 0 0 0 8 0
0 0 8 0 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 0 8 0 0
0 0 0 8 8 0 0
"""
expected_str = """
0 0 0 0 8 8 0
0 0 0 0 1 8 0
0 0 8 1 0 0 0
0 0 8 8 0 0 0
0 0 0 0 0 0 0
0 0 0 1 8 0 0
0 0 0 8 8 0 0
"""
transformed_str = """
0 0 0 0 1 8 0
0 0 0 0 0 1 0
0 0 1 0 0 0 0
0 0 1 8 0 0 0
0 0 0 0 0 0 0
0 0 0 0 1 0 0
0 0 0 1 8 0 0
"""

report = calculate_metrics(input_str, expected_str, transformed_str)
print(report)