from flask import Flask, render_template  # importing Flask class
app = Flask(__name__)  # setting this variable to __name__ which is used to set the main app

# - - - - - - route decorators - - - - - - - - - - - - -

@app.route('/generate')
def today():
    return render_template("main.html")

@app.route('/')
def index():
    return render_template("main.html")

if __name__ == '__main__':
    app.run()
