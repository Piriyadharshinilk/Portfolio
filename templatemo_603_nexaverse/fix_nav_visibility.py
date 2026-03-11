import re

html_file = "index.html"
css_file = "templatemo-nexaverse.css"

with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

# Remove all section-header-small blocks
# They start with <div class="section-header-small"> and end with </div> (nested)
# Since they are consistent, let's target the pattern or use a simpler approach.
# They usually contain the SVG and the PIRIYADHARSHINI name.

def remove_section_headers(content):
    # This is a bit aggressive but these blocks are very consistent
    cleaned = re.sub(r'<div class="section-header-small">.*?</div>\s*</div>\s*</div>', '', content, flags=re.DOTALL)
    # Wait, the closing divs might vary. Let's be more precise.
    return cleaned

# Let's try to remove each block manually to be safe or use a better regex
# Each header looks like this:
# <div class="section-header-small">
#   ... many lines ...
#   <div class="small-brand">
#     <h3>PIRIYADHARSHINI</h3>
#     <p>Digital Excellence</p>
#   </div>
# </div>

# Simpler: Replace the whole block including its container div if appropriate.
# Actually, the section-header-small is usually at the start of the content-section.

# Let's use a regex that matches the start of the div until its matching end.
# Since I know the structure, I'll look for the specific content.

# Re-checking the view_file from earlier
# 56:                 <div class="section-header-small">
# ...
# 74:                 </div>

# I'll just remove them using multi_replace or a script.
# Let's use a script to find and remove them.

pattern = r'<div class="section-header-small">[\s\S]*?Digital Excellence</p>\s*</div>\s*</div>'
html = re.sub(pattern, '', html)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html)


# Update CSS to make Top Nav Fixed
with open(css_file, "r", encoding="utf-8") as f:
    css = f.read()

css_update = """
/* Top Navigation Bar - FIXED */
.top-nav {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 50px;
    background: rgba(10, 10, 10, 0.8);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    z-index: 1000;
    transition: all 0.3s ease;
}

.container {
    padding-top: 100px !important; /* Spacing for fixed nav */
}
"""

# Replace the previous .top-nav definition or append
# I'll replace the previous one to avoid duplicates
old_nav_pattern = r'/\* Top Navigation Bar \*/\s*\.top-nav \{[\s\S]*?margin-bottom: 40px;\s*\}'
if re.search(old_nav_pattern, css):
    css = re.sub(old_nav_pattern, css_update, css)
else:
    css += css_update

with open(css_file, "w", encoding="utf-8") as f:
    f.write(css)

print("Fixed navigation and removed redundant headers.")
