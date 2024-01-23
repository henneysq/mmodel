import dash
from dash import Dash, dcc, html, Input, Output, callback

dash.register_page(__name__, path='/')

WELCOME_MSG = """
    # Markos' Risk Prediction Model

    Hi Markos! Congratulations on becoming a dad!

    Here's an ugly and incomplete rendition of your beautiful model. It's in progress..

    See [Background Information](#background-information) for model details about the model.

    """


LR_INDENT = (600, 600)

layout = html.Div(
    style={'margin-left': f"{LR_INDENT[0]}px", 'margin-right': f"{LR_INDENT[1]}px", "margin-top":"7px"},
    children=[
        dcc.Markdown(WELCOME_MSG, mathjax=True),
        # dcc.Markdown(WELCOME_MSG, mathjax=True),
        html.H4("Change the values of factors to calculate the risk of something!"),
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

        html.Hr(),
        html.Div(dcc.Markdown(id="number-out")),
        #dcc.Markdown(),
    ]
)

@callback(
        Output(component_id="number-out", component_property="children"),
        Input(component_id="age", component_property="value"),
        Input(component_id="sex", component_property="value"),
        Input(component_id="prosthesis", component_property="value"),
        Input(component_id="indication", component_property="value"),
        Input(component_id="comorb-cardiac", component_property="value"),
        Input(component_id="comorb-diabetic", component_property="value"),
        Input(component_id="comorb-renal", component_property="value"),
        Input(component_id="comorb-neuronal", component_property="value"),
)
def render_output(age, sex, prosthesis, indication, comcard, comdia, comren, comneu):
    if age is None:
        return f"#### Please enter age"
    
    try:
        sex = encode_sex(sex)
        prosthesis = encode_prosthesis(prosthesis)
        indication = encode_indication(indication)
        comcard = encode_comorb(comcard)
        comdia = encode_comorb(comdia)
        comren = encode_comorb(comren)
        comneu = encode_comorb(comneu)
        risk = 0.1 + 0.01*age + 0.01*sex + 0.01*prosthesis + 0.01*indication + 0.01*comcard + 0.01*comdia + 0.01*comren + 0.01*comneu
        risk = risk * 100
    except Exception as e:
        return str(e)

    #return f"Risk is {risk}% based on age: {age},\nsex: {sex},\nprosthesis: {prosthesis}, \nindication: {indication}, \ncardiac co-morbidity: {comcard}, \ndiabetic co-mobidity: {comdia}, \nrenal co-morbidity: {comren}, \nneuronal co-morbidity: {comneu}"
    return f"""
        #### {risk:.2f}% risk of serious adverse event(s) within [...] days of surgey.
    """

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
    return comorb_map[comorb]
