from flask import Flask, jsonify

# Create api instance
api = Flask(__name__)

# Set configuration
api.config.from_object('project.config.DevelopmentConfig')

@api.route('/guests/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong'
    })