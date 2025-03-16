"""
old display code using rich controls
"""

    #  def _format_banner(self, step_index: int, description: str) -> str:
    #  """Helper function to format the banner."""
    #  task_folder = self.step_dir.parent.name
    #  return f"# {task_folder} • {step_index} • {description}\n"

    #  def display_prompt(
        #  self, prompt: list, instructions: list, prompt_count: int, description: str
    #  ):
        #  """Displays the prompt and instructions using rich.markdown.Markdown."""
        #  banner = self._format_banner(prompt_count, description)  
        #  markdown_text = f"\n{banner}\n\n"  
        #  for part in prompt:
            #  markdown_text += str(part) + "\n"

        #  for part in instructions:
            #  markdown_text += str(part) + "\n"

        #  markdown = Markdown(markdown_text)
        #  print()
        #  print(markdown)

    #  def display_response(
        #  self,
        #  response_parts: list,
        #  prompt_count: int,
        #  description: str,
        #  respdict: dict,
        #  elapsed_time: float,
    #  ):
        #  """Displays the response using rich.markdown.Markdown."""
        #  banner = self._format_banner(prompt_count, description)  
        #  markdown_text = f"\n## RESPONSE\n\n"  

        #  for part in response_parts:
            #  markdown_text += str(part) + "\n"

        #  usage = respdict.get("usage_metadata", {})
        #  if usage:
            #  markdown_text += "\n---\n\n**Usage Meta**\n\n```json\n"
            #  markdown_text += json.dumps(usage, indent=2)
            #  markdown_text += "\n```\n"

        #  timing = respdict.get("timing", {})
        #  if timing:
            #  markdown_text += "\n**Timing Meta**\n\n```json\n"
            #  markdown_text += json.dumps(timing, indent=2)
            #  markdown_text += "\n```\n"
        #  markdown_text += f"\n**Total Elapsed Time:** {elapsed_time:.4f} seconds\n"

        #  markdown = Markdown(markdown_text)
        #  print()
        #  print(markdown)

    #  def display_config(self):
        #  """Displays the configuration information using rich.markdown.Markdown."""
        #  markdown_text = f"# {self.timestamp}\n\n"
        #  markdown_text += f"```yaml\n{json.dumps(self.config, indent=2)}\n```\n"
        #  markdown = Markdown(markdown_text)
        #  print()
        #  print(markdown)

    #  def display_test_results(self, test_results_str: str, prompt_count: int):
        #  """
        #  Displays the test results.
        #  """
        #  description = "Test Results"
        #  banner = self._format_banner(prompt_count, description)
        #  markdown_text = f"\n{banner}\n\n"
        #  markdown_text += test_results_str

        #  markdown = Markdown(markdown_text)
        #  print()
        #  print(markdown)



