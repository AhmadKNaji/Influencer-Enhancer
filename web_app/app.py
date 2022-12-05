from dash import Dash, dcc, html, Input, Output, State
import plotly.express as px
import pandas as pd
import get_data
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from creating_csvs import update_tweets
from get_data import monthly_favorites, monthly_retweets

# creating_csvs.update_tweets(1000)

app = Dash(__name__)

retweets = pd.read_csv('./assets/csv files/data/retweets.csv')

favorites = pd.read_csv('./assets/csv files/data/favorites.csv')

retweets_monthly = get_data.monthly_retweets(retweets)

favorites_monthly = get_data.monthly_favorites(favorites)


fig = make_subplots(
    rows=1, 
    cols=2, 
    subplot_titles=("Montly Retweets Report", "Monthly Favorites Report")
)

fig.add_trace(
    go.Bar(
        x=np.array(retweets_monthly['Time']), 
        y=np.array(retweets_monthly['nb_retweets']),
        showlegend=False,
        text = [f"{rt:,}" for rt in np.array(retweets_monthly['nb_retweets'])],
        hoverinfo='text'
        ),
    row=1, col=1
)

fig.add_trace(
    go.Bar(
        x=np.array(favorites_monthly['Time']), 
        y=np.array(favorites_monthly['nb_favorites']),
        showlegend=False,
        text = [f"{rt:,}" for rt in np.array(favorites_monthly['nb_favorites'])],
        hoverinfo='text'
        ),
    row=1, col=2
)

fig.update_traces(hoverinfo="none", hovertemplate=None)

######################################################

app.layout = html.Div([
    html.H1(children='Hello Elon'),

    html.Div(children = '''
        Retweets: Here's your monthly twitter report
    '''),

    dcc.Graph(
        id = 'retweets-monthly',
        figure = fig,
    ),
    
    html.Button([dbc.Button("Primary", color = "primary", className = "me-1")])

])

@app.callback(
    Output('container-button-basic', 'children'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value')
)
def predict_output(value, n_clicks):
    return 'Predicted number of retweets: "{}"\nPredicted number of favorites: "{}"'.format(1,3)


if __name__ == '__main__':
    app.run_server(debug=True)