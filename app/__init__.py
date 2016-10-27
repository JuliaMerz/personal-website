from flask import Flask, render_template, flash
app = Flask(__name__)

# flash to flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/press')
def press():
    return render_template('press.html')

@app.route('/involved')
def involved():
    return render_template('involved.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/awards')
def awards():
    return render_template('awards.html')
