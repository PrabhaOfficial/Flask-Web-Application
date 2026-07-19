from flask import Flask, render_template, request, jsonify
from services.genai_service import get_response

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    prompt = data.get("prompt", "")

    response = get_response(prompt)

    return jsonify({
        "response": response
    })


if __name__ == "__main__":
    app.run(debug=True)