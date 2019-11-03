from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return f"Hello world {2 * 4}"


if __name__ == "__main__":
    app.run()
