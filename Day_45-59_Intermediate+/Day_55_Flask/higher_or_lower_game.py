import random

from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return '<b>' + function() + '</b>'
    return wrapper

my_number = random.randint(0, 10)
second_number = random.randint(0, 10)


@app.route("/")
@make_bold
def main_page() -> str:
    return ("<h1>Guess a number between 1 and 10</h1>"
            "<img width=200 src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")

@app.route("/<int:number>")
def guess_number(number) -> str:
    if number == my_number:
        return (f"<h1 style='color: green'>You found me!</h1>"
                f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt='Win image'>")
    elif number > my_number:
        return (f"<h1 style='color: purple'>Too high, try again!</h1>"
                f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' alt='To high image'>")
    elif number < my_number:
        return (f"<h1 style='color: red'>Too low, try again!</h1>"
                f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' alt='To low image'>")
    else:
        return f"<h1 style='color: red'>Error</h1>"


if __name__ == "__main__":
    app.run(debug=True)