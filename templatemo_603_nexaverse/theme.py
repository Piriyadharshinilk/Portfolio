import os

css_file = "templatemo-nexaverse.css"
html_file = "index.html"

# Update CSS
with open(css_file, "r", encoding="utf-8") as f:
    css = f.read()

replacements = {
    "--primary: #00f0ff;": "--primary: #ff0000;",
    "--secondary: #ff00d4;": "--secondary: #aa0000;",
    "--accent: #9d4edd;": "--accent: #df0000;",
    "--dark-1: #0a0a12;": "--dark-1: #080000;",
    "--dark-2: #12121f;": "--dark-2: #100000;",
    "--dark-3: #1a1a2e;": "--dark-3: #150000;",
    "--glow-cyan: rgba(0, 240, 255, 0.4);": "--glow-cyan: rgba(255, 0, 0, 0.4);",
    "--glow-magenta: rgba(255, 0, 212, 0.4);": "--glow-magenta: rgba(170, 0, 0, 0.4);",
    "rgba(0, 240, 255": "rgba(255, 0, 0",
    "rgba(255, 0, 212": "rgba(170, 0, 0",
    "rgba(157, 78, 221": "rgba(223, 0, 0",
    "rgba(0, 200, 220": "rgba(200, 0, 0"
}

for old, new in replacements.items():
    css = css.replace(old, new)

with open(css_file, "w", encoding="utf-8") as f:
    f.write(css)

# Update HTML
with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace('stop-color:#00f0ff', 'stop-color:#ff0000')
html = html.replace('stop-color:#ff00d4', 'stop-color:#aa0000')

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html)

print("Theme updated successfully.")
