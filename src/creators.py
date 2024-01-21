import dash
from dash import Dash, dcc, html, Input, Output, callback

dash.register_page(__name__)

LR_INDENT = (600, 600)


SITE_INFO = """
            ## Site Information

            Based on.. by [Markos](),
            
            Made by [Mark Alexander Henney](https://orcid.org/0000-0002-4343-1068),

            Find the project on the [github repo](https://github.com/henneysq/mmodel/tree/master).
            """

layout = html.Div(
    style={'margin-left': f"{LR_INDENT[0]}px", 'margin-right': f"{LR_INDENT[1]}px", "margin-top":"7px"},
    children=[
        dcc.Markdown(SITE_INFO)
    ]
)