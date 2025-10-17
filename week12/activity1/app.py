from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, Flask!</p>"

@app.route("/username/<username>")
def show_username(username):
    return f"<h1>{username} is learning Flask!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
