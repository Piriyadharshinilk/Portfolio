import re
import os

html_file = "index.html"

# Load current HTML
with open(html_file, "r", encoding="utf-8") as f:
    full_html = f.read()

# 1. Extraction functions
def extract_section(html, section_id):
    # Find the start of the section
    start_match = re.search(rf'<div class="content-section" id="{section_id}">', html)
    if not start_match:
        return None
    
    start_idx = start_match.start()
    
    # Find the start of the NEXT section to determine boundaries
    next_section_match = re.search(r'<div class="content-section" id=', html[start_match.end():])
    if next_section_match:
        end_idx = start_match.end() + next_section_match.start()
    else:
        # If no next section, look for the footer or end of contentArea
        footer_match = re.search(r'<footer|</div>\s*</div>\s*<script', html[start_match.end():])
        if footer_match:
            end_idx = start_match.end() + footer_match.start()
        else:
            end_idx = len(html)
            
    content = html[start_idx:end_idx].strip()
    
    # Ensure it ends with a closing div for the section itself if it's missing
    # Count balance - highly simplistic but often works for these flat structures
    opens = content.count('<div ')
    closes = content.count('</div>')
    if opens > closes:
        content += "\n        " + ("</div>" * (opens - closes))
        
    return content

# Extract parts cleanly
# Header: everything up to the first content-section
header_end_match = re.search(r'<div class="content-section"', full_html)
header_part = full_html[:header_end_match.start()] if header_end_match else full_html.split('<div id="contentArea">')[0] + '<div id="contentArea">'

intro = extract_section(full_html, "introduction")
about = extract_section(full_html, "about")

# Define Skills and Soft Skills redesigned to match image
skills_html = """
        <div class="content-section" id="services">
            <div class="section-header">
                <h2 class="section-title">Technical & Soft Skills</h2>
                <div class="title-underline"></div>
            </div>

            <style>
                #services .skills-grid { 
                    display: grid !important; 
                    grid-template-columns: repeat(5, 1fr) !important; 
                    gap: 20px !important;
                    margin-top: 50px !important;
                }
                .title-underline {
                    width: 60px;
                    height: 4px;
                    background: var(--primary);
                    margin: 15px auto 0;
                    border-radius: 2px;
                }
                #services .skill-card { 
                    background: rgba(10, 20, 35, 0.6) !important;
                    border: 1px solid rgba(0, 255, 255, 0.1) !important;
                    border-radius: 12px !important;
                    padding: 30px 20px !important;
                    display: flex !important;
                    flex-direction: column !important;
                    align-items: center !important;
                    text-align: center !important;
                    transition: all 0.3s ease !important;
                    height: 100% !important;
                    justify-content: center !important;
                }
                #services .skill-card:hover {
                    transform: translateY(-5px) !important;
                    border-color: var(--primary) !important;
                    box-shadow: 0 10px 30px rgba(0, 255, 255, 0.1) !important;
                }
                #services .skill-icon-circle {
                    width: 60px;
                    height: 60px;
                    border-radius: 50%;
                    border: 1.5px solid var(--primary);
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    margin-bottom: 20px;
                    color: var(--primary);
                    font-size: 24px;
                }
                #services .skill-card h4 {
                    font-family: 'Syne', sans-serif;
                    font-size: 16px;
                    font-weight: 500;
                    color: #ffffff;
                    margin-bottom: 15px;
                    min-height: 40px;
                    display: flex;
                    align-items: center;
                }
                #services .skill-badge {
                    padding: 6px 15px;
                    border-radius: 20px;
                    font-size: 11px;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                    border: 1px solid;
                    background: transparent;
                }
                .badge-advanced { border-color: #00d4ff; color: #00d4ff; box-shadow: 0 0 10px rgba(0, 212, 255, 0.2); }
                .badge-intermediate { border-color: #0088ff; color: #0088ff; }
                .badge-basic { border-color: #00ffcc; color: #00ffcc; }
                .badge-soft { border-color: #b026ff; color: #b026ff; }

                @media (max-width: 1024px) {
                    #services .skills-grid { grid-template-columns: repeat(3, 1fr) !important; }
                }
                @media (max-width: 768px) {
                    #services .skills-grid { grid-template-columns: repeat(2, 1fr) !important; }
                }
                @media (max-width: 480px) {
                    #services .skills-grid { grid-template-columns: 1fr !important; }
                }
            </style>

            <div class="skills-grid">
                <!-- Python -->
                <div class="skill-card">
                    <div class="skill-icon-circle"><span>🐍</span></div>
                    <h4>Python</h4>
                    <span class="skill-badge badge-advanced">Advanced</span>
                </div>
                <!-- Java -->
                <div class="skill-card">
                    <div class="skill-icon-circle"><span>☕</span></div>
                    <h4>Java</h4>
                    <span class="skill-badge badge-basic">Basics</span>
                </div>
                <!-- Web Tech -->
                <div class="skill-card">
                    <div class="skill-icon-circle"><span>🌐</span></div>
                    <h4>Web Technologies</h4>
                    <span class="skill-badge badge-intermediate">Intermediate</span>
                </div>
                <!-- Linux -->
                <div class="skill-card">
                    <div class="skill-icon-circle"><span>&gt;_</span></div>
                    <h4>Linux</h4>
                    <span class="skill-badge badge-basic">Basics</span>
                </div>
                <!-- Networking -->
                <div class="skill-card">
                    <div class="skill-icon-circle"><span>🛡️</span></div>
                    <h4>Networking</h4>
                    <span class="skill-badge badge-intermediate">Intermediate</span>
                </div>
            </div>
        </div>
"""

