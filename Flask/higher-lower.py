from flask import Flask, render_template
from random import randint

app = Flask(__name__)

random_num = randint(0, 9)
# print(random_num)

@app.route("/")
def higher_lower():
    return "<h1>Guess a number between 0 and 9<h1/>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<int:user_response>")
def get_response(user_response):
    # dif = random_num - user_response
    dif = 9
    if random_num == user_response:
        return "<h1>You've Found Me!<h1/>" \
               f"<h2>{user_response}<h2/>" \
               "<img src='https://media.giphy.com/media/BPJmthQ3YRwD6QqcVD/giphy.gif'>"
    elif dif > 4:
        return render_template("index.html")
    elif dif < -4:
        return "<h1>Too high!<h1/>" \
               "<img src='https://media.giphy.com/media/fQogXfHt0uIgyOCXDo/giphy.gif'>"
    else:
        return "<h1>Almost there...<h1/>" \
               "<img src='https://media.giphy.com/media/fxTFYor37uSe099noX/giphy.gif'>"

if __name__ == "__main__":
    app.run(debug=True)
# $env:FLASK_APP = "C:\Users\Vin Muchiri\OneDrive\Python Programming\hello_flask\hello.py"