"""
prompt utils
"""
def get_pair_prompt(title, task_pair, include_images=True):
    prompt = [
        f"\n## {title}\n",
    ]
    for key, grid in task_pair.items():
        prompt += [
            f"\n**{key}:**\n```\n",
            grid.to_string(),
            "\n```\n\n",
        ]
        if include_images:
            prompt.append(grid.to_image())
            prompt.append("\n")

    return prompt

