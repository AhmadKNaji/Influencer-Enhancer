import pandas as pd

import matplotlib.pyplot as plt

def monthly_retweets(df):

    monthly_tweets = df.copy()

    monthly_tweets['Time'] = pd.to_datetime(monthly_tweets['Time'], format='%Y-%m').dt.strftime('%Y-%m')

    retweets_monthly_grouped = monthly_tweets.groupby('Time')['nb_retweets'].sum().reset_index()

    return retweets_monthly_grouped

def monthly_favorites(df):

    monthly_favorites = df.copy()

    monthly_favorites['Time'] = pd.to_datetime(monthly_favorites['Time'], format='%Y-%m').dt.strftime('%Y-%m')

    monthly_favorites_grouped = monthly_favorites.groupby('Time')['nb_favorites'].sum().reset_index()

    return monthly_favorites_grouped