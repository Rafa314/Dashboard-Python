from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruta": ["Maçãs", "Laranjas", "Bananas", "Maçãs", "Laranjas", "Bananas"],
    "Quantidade": [50, 47, 38, 55, 40, 31],
    "Vendedor": ["Francisco", "Francisco", "Francisco", "João", "João", "João"]
})

#criando o gráfico
fig = px.bar(df, x="Fruta", y="Quantidade", color="Vendedor", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Vendas'),
    html.H3(children='Comparando o número de vendas entre dois vendedores'),
    html.Div(children='''
        A simples comparação entre dois vendedores na feira
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)