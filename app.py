from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/user")
def index():
    return "Hello, Jochum!"

if __name__ == "__main__":
    app.run()