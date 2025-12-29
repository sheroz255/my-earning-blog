index_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="google-site-verification" content="X4FP-y7MQmptGMN" />
    
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-RPNNLFJ22K"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', 'G-RPNNLFJ22K');
    </script>

    <script type="text/javascript" src="https://pl28282752.effectivegatecpm.com/ba/73/ea/ba73ea6d4cc4e7b1ca664d63c70dc7e7.js"></script>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EarnSmart Global | 2026 Earning Portal</title>
    <style>
        body { background: #020617; color: #f8fafc; font-family: 'Inter', sans-serif; margin: 0; padding: 0; }
        .hero { background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); padding: 80px 20px; text-align: center; border-bottom: 2px solid #38bdf8; }
        h1 { font-size: 3rem; color: #38bdf8; margin-bottom: 10px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; padding: 50px 20px; max-width: 1200px; margin: auto; }
        .card { background: #1e293b; border-radius: 12px; padding: 25px; border: 1px solid #334155; transition: 0.3s; text-decoration: none; color: inherit; display: block; }
        .card:hover { border-color: #38bdf8; transform: translateY(-5px); box-shadow: 0 10px 30px rgba(56, 189, 248, 0.2); }
        .card h3 { color: #38bdf8; margin-top: 0; }
        .card p { color: #94a3b8; font-size: 0.95rem; }
        .footer { text-align: center; padding: 40px; border-top: 1px solid #334155; color: #64748b; }
    </style>
</head>
<body>
    <div class="hero">
        <h1>EarnSmart VIP Portal</h1>
        <p>Your Gateway to Automated Wealth in 2026</p>
    </div>

    <div class="grid">
"""

# 30 Blogs ke links generate karna
titles = [
    "TikTok Automation Mastery", "AI Crypto Trading Bots", "AI Side Hustles 2026",
    "Digital Real Estate", "Freelance Success Guide", "Web Development Strategy",
    "E-commerce Profit Plan", "Social Media Algorithms", "YouTube Cashcow Secrets",
    "Instagram Wealth Strategy", "Stock Market Mastery", "Virtual Assistant Training",
    "App Business Secrets", "Cyber Security Expert", "Video Editing Course",
    "Graphic Design Trends", "Advanced Dropshipping", "Ebook Selling Profits",
    "SaaS Startup Guide", "AI Prompt Engineering", "UI/UX Design Standards",
    "Payment Gateways 2026", "Python Automation Bots", "Gaming Revenue Streams",
    "Adsterra Revenue Secrets", "Voiceover AI Tools", "NFT Market Evolution",
    "Remote SEO Consulting", "Day Trading Techniques", "Pinterest Traffic Secrets"
]

for i, title in enumerate(titles, 1):
    index_content += f"""
        <a href="blog{i}.html" class="card">
            <h3>{title}</h3>
            <p>Access the exclusive 2026 blueprint and automation tools for {title}.</p>
        </a>"""

index_content += """
    </div>

    <div class="footer">
        &copy; 2025 EarnSmart Global Authority | All Rights Reserved
    </div>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(index_content)
print("✔ index.html updated with Ads and Verification!")

