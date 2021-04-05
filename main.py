from flask import Flask, jsonify, render_template, request
import json

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/random", methods=["GET"])
def get_random_cafe():
    with open('samples.json') as f:
        data = json.load(f)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)


# https://hidden-oasis-39444.herokuapp.com/ 