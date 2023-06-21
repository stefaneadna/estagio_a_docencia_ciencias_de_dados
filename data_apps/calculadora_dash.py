import dash
from dash import html, Dash, dcc
from dash.dependencies import Input, Output

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Calculadora"),
        html.Div(
            children=[
                dcc.Input(id="input-1", type="number", placeholder="Digite o primeiro número"),
                dcc.Input(id="input-2", type="number", placeholder="Digite o segundo número"),
                html.Button("Somar", id="button-sum", n_clicks=0),
                html.Button("Subtrair", id="button-subtract", n_clicks=0),
                html.Button("Multiplicar", id="button-multiply", n_clicks=0),
                html.Button("Dividir", id="button-divide", n_clicks=0),
                html.Div(id="output")
            ]
        )
    ]
)

@app.callback(
    Output("output", "children"),
    Input("button-sum", "n_clicks"),
     Input("button-subtract", "n_clicks"),
     Input("button-multiply", "n_clicks"),
     Input("button-divide", "n_clicks"),
    dash.dependencies.State("input-1", "value"),
     dash.dependencies.State("input-2", "value")
)
def update_output(sum_clicks, subtract_clicks, multiply_clicks, divide_clicks, input1, input2):
    if sum_clicks > 0:
        result = input1 + input2
    elif subtract_clicks > 0:
        result = input1 - input2
    elif multiply_clicks > 0:
        result = input1 * input2
    elif divide_clicks > 0:
        result = input1 / input2
    else:
        result = ""

    return f"Resultado: {result}"

if __name__ == "__main__":
    app.run_server(debug=True)
