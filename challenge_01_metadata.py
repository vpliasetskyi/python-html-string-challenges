html = """
<!DOCTYPE html>
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
</html>
"""
page_title = "Happiness course"
page_lang  = "fr"
html = html.replace("<title>My Page</title>",  f'<title>{page_title}</title>')
html = html.replace('<html lang="en">', f'<html lang="{page_lang}">')
print(html)

# We did't use count argument while using .replace(), because our variable does not have repeating text.
# Count argument might be used to define how many occupances of the same value we wanna replace.