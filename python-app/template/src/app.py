from flask import Flask, jsonify
import socket
from datetime import datetime
import os
import sys

app = Flask(__name__)

@app.route("/myflaskapp/v1/details")
def hello_details():
    return jsonify({
        "message": "Hello, World! latest 1.0",
        "hostname": socket.gethostname(),
        "ip_address": socket.gethostbyname(socket.gethostname()),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "environment": {
            "os": os.name,
            "platform": sys.platform,
            "python_version": sys.version
        },
        "app_status": "active"
    })

@app.route("/myflaskapp/v1/health")
def health_check():
    # Basic self-check metrics
    health_status = {
        "status": "healthy 1.0 ",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "checks": {
            "database_connected": True,  # Mock check
            "disk_space": "OK"            # Mock check
        }
    }
    return jsonify(health_status), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
