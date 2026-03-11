import re

html_file = "index.html"
css_file = "templatemo-nexaverse.css"

certs_html = """<div class="content-section" id="testimonials">
                <div class="section-header-small">
                    <div class="small-logo">
                        <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
                            <defs>
                                <linearGradient id="smallLogoGrad4" x1="0%" y1="0%" x2="100%" y2="100%">
                                    <stop offset="0%" style="stop-color:#00f0ff" />
                                    <stop offset="100%" style="stop-color:#ff00d4" />
                                </linearGradient>
                            </defs>
                            <polygon points="50,10 85,32 85,68 50,90 15,68 15,32" fill="none"
                                stroke="url(#smallLogoGrad4)" stroke-width="3" />
                            <circle cx="50" cy="50" r="10" fill="url(#smallLogoGrad4)" />
                        </svg>
                    </div>
                    <div class="small-brand">
                        <h3>PIRIYADHARSHINI</h3>
                        <p>Continuous Learning</p>
                    </div>
                </div>
                
                <div class="section-header">
                    <h2 class="section-title">Certifications & Events</h2>
                    <p class="section-subtitle">Professional credentials, workshops, and skill validations</p>
                </div>

                <div class="cert-grid">
                    <!-- Certificate 1 -->
                    <div class="cert-card">
                        <div class="cert-icon-wrap oracle">
                            <span class="cert-icon">☁️</span>
                        </div>
                        <div class="cert-content">
                            <div class="cert-meta">
                                <span class="cert-org">Oracle University</span>
                                <span class="cert-date">Valid: Nov 2025 - Nov 2027</span>
                            </div>
                            <h4 class="cert-title">Oracle Cloud Infrastructure - Data Science Professional</h4>
                            <p class="cert-desc">Demonstrates proficiency in cloud-based data science tools, machine learning workflows, and building scalable AI applications in modern cloud environments.</p>
                        </div>
                    </div>

                    <!-- Certificate 2 -->
                    <div class="cert-card">
                        <div class="cert-icon-wrap cisco">
                            <span class="cert-icon">🕸️</span>
                        </div>
                        <div class="cert-content">
                            <div class="cert-meta">
                                <span class="cert-org">Cisco Networking Academy</span>
                                <span class="cert-date">Completed: Feb 2026</span>
                            </div>
                            <h4 class="cert-title">Getting Started with Cisco Packet Tracer</h4>
                            <p class="cert-desc">Foundational knowledge of networking concepts, simulating network environments, configuring routers/switches, and network troubleshooting.</p>
                        </div>
                    </div>

                    <!-- Certificate 3 -->
                    <div class="cert-card">
                        <div class="cert-icon-wrap ai">
                            <span class="cert-icon">🤖</span>
                        </div>
                        <div class="cert-content">
                            <div class="cert-meta">
                                <span class="cert-org">Coimbatore Institute of Technology</span>
                                <span class="cert-date">Mar 2025</span>
                            </div>
                            <h4 class="cert-title">AI-Powered Chatbots Workshop</h4>
                            <p class="cert-desc">Gained insights into conversational AI design, natural language processing, and chatbot integration for modern applications to improve automation.</p>
                        </div>
                    </div>

                    <!-- Certificate 4 -->
                    <div class="cert-card">
                        <div class="cert-icon-wrap iot">
                            <span class="cert-icon">🌱</span>
                        </div>
                        <div class="cert-content">
                            <div class="cert-meta">
                                <span class="cert-org">KGiSL Institute of Technology</span>
                                <span class="cert-date">Oct 2024</span>
                            </div>
                            <h4 class="cert-title">AI Based Smart Aquaponics System</h4>
                            <p class="cert-desc">Introduced to integrating AI with smart agriculture, focusing on AI-based monitoring and automation in aquaponics to improve sustainability.</p>
                        </div>
                    </div>

                    <!-- Certificate 5 -->
                    <div class="cert-card">
                        <div class="cert-icon-wrap research">
                            <span class="cert-icon">📜</span>
                        </div>
                        <div class="cert-content">
                            <div class="cert-meta">
                                <span class="cert-org">KGiSL Institute of Technology</span>
                                <span class="cert-date">Apr 2025</span>
                            </div>
                            <h4 class="cert-title">Paper Presentation – "Subtitles of Technology"</h4>
                            <p class="cert-desc">Presented a research paper exploring the influence of technology on language and communication in modern society during a national-level seminar.</p>
                        </div>
                    </div>

                    <!-- Certificate 6 -->
                    <div class="cert-card">
                        <div class="cert-icon-wrap cyber">
                            <span class="cert-icon">🛡️</span>
                        </div>
                        <div class="cert-content">
                            <div class="cert-meta">
                                <span class="cert-org">OWASP Coimbatore Chapter</span>
                                <span class="cert-date">Mar 2026</span>
                            </div>
                            <h4 class="cert-title">Cybersecurity Workshop Meetup</h4>
                            <p class="cert-desc">Focused on Automotive Security and Quantum Threat Horizon, covering vehicle security systems, modern cyber threats, and ethical hacking practices.</p>
                        </div>
                    </div>
                </div>
            </div>"""

