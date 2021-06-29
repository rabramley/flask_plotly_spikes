import io
from flask import Flask, render_template, send_from_directory, send_file
import matplotlib.pyplot as plt


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gantt_image')
def gantt_image():
    filename = 'gantt.png'

    plt = graph()

    buf = io.BytesIO()
    plt.savefig(buf)
    buf.seek(0)

    return send_file(
        buf,
        attachment_filename='figure.png',
    )


def graph():
    # Declaring a figure "gnt"
    fig, gnt = plt.subplots()
    
    # Setting Y-axis limits
    gnt.set_ylim(0, 50)
    
    # Setting X-axis limits
    gnt.set_xlim(0, 160)
    
    # Setting labels for x-axis and y-axis
    gnt.set_xlabel('seconds since start')
    gnt.set_ylabel('Processor')
    
    # Setting ticks on y-axis
    gnt.set_yticks([15, 25, 35])
    # Labelling tickes of y-axis
    gnt.set_yticklabels(['1', '2', '3'])
    
    # Setting graph attribute
    gnt.grid(True)
    
    # Declaring a bar in schedule
    gnt.broken_barh([(40, 50)], (20, 1), facecolors =('tab:orange'))
    
    # Declaring multiple bars in at same level and same width
    gnt.broken_barh([(110, 10), (150, 10)], (10, 9), facecolors ='tab:blue')
    
    gnt.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9), facecolors =('tab:red'))

    return plt