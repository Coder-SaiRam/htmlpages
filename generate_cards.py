import os
import re

INDEX_FILE = "index.html"
SOURCE_DIR = "source/pages"

START_MARKER = "<!-- AUTO-CARDS-START -->"
END_MARKER = "<!-- AUTO-CARDS-END -->"

icons = {
    "docker": "🐳",
    "kubernetes": "☸️",
    "thread": "🧶",
    "spring": "🌱",
    "security": "🔐",
    "sql": "🗄️",
    "solid": "🏗️",
    "recursion": "🔄",
    "graph": "📈",
    "java": "☕",
    "trees": "🌳"
}

print("Reading index.html...")

with open(INDEX_FILE, "r", encoding="utf-8") as f:
    html = f.read()

cards = []

print("Scanning pages directory...")

for file in sorted(os.listdir(SOURCE_DIR)):

    if not file.endswith(".html"):
        continue

    title = file.replace(".html", "").replace("-", " ").title()

    icon = "🪟"
    for key in icons:
        if key in file.lower():
            icon = icons[key]
            break

    card = f"""
<div class="card" onclick="openPage('source/pages/{file}')">
    <div class="card-icon">{icon}</div>
    <div class="card-title">{title}</div>
    <div class="card-desc">
        Deep dive documentation for {title}
    </div>
</div>
"""

    cards.append(card)

cards_html = "\n".join(cards)

new_section = f"""
{START_MARKER}

{cards_html}

{END_MARKER}
"""

pattern = re.compile(
    r"<!--\s*AUTO-CARDS-START\s*-->.*?<!--\s*AUTO-CARDS-END\s*-->",
    re.DOTALL
)

html = pattern.sub(new_section, html)

print("Writing updated index.html...")

with open(INDEX_FILE, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Generated {len(cards)} cards successfully.")
