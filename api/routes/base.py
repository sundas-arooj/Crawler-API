from flask import Flask
import os
from api.controllers.base import BaseController

ROUTES = [
    {
        'endpoint': '/', 
        'handler': 'get', 
        'methods': ['GET'],
        'controller': BaseController
    }
]

class BaseRoutes:
    def __init__(self, app: Flask):
        self.app = app
        self.excluded_files = ['__init__.py']

    def register_routes(self):
        routes_dir = os.path.join(os.path.dirname(__file__), '')
        for filename in os.listdir(routes_dir):
            if filename.endswith('.py') and filename not in self.excluded_files:
                module_name = f'api.routes.{filename[:-3]}'
                routes = __import__(module_name, fromlist=['ROUTES']).ROUTES
                for route in routes:
                    self.app.add_url_rule(route['endpoint'], view_func=getattr(route['controller'](), route['handler']), methods=route.get('methods', ['GET']))