with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

# Replace the specific block
start_marker = '<div class="content-section" id="testimonials">'
end_marker = '            \n<div class="content-section" id="contact">'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_html = html[:start_idx] + certs_html + "\n\n" + html[end_idx:]
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(new_html)
    print("Replaced Testimonials with Certifications successfully.")
else:
    print("Could not find delimiters. Start:", start_idx, "End:", end_idx)


css_append = """
/* Advanced Certification Cards Styles */
.cert-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    gap: 30px;
    margin-top: 40px;
}

.cert-card {
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    border-radius: 16px;
    padding: 30px;
    position: relative;
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    backdrop-filter: blur(12px);
    display: flex;
    flex-direction: column;
    gap: 20px;
    z-index: 1;
}

.cert-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, var(--primary), var(--accent));
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.4s ease;
    z-index: 2;
}

.cert-card:hover {
    transform: translateY(-8px);
    border-color: rgba(176, 38, 255, 0.4);
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4), 0 0 20px rgba(176, 38, 255, 0.15);
}

.cert-card:hover::before {
    transform: scaleX(1);
}

.cert-icon-wrap {
    width: 60px;
    height: 60px;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 28px;
    color: #fff;
    margin-bottom: 5px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    border: 1px solid rgba(255,255,255,0.1);
}

.cert-icon-wrap.oracle { background: linear-gradient(135deg, #F80000 0%, #7A0000 100%); }
.cert-icon-wrap.cisco { background: linear-gradient(135deg, #049fd9 0%, #02597a 100%); }
.cert-icon-wrap.ai { background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%); }
.cert-icon-wrap.iot { background: linear-gradient(135deg, #00b09b 0%, #96c93d 100%); }
.cert-icon-wrap.research { background: linear-gradient(135deg, #ff9966 0%, #ff5e62 100%); }
.cert-icon-wrap.cyber { background: linear-gradient(135deg, #1f4037 0%, #99f2c8 100%); }

.cert-content {
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.cert-meta {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    font-size: 13px;
    color: rgba(255, 255, 255, 0.6);
    flex-wrap: wrap;
    gap: 10px;
}

.cert-org {
    color: var(--primary);
    font-weight: 600;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    font-size: 11px;
}

.cert-date {
    background: rgba(255,255,255,0.05);
    padding: 4px 10px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.1);
    white-space: nowrap;
}

.cert-title {
    font-family: 'Syne', sans-serif;
    font-size: 20px;
    font-weight: 600;
    color: #ffffff;
    line-height: 1.4;
    margin: 0;
    transition: color 0.3s ease;
}

.cert-card:hover .cert-title {
    color: var(--primary);
}

.cert-desc {
    color: rgba(255, 255, 255, 0.7);
    font-size: 14px;
    line-height: 1.6;
    margin: 0;
}
"""

with open(css_file, "a", encoding="utf-8") as f:
    f.write(css_append)
print("Appended CSS successfully.")
