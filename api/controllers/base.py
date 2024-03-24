from flask import jsonify

class BaseController:
    def get(self):
        return self.success_response({ "success": True, "message": "server is running" })

    def error_response(self, message, status_code):
        return jsonify({'error': message}), status_code

    def success_response(self, data):
        return jsonify(data)
