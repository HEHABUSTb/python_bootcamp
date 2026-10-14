from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    current_year = datetime.datetime.now().year

    return render_template("index.html", current_year=current_year)

@app.route('/guess/<string:name>')
def guess(name):
    gender_response = requests.get(f'https://api.genderize.io?name={name}').json()
    gender = gender_response.get('gender')

    age_response = requests.get(f'https://api.agify.io?name={name}').json()
    age = age_response.get('age')

    name = name.capitalize()

    return render_template("index.html", name=name, age=age, gender=gender)



if __name__ == "__main__":
    app.run(debug=True)