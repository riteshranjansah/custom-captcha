from flask import Flask, render_template, session, request, redirect, url_for
from PIL import Image, ImageDraw, ImageFont, ImageOps
import random
import os

app = Flask(__name__)
app.secret_key = 'verysecretkey'

def draw_bg(size):
    bg_image = Image.new('RGB', size)
    pixels = bg_image.load()
    for i in range(size[0]):
        for j in range(size[1]):
            pixels[i, j] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return bg_image

def create_captcha_images(rotations, bg_size=(100, 100)):
    for rotation in rotations:    
        char = random.choice('12457ABDEFGJKLMPQRTUVWY')
        image = draw_bg(bg_size)
        text_image = Image.new('RGBA', bg_size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(text_image)
        try:
            font = ImageFont.truetype("arial.ttf", 48)
        except IOError:
            font = ImageFont.load_default()
        text_length = draw.textlength(char, font=font)
        text_x = (bg_size[0] - text_length) / 2
        text_y = (bg_size[1] - text_length) / 2
        draw.text((text_x, text_y), char, font=font, fill=(0, 0, 0, 255))
        rotated_text_image = text_image.rotate(rotation, expand=1)
        final_image = ImageOps.fit(image, rotated_text_image.size, centering=(0.5, 0.5))
        final_image = Image.alpha_composite(final_image.convert('RGBA'), rotated_text_image)
        final_image = final_image.convert('RGB')
        final_image.save(f'static/captcha_{rotation}.png')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_response = int(request.form['rotation'])
        correct_answer = session['correct_rotation']
        print(correct_answer,user_response)
        if user_response == correct_answer:
            return "You are human"
        else:
            return "You are a bot"
        
    rotations = [0, 45, 90, 135, 180, 225, 270, 315]
    session['correct_rotation'] = random.choice(rotations)
    create_captcha_images(rotations)
    return render_template('index.html', rotations=rotations, correct_rotation=session['correct_rotation'])



