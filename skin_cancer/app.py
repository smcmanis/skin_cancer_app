import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,
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
    className='content',
    style={'display':'none'},
    children=[
        dcc.Upload(
            html.Button('Add Photo', id='upload-btn'), id='upload',
            accept='image/*', 
            className='btn',
            className_active='upload-active',), 
        html.Div(
            id='img-row',
            children=[
                html.Div([html.Img(id='display-img', className='display-img')], className='img-container')
            ]
        ),
        html.Button('Analyze',id='submit-btn', className='btn disabled')
    ]
)


# loading circle in the img-container whilst upload loaing
#  button greyed out then green when successful image 
@app.callback(
    [Output('display-img', 'src'),
    Output('img-store', 'src')],
    [Input('upload', 'contents'),
     Input('upload-btn', 'n_clicks')],
     [State('img-store', 'src')])
def upload_img(new_img, n_clicks, store):
    # if new_img is None:  
    if new_img is None:
        if store is None:
            return '', '' 
        else:
            return store, store
    else:
        return new_img, new_img

@app.callback(
    [Output('submit-btn', 'disabled'),
    Output('submit-btn', 'className')],
    [Input('display-img', 'src')])
def set_submit_btn(src):
    if src != '':
        return False, 'btn submit-rdy'
    return True,'btn disabled'
    

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
    style={'display':'none'},
    children=[
        html.Div(
        children=[
            html.Div([html.Img(id='analyzed-img', className='display-img')], className='img-container'),
            html.Div([

            ])
        ]
    )]
)


# Make results. might want to store them in a hidden div as well.
@app.callback(
    Output('analyzed-img', 'src'),
    [Input('results-content', 'style')],
    [State('img-store', 'src')])
def results(results, src):
    if src == '':
        raise PreventUpdate

    # Create image to show with results...
    analyzed_img = src
    return analyzed_img

app.layout = html.Div([
    html.Div([
        html.Img(id='img-store', style={'display': 'none'}),
        dcc.Tabs([
            dcc.Tab(label='About', value='about-tab', className='tab'),
            dcc.Tab(label='Start', value='start-tab', className='tab'),
            dcc.Tab(label='Results', value='results-tab', className='tab')
        ], id='tabs',
            value='start-tab',
            className='tab'),
        html.Div(id='tabs-container',
                 children=[
                     html.Div([
                         about_tab,
                         start_tab,
                         results_tab
                     ])
                 ]),

    ], className='container')
], className='page')


@app.callback(
    [Output('about-content', 'style'),
    Output('start-content', 'style'),
    Output('results-content', 'style')],
    [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'about-tab':
        return {}, {'display': 'none'}, {'display': 'none'}
    elif tab == 'start-tab':
        return {'display': 'none'}, {}, {'display': 'none'}
    elif tab == 'results-tab':
        return {'display': 'none'}, {'display': 'none'}, {}


# @app.callback(
#     Output('tabs-container', 'children'),
#     [Input('tabs', 'value')])
# def render_content(tab):
#     if tab == 'start-tab':
#         return start_tab
#     elif tab == 'about-tab':
#         return about_tab
# @app.callback(
#     Output("output", "children"),
#     [Input("upload-img", "value")],
# )
# def update_selection_mode(img):
#     if img:
#         return html.Div([
#             html.Div(
#                 id="img",
#                 children=[
#                     html.Img(
#                         src='assets/example.jpg',
#                         width='200px'
#                     ),
#                 ],
#             ),
#             html.P('Melanoma: 87%'),
#             html.P('Mole: 10%'),
#             html.P('Other: 3%'),
#         ])


server = app.server

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=5001, debug=True)
