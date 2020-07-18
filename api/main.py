from PIL import Image, ImageDraw, ImageFont
from http.server import HTTPServer, BaseHTTPRequestHandler
from flask import Flask, send_file, render_template
import io

app = Flask(__name__)

FONT_SIZE = 20
CURSOR_WIDTH = 5
CURSOR_HEIGHT = FONT_SIZE

def createBanner(stream: io.BytesIO):
    # text = "Hi, I am Vaibhav."
    # gif = []
    # pixel = [10, 10]
    # fnt = ImageFont.truetype("fonts/Roboto-Regular.ttf", FONT_SIZE)

    # prev_im = Image.new("RGB", (700, 150), (255,255,255))

    # for i in range(len(text)):
    #     temp_im = prev_im
    #     d = ImageDraw.Draw(temp_im)
    #     d.text(tuple(pixel), text[i], font=fnt, fill=(0, 0, 0))
    #     size = d.textsize(text[i], font=fnt)
    #     pixel[0] += size[0]
    #     prev_im = temp_im.copy()
    #     d.rectangle([pixel[0], pixel[1], pixel[0]+CURSOR_WIDTH, pixel[1]+CURSOR_HEIGHT], fill=(0,0,0))
    #     gif.append(temp_im)
    
    # gif[0].save(stream, format="GIF", save_all=True, append_images=gif[1:], duration=100)
    im = Image.open("static/stock.jpg")
    im.save(stream, format="JPEG")
    return

@app.route('/api/main')
def serve_image():
    stream = io.BytesIO() # Create a in memory byte stream
    try:
        createBanner(stream)
        stream.seek(0) # HACK
        return send_file(stream, mimetype="image/jpeg")
    except Exception as e:
        return str(e)