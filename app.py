import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "DevOps Flask App")
APP_ENV = os.getenv("APP_ENV", "production")
APP_VERSION = "1.0.0"


@app.route("/")
def hello():
    return f"Hello from {APP_NAME} 🚀"


@app.route("/health")
def health():
    return jsonify(
        status="ok",
        service=APP_NAME,
        environment=APP_ENV
    )


@app.route("/info")
def info():
    return jsonify(
        app=APP_NAME,
        environment=APP_ENV,
        version=APP_VERSION
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
