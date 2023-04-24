from bloglite import create_app
from flask import send_file, render_template

app, api = create_app()

@app.route('/')
def index():
    return render_template('index.html')
