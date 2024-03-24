import requests
import io
import tensorflow as tf
import numpy as np
from PIL import Image
from api.utils.common import Common

class Classifier:
    def __init__(self):
        self.model = tf.keras.applications.mobilenet_v2.MobileNetV2(weights='imagenet', include_top=True, input_shape=(224, 224, 3))
        self.common = Common()
    
    def analyze_image(self, image_path):
        img = self.load_image(image_path)

        if img is None:
            return {'error': 'Failed to load image.'}

        img = tf.keras.applications.mobilenet_v2.preprocess_input(img)
        predictions = self.model.predict(np.expand_dims(img, axis=0))
        decoded_predictions = tf.keras.applications.imagenet_utils.decode_predictions(predictions)

        analyzed_results = [{'image': self.common.get_filename(image_path), 'label': label, 'probability': float(prob)} for _, label, prob in decoded_predictions[0]]
        return analyzed_results
    
    def load_image(self, image_url_or_path):
        try:
            if self.common.validate_image_url(image_url_or_path):
                response = requests.get(image_url_or_path)
                img = Image.open(io.BytesIO(response.content))
            else:
                img = Image.open(image_url_or_path)

            img = img.resize((224, 224))
            img_array = tf.keras.preprocessing.image.img_to_array(img)
            return img_array
        except Exception as e:
            print(f"Error loading image: {e}")
            return None
