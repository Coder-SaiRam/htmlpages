import os

cards = ""

for file in os.listdir("."):
    if file.endswith(".html") and file != "index.html":
        name = file.replace(".html", "").replace("-", " ").title()

        cards += f"""
        <div class="card" onclick="openPage('{file}')">
            <div class="card-icon">📄</div>
            <div class="card-title">{name}</div>
            <div class="card-desc">
                Deep dive documentation for {name}
            </div>
        </div>
        """

index_template = f"""
<!DOCTYPE html>
<html>
<head>
<title>Sai Portfolio</title>
<link rel="stylesheet" href="style.css">
</head>

<body>

<h1>🚀 Sai's Tech Deep Dives</h1>

<div class="container">

{cards}

</div>

<script>
function openPage(url){{
window.open(url,"_blank");
}}
</script>

</body>
</html>
"""

with open("index.html","w") as f:
    f.write(index_template)
