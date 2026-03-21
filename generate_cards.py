import os
import re
from collections import defaultdict

INDEX_FILE = "index.html"
SOURCE_DIR = "/pages"

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

print("Scanning pages directory (ONLY nested folders)...")

# folder → list of cards
grouped_cards = defaultdict(list)

for root, dirs, files in os.walk(SOURCE_DIR):
    for file in files:

        if not file.endswith(".html"):
            continue

        full_path = os.path.join(root, file)

        # relative path from "pages"
        relative_path = os.path.relpath(full_path, "pages")

        parts = relative_path.split(os.sep)

        # ✅ Only allow /pages/<folder>/<file>.html
        if len(parts) != 3:
            continue

        # folder name
        folder = parts[1].replace("-", " ").title()

        # title from file
        title = file.replace(".html", "").replace("-", " ").title()

        # icon detection
        icon = "🪟"
        for key in icons:
            if key in file.lower():
                icon = icons[key]
                break

        card = f"""
<div class="card" onclick="openPage('{relative_path}')">
    <div class="card-icon">{icon}</div>
    <div class="card-title">{title}</div>
    <div class="card-desc">
        Deep dive documentation for {title}
    </div>
</div>
"""

        grouped_cards[folder].append(card)

print("Generating sections...")

sections = []

for folder in sorted(grouped_cards.keys()):
    cards_html = "\n".join(sorted(grouped_cards[folder]))

    section = f"""
<div class="section">
    <h2 class="section-title">{folder}</h2>
    <div class="card-container">
        {cards_html}
    </div>
</div>
"""
    sections.append(section)

final_html = "\n".join(sections)

new_section = f"""
{START_MARKER}

{final_html}

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

print(f"Generated sections: {len(grouped_cards)} 🚀")