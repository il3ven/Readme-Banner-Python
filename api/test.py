from flask import Flask, Response
app = Flask(__name__)

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
@app.route('/api/test')
def catch_all():
    return Response("<h1>Flask</h1><p>You visited:</p>", mimetype="text/html")