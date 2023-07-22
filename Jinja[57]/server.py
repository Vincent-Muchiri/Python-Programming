from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

current_year = datetime.now().year

def get_age_name(name):
    gender_api_result = requests.get(f'https://api.genderize.io?name={name}')
    gender_api_result.raise_for_status()
    gender_json = gender_api_result.json()
    gender = gender_json['gender']

    age_api_result = requests.get(f'https://api.agify.io/?name={name}')
    age_api_result.raise_for_status()
    age_json = age_api_result.json()
    age = age_json['age']

    return {'age': age, 'gender': gender}


@app.route("/")
def main():
    current_year = datetime.now().year
    return "<h1>Hello World!</h1>"


@app.route("/<string:name>")
def get_name(name):
    details = get_age_name(name=name)
    age = details['age']
    gender = details['gender']
    return render_template("index.html", name=name, age=age, gender=gender, year=current_year)

@app.route("/blog")
def blog():
    response = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391')
    response.raise_for_status()
    blog_post_data = response.json()
    return render_template('blog.html', blog_posts=blog_post_data, year=current_year)

if __name__ == "__main__":
    app.run(debug=True)
