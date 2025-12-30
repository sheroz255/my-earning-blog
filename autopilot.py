import os
import subprocess

def run_command(command):
    try:
        print(f"🚀 Running: {command}")
        result = subprocess.run(command, shell=True, check=True, text=True)
        return result
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running command: {command}\n{e}")

# 1. Blogs Update Karein (2000+ words unique content)
print("📝 Updating Blogs...")
run_command("python creator.py")

# 2. Homepage (index.html) Update Karein (3D UI & Search)
print("🏠 Updating Home Page...")
run_command("python update_index.py")

# 3. Legal Pages Update Karein
print("⚖️ Updating Legal Pages...")
run_command("python make_legal.py")

# 4. Sitemap Refresh Karein (For Google Search Console)
print("xml Refreshing Sitemap...")
run_command("python make_sitemap.py")

# 5. GitHub Par Push Karein
print("📤 Pushing to GitHub...")
run_command("git add .")
run_command('git commit -m "Auto-update: New long-form content and UI fixes"')
run_command("git push origin main --force")

print("✅ ALL TASKS COMPLETED SUCCESSFULLY!")

