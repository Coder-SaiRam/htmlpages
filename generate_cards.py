import os
import re

START_MARKER = "<!-- AUTO-CARDS-START -->"
END_MARKER = "<!-- AUTO-CARDS-END -->"

icons = {
    "docker": "🐳",
    "kubernetes": "☸️",
    "thread": "🧵",
    "spring": "🌱",
    "security": "🔐"
}

cards = []

for file in os.listdir("."):

    if file.endswith(".html") and file != "index.html":

        title = file.replace(".html","").replace("-"," ").title()

        icon = "📄"

        for key in icons:
            if key in file.lower():
                icon = icons[key]

        card = f"""
<div class="card" onclick="openPage('{file}')">
<div class="card-icon">{icon}</div>
<div class="card-title">{title}</div>
<div class="card-desc">
Deep dive documentation for {title}
</div>
</div>
"""

        cards.append(card)

generated_cards = "\n".join(sorted(cards))

with open("index.html","r") as f:
    content = f.read()

pattern = re.compile(
    f"{START_MARKER}.*?{END_MARKER}",
    re.DOTALL
)

replacement = f"{START_MARKER}\n{generated_cards}\n{END_MARKER}"

new_content = pattern.sub(replacement, content)

with open("index.html","w") as f:
    f.write(new_content)

print("Index updated successfully.")
