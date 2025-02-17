from rich import print
from rich.markdown import Markdown

import os
import google.generativeai as genai

import ast
import contextlib
import io

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-pro-exp-02-05",
  generation_config=generation_config,
  system_instruction="you are a python expert",
  tools='code_execution',
)

def process_executable_code(code_to_execute):
    """Processes the executable code extracted from the response.

    Parses the code, executes it in a controlled namespace,
    finds and calls defined functions, and captures output.
    """
    with open("code.py", "w") as f:
        f.write(code_to_execute)
    print("Code saved to code.py")

    # Parse the code using ast
    tree = ast.parse(code_to_execute)

    # Create a dictionary to serve as the namespace for execution
    namespace = {}

    # Capture stdout
    output_capture = io.StringIO()
    with contextlib.redirect_stdout(output_capture):
        # Execute the code within the namespace
        exec(compile(tree, filename="code.py", mode="exec"), namespace)

    # Find and call functions
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            function_name = node.name
            print(f"Calling function: {function_name}")
            if function_name in namespace:
                # Call the function (you might need to adapt this based on expected arguments)
                if function_name == 'is_prime':  # Example: specific to the expected output
                    result = namespace[function_name](10)  # Assuming a function named 'is_prime' that takes an argument
                    print(f"Result of {function_name}: {result}")
                else:
                    print(f"  Warning: Function '{function_name}' found, but not called (no specific handling).")

            else:
                print(f"  Error: Function '{function_name}' definition found, but not present in the execution namespace.")

    # Print captured output
    captured_output = output_capture.getvalue()
    if captured_output:
        print(f"Captured output:\n{captured_output}")


if __name__ == '__main__':
    response = model.generate_content(
      contents=[
            "using code_execution:\ncreate a full python module to find the first 10 prime numbers to \n\nonly respond with the code_execution\n",
      ]
    )


    print(response.candidates[0].content.parts)
    print("\n---\n")
    print(Markdown(response.text))

    # Extract and save the code
    for part in response.candidates[0].content.parts:
        if part.executable_code:
            process_executable_code(part.executable_code.code)
