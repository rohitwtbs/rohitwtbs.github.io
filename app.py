# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import dash_leaflet as dl

app = dash.Dash(__name__)
url = 'https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png'
attribution = '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>'

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
            "Amount": [4, 1, 2, 2, 4, 5],
                "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
                })

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
        html.H1(children='Hello i am rohit'),

            html.Div(children='''
                    Worked as backend,frontend,fullstack,hybrid app developer.
                    And now getting my hands dirty in extracting oil i.e
                    information from Data
                        '''),
            html.H1(children='Languages'),
            html.H3(children='Python'),
            html.H3(children='Node.js'),
            html.H3(children='Java'),
            html.Label('Python'),
            dcc.Slider(
                min=0,
                max=9,
                marks={i:'Label {}'.format(i)if i==1 else str(i) for i in range(1,6)},
                value=3

                ),
            html.Div([
                dl.Map(dl.TileLayer(url=url,maxZoom=20,attribution=attribution))
                ],
                style={'width':'100%','height':'50vh','margin':"auto","display":"block","position":"relative"}
                )

#                dcc.Graph(
#                            id='example-graph',
#                                    figure=fig
#                                        )
               ])

if __name__ == '__main__':
        app.run_server(debug=True)

