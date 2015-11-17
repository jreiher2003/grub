from flask import render_template
from menu import app,db

@app.route('/')
@app.route('/hello/')
def index():
    return render_template('base.html')
    # return 'Hello Jeffrey'