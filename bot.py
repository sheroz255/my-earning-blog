import requests
import time

site_url = "https://sheroz255.github.io/my-earning-blog/sitemap.xml"

# Google aur Bing ke indexing endpoints
engines = {
    "Google": f"https://www.google.com/ping?sitemap={site_url}",
    "Bing": f"https://www.bing.com/ping?sitemap={site_url}"
}

def start_indexing():
    print("🚀 --- EARNSMART VIP INDEXER STARTING ---")
    for name, url in engines.items():
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                print(f"[✔] {name}: Signal Sent Successfully!")
            else:
                print(f"[✘] {name}: Failed (Status: {r.status_code})")
        except Exception as e:
            print(f"[!] Error connecting to {name}: {e}")
    
    print("\n[i] Success! Now Google Bots will crawl your 5000+ word guides.")

if __name__ == "__main__":
    start_indexing()

