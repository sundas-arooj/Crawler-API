from flask import Flask
from config import DEBUG, HOST, PORT
from api.routes.base import BaseRoutes

app = Flask(__name__)

# Instantiate BaseRoutes class
routes = BaseRoutes(app)

# Register routes dynamically
routes.register_routes()

if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
