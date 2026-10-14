from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    print(current_year)
    print(type(current_year))
    return render_template("index.html", current_year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
