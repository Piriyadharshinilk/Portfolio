import re

html_file = "index.html"
css_file = "templatemo-nexaverse.css"

with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

nav_html = """
        <!-- Top Navigation Bar -->
        <nav class="top-nav">
            <div class="nav-brand">
                <a href="#introduction">&lt;/&gt; Piriyadharshini.dev</a>
            </div>
            <ul class="nav-links">
                <li><a href="#introduction">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#services">Skills</a></li>
                <li><a href="#testimonials">Certifications</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
"""

# Insert Nav right after <div class="container">
if '<nav class="top-nav">' not in html:
    html = html.replace('    <div class="container">', '    <div class="container">\n' + nav_html)

# Update Footer with Social Links
footer_find = '<footer class="footer" id="mainFooter">'
social_html = """
        <div class="social-links">
            <a href="https://github.com/Piriyadharshinilk" target="_blank" class="social-icon">
                <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
            </a>
            <a href="https://www.linkedin.com/in/piriyadharshini-l-k-2b8074315/" target="_blank" class="social-icon">
                <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
            </a>
        </div>
"""

if 'class="social-links"' not in html:
    html = html.replace(footer_find, footer_find + "\n" + social_html)

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html)


css_append = """
/* Top Navigation Bar */
.top-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 25px 50px;
    background: transparent;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    margin-bottom: 40px;
}

.nav-brand a {
    font-family: 'Syne', sans-serif;
    font-size: 24px;
    font-weight: 700;
    color: #fff;
    text-decoration: none;
    letter-spacing: 1px;
}

.nav-brand a:hover {
    color: var(--primary);
}

.nav-links {
    list-style: none;
    display: flex;
    gap: 30px;
    margin: 0;
    padding: 0;
}

.nav-links a {
    color: #a0a0a0;
    text-decoration: none;
    font-size: 15px;
    font-weight: 500;
    letter-spacing: 1px;
    transition: all 0.3s ease;
}

.nav-links a:hover {
    color: #fff;
    text-shadow: 0 0 10px var(--primary);
}

/* Social Links Footer */
.social-links {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-bottom: 20px;
}

.social-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 45px;
    height: 45px;
    border-radius: 50%;
    background: rgba(255,255,255,0.05);
    color: #a0a0a0;
    transition: all 0.3s ease;
    border: 1px solid rgba(255,255,255,0.1);
}

.social-icon:hover {
    background: rgba(176, 38, 255, 0.2);
    color: var(--primary);
    border-color: var(--primary);
    transform: translateY(-3px);
    box-shadow: 0 5px 15px rgba(176, 38, 255, 0.3);
}

.social-icon svg {
    width: 20px;
    height: 20px;
}
"""

with open(css_file, "a", encoding="utf-8") as f:
    f.write(css_append)

print("Navigation and social links injected successfully.")
