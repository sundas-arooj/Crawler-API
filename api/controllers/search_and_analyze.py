from flask import request
from api.controllers.base import BaseController
from api.services.crawler import Crawler
from api.services.classifier import Classifier
from api.utils.common import Common
from datetime import datetime
from config import ASSETS_URL

class SearchAndAnalyzeController(BaseController):
    def __init__(self):
        super().__init__()
        self.crawler = Crawler()
        self.classifier = Classifier()
        self.common = Common()

    def search_via_crawler(self):
        keyword = request.args.get('keyword')
        if not keyword:
            return self.error_response('Keyword parameter is required.', 400)

        # Get images from Crawler
        images = self.crawler.search_images(keyword)
        if not images:
            return self.error_response('No images found for the keyword.', 404)

        # Perform ML analysis on images
        analysis_results = []
        for i, image in enumerate(images):
            current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            file_path = f'{ASSETS_URL}/{keyword}_{i+1}_{current_time}.jpg'

            self.common.download_image(image, file_path)

            analysis = self.classifier.analyze_image(file_path)

            if 'error' in analysis:
                return self.error_response(analysis['error'], 400)

            analysis_results.append({'image': file_path, 'analysis': analysis})

        return self.success_response(analysis_results)
