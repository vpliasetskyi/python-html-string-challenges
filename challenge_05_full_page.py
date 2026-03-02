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

# Update lang and title using .replace()

lang = "es"
new_title = "Full Page Challenge"

html = html.replace('<html lang="en">', f'<html lang="{lang}">' )
html = html.replace('<title>My Page</title>', f'<title>{new_title}</title>')

# Update  style and script using find()

new_style = "app.min.css"
new_script = "main.bandle.js"

st_start_index = html.find('href="',) + len('href="')
st_end_index = html.find('">', st_start_index)

html = html[:st_start_index] + new_style + html[st_end_index:]

scr_start_index = html.find('src="') + len('src="')
scr_end_index = html.find('"></script>',scr_start_index)

html = html[:scr_start_index] + new_script + html[scr_end_index:]

# Validate style and script changes 

style_count = html.count('style.css')
script_count = html.count('app.js')

def val_style_js(): 
    if   style_count == 0 and script_count == 0:
    
     print("style.css and app.js successfully removed!")

    elif style_count > 0:

     print("style.css was not removed!")
 
    elif script_count > 0:
     
     print("app.js was not removed!")

# Heading injection 

h1 = "Python is a snake!"
h2 = "Python lives in jungles!"
h3 = "Python is a predator!"

split_html = html.split('<body>')

part_0 = split_html[0]
part_1 = split_html[1]

body_content = f""" 
    <h1>{h1}</h1> 
    <h2>{h2}</h2> 
    <h3>{h3}</h3>"""

html = part_0 + "<body>" + body_content + part_1

# Add paragraph and image content 

paragraph_text = "This project was built entirely by Python from Jungles using kill methods."
img_src = "python killer.jpg"
img_alt = "A python image for the page"

p_tag = f"<p>{paragraph_text}</p>"
img_tag = "<img src=\"" + img_src +  "\" alt=\"" + img_alt + "\">"

h1_index = html.rfind("</h1>")
h2_index = html.rfind("</h2>")
h3_index = html.rfind("</h3>")

last_h_index = max(h1_index,h2_index,h3_index)

heading_tag_end = last_h_index + len("</h3>")

added_content = f"\n    {p_tag}\n    {img_tag}"

html = html[:heading_tag_end] + added_content + html[heading_tag_end:]



#Add second paragraph fom title 

title_start_index = html.find('<title>') + len('<title>')
title_end_index = html.find('</title>')

extract_title = html[title_start_index : title_end_index]

p2_content = f"""    <p>This is extracted by Python title {extract_title}</p>"""

body_close_tag = html.find('</body>')

html = html[:body_close_tag] + p2_content + html[body_close_tag:]

# Final validation 

strip_html = html.strip()

def final_valiation():
      
    title_here = html.count('<title>Full Page Challenge</title>') > 0
    
    h1_here = html.count('<h1>') > 0
    h2_here = html.count('<h2>') > 0
    h3_here = html.count('<h3>') > 0

    image_here = html.count('<img') == 1
    p_count = html.count('<p>') == 2

    doctype_here = strip_html.startswith('<!DOCTYPE html>') == True
    close_here = strip_html.endswith('</html>') == True

    print("\n   Validation Report   ")
    print("-------------------------")

    print(f"{'✅' if title_here else '❌'} <title> is correct")
    print(f"{'✅' if h1_here else '❌'} <h1> found")
    print(f"{'✅' if h2_here else '❌'} <h2> found")
    print(f"{'✅' if h3_here else '❌'} <h3> found")
    print(f"{'✅' if image_here else '❌'} <img> appears exactly once")
    print(f"{'✅' if p_count else '❌'} <p> appears exactly twice")
    print(f"{'✅' if doctype_here else '❌'} Starts with <!DOCTYPE html>")
    print(f"{'✅' if close_here else '❌'} Ends with </html>")

    print("-------------------------")
  

val_style_js()
final_valiation()
print(html)
    






