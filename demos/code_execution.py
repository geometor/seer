from rich import print
from rich.markdown import Markdown

import os
import google.generativeai as genai

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
    dir(part)
    if part.executable_code:
        with open("code.py", "w") as f:
            f.write(part.executable_code.code)
        print("Code saved to extracted_code.py")
