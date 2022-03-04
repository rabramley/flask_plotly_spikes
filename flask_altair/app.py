# The linum library is broken from what I can see.

import altair as alt
from datetime import datetime
import pandas as pd
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gantt_image')
def gantt_image():

    data = [
        {
            'Task': 'BRICCS',
            'Start': datetime(2020, 3, 1),
            'End': datetime(2020, 3, 16),
            'Status': 'Open',
        },
        {
            'Task': 'BRICCS',
            'Start': datetime(2020, 4, 1),
            'End': datetime(2020, 4, 16),
            'Status': 'Open',
        },
        {
            'Task': 'GENVASC',
            'Start': datetime(2020, 3, 5),
            'End': datetime(2020, 6, 22),
            'Status': 'Closed',
        },
        {
            'Task': 'LIMB',
            'Start': datetime(2020, 6, 10),
            'End': datetime(2020, 11, 28),
            'Status': 'Open',
        },
    ]

    df = pd.DataFrame(data)

    chart = alt.Chart(df).mark_bar(size=40).encode(
        x=alt.X(
            "Start",
            axis=alt.Axis(
                values=[d.isoformat() for d in pd.date_range('2020-01-01', freq='1MS', periods=12)],
                format="%a %b %_d",
                tickCount=12,
                labelAngle=90,
                title='',
            )
        ),
        x2="End",
        y=alt.Y(
            "Task", 
            axis=alt.Axis(title=''),
            sort=list(
                df.sort_values(["Start"])
                ["Task"],
            )
        ),
        color=alt.Color("Status"),
    ).properties(
        width=1000,
        height=200,
    ).configure_axisY(
        labelFontSize=20,
        tickOpacity=0,
    )

    return chart.to_json()

# @app.route('/gantt_image')
# def gantt_image():

#     df = pd.read_csv("gantt.csv", parse_dates=["Start", "End"])

#     chart = alt.Chart(df).mark_bar(size=40).encode(
#         x=alt.X(
#             "Start",
#             axis=alt.Axis(
#                 values=[d.isoformat() for d in pd.date_range('2020-01-06', freq='7D', periods=52)],
#                 format="%a %b %_d",
#                 tickCount=52,
#                 labelAngle=90,
#                 title='',
#             )
#         ),
#         x2="End",
#         y=alt.Y(
#             "Task", 
#             axis=alt.Axis(title=''),
#             sort=list(
#                 df.sort_values(["Start"])
#                 ["Task"],
#             )
#         ), 
#         color=alt.Color("Task",legend=None)
#     ).properties(
#         width=1000,
#         height=200,
#     ).configure_axisY(
#         labelFontSize=20,
#         tickOpacity=0,
#     )

#     return chart.to_json()
