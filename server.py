from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # This route will render the HTML page that contains the p5.js canvas.
    return render_template('index.html')

@app.route('/set_size', methods=['POST'])
def set_size():
    # This route receives the size of the sphere chosen by the user and sends it to the front-end
    size = request.form.get('size')
    return {'size': size}, 200

if __name__ == "__main__":
    app.run(debug=True)
