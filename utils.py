"""
Created by Alejandro Daniel Noel
"""
from typing import List, Tuple

import plotly
from plotly.graph_objs import *


def plot_map(points: List[Tuple[float, float]] = (),
             names: List[str] = (),
             itinerary: List[Tuple[float, float]] = ()):
    mapbox_access_token = 'pk.eyJ1IjoiYWxlYWxlZGFuaWRhbmkiLCJhIjoiY2pnamxtdWF4MGM5ajMzcGFlOHJmcHZleSJ9._Tm6laqlGWPvEQL5UxqhWQ'

    data = Data([
        Scattermapbox(
            lat=[coords[0] for coords in points],
            lon=[coords[1] for coords in points],
            mode='markers',
            marker=Marker(
                size=9
            ),
            text=names,
        ),
        Scattermapbox(
            lat=[coords[0] for coords in itinerary],
            lon=[coords[1] for coords in itinerary],
            mode='lines',
            line={
                "width": 2,
                "color": '#FF1919'
            },
            opacity=0.8
        ),

    ])
    layout = Layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=-7.94249,
                lon=112.953
            ),
            pitch=0,
            zoom=5
        ),
    )

    fig = dict(data=data, layout=layout)
    plotly.offline.plot(fig, filename='Multiple Mapbox')


def transport_cost(dataframe, landmark1, landmark2):
    p1 = dataframe.loc[landmark1, "Cost to Ujung Kulon"]
    p2 = dataframe.loc[landmark2, "Cost to Ujung Kulon"]
    return abs(p1 - p2)
