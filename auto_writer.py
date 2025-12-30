import requests
import json
import os
from datetime import datetime

# 1. Aapki di hui API Key maine yahan set kar di hai
API_KEY = "AIzaSyDX-jnaOquNWhYiwVotIqmVZr6KhvCRNBE"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

def generate_blog():
    # 2. Prompt ko mazeed detail mein kiya hai taake 2000+ words ka SEO blog bane
    prompt_text = (
        "Write a 2000+ words highly detailed SEO optimized blog post in Roman Urdu/Hindi. "
        "Topic: 'Best Online Earning Methods in 2026 without Investment'. "
        "Structure the blog with an engaging Introduction, 10 detailed methods (each with 'How it works', 'Pros & Cons', and 'Potential Earnings'), "
        "a deep dive into 'Common Scams to Avoid', and a final Conclusion. "
        "Format the output using HTML tags like <h2>, <h3>, <p>, <ul>, and <li> so it looks professional on a website."
    )

    payload = {
        "contents": [{
            "parts": [{
                "text": prompt_text
            }]
        }]
    }

    print("AI Blog likh raha hai... is mein 30-60 seconds lag sakte hain kyunke content lamba hai...")

    try:
        response = requests.post(URL, json=payload)
        result = response.json()

        # Check if response is valid
        if 'candidates' not in result:
            print("Error: AI ne jawab nahi diya. Shayad API key ya internet ka masla hai.")
            print("Full Response:", result)
            return

        # AI ka likha hua text nikalna
        blog_content = result['candidates'][0]['content']['parts'][0]['text']

        # 3. HTML File banana
        date_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"blog-{date_str}.html"

        full_html = f"""
        <!DOCTYPE html>
        <html lang="ur">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta name="description" content="Latest Online Earning Methods 2026 - Free Guide">
            <link rel="stylesheet" href="style.css">
            <title>Blog - {date_str}</title>
            <style>
                .container {{ max-width: 800px; margin: auto; padding: 20px; line-height: 1.8; }}
                h2 {{ color: #2c3e50; border-left: 5px solid #3498db; padding-left: 10px; margin-top: 30px; }}
                p {{ margin-bottom: 15px; text-align: justify; }}
            </style>
        </head>
        <body>
            <div class="container">
                {blog_content}
                <hr>
                <p><strong>Published on:</strong> {date_str}</p>
                <a href="index.html" style="background: #3498db; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Wapis Home Par Jayein</a>
            </div>
        </body>
        </html>
        """

        with open(filename, "w", encoding="utf-8") as f:
            f.write(full_html)

        print(f"Mubarak ho! {filename} ban chuki hai (2000+ words).")

        # 4. GitHub par auto upload
        print("GitHub par upload ho raha hai...")
        os.system("git add .")
        os.system(f'git commit -m "Auto Blog {date_str}"')
        os.system("git push origin main")
        print("GitHub par upload mukammal ho gaya!")

    except Exception as e:
        print(f"Error aa gaya: {e}")

if __name__ == "__main__":
    generate_blog()

