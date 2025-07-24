from flask import Flask

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Hello from the backend!"

# About route
@app.route('/about')
def about():
    return "This is the about page."

# API route
@app.route('/api/data')
def data():
    return {"message": "This is JSON data from backend"}

if __name__ == '__main__':
    app.run(debug=True)
