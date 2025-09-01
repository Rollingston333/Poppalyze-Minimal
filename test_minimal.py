#!/usr/bin/env python3
"""
Minimal Test App for Render Deployment
This is a stripped-down version to isolate deployment issues.
"""

import os
import logging
from datetime import datetime
from flask import Flask, jsonify, request

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__)

# =====================================================
# SKELETON ROUTES FROM REAL APP
# =====================================================

@app.route('/')
def screener():
    """Main screener page - skeleton version"""
    logger.info("📄 Main screener page requested")
    
    # Return JSON instead of template for testing
    return jsonify({
        'status': 'success',
        'message': 'Main screener page - skeleton version',
        'timestamp': datetime.now().isoformat(),
        'environment': os.environ.get('FLASK_ENV', 'development'),
        'note': 'This is a skeleton route without yfinance or database dependencies'
    })

@app.route('/api/cache_status')
def api_cache_status():
    """Get cache status - skeleton version"""
    logger.info("📊 Cache status requested")
    
    return jsonify({
        'status': 'skeleton',
        'message': 'Cache status endpoint - skeleton version',
        'stock_count': 0,
        'age_minutes': 0.0,
        'last_update': datetime.now().isoformat(),
        'note': 'This is a skeleton route without cache dependencies'
    })

@app.route('/api/event', methods=['POST'])
def analytics_event():
    """Handle analytics events - skeleton version"""
    logger.info("📊 Analytics event received")
    
    try:
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
        
        data = request.get_json()
        
        # Validate required fields
        if not data or 'event' not in data:
            return jsonify({'error': 'Missing event type'}), 400
        
        event_type = data.get('event')
        
        logger.info(f"📊 ANALYTICS [SKELETON] Event: {event_type} | IP: {request.remote_addr}")
        
        return jsonify({
            'status': 'ok',
            'message': 'Analytics event processed - skeleton version',
            'event_type': event_type,
            'timestamp': datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        logger.error(f"⚠️ Error processing analytics event: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/geolocation/stats')
def api_geolocation_stats():
    """Get geolocation statistics - skeleton version"""
    logger.info("🌍 Geolocation stats requested")
    
    return jsonify({
        'status': 'skeleton',
        'message': 'Geolocation stats - skeleton version',
        'countries': [],
        'cities': [],
        'regions': [],
        'total_stats': {
            'unique_visitors': 0,
            'total_visits': 0,
            'total_countries': 0,
            'total_cities': 0
        },
        'note': 'This is a skeleton route without database dependencies'
    })

@app.route('/api/geolocation/countries')
def api_geolocation_countries():
    """Get detailed country statistics - skeleton version"""
    logger.info("🌍 Country stats requested")
    
    return jsonify({
        'status': 'skeleton',
        'message': 'Country statistics - skeleton version',
        'countries': [],
        'note': 'This is a skeleton route without database dependencies'
    })

@app.route('/api/geolocation/cities')
def api_geolocation_cities():
    """Get detailed city statistics - skeleton version"""
    logger.info("🌍 City stats requested")
    
    return jsonify({
        'status': 'skeleton',
        'message': 'City statistics - skeleton version',
        'cities': [],
        'note': 'This is a skeleton route without database dependencies'
    })

@app.route('/api/scanner_status')
def api_scanner_status():
    """Check if the background scanner is running - skeleton version"""
    logger.info("🔍 Scanner status requested")
    
    return jsonify({
        'scanner_running': False,
        'stock_count': 0,
        'thread_alive': False,
        'cache_exists': False,
        'last_scan': 'Never',
        'message': 'Scanner status - skeleton version',
        'note': 'This is a skeleton route without scanner dependencies'
    })

# =====================================================
# ORIGINAL MINIMAL ROUTES
# =====================================================

@app.route("/health")
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'python_version': os.environ.get('PYTHON_VERSION', 'unknown'),
        'port': os.environ.get('PORT', 'unknown'),
        'message': 'Health check working - skeleton routes added'
    })

@app.route("/test")
def test():
    """Test endpoint with environment info"""
    return jsonify({
        'app_name': 'minimal-test-with-skeleton-routes',
        'python_version': os.environ.get('PYTHON_VERSION', 'unknown'),
        'flask_env': os.environ.get('FLASK_ENV', 'development'),
        'port': os.environ.get('PORT', 'unknown'),
        'timestamp': datetime.now().isoformat(),
        'message': 'Test endpoint - skeleton routes from real app added'
    })

if __name__ == '__main__':
    # Get port from environment variable (Render sets PORT)
    port = int(os.environ.get('PORT', 5002))
    
    logger.info(f"Starting minimal test app with skeleton routes on port {port}")
    logger.info(f"Environment: {os.environ.get('FLASK_ENV', 'development')}")
    
    app.run(host='0.0.0.0', port=port, debug=False)
