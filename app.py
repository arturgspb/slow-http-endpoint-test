import time
from flask import Flask
app = Flask(__name__)

@app.route("/<sec>")
def hello(sec):
    time.sleep(int(sec))
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")

