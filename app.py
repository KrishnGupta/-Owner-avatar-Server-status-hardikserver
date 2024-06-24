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

    response_aapanal = requests.get('http://thelocalstreet.in/hardik/uptime.json')
    aapanal_data = response_aapanal.text

    # server_status= aapanal_data['server_status']
    # print(server_status)

    return render_template('index.html',data=status,days=days,hours=hours,mins=mins,secs=secs,uptime_percentage=uptime_percentage,load=load)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True,port=5001)
