from flask import Flask, render_template, jsonify, request
from gemini_content import generate_response, generate_response_from_voice

app = Flask(__name__)

@app.route("/process_message", methods=["POST"])
def process_message_func1():
    msg = request.json['message']
    resp = generate_response(msg)
    return jsonify({"response": resp})

@app.route("/process_voice", methods=["POST"])
def process_voice_func1():
    resp = generate_response_from_voice()
    return jsonify({"response": resp})

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
