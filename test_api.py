from flask import Flask, jsonify

app = Flask(__name__)

# Sample data
server_status = {
    "timestamp": "2024-06-25T11:51:01+0200",
    "serverStatus": "Stop",
    "load_averages": "0.09, 0.07, 0.08",
    "uptime": {
        "days": 57,
        "hours": "04",
        "mins": "00",
        "secs": "12"
    },
    "http_status": "not running",
    "ftp_status": "not running",
    "pop3_status": "running"
}

# Route to return server status JSON
@app.route('/api/server_status', methods=['GET'])
def get_server_status():
    return jsonify(server_status)

if __name__ == '__main__':
    app.run(debug=True)
