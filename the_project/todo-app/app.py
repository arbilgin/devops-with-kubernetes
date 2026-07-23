import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Server started"


if __name__ == "__main__":
    port = os.getenv("PORT")
    print(f"Server started in port {port}", flush=True)
    app.run(host="0.0.0.0", port=port)
