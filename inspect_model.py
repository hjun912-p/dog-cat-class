import tensorflow as tf
import sys

try:
    model = tf.keras.models.load_model('c:/Users/june4/github/dog-cat-class/best_model_xception.keras')
    print("Input shape:", model.input_shape)
    print("Output shape:", model.output_shape)
except Exception as e:
    print(f"Error loading model: {e}")
    sys.exit(1)
