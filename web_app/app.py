from dash import Dash, dcc, html, Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
from dash.dependencies import Input, Output
from creating_csvs import update_tweets
from get_data import monthly_favorites, monthly_retweets
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from data_clean import clean_tweet
app = Dash(__name__)
######################################################
app.layout = html.Div([
    html.H1(children='Hello Elon'),
    html.Div(children = '''
        Check out your monthly twitter report
    '''),
    html.Div(id = 'graphs', children = []),
    html.A(html.Button('Update Tweets', id = 'tweet-update-event', style = {'position' : 'absolute', 'right': '10px'})),
    html.Div(id = 'prediction', children=[
        html.Div(dcc.Textarea(id = 'input-box', value = "What's on your mind"), style={'margin-top' : '1em'}),
        html.Button('Predict Feedback', id = 'predict-button', style={'margin-top' : '1em'}),
        html.Div(id = 'prediction-output', children='Enter tweet to predict feedback', style={'margin-top' : '1em'})
    ])
])
@app.callback(
    Output("graphs", "children"),
    Input('tweet-update-event', 'n_clicks')
)
def update(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        # update_tweets(1000)
        retweets = pd.read_csv('./assets/csv files/data/retweets.csv')
        favorites = pd.read_csv('./assets/csv files/data/favorites.csv')
        retweets_monthly = monthly_retweets(retweets)
        favorites_monthly = monthly_favorites(favorites)
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
        return dcc.Graph(
        id = 'retweets-monthly',
        figure = fig,
    )
@app.callback(
    Output('prediction-output', 'children'),
    [Input('predict-button', 'n_clicks')],
    [State('input-box', 'value')]
)
def predict_output(n_clicks, value):
    if n_clicks is None:
        raise PreventUpdate
    else:
        retweets = pd.read_csv('./assets/csv files/data/retweets.csv')
        favorites = pd.read_csv('./assets/csv files/data/favorites.csv')
        retweets = retweets.dropna()
        favorites = favorites.dropna()
        stemmed_tweet = clean_tweet(value)
        tf_idf = TfidfVectorizer(max_features=20)
        ##########################################################
        favorites_prediction = pickle.load(open('model/favorites.pkl', 'rb'))
        tf_x_favorites = tf_idf.fit_transform(favorites['Tweet'])
        y_favorites = favorites[['nb_favorites']]
        x_favorites_test = tf_idf.transform([stemmed_tweet])
        favorites_prediction.fit(tf_x_favorites,y_favorites)
        fav_pred = int(np.absolute(favorites_prediction.predict(x_favorites_test)[0][0]))
        ######################################################
        retweets_prediction = pickle.load(open('model/retweets.pkl', 'rb'))
        tf_x_retweets = tf_idf.fit_transform(retweets['Tweet'])
        y_retweets = retweets[['nb_retweets']]
        x_retweets_test = tf_idf.transform([stemmed_tweet])
        retweets_prediction.fit(tf_x_retweets,y_retweets)
        ret_pred = int(np.absolute(retweets_prediction.predict(x_retweets_test)[0][0]))
        ##################################################################
        return (f"Predicted number of favorites: {fav_pred} Predicted number of retweets: {ret_pred}")
if __name__ == '__main__':
    app.run_server(debug=True)