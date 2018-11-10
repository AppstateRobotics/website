from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start(name=None):
    return render_template('home.html', name=name)