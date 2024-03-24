from api.controllers.analyze import AnalyzeController

ROUTES = [
    {
        'endpoint': '/analyze', 
        'handler': 'analyze_image', 
        'methods': ['POST'],
        'controller': AnalyzeController
    }
]
