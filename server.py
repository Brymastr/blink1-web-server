from flask import Flask
import socket
from routes import api

ip = socket.gethostbyname(socket.gethostname())

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/build')


if __name__ == "__main__":
    app.run(host=ip)
