from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)

# Declare server for Heroku deployment. Needed for Procfile.
server = app.server

hidden_div = html.Div(id="hidden-div", style={"display": "none"})

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')

if __name__ == '__main__':
    app.run(debug=True)


# '''
#  # @ Create Time: 2024-01-21 14:22:40.066094
# '''


# from dash import Dash, html, dcc, Input, Output, ClientsideFunction
# import dash_bootstrap_components as dbc
# from components.navbar import navbar
# from components.footer import footer
# from containers.home import home_page
# from containers.about import about_page
# from containers.error import error_page


# # global app definition
# app = Dash(
#     __name__,
#     external_stylesheets=[dbc.themes.FLATLY],
#     external_scripts=[
#         "https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"],
#     title="MarkosRiskModel",
#     update_title=None,
#     prevent_initial_callbacks=True,
#     suppress_callback_exceptions=True,
# )


# # Declare server for Heroku deployment. Needed for Procfile.
# server = app.server

# hidden_div = html.Div(id="hidden-div", style={"display": "none"})

# @app.callback(Output("page-content", "children"), [Input("url", "pathname")])
# def render_page_content(pathname: str):
#     """Generate the page content based on the pathname"""

#     # Upload Page
#     if pathname == "/home" or pathname == "/":
#         return html.Div(
#             [
#                 hidden_div,
#                 navbar(),
#                 home_page(app),
#                 footer()],
#             style={"backgroundColor": "#fff"})

#     # About Page
#     elif pathname == "/about":
#         return html.Div(
#             [
#                 navbar(),
#                 about_page(app),
#                 footer()],
#             style={"backgroundColor": "#fff"})

#     # Error Page
#     else:
#         return html.Div(
#             [
#                 navbar(),
#                 error_page(pathname),
#                 footer()],
#             style={"backgroundColor": "#202124"})



# # Confetti animation on button click
# app.clientside_callback(
#     ClientsideFunction(namespace="my_clientside_library",
#                        function_name="confetti_onclick"),
#     Output("hidden-div", "children"),
#     Input("send-call-button", "n_clicks"),
# )


# app.layout = html.Div([
#     # represents the URL bar, doesn't render anything
#     dcc.Location(id='url', refresh=False),

#     # content will be rendered in this element
#     html.Div(id='page-content',
#              style={"backgroundColor": "#202124"}
#              ),

# ], style={"position": "relative", "minHeight": "100vh", 'backgroundColor': '#202124'})


# if __name__ == '__main__':
#     app.run_server(debug=True, threaded=True)
