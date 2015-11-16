from flask import render_template
from menu import app

@app.route('/')
@app.route('/hello')
def index():
    return render_template('index.html')
    # return 'Hello Jeffrey'