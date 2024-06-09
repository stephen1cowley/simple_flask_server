from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to my API"


@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "name": "Stephen",
        "age": 21,
        "country": "UK"
    }
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def post_data():
    new_data = request.json
    # Process and store
    return jsonify(new_data), 201


if __name__ == '__main__':
    app.run(debug=True)
