from flask import Flask, Response
app = Flask(__name__)

@app.route('/api/test')
def catch_all():
    return Response("<h1>Flask</h1>", mimetype="text/html")