from flask import Flask, render_template, request  # importing Flask class
app = Flask(__name__)  # setting this variable to __name__ which is used to set the main app
from datetime import date

# - - - - - - route decorators - - - - - - - - - - - - -

@app.route('/generate')
def today():
    today="Tuesday"
    return render_template("main.html", name=today)

@app.route('/')
def index():
    name = "Jack"
    return render_template("main.html", name=name)


if __name__ == '__main__':
    app.run(host="0.0.0.0")

## https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
