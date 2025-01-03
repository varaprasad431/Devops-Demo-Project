from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/message', methods=['GET'])
def message():
    return jsonify({"message": "Welcome to DevOps!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