certs_html = """
        <div class="content-section" id="testimonials">
            <div class="section-header">
                <h2 class="section-title">Certifications & Events</h2>
                <div class="title-underline"></div>
            </div>

            <style>
                #testimonials .cert-grid { 
                    display: grid !important; 
                    grid-template-columns: repeat(3, 1fr) !important; 
                    gap: 25px !important;
                    margin-top: 50px !important;
                }
                #testimonials .cert-card { 
                    background: rgba(15, 25, 45, 0.4) !important;
                    border: 1px solid rgba(176, 38, 255, 0.1) !important;
                    border-radius: 16px !important;
                    padding: 25px !important;
                    display: flex !important;
                    flex-direction: column !important;
                    transition: all 0.3s ease !important;
                    height: 100% !important;
                    position: relative !important;
                    overflow: hidden !important;
                }
                #testimonials .cert-card:hover {
                    transform: translateY(-8px) !important;
                    border-color: var(--secondary) !important;
                    box-shadow: 0 15px 35px rgba(176, 38, 255, 0.15) !important;
                    background: rgba(15, 25, 45, 0.6) !important;
                }
                #testimonials .cert-icon-box {
                    width: 50px;
                    height: 50px;
                    background: rgba(176, 38, 255, 0.1);
                    border-radius: 12px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    font-size: 24px;
                    margin-bottom: 20px;
                    color: var(--secondary);
                }
                #testimonials .cert-org {
                    font-size: 11px;
                    text-transform: uppercase;
                    letter-spacing: 2px;
                    color: var(--secondary);
                    margin-bottom: 8px;
                    font-weight: 600;
                }
                #testimonials .cert-title {
                    font-family: 'Syne', sans-serif;
                    font-size: 17px;
                    color: #ffffff;
                    margin-bottom: 12px;
                    line-height: 1.4;
                    font-weight: 500;
                }
                #testimonials .cert-date {
                    font-size: 12px;
                    color: rgba(255, 255, 255, 0.5);
                    margin-bottom: 15px;
                    display: flex;
                    align-items: center;
                    gap: 6px;
                }
                #testimonials .cert-desc {
                    font-size: 13px;
                    line-height: 1.6;
                    color: rgba(255, 255, 255, 0.7);
                }

                @media (max-width: 1024px) {
                    #testimonials .cert-grid { grid-template-columns: repeat(2, 1fr) !important; }
                }
                @media (max-width: 650px) {
                    #testimonials .cert-grid { grid-template-columns: 1fr !important; }
                }
            </style>

            <div class="cert-grid">
                <!-- 1. Oracle -->
                <div class="cert-card">
                    <div class="cert-icon-box">☁️</div>
                    <div class="cert-org">Oracle University</div>
                    <h4 class="cert-title">OCI – Data Science Professional</h4>
                    <div class="cert-date">📅 Nov 2025 - Nov 2027</div>
                    <p class="cert-desc">Proficiency in cloud-based data science tools, machine learning workflows, and scalable AI applications on Oracle Cloud Infrastructure.</p>
                </div>

                <!-- 2. Cisco -->
                <div class="cert-card">
                    <div class="cert-icon-box">🕸️</div>
                    <div class="cert-org">Cisco Networking Academy</div>
                    <h4 class="cert-title">Getting Started with Cisco Packet Tracer</h4>
                    <div class="cert-date">📅 Feb 2026</div>
                    <p class="cert-desc">Foundational knowledge of networking, simulating environments, and configuring routers/switches for practical communication.</p>
                </div>

                <!-- 3. AI Chatbots -->
                <div class="cert-card">
                    <div class="cert-icon-box">🤖</div>
                    <div class="cert-org">Coimbatore Institute of Technology</div>
                    <h4 class="cert-title">AI-Powered Chatbots Workshop</h4>
                    <div class="cert-date">📅 Mar 15, 2025</div>
                    <p class="cert-desc">Insights into conversational AI design, Natural Language Processing (NLP), and integrating automation into modern applications.</p>
                </div>

                <!-- 4. Smart Aquaponics -->
                <div class="cert-card">
                    <div class="cert-icon-box">🌱</div>
                    <div class="cert-org">E-Cell, KGiSL IT</div>
                    <h4 class="cert-title">AI Based Smart Aquaponics System</h4>
                    <div class="cert-date">📅 Oct 28, 2024</div>
                    <p class="cert-desc">Explored integrating AI with smart agriculture, focusing on automated monitoring systems for productivity and sustainability.</p>
                </div>

                <!-- 5. Paper Presentation -->
                <div class="cert-card">
                    <div class="cert-icon-box">📄</div>
                    <div class="cert-org">KGiSL Institute of Technology</div>
                    <h4 class="cert-title">Paper Presentation: Language & Society</h4>
                    <div class="cert-date">📅 Apr 11, 2025</div>
                    <p class="cert-desc">Presented research on "Subtitles of Technology," exploring the influence of tech on modern communication and society.</p>
                </div>

                <!-- 6. OWASP Meetup -->
                <div class="cert-card">
                    <div class="cert-icon-box">🛡️</div>
                    <div class="cert-org">OWASP Coimbatore Chapter</div>
                    <h4 class="cert-title">Cybersecurity Workshop – Meetup</h4>
                    <div class="cert-date">📅 Mar 7, 2026</div>
                    <p class="cert-desc">Advanced session on Automotive Security and Quantum Threat Horizon, covering vehicle hacking and emerging cyber threats.</p>
                </div>
            </div>
        </div>
"""

contact = extract_section(full_html, "contact")

# Footer Part: from mainFooter onwards
footer_match = re.search(r'<footer class="footer" id="mainFooter">', full_html)
if footer_match:
    footer_part = "\n    </div>\n\n    " + full_html[footer_match.start():]
    # Clean up any potential duplication within full_html itself if it was already messed up
    footer_part = footer_part.split('</html>')[0] + '</html>'
else:
    footer_part = "\n    </div>\n</body>\n</html>"

# Final Assembly in correct order: Intro -> About -> Skills -> Certs -> Contact
reconstructed = header_part + "\n" + intro + "\n" + about + "\n" + skills_html + "\n" + certs_html + "\n" + contact + footer_part

# Write back
with open(html_file, "w", encoding="utf-8") as f:
    f.write(reconstructed)

print("Reconstructed index.html with ORDER: Intro -> About -> Skills -> Certs -> Contact.")
