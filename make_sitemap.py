import datetime

base_url = "https://sheroz255.github.io/my-earning-blog/"
pages = ["index.html", "about.html", "contact.html", "privacy.html"]
for i in range(1, 31):
    pages.append(f"blog{i}.html")

now = datetime.datetime.now().strftime("%Y-%m-%d")

sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for page in pages:
    sitemap_content += f'  <url>\n'
    sitemap_content += f'    <loc>{base_url}{page}</loc>\n'
    sitemap_content += f'    <lastmod>{now}</lastmod>\n'
    sitemap_content += f'    <priority>{"1.0" if page == "index.html" else "0.8"}</priority>\n'
    sitemap_content += f'  </url>\n'

sitemap_content += '</urlset>'

with open("sitemap.xml", "w") as f:
    f.write(sitemap_content)

print("✅ New sitemap.xml generated successfully!")

