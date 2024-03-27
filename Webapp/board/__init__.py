# Inside DividedWeFall/Webapp/board/__init__.py
import sys
import os
from flask import Flask, request, jsonify, render_template, send_from_directory

# Adjust the Python path to include the directory where webscraper.py is located
basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(basedir)

# Now, import the inference function from your webscraper module
from webscraping.webscraper import inference

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    url = data['url']

    # Call the inference function from your web scraper
    scores = inference(url)

    # Return the bias scores as JSON
    return jsonify({"scores": scores})

@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory('Images', filename)

if __name__ == '__main__':
    app.run(debug=True)
