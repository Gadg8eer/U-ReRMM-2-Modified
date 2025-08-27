import re
from PIL import Image, ImageDraw

print("Script started.")

try:
    with open('templates.txt', encoding='utf-8') as f:
        text = f.read()
    print("Loaded templates.txt.")
except Exception as e:
    print("Failed to open templates.txt:", e)
    exit(1)

precomb_block = re.search(
    r'template\s+tmpl_precombined_type\s*\(\)\s*\{([\s\S]*?)\}',
    text, re.MULTILINE)
if not precomb_block:
    print("tmpl_precombined_type() not found.")
    exit(1)
precomb_block = precomb_block.group(1)

tiles = re.findall(r'precombined_tile\s*\(\s*([-+]?\d+)\s*,\s*([-+]?\d+)\s*\)', precomb_block)
if not tiles:
    print("No precombined_tile(x, y) found.")
    exit(1)
tiles = [(int(x), int(y)) for x, y in tiles]
print("Number of tile boxes:", len(tiles))

w, h = 64, 31
max_x = max(x for x, y in tiles) + w
max_y = max(y for x, y in tiles) + h
img_w = max_x
img_h = max_y
print("PNG size will be {}x{}".format(img_w, img_h))

img = Image.new('RGBA', (img_w, img_h), (255, 255, 255, 0))
draw = ImageDraw.Draw(img)

for x, y in tiles:
    draw.rectangle([x, y, x + w - 1, y + h - 1], outline=(0, 0, 255, 255), width=2)
print("All rectangles drawn.")

img.save('precombined_template.png')
print("Saved as precombined_template.png")
