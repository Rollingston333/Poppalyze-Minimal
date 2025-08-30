#!/usr/bin/env python3
"""
Minimal Test App for Render Deployment
This is a stripped-down version to isolate deployment issues.
"""

import os
import logging
from datetime import datetime
from flask import Flask, jsonify

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__)

@app.route('/')
def home():
    """Simple home page"""
    return jsonify({
        'status': 'success',
        'message': 'Minimal test app is running!',
        'timestamp': datetime.now().isoformat(),
        'environment': os.environ.get('FLASK_ENV', 'development')
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'python_version': os.environ.get('PYTHON_VERSION', 'unknown'),
        'port': os.environ.get('PORT', 'unknown')
    })

@app.route('/test')
def test():
    """Test endpoint with environment info"""
    return jsonify({
        'app_name': 'minimal-test',
        'python_version': os.environ.get('PYTHON_VERSION', 'unknown'),
        'flask_env': os.environ.get('FLASK_ENV', 'development'),
        'port': os.environ.get('PORT', 'unknown'),
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    # Get port from environment variable (Render sets PORT)
    port = int(os.environ.get('PORT', 5001))
    
    logger.info(f"Starting minimal test app on port {port}")
    logger.info(f"Environment: {os.environ.get('FLASK_ENV', 'development')}")
    
    app.run(host='0.0.0.0', port=port, debug=False)
