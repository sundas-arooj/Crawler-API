from flask import request
from api.controllers.base import BaseController
from api.services.classifier import Classifier
from api.utils.common import Common
from config import SUPPORTED_IMAGE_FORMAT

class AnalyzeController(BaseController):
    def __init__(self):
        super().__init__()
        self.classifier = Classifier()
        self.common = Common()

    def analyze_image(self):
        if 'file' in request.files:  # Check if file was uploaded
            file = request.files['file']
            if file.filename == '':
                return self.error_response('No file selected.', 400)
            elif not self.common.is_file_valid(file):
                return self.error_response(f'Only {", ".join(SUPPORTED_IMAGE_FORMAT)} image files are supported.', 400)
        elif 'file' in request.form:  # Check if image URL was provided
            file = request.form['file']
        else:
            return self.error_response('No file found in the request.', 400)

        # Perform ML analysis on uploaded image
        analysis = self.classifier.analyze_image(file)

        if 'error' in analysis:
            return self.error_response(analysis['error'], 400)

        return self.success_response(analysis)
