html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Page</title>
    <link rel="stylesheet" href="styles.css">
    <script src="app.js"></script>
</head>
<body> 
    <h1>Welcome to Wonderland</h1> 
    <h2>About this rabbit hole</h2> 
    <h3>Escape technical details</h3>
</body>
</html>
"""
# Define  variables

paragraph_text = "This project was built entirely using Python string methods."
img_src = "hero.jpg"
img_alt = "A hero image for the page"

# Build tags for paragraph and sourse image 

p_tag = f"<p>{paragraph_text}</p>"
img_tag = "<img src=\"" + img_src +  "\" alt=\"" + img_alt + "\">"

# Use .rfind() to find the last closing tag 

h1_place = html.rfind("</h1>")
h2_place = html.rfind("</h2>")
h3_place = html.rfind("</h3>")

# Define last closing tag by index

last_heading_index = max(h1_place, h2_place, h3_place)

# Find end of index of the last tag

heading_end = last_heading_index + len("</h3>")

#Add content and concatenates 

added_content = f"\n    {p_tag}\n    {img_tag}"

html = html[:heading_end] + added_content + html[heading_end:]

print(html)