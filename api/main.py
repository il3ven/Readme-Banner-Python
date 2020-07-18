import sys
from flask import Flask, send_file, render_template
from banner import createBanner
import io

app = Flask(__name__)

@app.route('/api/main')
def serve_image():
    stream = io.BytesIO() # Create a in memory byte stream
    try:
        createBanner(stream)
        stream.seek(0) # HACK
        return send_file(stream, mimetype="image/gif")
    except Exception as e:
        return str(e)