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
def inference():
    url = request.json['urlInput']
    # BREAKS WHEN ASSIGNING VALUE TO RESULT
    result = utils.inference(url)
    app.logger.info("Results", result[0])
    return jsonify({'result1': str(result[0]), 'result2': str(result[1])})

 
if __name__=='__main__':
    app.run(port=8000, debug = True)
