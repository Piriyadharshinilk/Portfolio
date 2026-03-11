import re

html_file = "index.html"
css_file = "templatemo-nexaverse.css"

with open(html_file, "r", encoding="utf-8") as f:
    html = f.read()

profile_html = """
                    <div class="intro-hero-visual">
                        <div class="profile-container">
                            <!-- Orbit Rings -->
                            <div class="orbit ring-1">
                                <div class="orbit-icon icon-1">⚡</div>
                            </div>
                            <div class="orbit ring-2">
                                <div class="orbit-icon icon-2">☁️</div>
                                <div class="orbit-icon icon-3">🔒</div>
                            </div>
                            
                            <!-- Profile Picture Inner Circle -->
                            <div class="profile-circle">
                                <img src="C:\Users\Piriya\OneDrive\Desktop\Portfolio\templatemo_603_nexaverse\images\mine.jpeg" alt="Piriyadharshini L K Profile Picture" class="profile-img">
                                <div class="profile-glow"></div>
                            </div>
                        </div>
                    </div>
"""

# Replace the intro-hero-visual div and its contents
pattern = r'<div class="intro-hero-visual">.*?</div>\s*</div>\s*<!-- Metrics Strip -->'
replacement = profile_html + "\n                </div>\n\n                <!-- Metrics Strip -->"

# Need to handle exact replacement manually since regex might be tricky with nested divs
start_idx = html.find('<div class="intro-hero-visual">')
end_idx = html.find('<!-- Metrics Strip -->')

if start_idx != -1 and end_idx != -1:
    # Need to preserve the closing div of intro-hero
    html = html[:start_idx] + profile_html + "\n                </div>\n\n                " + html[end_idx:]
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html)
    print("Replaced intro-hero-visual successfully.")
else:
    print("Could not find intro-hero-visual markers.")


css_append = """
/* Profile Image Section Styles */
.intro-hero {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: center;
    position: relative;
    z-index: 10;
}

.intro-hero-visual {
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    height: 400px;
}

.profile-container {
    position: relative;
    width: 350px;
    height: 350px;
    display: flex;
    justify-content: center;
    align-items: center;
}

/* Profile Picture Circle */
.profile-circle {
    position: relative;
    width: 280px;
    height: 280px;
    border-radius: 50%;
    z-index: 5;
    background: var(--dark-3);
    border: 4px solid var(--primary);
    box-shadow: 0 0 30px rgba(176, 38, 255, 0.4), inset 0 0 20px rgba(176, 38, 255, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
}

.profile-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 50%;
    transition: transform 0.5s ease;
}

.profile-container:hover .profile-img {
    transform: scale(1.05);
}

.profile-glow {
    position: absolute;
    inset: 0;
    border-radius: 50%;
    background: radial-gradient(circle at center, transparent 40%, rgba(176, 38, 255, 0.3) 100%);
    pointer-events: none;
}

/* Orbital Rings */
.orbit {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    border-radius: 50%;
    border: 1px dashed rgba(255, 255, 255, 0.15);
    pointer-events: none;
    z-index: 1;
}

.orbit.ring-1 {
    width: 320px;
    height: 320px;
    animation: orbitRotate 20s linear infinite;
    border: 1px solid rgba(176, 38, 255, 0.3);
}

.orbit.ring-2 {
    width: 380px;
    height: 380px;
    animation: orbitRotateReverse 30s linear infinite;
}

.orbit-icon {
    position: absolute;
    width: 40px;
    height: 40px;
    background: var(--dark-2);
    border: 1px solid var(--primary);
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 18px;
    box-shadow: 0 0 15px rgba(176, 38, 255, 0.5);
}

/* Positioning icons on orbits */
.icon-1 { top: -20px; left: 50%; transform: translateX(-50%); animation: iconRotateReverse 20s linear infinite; }
.icon-2 { top: 50%; right: -20px; transform: translateY(-50%); animation: iconRotate 30s linear infinite; }
.icon-3 { bottom: -20px; left: 50%; transform: translateX(-50%); animation: iconRotate 30s linear infinite; }

@keyframes orbitRotate { 0% { transform: translate(-50%, -50%) rotate(0deg); } 100% { transform: translate(-50%, -50%) rotate(360deg); } }
@keyframes orbitRotateReverse { 0% { transform: translate(-50%, -50%) rotate(360deg); } 100% { transform: translate(-50%, -50%) rotate(0deg); } }

/* Counter-rotate icons so they stay upright */
@keyframes iconRotate { 0% { transform: rotate(0deg); } 100% { transform: rotate(-360deg); } }
@keyframes iconRotateReverse { 0% { transform: translateX(-50%) rotate(0deg); } 100% { transform: translateX(-50%) rotate(-360deg); } }

/* Mobile responsiveness */
@media (max-width: 900px) {
    .intro-hero {
        grid-template-columns: 1fr;
        text-align: center;
    }
    .profile-container {
        margin: 50px auto;
        transform: scale(0.85);
    }
}
"""

with open(css_file, "a", encoding="utf-8") as f:
    f.write(css_append)
print("CSS injected successfully.")
