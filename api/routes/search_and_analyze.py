from api.controllers.search_and_analyze import SearchAndAnalyzeController

ROUTES = [
    {
        'endpoint': '/search-via-crawler', 
        'handler': 'search_via_crawler', 
        'methods': ['GET'],
        'controller': SearchAndAnalyzeController
    }
]
