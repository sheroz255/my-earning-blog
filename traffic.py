import random

base_url = "https://sheroz255.github.io/my-earning-blog/"

blogs = [
    "TikTok Automation Masterclass", "AI Crypto Trading Bot", "AI Side Hustles",
    "Digital Assets Investment", "Freelance Professional Guide", "Web Development Strategy",
    "E-commerce Profit Plan", "Social Media Growth", "YouTube Cashcow Secrets",
    "Instagram Wealth Strategy", "Stock Market Mastery", "Virtual Assistant Training",
    "App Creator Business", "Cyber Security Expert", "Professional Video Editing",
    "Graphic Design Course", "Dropshipping Business", "Ebook Selling Profits",
    "SaaS Startup Guide", "AI Training Modules", "UI/UX Design Trends",
    "Payment Gateways 2026", "Python Automation Bots", "Gaming Stream Revenue",
    "Adsterra Revenue Secrets", "Voiceover AI Tools", "NFT Trading Profits",
    "Remote SEO Jobs", "Stock Trading Strategy", "Pinterest Viral Traffic"
]

captions = [
    "🔥 Urgent: This hidden tool is paying $500 daily. Check the full 5000-word guide here:",
    "🚀 Stop wasting time! Learn how to automate your income in 2026. Full details:",
    "⚠️ System Alert: New earning loophole found in {topic}. Access the VIP guide:",
    "💰 My student made $1200 using this exact method. No experience needed:",
    "💎 Exclusive: The secret blueprint for {topic} is now public. Read now:"
]

print("--- EARNSMART SOCIAL TRAFFIC GENERATOR ---")
for i in range(5): # 5 Random posts generate karega
    idx = random.randint(0, 29)
    topic = blogs[idx]
    link = f"{base_url}blog{idx+1}.html"
    cap = random.choice(captions).format(topic=topic)
    print(f"\nPOST {i+1}:\n{cap}\n{link}\n" + "-"*30)

