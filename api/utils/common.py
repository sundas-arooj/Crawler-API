import requests
import io
from PIL import Image
from werkzeug.datastructures import FileStorage
from config import SUPPORTED_IMAGE_FORMAT

class Common:
    def __init__(self):
        pass
    
    def download_image(self, image_url, path):
        img = requests.get(image_url)
        img = Image.open(io.BytesIO(img.content)).convert('RGB')
        img.save(path, 'JPEG')

    def is_file_valid(self, file):
        return file.filename.lower().endswith(tuple(SUPPORTED_IMAGE_FORMAT))
    
    def get_filename(self, file):
        if isinstance(file, FileStorage):
            # Get the filename
            file = file.filename
        return file

    def validate_image_url(self, img_path):
        return isinstance(img_path, str) and img_path.startswith('http')
