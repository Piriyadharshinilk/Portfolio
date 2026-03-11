import os

css_file = "templatemo-nexaverse.css"
html_file = "index.html"

# Update CSS
with open(css_file, "r", encoding="utf-8") as f:
    css = f.read()

replacements = {
    "--primary: #ff0000;": "--primary: #b026ff;",
    "--secondary: #aa0000;": "--secondary: #6e00ff;",
    "--accent: #df0000;": "--accent: #d000ff;",
    "--dark-1: #080000;": "--dark-1: #0a0512;",
    "--dark-2: #100000;": "--dark-2: #120a1f;",
    "--dark-3: #150000;": "--dark-3: #1a0f2e;",
    "--glow-cyan: rgba(255, 0, 0, 0.4);": "--glow-cyan: rgba(176, 38, 255, 0.4);",
    "--glow-magenta: rgba(170, 0, 0, 0.4);": "--glow-magenta: rgba(110, 0, 255, 0.4);",
    "rgba(255, 0, 0": "rgba(176, 38, 255",
    "rgba(170, 0, 0": "rgba(110, 0, 255",
    "rgba(223, 0, 0": "rgba(208, 0, 255",
    "rgba(200, 0, 0": "rgba(150, 0, 255"
}

for old, new in replacements.items():
    css = css.replace(old, new)

with open(css_file, "w", encoding="utf-8") as f:
    f.write(css)

# Update HTML
with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace('stop-color:#ff0000', 'stop-color:#b026ff')
html = html.replace('stop-color:#aa0000', 'stop-color:#6e00ff')

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html)

print("Theme updated to Purple/Black successfully.")
