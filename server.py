from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Route for rendering HTML template
@app.route('/')
def index():
    return render_template('index.html')

# Route for returning JSON response
@app.route('/feed')
def feed():
    return jsonify({'message': 'Hello, world!'})

if __name__ == '__main__':
    app.run(debug=True)
