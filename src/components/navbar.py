# Created on 2024-01-21 14:22:40.399293
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc



def home_header():
    """
    Home header
    """
    from ..app import app
    layout = html.Div([

        html.Div(
            [

                html.Div(
                    [
                        dcc.Link([
                            html.Img(
                                src=app.get_asset_url(
                                    'img/banner.svg'),
                                style={
                                    "height": "42px",
                                    "width": "auto",
                                    "margin-left": "40px",
                                    'margin-top': '-5px'
                                },
                            ),
                        ],
                            href="/",
                            target='_top',
                            style={
                                'display': 'inline-block',
                        }
                        ),

                    ], style={'display': 'inline-block'}
                ),

                html.Div(
                    [
                        html.A(
                            dbc.Button(html.Div(["Visit About Page"], style={
                                'color': 'black', 'font-size': '15px', 'font-style': 'italic'}), color='white'),
                            href="/about",
                        ),

                    ],
                    style={
                        "display": "inline-block",
                        "float": "right",
                        "padding-right": "30px",
                        'margin-top': '-5px'
                    }
                )

            ],
            style={
                "display": "inline-block",
                "width": "100%"
            }
        )],

        id="header",
        className="flex-display",
        style={
            "margin-top": "10px",
            "width": "100%",
            "height": "35px",
            "display": "inline-block"
    },
    )

    return layout

# Create the navbar layout
def navbar():
    """
    Configurable Navbar
    """

    navbar = dbc.Navbar(
        [home_header()],
        dark=True,
        sticky="top",
        color='#ffffff'
    )

    return navbar