import os

# 100 Titles (Ensure this list matches your creator.py titles exactly)
titles = [
    "TikTok Automation Mastery", "AI Crypto Trading Bots", "AI Side Hustles 2026", "Digital Real Estate", 
    "Freelance Success Guide", "Web Development Strategy", "E-commerce Profit Plan", "Social Media Algorithms", 
    "YouTube Cashcow Secrets", "Instagram Wealth Strategy", "Stock Market Mastery", "Virtual Assistant Training", 
    "App Business Secrets", "Cyber Security Expert", "Video Editing Course", "Graphic Design Trends", 
    "Advanced Dropshipping", "Ebook Selling Profits", "SaaS Startup Guide", "AI Prompt Engineering", 
    "UI/UX Design Standards", "Global Payment Gateways", "Python Automation Bots", "Gaming Revenue Streams", 
    "Adsterra Revenue Secrets", "Voiceover AI Tools", "NFT Market Evolution", "Remote SEO Consulting", 
    "Day Trading Techniques", "Pinterest Traffic Secrets", "CPA Marketing Hacks", "Email Marketing Funnels",
    "Metaverse Business Models", "Cloud Computing Basics", "Podcasting for Profit", "Influencer Outreach",
    "Data Analytics for Beginners", "High-Ticket Sales", "Domain Flipping Guide", "Copywriting for Conversions",
    "Shopify SEO Mastery", "Amazon FBA Blueprint", "Google Ads Optimization", "Facebook Ads Scaling",
    "LinkedIn Lead Gen", "Snapchat Marketing", "Telegram Bot Business", "Quora Traffic Engine",
    "Software Testing Career", "Blockchain Architecture", "DeFi Yield Farming", "Smart Contract Audits",
    "Real Estate Tokenization", "Wealth Management AI", "Credit Score Repair", "Personal Finance Hacks",
    "Online Coaching Business", "Web3 Development", "Cyber Hygiene for Pros", "Remote Work Setup",
    "Digital Nomad Lifestyle", "SaaS Growth Hacking", "Low-Code App Design", "Micro-SaaS Ideas",
    "Subscription Box Business", "Print on Demand Profits", "Art Gallery NFTs", "Music Royalty Investing",
    "Solar Energy Side Hustles", "EV Charging Station Business", "Vertical Farming Tech", "Space Economy Future",
    "Quantum Computing Impact", "Biotech Investment Trends", "Cyber Security for Small Business", "Zero Trust Security",
    "Content Strategy 2026", "Viral Marketing Psychology", "Branding for Startups", "Customer Retention AI",
    "Logistics Automation", "Supply Chain Transparency", "Agile Project Management", "Remote Team Leadership",
    "Public Speaking Skills", "Body Language for Sales", "Negotiation Strategies", "Mindset for Millionaires",
    "Productivity Systems", "Deep Work Strategies", "Biohacking for Founders", "Sustainable Business Models",
    "Social Impact Ventures", "Crowdfunding Success", "Angel Investing Basics", "VC Funding Roadmap",
    "Exit Strategy Planning", "Global Tax Optimization", "Legal Tech Evolution", "AI Ethics for Business"
]

images = [
    "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=500",
    "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=500",
    "https://images.unsplash.com/photo-1551288049-bbbda536639a?w=500",
    "https://images.unsplash.com/photo-1526304640581-d334cdbbf45e?w=500",
    "https://images.unsplash.com/photo-1553729459-efe14ef6055d?w=500",
    "https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=500"
]

index_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="google-site-verification" content="X4FP-y7MQmptGMN" />
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-RPNNLFJ22K"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-RPNNLFJ22K');</script>
    <script type="text/javascript" src="https://pl28282752.effectivegatecpm.com/ba/73/ea/ba73ea6d4cc4e7b1ca664d63c70dc7e7.js"></script>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EarnSmart | Global 2026 Authority Portal</title>
    <style>
        :root {{ --primary: #38bdf8; --bg: #020617; --card-bg: #1e293b; }}
        body {{ background: var(--bg); color: #f8fafc; font-family: 'Inter', sans-serif; margin: 0; }}
        nav {{ background: rgba(15, 23, 42, 0.9); backdrop-filter: blur(10px); padding: 20px 50px; display: flex; justify-content: space-between; position: sticky; top: 0; z-index: 1000; border-bottom: 1px solid #334155; }}
        .nav-links a {{ color: white; text-decoration: none; margin-left: 20px; font-weight: 600; }}
        .hero {{ padding: 120px 20px; text-align: center; background: radial-gradient(circle at center, #1e293b 0%, #020617 100%); }}
        #searchBar {{ width: 80%; max-width: 600px; padding: 18px 30px; border-radius: 50px; border: 2px solid var(--primary); background: #0f172a; color: white; font-size: 1.2rem; outline: none; margin-top: 30px; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; padding: 60px 40px; max-width: 1400px; margin: auto; }}
        .card {{ background: var(--card-bg); border-radius: 20px; overflow: hidden; border: 1px solid #334155; transition: 0.4s; text-decoration: none; color: inherit; }}
        .card:hover {{ transform: translateY(-10px); border-color: var(--primary); box-shadow: 0 20px 40px rgba(56, 189, 248, 0.2); }}
        .card img {{ width: 100%; height: 200px; object-fit: cover; }}
        .card-body {{ padding: 25px; }}
        .card h3 {{ color: var(--primary); margin: 0 0 10px 0; font-size: 1.4rem; }}
        footer {{ text-align: center; padding: 60px; border-top: 1px solid #334155; color: #64748b; }}
    </style>
</head>
<body>
    <nav>
        <a href="index.html" style="color:var(--primary); font-size:1.6rem; font-weight:900; text-decoration:none;">EARNSMART</a>
        <div class="nav-links">
            <a href="index.html">Home</a>
            <a href="about.html">About</a>
            <a href="contact.html">Contact</a>
            <a href="privacy.html">Privacy</a>
        </div>
    </nav>
    <div class="hero">
        <h1>100+ Premium Wealth Blueprints</h1>
        <p>Your Automated Gateway to the 2026 Digital Economy</p>
        <input type="text" id="searchBar" placeholder="Search 100+ guides..." onkeyup="filterBlogs()">
    </div>
    <div class="grid" id="blogGrid">
"""

for i, title in enumerate(titles, 1):
    img = images[i % 6]
    index_content += f"""
        <a href="blog{i}.html" class="card">
            <img src="{img}" alt="{title}">
            <div class="card-body">
                <h3>{title}</h3>
                <p>Comprehensive 2000+ word expert analysis and automation roadmap.</p>
            </div>
        </a>"""

index_content += """
    </div>
    <footer>
        <p>&copy; 2025-2026 EarnSmart Global Authority</p>
        <a href="privacy.html" style="color:#64748b; text-decoration:none;">Privacy Policy</a> | 
        <a href="about.html" style="color:#64748b; text-decoration:none;">About Us</a>
    </footer>
    <script>
        function filterBlogs() {
            let input = document.getElementById('searchBar').value.toLowerCase();
            let cards = document.getElementsByClassName('card');
            for (let i = 0; i < cards.length; i++) {
                let title = cards[i].getElementsByTagName('h3')[0].innerText.toLowerCase();
                cards[i].style.display = title.includes(input) ? "" : "none";
            }
        }
    </script>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(index_content)
print("✔ index.html updated with 100 Pro Cards!")

