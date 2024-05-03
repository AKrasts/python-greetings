from flask import Flask, jsonify
import sys

app = Flask(__name__)

@app.route('/greetings')
def greetings():
    return jsonify({"greeting": "Hello from Python App!"})

if __name__ == '__main__':
    port = 3000
    if sys.argv[2].isnumeric(): 
        port = sys.argv[2]
    app.run(host="0.0.0.0", debug=True, port=port)
