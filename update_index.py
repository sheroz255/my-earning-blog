import os

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

index_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="google-site-verification" content="X4FP-y7MQmptGMN" />
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-RPNNLFJ22K"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-RPNNLFJ22K');</script>
    <script type="text/javascript" src="https://pl28282752.effectivegatecpm.com/ba/73/ea/ba73ea6d4cc4e7b1ca664d63c70dc7e7.js"></script>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EarnSmart | Global Authority 2026</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;700;800&display=swap');
        :root {{ --primary: #38bdf8; --bg: #020617; --surface: #0f172a; }}
        body {{ background: var(--bg); color: #fff; font-family: 'Plus Jakarta Sans', sans-serif; margin: 0; }}
        nav {{ background: rgba(2, 6, 23, 0.9); backdrop-filter: blur(10px); padding: 15px 5%; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 1000; border-bottom: 1px solid #1e293b; }}
        .logo {{ font-size: 1.5rem; font-weight: 800; color: var(--primary); text-decoration: none; letter-spacing: -1px; }}
        .nav-links a {{ color: #94a3b8; text-decoration: none; margin-left: 20px; font-weight: 600; font-size: 0.9rem; }}
        .hero {{ padding: 100px 5%; text-align: center; background: radial-gradient(circle at 50% 50%, #1e293b 0%, #020617 100%); }}
        h1 {{ font-size: clamp(2.5rem, 8vw, 4rem); margin-bottom: 15px; letter-spacing: -2px; }}
        .search-box {{ width: 100%; max-width: 600px; padding: 15px 25px; border-radius: 12px; border: 1px solid #334155; background: var(--surface); color: white; font-size: 1rem; margin-top: 30px; outline: none; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 25px; padding: 50px 5%; }}
        .card {{ background: var(--surface); border-radius: 16px; overflow: hidden; border: 1px solid #1e293b; transition: 0.3s; text-decoration: none; color: inherit; }}
        .card:hover {{ transform: translateY(-5px); border-color: var(--primary); box-shadow: 0 15px 30px rgba(0,0,0,0.4); }}
        .card img {{ width: 100%; height: 180px; object-fit: cover; }}
        .card-body {{ padding: 20px; }}
        .card h3 {{ color: var(--primary); margin: 0 0 10px 0; font-size: 1.2rem; }}
        .card p {{ color: #94a3b8; font-size: 0.85rem; line-height: 1.5; }}
        footer {{ text-align: center; padding: 50px; border-top: 1px solid #1e293b; color: #475569; }}
    </style>
</head>
<body>
    <nav>
        <a href="index.html" class="logo">EARNSMART<span style="color:#fff">.</span></a>
        <div class="nav-links">
            <a href="about.html">About</a>
            <a href="contact.html">Contact</a>
            <a href="privacy.html">Privacy</a>
        </div>
    </nav>
    <div class="hero">
        <h1>Global Wealth Intelligence</h1>
        <p style="color:#94a3b8; font-size:1.2rem;">Premium automation blueprints for the 2026 digital era.</p>
        <input type="text" id="searchBar" class="search-box" placeholder="Search 100+ guides..." onkeyup="filterBlogs()">
    </div>
    <div class="grid" id="blogGrid">
"""

for i, title in enumerate(titles, 1):
    kw = title.replace(" ", ",").lower()
    index_content += f"""
        <a href="blog{i}.html" class="card">
            <img src="https://source.unsplash.com/400x250/?{kw}" alt="{title}">
            <div class="card-body">
                <h3>{title}</h3>
                <p>Access the exclusive 2026 masterclass on {title} with automated workflows.</p>
            </div>
        </a>"""

index_content += """
    </div>
    <footer>&copy; 2025 EarnSmart Authority | High-Fidelity Content Hub</footer>
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
print("✔ index.html updated with Premium UI!")

