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
                lat=38.92,
                lon=-77.07
            ),
            pitch=0,
            zoom=10
        ),
    )

    fig = dict(data=data, layout=layout)
    plotly.offline.plot(fig, filename='Multiple Mapbox')


if __name__ == "__main__":
    lat = ['38.91427', '38.91538', '38.91458',
           '38.92239', '38.93222', '38.90842',
           '38.91931', '38.93260', '38.91368',
           '38.88516', '38.921894', '38.93206',
           '38.91275']
    lon = ['-77.02827', '-77.02013', '-77.03155',
           '-77.04227', '-77.02854', '-77.02419',
           '-77.02518', '-77.03304', '-77.04509',
           '-76.99656', '-77.042438', '-77.02821',
           '-77.01239']
    place_names = ["The coffee bar", "Bistro Bohem", "Black Cat",
                   "Snap", "Columbia Heights Coffee", "Azi's Cafe",
                   "Blind Dog Cafe", "Le Caprice", "Filter",
                   "Peregrine", "Tryst", "The Coupe",
                   "Big Bear Cafe"]

    plot_map(points=list(zip(lat, lon)), names=place_names, itinerary=list(zip(lat, lon)))
