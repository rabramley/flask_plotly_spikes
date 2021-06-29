# The linum library is broken from what I can see.

from linum import SvgRenderer
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gantt_image')
def gantt_image():
    filename = 'gantt.svg'

    sr = SvgRenderer('tasks.yaml', out_path='filename')
    print('Prerender')
    sr.render()

    print('Huh!')

    return send_from_directory('.', filename)
