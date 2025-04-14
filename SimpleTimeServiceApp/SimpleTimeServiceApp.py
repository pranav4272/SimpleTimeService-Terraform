from flask import Flask, request, jsonify
from datetime import datetime

SimpleTimeServiceApp = Flask(__name__)

@SimpleTimeServiceApp.route('/time', methods=['GET'])
def get_time():
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    return jsonify({
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "ip": client_ip
    })

if __name__ == "__main__":
    SimpleTimeServiceApp.run(host="0.0.0.0", port=5000)
