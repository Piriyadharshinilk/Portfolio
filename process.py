import re
import sys

filepath = r'c:\Users\Piriya\OneDrive\Desktop\Portfolio\templatemo_603_nexaverse\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Menu Grid
text = re.sub(r'<!-- Menu Grid -->.*?<!-- Content Sections -->', 
              r'''<!-- Menu Grid -->
        <div class="menu-grid" id="menuGrid">
            <div class="menu-item initial-load" data-section="introduction">
                <div class="menu-badge">IN</div>
                <div class="menu-title">Introduction</div>
            </div>
            <div class="menu-item initial-load" data-section="certification">
                <div class="menu-badge">CR</div>
                <div class="menu-title">Certification</div>
            </div>
            <div class="menu-item initial-load" data-section="about">
                <div class="menu-badge">AB</div>
                <div class="menu-title">About</div>
            </div>
            <div class="menu-item initial-load" data-section="contact">
                <div class="menu-badge">CT</div>
                <div class="menu-title">Contact</div>
            </div>
        </div>

        <!-- Content Sections -->''', text, flags=re.DOTALL)

# Replace Sections
text = re.sub(r'<!-- Services Section -->.*?<!-- About Section -->',
              r'''<!-- Certifications Section -->
            <div class="content-section" id="certification">
                <div class="section-header-small">
                    <div class="small-logo">
                        <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
                            <defs>
                                <linearGradient id="smallLogoGrad7" x1="0%" y1="0%" x2="100%" y2="100%">
                                    <stop offset="0%" style="stop-color:#00f0ff" />
                                    <stop offset="100%" style="stop-color:#ff00d4" />
                                </linearGradient>
                            </defs>
                            <polygon points="50,10 85,32 85,68 50,90 15,68 15,32" fill="none"
                                stroke="url(#smallLogoGrad7)" stroke-width="3" />
                            <circle cx="50" cy="50" r="10" fill="url(#smallLogoGrad7)" />
                        </svg>
                    </div>
                    <div class="small-brand">
                        <h3>PIRIYADHARSHINI</h3>
                        <p>Digital Excellence</p>
                    </div>
                </div>
                <button class="back-btn" onclick="backToMenu()">← Back to Menu</button>

                <div class="section-header">
                    <h2 class="section-title">Certifications</h2>
                    <p class="section-subtitle">My professional achievements</p>
                </div>

                <div class="about-content" style="padding: 20px; background: rgba(255,255,255,0.05); border-radius: 15px;">
                    <h3>Cyber Security & Networking</h3>
                    <p>Certified in various technologies and fields. Continuous learner and enthusiast.</p>
                </div>
            </div>

            <!-- About Section -->''', text, flags=re.DOTALL)

# Replace Contact info
text = re.sub(r'<div class="contact-info">.*?</div>\s*</div>\s*</div>\s*</div>',
              r'''<div class="contact-info">
                        <div class="contact-item">
                            <div class="contact-icon">📍</div>
                            <div class="contact-details">
                                <h4>Location</h4>
                                <p>Native: Kallakurichi<br>Current: Coimbatore</p>
                            </div>
                        </div>
                        <div class="contact-item">
                            <div class="contact-icon">📧</div>
                            <div class="contact-details">
                                <h4>Email</h4>
                                <p>piriyakannan29@gmail.com</p>
                            </div>
                        </div>
                        <div class="contact-item">
                            <div class="contact-icon">📞</div>
                            <div class="contact-details">
                                <h4>Phone</h4>
                                <p>+91 9360221192</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>''', text, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)
print('Done!')
