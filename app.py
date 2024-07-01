from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys
from model import convert_to_wav, predict_speaker

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = os.path.abspath('uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file part"}), 400
    file = request.files['audio']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        
        wav_file_path = convert_to_wav(filepath)
        result_label, probabilities = predict_speaker(wav_file_path)

        print(f"Tahmin edilen konuşmacı: {result_label}")
        return jsonify({"message": " Konuşmacı, "+result_label}), 200

if __name__ == '__main__':
    app.run(debug=True)
