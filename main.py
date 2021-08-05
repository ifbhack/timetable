from flask import Flask, render_template, url_for, flash
app = Flask(__name__)


#landing page is the login
@app.route('/')
def index():
  return render_template("login2.html")



#homepage link - opens from the login page
@app.route('/home')
def home():
    return render_template("home.html")

#details link
@app.route('/detail')
def detail():
    return render_template('details.html')


#extra static page to show the maps of qut campuses
@app.route('/map')
def maps():
    return 'hello world' #render_template('map.html')

@app.route('/FAQ')
def help():
    return 'FAQ and help page' #render_template('help.html')

if __name__ == '__main__':
   app.run(debug = True)
