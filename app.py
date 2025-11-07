from dash import Dash, dcc, html, Input, Output, callback

app = Dash(__name__)
app.title = "Kaffe"
server = app.server

app.layout = html.Div([
    html.Div(
        children=html.Div([
            html.H1('Kaffekalkulator')
        ])
    ),   
    html.Div(["Oppgi vann i ml: ",
        dcc.Input(id='my-input', value="initial-value", type='number')
    ]),
    html.Br(),
    html.Div(id='my-output'),

])

@callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def vanntilkaffe(vann, forhold = (1000/60)):
    mengdekaffe = round(vann/forhold, 2)
    return f'Gram kaffe: {mengdekaffe} g'

if __name__ == '__main__':
    app.run(debug=False)