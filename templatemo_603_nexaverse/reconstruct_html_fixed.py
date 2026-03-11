import re
import os

html_file = "index.html"

# 1. Read Current HTML
with open(html_file, "r", encoding="utf-8") as f:
    current_html = f.read()

# 2. Extract Intro & About
curr_idx = current_html.find('id="about"')
about_end_pattern = r'            </div>\s*</div>\s*</div>'
about_search_area = current_html[curr_idx:]
about_end_match = re.search(about_end_pattern, about_search_area)

if about_end_match:
    intro_about_content = current_html[:curr_idx + about_end_match.end()]
else:
    # Fallback splitting
    intro_about_content = current_html.split('<div class="content-section" id="services">')[0]

# 3. Define Missing Sections
skills_html = """
        <div class="content-section" id="services">
            <div class="section-header">
                <h2 class="section-title">Technical Skills</h2>
                <p class="section-subtitle">Core competencies and technical proficiencies</p>
            </div>

            <div class="skills-grid">
                <div class="skill-card">
                    <div class="skill-icon"><span style="font-size: 2rem;">🌐</span></div>
                    <h4>Networking</h4>
                    <span class="skill-badge intermediate">Intermediate</span>
                </div>
                <div class="skill-card">
                    <div class="skill-icon"><span style="font-size: 2rem;">🐧</span></div>
                    <h4>Linux</h4>
                    <span class="skill-badge beginner">Beginner</span>
                </div>
                <div class="skill-card">
                    <div class="skill-icon"><span style="font-size: 2rem;">🐍</span></div>
                    <h4>Python</h4>
                    <span class="skill-badge advanced">Advanced</span>
                </div>
                <div class="skill-card">
                    <div class="skill-icon"><span style="font-size: 2rem;">💻</span></div>
                    <h4>Web Technologies</h4>
                    <span class="skill-badge basics">Basics</span>
                </div>
                <div class="skill-card">
                    <div class="skill-icon"><span style="font-size: 2rem;">☕</span></div>
                    <h4>Java</h4>
                    <span class="skill-badge intermediate">Intermediate</span>
                </div>
            </div>
        </div>
"""

certs_html = """
        <div class="content-section" id="testimonials">
            <div class="section-header">
                <h2 class="section-title">Certifications & Events</h2>
                <p class="section-subtitle">Professional credentials, workshops, and skill validations</p>
            </div>

            <div class="cert-grid">
                <div class="cert-card">
                    <div class="cert-icon-wrap oracle"><span class="cert-icon">☁️</span></div>
                    <div class="cert-content">
                        <div class="cert-meta"><span class="cert-org">Oracle University</span><span class="cert-date">Valid: Nov 2025 - Nov 2027</span></div>
                        <h4 class="cert-title">Oracle Cloud Infrastructure - Data Science Professional</h4>
                        <p class="cert-desc">Demonstrates proficiency in cloud-based data science tools and machine learning workflows.</p>
                    </div>
                </div>
                <div class="cert-card">
                    <div class="cert-icon-wrap cisco"><span class="cert-icon">🕸️</span></div>
                    <div class="cert-content">
                        <div class="cert-meta"><span class="cert-org">Cisco Networking Academy</span><span class="cert-date">Completed: Feb 2026</span></div>
                        <h4 class="cert-title">Getting Started with Cisco Packet Tracer</h4>
                        <p class="cert-desc">Simulating network environments and troubleshooting connectivity issues.</p>
                    </div>
                </div>
                <!-- ... other certs omitted for brevity but I will include them in final assembly ... -->
            </div>
        </div>
"""

# Re-including all certs for completeness
full_certs_html = """
        <div class="content-section" id="testimonials">
            <div class="section-header">
                <h2 class="section-title">Certifications & Events</h2>
                <p class="section-subtitle">Professional credentials, workshops, and skill validations</p>
            </div>

            <div class="cert-grid">
                <div class="cert-card">
                    <div class="cert-icon-wrap oracle"><span class="cert-icon">☁️</span></div>
                    <div class="cert-content">
                        <div class="cert-meta"><span class="cert-org">Oracle University</span><span class="cert-date">Valid: Nov 2025 - Nov 2027</span></div>
                        <h4 class="cert-title">Oracle Cloud Infrastructure - Data Science Professional</h4>
                        <p class="cert-desc">Demonstrates proficiency in cloud-based data tools and ML workflows.</p>
                    </div>
                </div>
                <div class="cert-card">
                    <div class="cert-icon-wrap cisco"><span class="cert-icon">🕸️</span></div>
                    <div class="cert-content">
                        <div class="cert-meta"><span class="cert-org">Cisco Networking Academy</span><span class="cert-date">Feb 2026</span></div>
                        <h4 class="cert-title">Cisco Packet Tracer Getting Started</h4>
                        <p class="cert-desc">Network simulation and configuration of devices.</p>
                    </div>
                </div>
                <div class="cert-card">
                    <div class="cert-icon-wrap ai"><span class="cert-icon">🤖</span></div>
                    <div class="cert-content">
                        <div class="cert-meta"><span class="cert-org">CIT Coimbatore</span><span class="cert-date">Mar 2025</span></div>
                        <h4 class="cert-title">AI-Powered Chatbots</h4>
                    </div>
                </div>
                <div class="cert-card">
                    <div class="cert-icon-wrap cyber"><span class="cert-icon">🛡️</span></div>
                    <div class="cert-content">
                        <div class="cert-meta"><span class="cert-org">OWASP Meetup</span><span class="cert-date">Mar 2026</span></div>
                        <h4 class="cert-title">Cybersecurity & Quantum Workshop</h4>
                    </div>
                </div>
            </div>
        </div>
"""

# 4. Extract Contact
# Look for 'Get in touch' anywhere if the structure is broken
contact_pattern = r'<div class="contact-grid">[\s\S]*?</div>\s*</div>'
contact_match = re.search(contact_pattern, current_html)

if contact_match:
    contact_section = """
        <div class="content-section" id="contact">
            <div class="section-header">
                <h2 class="section-title">Contact</h2>
                <p class="section-subtitle">Let's create something amazing together</p>
            </div>
            """ + contact_match.group() + "\n        </div>"
else:
    contact_section = "<!-- Contact Not Found -->"

# 5. Extract Footer & Scripts
footer_idx = current_html.find('<footer class="footer"')
if footer_idx != -1:
    footer_scripts = current_html[footer_idx:]
else:
    footer_scripts = "</body></html>"

# Assemble
final_html = intro_about_content + skills_html + full_certs_html + contact_section + "\n    </div>\n\n    " + footer_scripts

with open(html_file, "w", encoding="utf-8") as f:
    f.write(final_html)

print("index.html reconstructed without walrus operator.")
