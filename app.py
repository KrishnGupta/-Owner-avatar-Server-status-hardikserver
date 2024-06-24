from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL (/) - this is the default route
@app.route('/')
def hello():
    return render_template('index.html')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True,port=5001)
