"""Simple Flask web application for CodeAlpha CI/CD Azure task."""

from flask import Flask, jsonify
import os
import platform
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    """Root endpoint."""
    return jsonify({
        'message': 'CodeAlpha DevOps Internship - Task 1: CI/CD Pipeline using Azure',
        'author': 'Marwan Tamer',
        'status': 'running',
        'timestamp': datetime.datetime.utcnow().isoformat() + 'Z'
    })


@app.route('/health')
def health():
    """Health check endpoint used by Azure App Service and smoke tests."""
    return jsonify({
        'status': 'healthy',
        'service': 'codealpha-webapp',
        'python_version': platform.python_version(),
        'timestamp': datetime.datetime.utcnow().isoformat() + 'Z'
    }), 200


@app.route('/info')
def info():
    """App information endpoint."""
    return jsonify({
        'app': 'codealpha-webapp',
        'version': os.environ.get('APP_VERSION', '1.0.0'),
        'environment': os.environ.get('ENVIRONMENT', 'development'),
        'build_id': os.environ.get('BUILD_ID', 'local')
    })


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)
