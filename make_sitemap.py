import datetime

base_url = "https://sheroz255.github.io/my-earning-blog/"
blogs = [f"blog{i}.html" for i in range(1, 31)]
today = datetime.date.today().isoformat()

sitemap_content = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sitemap_content += f'  <url>\n    <loc>{base_url}</loc>\n    <lastmod>{today}</lastmod>\n    <priority>1.0</priority>\n  </url>\n'

for blog in blogs:
    sitemap_content += f'  <url>\n    <loc>{base_url}{blog}</loc>\n    <lastmod>{today}</lastmod>\n    <priority>0.8</priority>\n  </url>\n'

sitemap_content += '</urlset>'

with open("sitemap.xml", "w") as f:
    f.write(sitemap_content)
print("✔ Sitemap.xml created with 30 blogs!")

