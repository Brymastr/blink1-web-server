from flask import Flask
from light import blink

app = Flask(__name__)


@app.route("/blink", methods=['POST'])
def hell():
    blink()
    return "success"


if __name__ == '__main__':
    app.run()
