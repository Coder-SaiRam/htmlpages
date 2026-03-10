import os
import re

INDEX_FILE = "index.html"
SOURCE_DIR = "source/pages"

START_MARKER = "<!-- AUTO-CARDS-START -->"
END_MARKER = "<!-- AUTO-CARDS-END -->"

icons = {
    "docker": "🐳",
    "kubernetes": "☸️",
    "thread": "🧵",
    "spring": "🌱",
    "security": "🔐",
    "sql": "🗄️"
}

# Read index.html
with open(INDEX_FILE, "r", encoding="utf-8") as f:
    html = f.read()

cards = []

for file in sorted(os.listdir(SOURCE_DIR)):

    if not file.endswith(".html"):
        continue

    title = file.replace(".html", "").replace("-", " ").title()

    icon = "📄"
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

# Replace ENTIRE marker block
html = re.sub(
    f"{START_MARKER}.*?{END_MARKER}",
    new_section,
    html,
    flags=re.DOTALL
)

with open(INDEX_FILE, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Generated {len(cards)} cards successfully.")
