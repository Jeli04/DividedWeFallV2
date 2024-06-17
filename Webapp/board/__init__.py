from flask import Flask, render_template, send_from_directory, request, jsonify
import webscraping.webscraper as utils
 
app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    url = data['url']

    scores = inference(url)

    # return the bias scores as JSON
    return jsonify({"scores": scores})

@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory('Images', filename)

@app.route('/inference', methods=['POST'])
def run_inference():
    data = request.get_json()
    app.logger.info("Received data: %s", data)
    if not data or 'urlInput' not in data:
        app.logger.error("No URL provided or invalid data")
        return jsonify({"error": "No URL provided"}), 400

    url = data['urlInput']
    app.logger.info("Processing URL: %s", url)
    result = utils.inference(url) 
    
    return jsonify(result)
 
if __name__=='__main__':
    app.run(port=8000, debug = True)
