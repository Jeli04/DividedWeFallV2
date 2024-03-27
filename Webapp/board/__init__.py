from flask import Flask, render_template, send_from_directory
 
app = Flask(__name__, template_folder='templates', static_folder='static')
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory('Images', filename)
 
if __name__=='__main__':
    app.run(debug = True)