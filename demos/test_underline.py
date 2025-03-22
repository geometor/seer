from rich.console import Console

console = Console()

# Method 1: Using style in console.print()
console.print("This text is underlined.", style="underline")

# Method 2: Using style in Text class
from rich.text import Text
text = Text("This text is also underlined.")
text.stylize("underline")
console.print(text)

# Method 3: Combining styles
console.print("This is bold and underlined.", style="bold underline")

# Method 4: Doubly underlined
console.print(" " * 5 , style="black on red underline")
console.print(" " * 5 , style="black on red underline")
