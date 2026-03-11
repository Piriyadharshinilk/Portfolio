import os

html_file = "index.html"

with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

# Replace the literal characters "\n\n" that were written by mistake
html = html.replace("\\n\\n", "\n\n")

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html)

print("Removed literal \\n\\n")
