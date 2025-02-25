from flask import Flask, request, jsonify
from flask_cors import CORS
import text_generation_api
import stable_diffusion_api

app = Flask(__name__)
CORS(app)

@app.after_request

def add_headers(response):
    response.headers["X-Frame-Options"] = "ALLOWALL"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.route('/api/textgen', methods=['POST'])

def generate_text_endpoint():
    data = request.get_json()
    prompt = data.get("prompt", "")
    result = text_generation_api.generate_text(prompt)
    return jsonify(result)

@app.route('/api/stablediffuse', methods=['POST'])

def generate_image_endpoint():
    data = request.get_json()
    prompt = data.get("prompt", "")
    result = stable_diffusion_api.generate_image(prompt)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
