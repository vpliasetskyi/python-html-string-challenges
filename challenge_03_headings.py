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
</body>
</html>"""

# Create headings variables 

h1 = "Welcome to Wonderland" 
h2 = "About this rabbit hole" 
h3 = "Escape technical details"

# Split html

body_break = html.split('<body>')

# Define index variables

heading_start_index = int(html.find('<body>') + len('<body>'))
heading_end_index = int(html.find('</body>') - len('</body>'))

part_0 = body_break[0] + '<body>'
part_1 = body_break[1] 

body_content = f""" 
    <h1>{h1}</h1> 
    <h2>{h2}</h2> 
    <h3>{h3}</h3>"""

# Combine body content and html

html = part_0  + body_content + part_1


print(html)
