import os
import re

START_MARKER = "<!-- AUTO-CARDS-START -->"
END_MARKER = "<!-- AUTO-CARDS-END -->"

SOURCE_DIR = "./source/pages"

icons = {
    "docker": "🐳",
    "kubernetes": "☸️",
    "thread": "🧵",
    "spring": "🌱",
    "security": "🔐",
    "sql": "🗄️"
}

# Load index.html
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

cards = []

# Scan all html pages
for file in sorted(os.listdir(SOURCE_DIR)):

    if file.endswith(".html") and file != "index.html":

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

new_cards_section = "\n".join(cards)

# Replace content between markers
pattern = re.compile(
    f"{START_MARKER}(.*?){END_MARKER}",
    re.DOTALL
)

replacement = f"{START_MARKER}\n\n{new_cards_section}\n\n{END_MARKER}"

new_content = pattern.sub(replacement, content)

# Save index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"{len(cards)} cards generated successfully.")
