# Created on 2024-01-21 14:22:40.415372

import dash_bootstrap_components as dbc
from dash import html, Dash, dcc
import platform
import datetime


def about_page(app: Dash):
    """
    About Page for MarkosRiskModel
    """

    return html.Div([

        html.Div([
            html.Div([
                # Text and Titles
                html.H3(
                    "MarkosRiskModel About Page",
                    style={'padding-top': '10px'},
                ),
                html.H5([
                    "Created on 2024-01-21 14:22:40.415372",
                ], style={'margin-bottom': '0px'}),
                html.Hr(style={'color': 'black',
                               'margin-top': '0px', 'margin-bottom': '30px'}),

                html.Div(id='not-used'),
                html.Div([
                    dbc.Button(
                        [
                            html.P("Another Wild Button", style={
                                   'display': 'inline-block', 'height': '0px'}),
                        ],
                        id='about-page-button',
                        href='/',
                        className="uploadButton",
                        type="button",
                    ),
                ], style={
                    'width': '100%',
                    'display': 'flex',
                    'justify-content': 'center',
                    'margin-top': '30px',
                },
                    id="about-button"),
            ],
                style={
                    'min-width': '400px',
                    'margin-bottom': '10px',
                    'color': '#444',
                    'padding-bottom': '100px'
            }),
        ],
            style={
                'width': '70%',
        },
            className='center'
        ),
    ],
        style={
            'padding-top': '10px',
            'margin-bottom': '60px',
            'min-height': '100vh',
    },
    )