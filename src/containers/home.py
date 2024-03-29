# Created on 2024-01-21 14:22:40.431500

import dash_bootstrap_components as dbc
from dash import html, Dash, dcc
import platform
import datetime


def forms():
    """
    Generates user input forms for upload screen
    """

    destination_phone_number = dbc.Row(
        [
            dbc.Label("Destination Number",
                      html_for="dest-phone-number", width=3),
            dbc.Col(
                dbc.Input(
                    id="dest-phone-number",
                    html_size='tel',
                    type='tel',
                    autocomplete='off',
                    placeholder="(123) 456-7890",
                    style={
                        'lineHeight': '1px',
                        'minHeight': '1px',
                        'fontWeight': '100',
                        'borderStyle': 'solid',
                        'borderRadius': '0.25rem',
                    }
                ),
                width=9,
            ),
        ],
        className="mb-2 form-item",
    )

    call_template = dbc.Row(
        [
            dbc.Label("Call Template", html_for="call-template-select", width=3),
            dbc.Col(
                dbc.Select(
                    id='call-template-select',
                    value=1,
                    options=[
                        {"label": "English-US (Standard)", "value": 1},
                        {"label": "English-IN (Short)", "value": 2},
                        {"label": "Spanish-MX (Short)", "value": 3},
                    ],
                ),
                width=9,
            ),
        ],
        className="mb-2 form-item",
    )

    provider = dbc.Row(
        [
            dbc.Label("Healthcare Provider",
                      html_for="provider-input", width=3),
            dbc.Col(
                dbc.Input(
                    id="provider-input",
                    value="Joy Health",
                    autocomplete='off',
                    placeholder="Healthcare Provider Name",
                    style={
                        'lineHeight': '1px',
                        'minHeight': '1px',
                        'fontWeight': '100',
                        'borderStyle': 'solid',
                        'borderRadius': '0.25rem',
                    }
                ),
                width=9,
            ),
        ],
        className="mb-2 form-item",
    )

    # Determine if OS is Windows or Mac
    if platform.system() == "Windows":
        date_format = "%B %#d"
    else:
        date_format = "%B %-d"

    visitDate = dbc.Row(
        [
            dbc.Label("Visit Date",
                      html_for="visit-date-input", width=3),
            dbc.Col(
                dbc.Input(
                    id="visit-date-input",
                    autocomplete='off',
                    placeholder="Visit Date",
                    value=datetime.datetime.now().strftime(date_format),
                    style={
                        'lineHeight': '1px',
                        'minHeight': '1px',
                        'fontWeight': '100',
                        'borderStyle': 'solid',
                        'borderRadius': '0.25rem',
                    }
                ),
                width=9,
            ),
        ],
        className="mb-2 form-item",
    )

    callerName = dbc.Row(
        [
            dbc.Label("Recipient Name",
                      html_for="caller-name-input", width=3),
            dbc.Col(
                dbc.Input(
                    id="caller-name-input",
                    placeholder="Name",
                    autocomplete='off',
                    value="John Doe",
                    style={
                        'lineHeight': '1px',
                        'minHeight': '1px',
                        'fontWeight': '100',
                        'borderStyle': 'solid',
                        'borderRadius': '0.25rem',
                    }
                ),
                width=9,
            ),
        ],
        className="mb-2 form-item",
    )

    return dbc.Form([callerName, call_template, destination_phone_number, provider, visitDate])


def home_page(app: Dash):
    """
    Main landing page for MarkosRiskModel
    """

    return html.Div([

        html.Div([
            html.Div([
                # Text and Titles
                html.H3(
                    "MarkosRiskModel",
                    style={'padding-top': '10px'},
                ),
                html.H5([
                    "Application Details"
                ], style={'margin-bottom': '0px'}),
                html.Hr(style={'color': 'black',
                               'margin-top': '0px', 'margin-bottom': '30px'}),

                # Application Details
                forms(),

                html.Div(id='call-status-text'),
                html.Div([
                    dbc.Button(
                        [
                            html.P("Amazing Button", style={
                                   'display': 'inline-block', 'height': '0px'}),
                        ],
                        id='send-call-button',
                        className="uploadButton",
                        type="button",
                    ),
                ], style={
                    'width': '100%',
                    'display': 'flex',
                    'justify-content': 'center',
                    'margin-top': '30px',
                },
                    id="upload-button-container"),
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