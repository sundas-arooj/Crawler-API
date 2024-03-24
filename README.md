# Crawler-API
This project is a simple crawler API built using Flask in Python. It allows users to search for images on a social network (currently supporting Instagram), and perform machine learning (ML) analysis on the retrieved images using a pre-trained MobileNetV2 model, and also provides analysis on images provided by users directly.

## Features
- Integration with Flask to handle HTTP requests and responses.
- Utilizes BeautifulSoup and Selenium for web scraping to retrieve images from a social network.
- Implements TensorFlow and the MobileNetV2 model for image classification.
- Provides two API endpoints:
  - **Search via Crawler:** Accepts a keyword, searches for related images on Instagram, and returns ML analysis on up to 5 images found.
  - **Upload Images:** Allows users to upload an image file directly for ML analysis.
