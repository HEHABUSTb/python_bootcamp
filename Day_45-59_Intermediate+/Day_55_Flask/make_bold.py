from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        text = function()
        bold_text = '<b>' + text + '</b>'
        return bold_text
    return wrapper_function


@app.route("/")
@make_bold
def hello_world() -> str:
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)