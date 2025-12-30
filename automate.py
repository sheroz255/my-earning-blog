import os
import requests
from datetime import datetime

# Yahan hum AI ka use karke content mangwayenge (Gemini API use ho sakti hai)
def get_ai_blog():
    # Example: Simple content (Asliyat mein yahan API call hogi)
    return "# New Earning Trick\nThis is a 2000+ words blog content..."

def upload_to_github():
    title = f"blog-{datetime.now().strftime('%Y%m%d')}.html"
    content = get_ai_blog()
    
    # File save karna
    with open(title, "w") as f:
        f.write(content)
    
    # GitHub par push karna
    os.system("git add .")
    os.system('git commit -m "Auto daily blog update"')
    os.system("git push origin main")

if __name__ == "__main__":
    upload_to_github()
    print("Blog automated and uploaded!")

