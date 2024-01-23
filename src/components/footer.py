# Created on 2024-01-21 14:22:40.399293

import dash_bootstrap_components as dbc
from dash import dcc, html


def footer():
    """
    App footer
    """
    return html.Div([
        # # # # # # # # Footer # # # # # # # #
        dbc.CardFooter(
            [
                dcc.Markdown(
                    "MarkosRiskModel - My Plotly Dash Application - Footer",
                    style={
                        "display": "inline-block",
                        'font-size': '15px'}),
            ],
            style={'backgroundColor': 'black',
                   'textAlign': 'center',
                   'width': '100%',
                   'color': 'white',
                   'height': 'auto'},
            className='align-bottom'),
    ],
        style={
            'backgroundColor': 'black',
            'width': '100%',
    }
    )