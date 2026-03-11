import os

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

new_cert_html = """            <!-- Certifications Section -->
            <div class="content-section" id="certifications">
                <div class="section-header-small">
                    <div class="small-logo">
                        <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
                            <defs>
                                <linearGradient id="smallLogoGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
                                    <stop offset="0%" style="stop-color:#00f0ff" />
                                    <stop offset="100%" style="stop-color:#ff00d4" />
                                </linearGradient>
                            </defs>
                            <polygon points="50,10 85,32 85,68 50,90 15,68 15,32" fill="none"
                                stroke="url(#smallLogoGrad2)" stroke-width="3" />
                            <circle cx="50" cy="50" r="10" fill="url(#smallLogoGrad2)" />
                        </svg>
                    </div>
                    <div class="small-brand">
                        <h3>PIRIYADHARSHINI</h3>
                        <p>Cybersecurity Enthusiast</p>
                    </div>
                </div>
                <button class="back-btn" onclick="backToMenu()">← Back to Menu</button>

                <div class="section-header">
                    <h2 class="section-title">Certifications</h2>
                    <p class="section-subtitle">Professional credentials and skill validations from industry leaders.</p>
                </div>

                <div class="tabs-container">
                    <div class="tab-buttons">
                        <button class="tab-btn active" onclick="switchTab(this, 'ai-cloud')">AI & Cloud</button>
                        <button class="tab-btn" onclick="switchTab(this, 'programming')">Programming</button>
                        <button class="tab-btn" onclick="switchTab(this, 'cybersec')">Cybersecurity</button>
                    </div>

                    <div class="tab-content">
                        <div class="tab-pane active" id="ai-cloud">
                            <div class="services-list">
                                <div class="service-row">
                                    <div class="service-row-icon">
                                        <img src="images/google-cloud-icon.jpg" alt="Google Cloud">
                                    </div>
                                    <div class="service-row-content">
                                        <h4>Google Cloud Computing Foundations</h4>
                                        <p>Data, ML, and AI in Google Cloud. Focused on cloud infrastructure and machine learning integration.</p>
                                    </div>
                                    <div class="service-row-arrow">→</div>
                                </div>
                                <div class="service-row">
                                    <div class="service-row-icon">
                                        <img src="images/gen-ai-icon.jpg" alt="Generative AI">
                                    </div>
                                    <div class="service-row-content">
                                        <h4>Career Essentials in Generative AI</h4>
                                        <p>By Microsoft and LinkedIn. Covers the fundamental shift and application of LLMs in the modern workforce.</p>
                                    </div>
                                    <div class="service-row-arrow">→</div>
                                </div>
                            </div>
                        </div>

                        <div class="tab-pane" id="programming">
                            <div class="services-list">
                                <div class="service-row">
                                    <div class="service-row-icon">
                                        <img src="images/python-icon.jpg" alt="Python Basic">
                                    </div>
                                    <div class="service-row-content">
                                        <h4>Python (Basic) - HackerRank</h4>
                                        <p>Validation of core Python programming skills, data structures, and functional programming.</p>
                                    </div>
                                    <div class="service-row-arrow">→</div>
                                </div>
                                <div class="service-row">
                                    <div class="service-row-icon">
                                        <img src="images/problem-solving-icon.jpg" alt="Problem Solving">
                                    </div>
                                    <div class="service-row-content">
                                        <h4>Problem Solving (Basic) - HackerRank</h4>
                                        <p>Demonstrated proficiency in algorithmic thinking and solving complex computational logic.</p>
                                    </div>
                                    <div class="service-row-arrow">→</div>
                                </div>
                            </div>
                        </div>

                        <div class="tab-pane" id="cybersec">
                            <div class="services-list">
                                <div class="service-row">
                                    <div class="service-row-icon">
                                        <img src="images/cyber-ds-icon.jpg" alt="Cybersecurity Data Science">
                                    </div>
                                    <div class="service-row-content">
                                        <h4>Cybersecurity for Data Science</h4>
                                        <p>Specialized training focusing on securing data pipelines and identifying vulnerabilities in AI models.</p>
                                    </div>
                                    <div class="service-row-arrow">→</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>"""

start_marker = '            <!-- Services Section -->'
end_marker = '            <!-- Gallery Section -->'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_cert_html + "\\n\\n" + content[end_idx:]
    
    # Also update the menu item linking to id="services" which is now id="certifications"
    content = content.replace('data-section="services"', 'data-section="certifications"')
    content = content.replace('data-section="testimonials"\\n                <div class="menu-badge">Cert</div>\\n                <div class="menu-title">Certifications</div>', 'data-section="testimonials"\\n                <div class="menu-badge">TM</div>\\n                <div class="menu-title">Testimonials</div>')

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)
    print("Replaced section successfully.")
else:
    print("Could not find markers.")
