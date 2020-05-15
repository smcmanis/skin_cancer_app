import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

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

# header = html.Header(
#     children=[
#         html.Div(
#             className='left-header',
#             children=[html.H1('MelaKNOWma')]
#             # ['BetterDriver'], className='header-title'
#         ),
#         html.Div(
#             className='right-header',
#         )
#     ]
# )


# start_tab = html.Div(
#     id='start-content',
#     className='content',
#     children=[
#         html.Div([
#             dcc.Upload(
#                 html.Button('Add Photo', id='upload-btn'))
#         ], className="row"),

#         html.Div(
#             id='image-row',
#             children=[
#                 html.H3("hello"),
#                 html.Div([
#                     html.Img(src='assets/example.jpg')
#                 ])
#             ]
#         ),
#         html.
#     ]
# )

start_tab = html.Div(
    id='start-content',
    className='content',
    children=[
        dcc.Upload(
            html.Button('Add Photo', id='upload')),
        html.Div(
            id='image-row',
            children=[
                html.H3("hello"),
                html.Div([], id='img-container')
            ]
        ),
        html.Button('Analyze')
    ]
)


@app.callback(
    Output('img-container', 'children'),
    [Input('upload', 'contents')]
)
def upload_image(image):
    return image
pass

about_tab = html.Div()

app.layout = html.Div([
    html.Div([
        dcc.Tabs([
            dcc.Tab(label='About', value='about-tab', className='tab'),
            dcc.Tab(label='Start', value='start-tab', className='tab'),
            dcc.Tab(label='Results', value='results-tab', className='tab')
        ], id='tabs',
            value='start-tab',
            className='tab'),
        html.Div(id='tabs-container')
    ], className='container')
], className='page')



@app.callback(
    Output('tabs-container', 'children'),
    [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'start-tab':
        return start_tab
    elif tab == 'about-tab':
        return about_tab
# @app.callback(
#     Output("output", "children"),
#     [Input("upload-image", "value")],
# )
# def update_selection_mode(img):
#     if img:
#         return html.Div([
#             html.Div(
#                 id="image",
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
