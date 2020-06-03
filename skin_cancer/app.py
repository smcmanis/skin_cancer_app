import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {
            'charset': 'utf-8',
        },
        {
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1, shrink-to-fit=no'
        }
    ],)

start_tab = html.Div(
    id='start-content',
    style={'display':'none', 'min-height': '50vh'},
    children=[
    dbc.Row(
        [
            dbc.Col(
                dcc.Upload(
                    dbc.Button("Add Photo", color="primary", id="upload-btn", block=True),
                    id="upload",
                    accept='image/*'),
                width={"size":3})
        ],
        justify="center"
    ),
    dbc.Row(
        [
            dbc.Col(dbc.Row(
                html.Img(id='display-img', className='display-img'),
                justify="center"
            ), width={"size":8} ),
        ],
        # justify="center"
    ),
    dbc.Row(
        [
            dbc.Col(
                dbc.Button("Analyze", color="success", id="submit-btn", disabled=True, block=True),
                width={"size":3})
        ],
        justify="center"
    ),
    dbc.Row([dbc.Col(dbc.Card(id='results-card'), width=10)])
    ],
)

about_tab = html.Div(
    id='about-content',
    className='content',
    style={'display':'none'},
    children=[
        html.H1('Skin Cancer App')
    ]
)
results_tab = html.Div(
    id='results-content',
    className='content',
    style={'display':'none'}
)

card = dbc.Card(
    [
        dbc.CardHeader(
            dbc.Tabs(
                [
                    dbc.Tab(label="About", tab_id="tab-about"
                    ),
                    dbc.Tab(label="Start", tab_id="tab-start"),
                    dbc.Tab(label="Results", tab_id="tab-results"),
                ],
                id="card-tabs",
                card=True,
                active_tab="tab-start",
                persistence=True, 
                persistence_type="session"
            )
        ),
        dbc.CardBody(html.P(
            id="card-content", 
            className="card-text",
            children=[about_tab, start_tab, results_tab])),
    ]
)


@app.callback(
    [Output('about-content', 'style'),
    Output('start-content', 'style'),
    Output('results-content', 'style')], 
    [Input("card-tabs", "active_tab")]
)
def tab_content(active_tab):
    if active_tab == 'tab-about':
        return {}, {'display': 'none'}, {'display': 'none'}
    elif active_tab == 'tab-start':
        return {'display': 'none'}, {}, {'display': 'none'}
    elif active_tab == 'tab-results':
        return {'display': 'none'}, {'display': 'none'}, {}

@app.callback(
    Output('display-img', 'src'),
    [Input('upload', 'contents'),
    Input('upload-btn', 'n_clicks')])
def upload_img(new_img, n_clicks):
    if new_img is None:  
        raise PreventUpdate
    return new_img


@app.callback(
    Output('submit-btn', 'disabled'),
    [Input('display-img', 'src')])
def set_submit_btn(src):
    if src != '':
        return False
    return True

@app.callback(
    Output('results-card', 'children'),
    [Input('submit-btn', 'n_clicks'),
    Input('display-img', 'src')]
)
def show_results(n_clicks, img):
    if not n_clicks or not img:
        raise PreventUpdate
    # CNN call
    risk = "High"
    class_probs = [
        (0.8375, 'Melanocytic Nevi (mole)'), 
        (0.0962, 'Melanoma'),
        (0.0663, 'Benign Keratosis')
        ]
    return [
        dbc.CardHeader("Results"),
        dbc.CardBody([
            dbc.Row([
                dbc.Col(f"{(class_probs[0][0]*100):.2f}%", width=3), 
                dbc.Col(f"{class_probs[0][1]}", width=9), 
                ],
                justify="between"),
            dbc.Row([
                dbc.Col(f"{(class_probs[1][0]*100):.2f}%", width=3), 
                dbc.Col(f"{class_probs[1][1]}", width=9), 
                ],
                justify="between"),
            dbc.Row([
                dbc.Col(f"{(class_probs[2][0]*100):.2f}%", width=3), 
                dbc.Col(f"{class_probs[2][1]}", width=9), 
                ],
                justify="between"),
            
        ])
        
        # dbc.CardBody(
        #     [

        #         html.H4('Risk'),
        #         dbc.Row([
        #             html.P(risk),
        #             html.P(f"{class_probs[0][1]}, {(class_probs[0][0]*100):.2f}%")
        #         ])
        #     ]
        # ),
    ]


app.layout = dbc.Container(
    card
)

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=5001, debug=True)
