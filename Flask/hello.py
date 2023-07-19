from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_func():
        result = function()
        return f"<b>{result}<b>"

    return wrapper_func


def make_italic(function):
    def wrapper_func():
        result = function()
        return f"<em>{result}<em>"

    return wrapper_func


def make_underline(function):
    def wrapper_func():
        result = function()
        return f"<u>{result}<u>"

    return wrapper_func


@app.route('/')  # Decorator func makes sure only to execute hello_world() when user is accessing the home page or root
@make_bold
@make_underline
@make_italic
def hello_world():
    return "Hello World"


# TODO Adding HTML and CSS attributes
@app.route('//username/<string:username>/profile')
def populate_html(username):
    return f'<h1 style="text-align: center">Hi! My name is {username}<h1>' \
           '<p>I am a Mechatronics Engineering graduate ready to help you come up with smart solutions ' \
           'by combining systems thinking and engineering tools such as product design, hardware programming' \
           'and IoT, programming, UI/UX design and data science<p>' \
           '<img src = "https://media4.giphy.com/media/kT9ZB9ALydctmXRb0V/giphy.gif?cid=ecf05e47es9b4bdtg1j8upj8rzebxpg6v7w4d7f6ci92bhxn&ep=v1_gifs_search&rid=giphy.gif&ct=g">'


# TODO Using <variables> to get values in a link
@app.route('/<some_value>')
def get_value(some_value):
    return some_value


# TODO Using Converters to retrieve parts of the url as a specific data type
# path and other data types
@app.route('/username/<string:username>/profile')
def get_username(username):
    return f"Hi {username}"





# In case set FLASK_APP=hello.py fails, use:
# $env:FLASK_APP = "C:\Users\Vin Muchiri\OneDrive\Python Programming\hello_flask\hello.py"
# Also, using .run() is much faster
if __name__ == "__main__":  # Confirms that we are not running from an imported file
    # Run the app in debug mode to auto render changed content
    app.run(debug=True)
