import os
import subprocess
from datetime import datetime

def run_command(command):
    subprocess.run(command, shell=True)

print(f"🚀 Autopilot started at: {datetime.now()}")

# 1. Naye blogs generate karein (Humaara purana creator script)
print("📝 Generating/Updating Blogs...")
run_command("python creator.py")

# 2. Sitemap update karein
print("xml Updating Sitemap...")
run_command("python make_sitemap.py")

# 3. GitHub par upload karein
print("📦 Pushing to GitHub...")
run_command("git add .")
run_command("git commit -m 'Daily Auto-Update: ' " + str(datetime.now()))
run_command("git push origin main")

print("✅ All tasks completed successfully!")

