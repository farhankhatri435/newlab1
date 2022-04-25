from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello this is farhan khatri!'


@app.route('/health')
def health_checking():
    ret = {'status': 'UP'}
    return jsonify(ret)
