import os

DEBUG = True
HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT', '5000'))
ASSETS_URL = 'static/assets'
SUPPORTED_IMAGE_FORMAT = ['png', 'jpg', 'jpeg']