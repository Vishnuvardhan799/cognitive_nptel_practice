import os
import re

file_path = "CogniQuiz.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Extract CSS
style_pattern = re.compile(r"<style>(.*?)</style>", re.DOTALL)
style_match = style_pattern.search(content)
if style_match:
    with open("style.css", "w", encoding="utf-8") as f:
        f.write(style_match.group(1).strip())
    content = style_pattern.sub('<link rel="stylesheet" href="style.css">', content)

# Extract scripts
script_pattern = re.compile(r"<script>(.*?)</script>", re.DOTALL)
scripts = script_pattern.findall(content)

if len(scripts) >= 2:
    with open("data.js", "w", encoding="utf-8") as f:
        f.write(scripts[0].strip())
    with open("script.js", "w", encoding="utf-8") as f:
        f.write(scripts[1].strip())
    
    # Replace first script with <script src="data.js"></script>
    content = content.replace(f"<script>{scripts[0]}</script>", '<script src="data.js"></script>')
    # Replace second script with <script src="script.js"></script>
    content = content.replace(f"<script>{scripts[1]}</script>", '<script src="script.js"></script>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Files extracted successfully.")
