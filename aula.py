#importando bibliotecas
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

#inicializando o aplicatvo
app = Dash(__name__)

#Criando o Dataframe
df = pd.DataFrame({
    "Fruta": ["Maçãs", "Laranjas", "Bananas", "Maçãs", "Laranjas", "Bananas"],
    "Quantidade": [50, 27, 38, 37, 50, 51],
    "Vendedor": ["Francisco", "Francisco", "Francisco", "João", "João", "João"]
})

#criando o gráfico
fig = px.bar(df, x="Fruta", y="Quantidade", color="Vendedor", barmode="group")

#Criando o layout com html e dcc
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

#Rodando em um servidor local
if __name__ == '__main__':
    app.run_server(debug=True)