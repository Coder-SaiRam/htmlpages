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

# Load index.html
with open("index.html", "r") as f:
    content = f.read()

# Extract current cards section
pattern = re.compile(
    f"{START_MARKER}(.*?){END_MARKER}",
    re.DOTALL
)

match = pattern.search(content)

existing_section = ""

if match:
    existing_section = match.group(1)

# Detect already loaded html files
loaded_files = set(
    re.findall(r"openPage\('([^']+)'\)", existing_section)
)

cards_to_add = []

for file in os.listdir("."):

    if file.endswith(".html") and file != "index.html":

        if file not in loaded_files:

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

            cards_to_add.append(card)

# Combine existing + new cards
updated_section = existing_section + "\n".join(cards_to_add)

replacement = f"{START_MARKER}\n{updated_section}\n{END_MARKER}"

new_content = pattern.sub(replacement, content)

# Save updated index
with open("index.html", "w") as f:
    f.write(new_content)

print(f"{len(cards_to_add)} new cards added.")
