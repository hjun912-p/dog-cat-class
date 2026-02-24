import os
import io
import numpy as np
from PIL import Image
from flask import Flask, request, render_template, jsonify
# Optional: suppress tf warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

app = Flask(__name__)

model = None
try:
    import tensorflow as tf
    from tensorflow.keras.preprocessing import image
    MODEL_PATH = 'best_model_xception.keras'
    model = tf.keras.models.load_model(MODEL_PATH)
    print("✅ Model loaded successfully.")
except Exception as e:
    print(f"❌ Error loading model or tensorflow: {e}")
    print("❗ Please make sure you are in the correct conda environment (e.g. `conda activate DS`) and tensorflow is installed.")
    import sys
    sys.exit(1)

TARGET_SIZE = (150, 150) # Model was trained with 150x150 images

def preprocess_image(img_bytes):
    img = Image.open(io.BytesIO(img_bytes))
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(TARGET_SIZE)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    
    # Xception preprocess_input
    img_array = tf.keras.applications.xception.preprocess_input(img_array)
    return img_array

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': '모델이 로드되지 않았거나 TensorFlow가 설치되어 있지 않습니다.'}), 500
        
    if 'file' not in request.files:
        return jsonify({'error': '업로드된 파일이 없습니다.'}), 400
        
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': '파일이 선택되지 않았습니다.'}), 400
        
    if file:
        try:
            img_bytes = file.read()
            processed_image = preprocess_image(img_bytes)
            
            predictions = model.predict(processed_image)
            
            # Binary classification (Cat vs Dog)
            if predictions.shape[-1] == 1:
                score = float(predictions[0][0])
                # Typically, generator class indices: 0 for Cat, 1 for Dog, but depends on training
                class_name = '강아지 (Dog)' if score > 0.5 else '고양이 (Cat)'
                confidence = score if score > 0.5 else 1 - score
            else:
                class_idx = np.argmax(predictions[0])
                score = float(predictions[0][class_idx])
                class_name = '강아지 (Dog)' if class_idx == 1 else '고양이 (Cat)'
                confidence = score
                
            return jsonify({
                'class': class_name,
                'confidence': f"{confidence * 100:.2f}%"
            })
        except Exception as e:
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
