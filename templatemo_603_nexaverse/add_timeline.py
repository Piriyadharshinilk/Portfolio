import os

html_file = "index.html"
css_file = "templatemo-nexaverse.css"

new_html = """                    <div class="education-timeline">
                        <h3 class="timeline-main-title">Education Timeline</h3>
                        
                        <div class="timeline-item">
                            <div class="timeline-dot"></div>
                            <div class="timeline-content">
                                <div class="timeline-header">
                                    <h4>B.E CSE (CYS)</h4>
                                    <span class="timeline-date">Pursuing</span>
                                </div>
                                <p class="institute"><span class="icon">🎓</span> Kgisl institute of technology</p>
                            </div>
                        </div>

                        <div class="timeline-item">
                            <div class="timeline-dot"></div>
                            <div class="timeline-content">
                                <div class="timeline-header">
                                    <h4>H.S.C</h4>
                                    <span class="timeline-date">2024 (88.3%)</span>
                                </div>
                                <p class="institute"><span class="icon">🎓</span> Jeevan Matric Higher Secondary School, Chinnasalem</p>
                            </div>
                        </div>

                        <div class="timeline-item">
                            <div class="timeline-dot"></div>
                            <div class="timeline-content">
                                <div class="timeline-header">
                                    <h4>S.S.L.C</h4>
                                    <span class="timeline-date">2022 (93%)</span>
                                </div>
                                <p class="institute"><span class="icon">🎓</span> Jeevan Matric Higher secondary School, Chinnasalem</p>
                            </div>
                        </div>
                    </div>"""

with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

start_marker = '<div class="about-image">'
end_marker = '</div>\n                </div>\n            </div>\n\n            <!-- Contact Section -->'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    html = html[:start_idx] + new_html + "\n                " + html[end_idx:]
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html)
    print("Replaced HTML successfully.")
else:
    print("Could not find HTML markers.")


css_append = """
/* Education Timeline */
.education-timeline {
    position: relative;
    padding-left: 30px;
    margin-top: 20px;
}

.education-timeline::before {
    content: '';
    position: absolute;
    top: 0;
    bottom: 0;
    left: 4px;
    width: 2px;
    background: linear-gradient(180deg, var(--primary) 0%, rgba(176, 38, 255, 0.1) 100%);
    border-radius: 2px;
}

.timeline-main-title {
    font-family: 'Syne', sans-serif;
    font-size: 24px;
    font-weight: 600;
    margin-bottom: 30px;
    color: #ffffff;
}

.timeline-item {
    position: relative;
    margin-bottom: 30px;
}

.timeline-item:last-child {
    margin-bottom: 0;
}

.timeline-dot {
    position: absolute;
    top: 5px;
    left: -33px;
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: var(--dark-1);
    border: 2px solid var(--primary);
    box-shadow: 0 0 10px var(--glow-cyan);
    z-index: 2;
}

.timeline-content {
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid var(--glass-border);
    border-radius: 12px;
    padding: 20px;
    transition: all 0.3s ease;
}

.timeline-content:hover {
    border-color: var(--primary);
    box-shadow: 0 5px 20px rgba(176, 38, 255, 0.15);
    background: rgba(255, 255, 255, 0.05);
}

.timeline-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 12px;
    flex-wrap: wrap;
    gap: 10px;
}

.timeline-header h4 {
    font-family: 'Syne', sans-serif;
    font-size: 18px;
    font-weight: 600;
    color: #ffffff;
    margin: 0;
}

.timeline-date {
    font-size: 12px;
    padding: 4px 12px;
    background: rgba(176, 38, 255, 0.1);
    color: var(--primary);
    border-radius: 20px;
    border: 1px solid rgba(176, 38, 255, 0.3);
}

.institute {
    font-size: 14px;
    color: rgba(255, 255, 255, 0.7);
    margin: 0;
    display: flex;
    align-items: center;
    gap: 8px;
}

.institute .icon {
    font-size: 16px;
}

@media (max-width: 768px) {
    .about-content {
        grid-template-columns: 1fr;
    }
}
"""

with open(css_file, "a", encoding="utf-8") as f:
    f.write(css_append)
print("Appended CSS successfully.")
