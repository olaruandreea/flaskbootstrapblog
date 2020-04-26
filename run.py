from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/addpost')
def add_post():
    return render_template('addpost.html')


@app.route('/aboutme')
def about_me():
    return render_template('aboutme.html')

if __name__ == '__main__':
    app.run(debug=True)