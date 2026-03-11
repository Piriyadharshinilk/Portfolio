import os

html_file = "index.html"
css_file = "templatemo-nexaverse.css"

skills_html = """            <!-- Skills Section -->
            <div class="content-section" id="services">
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
                    <h2 class="section-title">Technical Skills</h2>
                    <p class="section-subtitle">Core competencies and technical proficiencies</p>
                </div>

                <div class="skills-grid">
                    <!-- Networking -->
                    <div class="skill-card">
                        <div class="skill-icon">
                            <span style="font-size: 2rem;">🌐</span>
                        </div>
                        <h4>Networking</h4>
                        <span class="skill-badge intermediate">Intermediate</span>
                    </div>

                    <!-- Linux -->
                    <div class="skill-card">
                        <div class="skill-icon">
                            <span style="font-size: 2rem;">🐧</span>
                        </div>
                        <h4>Linux</h4>
                        <span class="skill-badge beginner">Beginner</span>
                    </div>

                    <!-- Python -->
                    <div class="skill-card">
                        <div class="skill-icon">
                            <span style="font-size: 2rem;">🐍</span>
                        </div>
                        <h4>Python</h4>
                        <span class="skill-badge advanced">Advanced</span>
                    </div>

                    <!-- Web Technologies -->
                    <div class="skill-card">
                        <div class="skill-icon">
                            <span style="font-size: 2rem;">💻</span>
                        </div>
                        <h4>Web Technologies</h4>
                        <span class="skill-badge basics">Basics</span>
                    </div>

                    <!-- Java -->
                    <div class="skill-card">
                        <div class="skill-icon">
                            <span style="font-size: 2rem;">☕</span>
                        </div>
                        <h4>Java</h4>
                        <span class="skill-badge intermediate">Intermediate</span>
                    </div>
                </div>
            </div>"""

with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

start_marker = '<!-- Services Section -->\n            <div class="content-section" id="services">'
end_marker = '<!-- Gallery Section -->'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    # We replace from start_idx to end_idx with the new skills HTML
    new_html = html[:start_idx] + skills_html + "\n\n            " + html[end_idx:]
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(new_html)
    print("Replaced Services with Skills section successfully.")
else:
    print("Could not find delimiters. Start:", start_idx, "End:", end_idx)


css_append = """
/* Skills Section Styles */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 30px;
    margin-top: 30px;
}

.skill-card {
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    border-radius: 15px;
    padding: 30px 20px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
}

.skill-card:hover {
    transform: translateY(-5px);
    border-color: var(--primary);
    box-shadow: 0 10px 30px rgba(176, 38, 255, 0.2);
    /* Adding subtle glow internally and externally for that hacker card feel */
    background: rgba(176, 38, 255, 0.05);
}

.skill-icon {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.02);
    border: 1px solid rgba(255, 255, 255, 0.05);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
    color: var(--primary);
    box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.5);
    transition: all 0.3s ease;
}

.skill-card:hover .skill-icon {
    border-color: var(--primary);
    box-shadow: 0 0 20px var(--glow-cyan), inset 0 0 10px var(--glow-cyan);
}

.skill-card h4 {
    font-family: 'Syne', sans-serif;
    color: #fff;
    font-size: 1.1rem;
    margin-bottom: 15px;
    font-weight: 600;
}

.skill-badge {
    font-size: 0.75rem;
    padding: 6px 15px;
    border-radius: 20px;
    font-weight: 500;
    letter-spacing: 1px;
    text-transform: uppercase;
    border: 1px solid;
}

.skill-badge.advanced {
    color: #00ff88;
    background: rgba(0, 255, 136, 0.1);
    border-color: rgba(0, 255, 136, 0.3);
}

.skill-badge.intermediate {
    color: #00d4ff;
    background: rgba(0, 212, 255, 0.1);
    border-color: rgba(0, 212, 255, 0.3);
}

.skill-badge.beginner {
    color: #ffb800;
    background: rgba(255, 184, 0, 0.1);
    border-color: rgba(255, 184, 0, 0.3);
}

.skill-badge.basics {
    color: #ff5555;
    background: rgba(255, 85, 85, 0.1);
    border-color: rgba(255, 85, 85, 0.3);
}
"""

with open(css_file, "a", encoding="utf-8") as f:
    f.write(css_append)
print("Appended CSS successfully.")
