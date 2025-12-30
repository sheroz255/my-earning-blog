import os

titles = [ "TikTok Automation Mastery", "AI Crypto Trading Bots", "AI Side Hustles 2026", "Digital Real Estate", "Freelance Success Guide", "Web Development Strategy", "E-commerce Profit Plan", "Social Media Algorithms", "YouTube Cashcow Secrets", "Instagram Wealth Strategy", "Stock Market Mastery", "Virtual Assistant Training", "App Business Secrets", "Cyber Security Expert", "Video Editing Course", "Graphic Design Trends", "Advanced Dropshipping", "Ebook Selling Profits", "SaaS Startup Guide", "AI Prompt Engineering", "UI/UX Design Standards", "Global Payment Gateways", "Python Automation Bots", "Gaming Revenue Streams", "Adsterra Revenue Secrets", "Voiceover AI Tools", "NFT Market Evolution", "Remote SEO Consulting", "Day Trading Techniques", "Pinterest Traffic Secrets", "CPA Marketing Hacks", "Email Marketing Funnels", "Metaverse Business Models", "Cloud Computing Basics", "Podcasting for Profit", "Influencer Outreach", "Data Analytics for Beginners", "High-Ticket Sales", "Domain Flipping Guide", "Copywriting for Conversions", "Shopify SEO Mastery", "Amazon FBA Blueprint", "Google Ads Optimization", "Facebook Ads Scaling", "LinkedIn Lead Gen", "Snapchat Marketing", "Telegram Bot Business", "Quora Traffic Engine", "Software Testing Career", "Blockchain Architecture", "DeFi Yield Farming", "Smart Contract Audits", "Real Estate Tokenization", "Wealth Management AI", "Credit Score Repair", "Personal Finance Hacks", "Online Coaching Business", "Web3 Development", "Cyber Hygiene for Pros", "Remote Work Setup", "Digital Nomad Lifestyle", "SaaS Growth Hacking", "Low-Code App Design", "Micro-SaaS Ideas", "Subscription Box Business", "Print on Demand Profits", "Art Gallery NFTs", "Music Royalty Investing", "Solar Energy Side Hustles", "EV Charging Station Business", "Vertical Farming Tech", "Space Economy Future", "Quantum Computing Impact", "Biotech Investment Trends", "Cyber Security for Small Business", "Zero Trust Security", "Content Strategy 2026", "Viral Marketing Psychology", "Branding for Startups", "Customer Retention AI", "Logistics Automation", "Supply Chain Transparency", "Agile Project Management", "Remote Team Leadership", "Public Speaking Skills", "Body Language for Sales", "Negotiation Strategies", "Mindset for Millionaires", "Productivity Systems", "Deep Work Strategies", "Biohacking for Founders", "Sustainable Business Models", "Social Impact Ventures", "Crowdfunding Success", "Angel Investing Basics", "VC Funding Roadmap", "Exit Strategy Planning", "Global Tax Optimization", "Legal Tech Evolution", "AI Ethics for Business" ]

index_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="google-site-verification" content="X4FP-y7MQmptGMN" />
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-RPNNLFJ22K"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-RPNNLFJ22K');</script>
    <script type="text/javascript" src="https://pl28282752.effectivegatecpm.com/ba/73/ea/ba73ea6d4cc4e7b1ca664d63c70dc7e7.js"></script>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EarnSmart | 2026 Authority</title>
    <style>
        body {{ background: #020617; color: white; font-family: sans-serif; margin: 0; }}
        nav {{ background: #0f172a; padding: 20px; border-bottom: 1px solid #1e293b; text-align: center; }}
        .logo {{ font-size: 1.8rem; font-weight: bold; color: #38bdf8; text-decoration: none; }}
        .hero {{ padding: 80px 20px; text-align: center; background: #020617; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; padding: 40px; }}
        .card {{ background: #0f172a; border-radius: 12px; border: 1px solid #1e293b; overflow: hidden; text-decoration: none; color: inherit; transition: 0.3s; }}
        .card:hover {{ border-color: #38bdf8; transform: translateY(-5px); }}
        .card img {{ width: 100%; height: 180px; object-fit: cover; }}
        .card-body {{ padding: 20px; }}
        .card h3 {{ color: #38bdf8; margin: 0; font-size: 1.2rem; }}
        .search {{ width: 80%; max-width: 500px; padding: 12px; border-radius: 8px; border: 1px solid #1e293b; background: #0f172a; color: white; margin-top: 20px; }}
    </style>
</head>
<body>
    <nav><a href="index.html" class="logo">EARNSMART.</a></nav>
    <div class="hero">
        <h1>Global Wealth Intelligence</h1>
        <input type="text" class="search" id="sb" placeholder="Search guides..." onkeyup="f()">
    </div>
    <div class="grid" id="bg">
"""

for i, title in enumerate(titles, 1):
    index_content += f"""
        <a href="blog{i}.html" class="card">
            <img src="https://images.unsplash.com/photo-1553729459-efe14ef6055d?auto=format&fit=crop&w=400&q=80" alt="Card">
            <div class="card-body"><h3>{title}</h3><p>2026 Masterclass for {title}</p></div>
        </a>"""

index_content += """
    </div>
    <script>function f(){let i=document.getElementById('sb').value.toLowerCase();let c=document.getElementsByClassName('card');for(let j=0;j<c.length;j++){let t=c[j].getElementsByTagName('h3')[0].innerText.toLowerCase();c[j].style.display=t.includes(i)?"":"none";}}</script>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(index_content)
print("✔ index.html Fixed!")

