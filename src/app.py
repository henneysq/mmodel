import dash
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc

WELCOME_MSG = """
    # Markos' Risk Prediction Model

    Hi Markos! Congratulations on becoming a dad!

    Here's an ugly and incomplete rendition of your beautiful model. It's in progress..

    See [Background Information](/background-information) for model details.
    """

SITE_INFO = """
            ## Site Information

            Based on.. by [Markos](),
            
            Made by [Mark Alexander Henney](https://orcid.org/0000-0002-4343-1068),

            Find the project on the [github repo](https://github.com/henneysq/mmodel/tree/master).
            """

EXTERNAL_STYLESHEETS = [
    "https://raw.githubusercontent.com/kevquirk/simple.css/main/simple-v1.css"
]

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
}


app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY], use_pages=True, pages_folder=".")# external_stylesheets=EXTERNAL_STYLESHEETS)

# Declare server for Heroku deployment. Needed for Procfile.
server = app.server
hidden_div = html.Div(id="hidden-div", style={"display": "none"})

sidebar = html.Div(
    [
        html.H2("Content", className="display-4"),
        html.Hr(),
        html.P(
            "Risk of adverse events after shoulder arthoplasty", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/home", active="exact"),
                dbc.NavLink("Background Information", href="/background-information", active="exact"),
                dbc.NavLink("Creators", href="/creators", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


info_content = html.Div(
    [
        dcc.Markdown(SITE_INFO)
    ]
)
# content = html.Div(id="page-content")

app.layout = html.Div([dcc.Location(id="url"), sidebar, dash.page_container, info_content])


# @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
# def render_page_content(pathname):
#     if pathname == "/":
#         return html.P("This is the content of the home page!")
#     elif pathname == "/page-1":
#         return html.P("This is the content of page 1. Yay!")
#     elif pathname == "/page-2":
#         return html.P("Oh cool, this is page 2!")
#     # If the user tries to reach a different page, return a 404 message
#     return html.Div(
#         [
#             html.H1("404: Not found", className="text-danger"),
#             html.Hr(),
#             html.P(f"The pathname {pathname} was not recognised..."),
#         ],
#         className="p-3 bg-light rounded-3",
#     )

if __name__ == "__main__":
    app.run(debug=True)

