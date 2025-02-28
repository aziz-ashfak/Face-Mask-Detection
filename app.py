from flask import Flask, Response, render_template, request, jsonify
import cv2
import torch
from ultralytics import YOLO
import os
import time
from werkzeug.utils import secure_filename
import numpy as np

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads/"
RESULT_FOLDER = "static/results/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

# Load YOLO model once
model = YOLO("best_model/best.onnx")

# Webcam control
cap = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/toggle_webcam', methods=['POST'])
def toggle_webcam():
    global cap
    action = request.json.get("action")
    
    if action == "start":
        if cap is None or not cap.isOpened():
            cap = cv2.VideoCapture(0)
        return jsonify({"status": "started"})
    elif action == "stop":
        if cap is not None and cap.isOpened():
            cap.release()
            cap = None
        return jsonify({"status": "stopped"})
    
    return jsonify({"status": "invalid action"})

def generate_frames():
    global cap
    if cap is None:
        cap = cv2.VideoCapture(0)  # Reopen if closed

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        
        results = model(frame)
        for result in results:
            plotted_img = result.plot()

        _, buffer = cv2.imencode('.jpg', plotted_img)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file uploaded!"
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file!"
    
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # Read and process image
    img = cv2.imread(filepath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = model(img)

    for result in results:
        plotted_img = result.plot()

    # Save processed image
    result_path = os.path.join(RESULT_FOLDER, filename)
    cv2.imwrite(result_path, cv2.cvtColor(plotted_img, cv2.COLOR_RGB2BGR))

    return render_template('index.html', uploaded=True, result_image=result_path)

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)

