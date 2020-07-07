# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont


font = ImageFont.truetype('./fonts/Italic.ttf', 20)
image = Image.open('./pics/demo.png')
draw = ImageDraw.Draw(image)
draw.text((100, 200), 'Hello world', (255, 255, 255), font=font)
image.save('./output/new_img.png')
