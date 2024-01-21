import dash
from dash import Dash, dcc, html, Input, Output, callback

dash.register_page(__name__)

LR_INDENT = (600, 600)

BACKGROUND_MSG = """
    # Background Information 

    This tool implements the prediction model for risk of serious adverse events
    
    ## Model Definition
    
    The risk prediction model is based on a [...] model:

    $y = \mathbf{X} \\beta$,

    where $y$ is the risk of serious adverse events,
    $\mathbf{X}$ is the set of predictive variables,
    and $\\beta$ are the parameters weights.

    ## Parameter Encoding

    Currently, all parameter weights are $0.01$, and the off-set is $0.1$.

    Sex is encoded `'male': 1, 'female': 2`

    Prosthesis is encoded `'hemi': 1, 'reverse': 2, 'anatomical': 3`

    Indication is encoded `'acute fracture': 0, 'fraktur sequelae': 1, 'osteoarthritis': 2, 'cuff damage': 4`
"""


layout = html.Div(
    style={'margin-left': f"{LR_INDENT[0]}px", 'margin-right': f"{LR_INDENT[1]}px", "margin-top":"7px"},
    children=[
        dcc.Markdown(BACKGROUND_MSG, mathjax=True),
    ]
)
