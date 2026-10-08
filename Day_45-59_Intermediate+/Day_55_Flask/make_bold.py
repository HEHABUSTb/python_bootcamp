from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return '<b>' + function() + '</b>'
    return wrapper


@app.route("/")
@make_bold
def hello_world() -> str:
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)