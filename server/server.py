from flask import Flask, render_template, request, redirect, Response, url_for, jsonify
import util

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World !'
    # return render_template('index.html')

@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']

    response = jsonify(util.classify_image(image_data))
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == '__main__':
    print('Starting Python Flask Server For Image Detection')
    util.load_saved_artifacts()
    app.run(debug=True)