import re

html_file = "index.html"
css_file = "templatemo-nexaverse.css"

with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove the menu grid
html = re.sub(r'<!-- Menu Grid -->.*?<!-- Content Sections -->', '<!-- Content Sections -->', html, flags=re.DOTALL)

# 2. Remove all back buttons
html = re.sub(r'<button class="back-btn" onclick="backToMenu\(\)">← Back to Menu</button>', '', html)

# 3. Use string splitting to safely get each section
sections = {
    "introduction": "",
    "about": "",
    "services": "",
    "testimonials": "",
    "contact": ""
}

for sec_id in sections.keys():
    start = html.find(f'<div class="content-section" id="{sec_id}">')
    if start == -1: 
        print(f"Could not find {sec_id}")
        continue
    
    # find the next section or the footer
    next_tags = ['<!-- Introduction Section -->', '<!-- Services Section -->', '<!-- Gallery Section -->', 
                 '<!-- Testimonials Section -->', '<!-- About Section -->', '<!-- Contact Section -->', '<!-- Footer -->']
    
    end = len(html)
    for tag in next_tags:
        idx = html.find(tag, start + 10)
        if idx != -1 and idx < end:
            end = idx
            
    sections[sec_id] = html[start:end]


# We want intro -> about -> skills(services) -> certs(testimonials) -> contact
new_content_area = (
    '<div id="contentArea">\n' +
    sections["introduction"] + '\n' +
    sections["about"] + '\n' +
    sections["services"] + '\n' +
    sections["testimonials"] + '\n' +
    sections["contact"] + '\n' +
    '        <!-- Footer -->'
)

# replace the old content area through footer
start_content = html.find('<div id="contentArea">')
end_footer = html.find('<!-- Footer -->')
if start_content != -1 and end_footer != -1:
    html = html[:start_content] + new_content_area + html[end_footer + 15:]
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html)
    print("Replaced HTML successfully.")
else:
    print("Error replacing HTML block")


# Update CSS to allow scrolling and show all sections
with open(css_file, "r", encoding="utf-8") as f:
    css = f.read()

# Make content-section display block and remove opacity/animation 
if "display: none;" in css and "opacity: 0;" in css:
    css = css.replace("display: none;\n\topacity: 0;", "display: block;\n\topacity: 1;\n\tmargin-bottom: 50px;")
    with open(css_file, "w", encoding="utf-8") as f:
        f.write(css)
    print("Updated CSS successfully.")
else:
    print("Could not find CSS display toggle.")
