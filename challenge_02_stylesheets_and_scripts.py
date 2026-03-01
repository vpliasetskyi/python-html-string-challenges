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
# Define substitute links values

stylesheet = "main.min.css"
script_file = "bundle.js"

# Find start and end index of style.css usinf .find()

style_start_index = html.find('href="') + len('href="')
style_end_index = html.find('">', style_start_index)

# Update html variable with the new value

html = html[:style_start_index] + stylesheet + html[style_end_index:]

# Find start and end of script by using .index() and .find() combined

script_start_index = int(html.index('src="') + len('src="'))
script_find_break = int(html.find('</head>'))
script_end_index = int(html.find('">', script_start_index, script_find_break))

# Update html value with new script file value 

html = html[:script_start_index] + script_file + html[script_end_index:]

print(html)