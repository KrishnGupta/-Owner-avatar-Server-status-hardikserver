from flask import Flask, render_template
import requests

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL (/) - this is the default route
@app.route('/')
def hello():
    response = requests.get('https://status.skyserver.in/status.php')
    data = response.json()
    status = data['serverStatus']
    days = data['uptime']['days']
    hours = data['uptime']['hours']
    mins = data['uptime']['mins']
    secs = data['uptime']['secs']
    uptime_percentage = data['uptime_percentage']
    load = data['load']

    # response_aapanal = requests.get('https://status.skyserver.net.in/uptime.json')
    response_aapanal = requests.get('http://127.0.0.1:5000/api/server_status')
    aapanal_data = response_aapanal.json()

    server_status= aapanal_data['serverStatus']
    aapanal_days = aapanal_data['uptime']['days']
    aapanal_hours = aapanal_data['uptime']['hours']
    aapanal_mins = aapanal_data['uptime']['mins']
    aapanal_secs = aapanal_data['uptime']['secs']

    return render_template('index.html',data=status,days=days,hours=hours,mins=mins,secs=secs,uptime_percentage=uptime_percentage,load=load,server_status=server_status,aapanal_days=aapanal_days,aapanal_hours=aapanal_hours,aapanal_mins=aapanal_mins,aapanal_secs=aapanal_secs)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True,port=5001)
