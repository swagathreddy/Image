from flask import Flask, request, jsonify, render_template
from generate_image import generate_image_base64

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "Prompt is missing."}), 400
    try:
        image_base64 = generate_image_base64(prompt)
        return jsonify({"image": image_base64})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
