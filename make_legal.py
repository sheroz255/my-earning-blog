import os

pages = {
    "privacy.html": {
        "title": "Privacy Policy",
        "content": "At EarnSmart 2026, we prioritize your privacy. This policy outlines the types of personal information that is received and collected by our website and how it is used. We use cookies to improve user experience and analyze traffic through Google Analytics. Your data is never sold to third parties."
    },
    "about.html": {
        "title": "About Us",
        "content": "EarnSmart 2026 is a premier digital authority dedicated to providing high-quality, automated wealth-building strategies. Our mission is to empower entrepreneurs with 2026-ready blueprints for TikTok automation, Crypto trading, and AI-driven side hustles."
    },
    "contact.html": {
        "title": "Contact Us",
        "content": "Have questions or need support regarding our automation guides? You can reach our team at support@earnsmart.global. We aim to respond to all inquiries within 24-48 hours."
    }
}

template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | EarnSmart 2026</title>
    <style>
        body {{ background: #020617; color: #cbd5e1; font-family: 'Inter', sans-serif; line-height: 1.8; padding: 40px; }}
        .box {{ max-width: 800px; margin: auto; background: #1e293b; padding: 40px; border-radius: 15px; border: 1px solid #334155; }}
        h1 {{ color: #38bdf8; }}
        p {{ font-size: 1.1rem; }}
        .home-link {{ display: inline-block; margin-top: 20px; color: #38bdf8; text-decoration: none; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="box">
        <h1>{title}</h1>
        <p>{content}</p>
        <a href="index.html" class="home-link">← Back to Home</a>
    </div>
</body>
</html>
"""

for filename, data in pages.items():
    with open(filename, "w") as f:
        f.write(template.format(title=data['title'], content=data['content']))
    print(f"✔ Created: {filename}")

