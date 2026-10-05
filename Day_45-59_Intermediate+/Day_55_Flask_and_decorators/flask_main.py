from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world() -> str:
    return "Hello World!"

@app.route("/bye")
def say_bye() -> str:
    return "Bye"

if __name__ == "__main__":
    app.run()
