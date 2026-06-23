import pandas as pd
import dash
import plotly.graph_objs as go
from dash import html, dcc

data=pd.read_csv('gapminder.csv')
app = dash.Dash()

app.layout= html.H1(children="My first Dashboard", style={'color':'red', 'text-align':'center'})
app.layout = html.Div([
    html.Div(children=[
        html.H1("My First DashBoard", style={'color': 'red', 'text-align':'center'})
    ],style={'border': '1px black solid', 'float': 'left', 'width':'100%', 'height': '50px'}),
    html.Div(children=[
        dcc.Graph(id='scatter-plot', figure={'data':[go.Scatter(
            x=data['pop'],
            y = data['gdpPercap'],
            mode='markers'
        )],
                                             'layout': go.Layout(title='Scatter plot')})
    ],style={'border': '1px black solid', 'float': 'left', 'width':'49%', 'height': '350px'}),
    html.Div(children=[
      dcc.Graph(id='box-plot',
             figure = {
                 'data':[go.Box(x=data['gdpPercap'])],
                 'layout':go.Layout(title='Boxplot')
             }
                )
    ],style={'border': '1px black solid', 'float': 'left', 'width':'49%'})
])

if __name__ == '__main__':
    app.run(debug=True)