from flask import Flask, render_template, url_for, flash
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("login.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/detail')
def detail():
    return render_template('details.html')


if __name__ == '__main__':
   app.run(debug = True)
