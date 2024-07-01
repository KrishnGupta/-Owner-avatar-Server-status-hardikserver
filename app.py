from flask import Flask, render_template
import requests

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL (/) - this is the default route
@app.route('/')
def hello():
    try:
        response = requests.get('https://SkyServer.in/client/status/status.php')
        data = response.json()
        status = data['serverStatus']
        days = data['uptime']['days']
        hours = data['uptime']['hours']
        mins = data['uptime']['mins']
        secs = data['uptime']['secs']
        uptime_percentage = data['uptime_percentage']
        load = data['load']
    except (requests.RequestException, KeyError) as e:
        status = "Stop"
        days = 0
        hours = 0
        mins = 0
        secs = 0
        uptime_percentage = 0
        load = 0

    try:
        response_aapanal = requests.get('https://status.skyserver.net.in/uptime.json')
        # response_aapanal = requests.get('http://127.0.0.1:5000/api/server_status')
        aapanal_data = response_aapanal.json()
        server_status = aapanal_data['serverStatus']
        aapanal_days = aapanal_data['uptime']['days']
        aapanal_hours = aapanal_data['uptime']['hours']
        aapanal_mins = aapanal_data['uptime']['mins']
        aapanal_secs = aapanal_data['uptime']['secs']
        aapanal_load = aapanal_data['load']
    except (requests.RequestException, KeyError) as e:
        server_status = "Stop"
        aapanal_days = 0
        aapanal_hours = 0
        aapanal_mins = 0
        aapanal_secs = 0
        aapanal_load = 0

    return render_template('index.html',
                           data=status,
                           days=days,
                           hours=hours,
                           mins=mins,
                           secs=secs,
                           uptime_percentage=uptime_percentage,
                           load=load,
                           server_status=server_status,
                           aapanal_days=aapanal_days,
                           aapanal_hours=aapanal_hours,
                           aapanal_mins=aapanal_mins,
                           aapanal_secs=aapanal_secs,
                           aapanal_load=aapanal_load)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, port=5001)
