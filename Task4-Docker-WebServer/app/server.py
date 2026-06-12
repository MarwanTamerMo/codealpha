"""Flask web server for Task 4: Web Server using Docker."""

from flask import Flask, jsonify, render_template_string
import os
import platform
import datetime
import socket

app = Flask(__name__, static_folder='../static')

START_TIME = datetime.datetime.utcnow()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CodeAlpha - Docker Web Server</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
        }
        .card {
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 16px;
            padding: 40px 50px;
            max-width: 600px;
            width: 90%;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        }
        .badge {
            display: inline-block;
            background: #00d4ff;
            color: #000;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: bold;
            margin-bottom: 20px;
            letter-spacing: 1px;
        }
        h1 { font-size: 2rem; margin-bottom: 8px; }
        .subtitle { color: #aaa; margin-bottom: 30px; font-size: 0.95rem; }
        .info-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            margin-top: 20px;
        }
        .info-item {
            background: rgba(255,255,255,0.05);
            border-radius: 8px;
            padding: 14px;
        }
        .info-label { font-size: 11px; color: #888; text-transform: uppercase; letter-spacing: 1px; }
        .info-value { font-size: 14px; margin-top: 4px; color: #00d4ff; }
        .endpoints { margin-top: 24px; }
        .endpoint {
            display: flex;
            align-items: center;
            padding: 10px 14px;
            margin: 6px 0;
            background: rgba(0,212,255,0.08);
            border-radius: 8px;
            font-size: 13px;
        }
        .method { background: #00d4ff; color: #000; padding: 2px 8px;
                  border-radius: 4px; font-size: 11px; font-weight: bold; margin-right: 10px; }
        .status-ok { color: #00ff88; font-weight: bold; }
    </style>
</head>
<body>
  <div class="card">
    <div class="badge">TASK 4 • DOCKER WEB SERVER</div>
    <h1>🐳 CodeAlpha</h1>
    <p class="subtitle">Web Server running inside a Docker container</p>
    <p>Status: <span class="status-ok">✅ Healthy &amp; Running</span></p>

    <div class="info-grid">
      <div class="info-item">
        <div class="info-label">Container</div>
        <div class="info-value">{{ hostname }}</div>
      </div>
      <div class="info-item">
        <div class="info-label">Python</div>
        <div class="info-value">{{ python_version }}</div>
      </div>
      <div class="info-item">
        <div class="info-label">Environment</div>
        <div class="info-value">{{ environment }}</div>
      </div>
      <div class="info-item">
        <div class="info-label">Uptime</div>
        <div class="info-value">{{ uptime }}</div>
      </div>
    </div>

    <div class="endpoints">
      <p style="margin-bottom:10px;font-size:13px;color:#aaa;">Available Endpoints:</p>
      <div class="endpoint"><span class="method">GET</span> /</div>
      <div class="endpoint"><span class="method">GET</span> /health</div>
      <div class="endpoint"><span class="method">GET</span> /api/info</div>
      <div class="endpoint"><span class="method">GET</span> /api/stats</div>
    </div>
  </div>
</body>
</html>
"""


def _uptime() -> str:
    delta = datetime.datetime.utcnow() - START_TIME
    total_seconds = int(delta.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours}h {minutes}m {seconds}s"


@app.route('/')
def index():
    return render_template_string(
        HTML_TEMPLATE,
        hostname=socket.gethostname(),
        python_version=platform.python_version(),
        environment=os.environ.get('ENVIRONMENT', 'development'),
        uptime=_uptime()
    )


@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'codealpha-docker-webserver',
        'container': socket.gethostname(),
        'timestamp': datetime.datetime.utcnow().isoformat() + 'Z'
    }), 200


@app.route('/api/info')
def api_info():
    return jsonify({
        'app': 'codealpha-docker-webserver',
        'version': os.environ.get('APP_VERSION', '1.0.0'),
        'environment': os.environ.get('ENVIRONMENT', 'development'),
        'python': platform.python_version(),
        'platform': platform.system(),
        'container_id': socket.gethostname()
    })


@app.route('/api/stats')
def api_stats():
    return jsonify({
        'uptime': _uptime(),
        'start_time': START_TIME.isoformat() + 'Z',
        'current_time': datetime.datetime.utcnow().isoformat() + 'Z',
        'pid': os.getpid()
    })


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
