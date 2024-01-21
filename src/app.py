
from dash import Dash, dcc, html, Input, Output, callback

external_stylesheets = ["https://gist.githubusercontent.com/ZachSaucier/8295d9dc926d7064ff0d4f3f04b35b55/raw/06a8cc03bbdbb7e36f7ae192f834226320f752cd/dark-theme.css"]

app = Dash(__name__)

# Declare server for Heroku deployment. Needed for Procfile.
server = app.server
hidden_div = html.Div(id="hidden-div", style={"display": "none"})

app.layout = html.Div(
    [
        html.H6(
            """ Hi Markos! Congratulations on becoming a dad!

            Here's an ugly and incomplete rendition of your beautiful model. 

            """
        ),
        html.H6("Change the value in the to calculate the risk of something!"),
        html.Div([
            "Age: ",
            dcc.Input(id="age", type="number", placeholder="Age"),
        ]),
        html.Div([
            "Sex: ",
            dcc.Dropdown(['male', 'female'], 'male', id='sex'),
        ]),
        html.Div([
            "Prosthesis: ",
            dcc.Dropdown(['hemi', 'reverse', 'anatomical'], 'hemi', id='prosthesis'),
        ]),
        html.Div([
            "Indication: ",
            dcc.Dropdown(['acute fracture', 'fraktur sequelae',
                      'osteoarthritis', 'cuff damage'], 'acute fracture', id='indication'),
        ]),
        # html.Hr(),
        html.Div([
            "Cardiac co-morbidity: ",
            dcc.Dropdown(['yes', 'no'], 'no', id='comorb-cardiac'),
        ]),
        html.Div([
            "Diabetic co-morbidity: ",
            dcc.Dropdown(['yes', 'no'], 'no', id='comorb-diabetic'),
        ]),
        html.Div([
            "Renal co-morbidity: ",
            dcc.Dropdown(['yes', 'no'], 'no', id='comorb-renal'),
        ]),
        html.Div([
            "Neurological co-morbidity: ",
            dcc.Dropdown(['yes', 'no'], 'no', id='comorb-neuronal'),
        ]),

        # dcc.Input(
        #     id="dtrue", type="number",
        #     debounce=True, placeholder="Debounce True",
        # ),
        html.Hr(),
        html.Div(id="number-out"),
    ]
)

@callback(
        Output(component_id="number-out", component_property="children"),
        Input(component_id="age", component_property="value"),
        Input(component_id="sex", component_property="value")
)
def render_output(age, sex):
    if age is None:
        return f"Please enter age"
    
    return f"Age is {age}, sex is {sex}"

# @callback(
#     Output("number-out", "children"),
#     Input("age", "value"),
#     Input("sex", "value"),
#     Input("prothesis", "value"),
#     Input("indication", "value"),
# )
# def number_render(age, sex, prothesis, indication):
#     return f"sex: {sex}, age: {age}"
#     sex = encode_sex(sex=sex)
#     prothesis = encode_prosthesis(prothesis=prothesis)
#     indication = encode_indication(indication)
#     indication = encode_indication(indication)
#     risk = 0.03*sex + 0.1*age + 0.01*prothesis
#     return f"risk of something: {risk*100}%"

def encode_sex(sex: str) -> int:
    sex_map = {
        "male": 1,
        "female": 2
    }
    return sex_map[sex]

def encode_prosthesis(prosthesis: str) -> int:
    prosthesis_map = {
        'hemi': 1,
        'reverse': 2,
        'anatomical': 3
    }
    return prosthesis_map[prosthesis]

def encode_indication(indication: str) -> int:
    indication_map = {
        'acute fracture': 0,
        'fraktur sequelae': 1,
        'osteoarthritis': 2,
        'cuff damage': 4     
    }
    return indication_map[indication]

def encode_comorb(comorb: str) -> int:
    comorb_map = {
        "yes": 1,
        "no": 0
    }

if __name__ == "__main__":
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
