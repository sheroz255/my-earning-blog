import requests
from bs4 import BeautifulSoup

# Aapka Website URL set kar diya gaya hai
url = "https://sheroz255.github.io/my-earning-blog/"

try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    print(f"--- SEO AUDIT REPORT FOR: {url} ---\n")

    # 1. Title Check
    title = soup.find('title')
    print(f"[✔] Title: {title.string if title else 'MISSING!'}")

    # 2. Images Alt Tags Check
    images = soup.find_all('img')
    missing_alt = 0
    for i, img in enumerate(images):
        if not img.get('alt'):
            missing_alt += 1

    if missing_alt > 0:
        print(f"[✘] Warning: {missing_alt} images are missing ALT tags! (Google won't index these properly)")
    else:
        print("[✔] All images have Alt tags.")

    # 3. Links Check
    links = soup.find_all('a')
    print(f"[i] Total Links Found: {len(links)}")

    # 4. Meta Description Check
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    if meta_desc:
        print(f"[✔] Meta Description: {meta_desc['content'][:50]}...")
    else:
        print("[✘] ERROR: Meta Description is MISSING!")

except Exception as e:
    print(f"Error connecting to site: {e}")


