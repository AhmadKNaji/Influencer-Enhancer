import pandas as pd
def monthly_retweets(df):
    """
    This function returns the dataframe with the retweets grouped by month.
    params:
    df(DataFrame): The Dataframe containing the retweets target.
    returns:
    retweets_monthly_grouped(Dataframe): Grouped retweets by month
    """
    monthly_tweets = df.copy()
    monthly_tweets['Time'] = pd.to_datetime(monthly_tweets['Time'], format='%Y-%m').dt.strftime('%Y-%m')
    retweets_monthly_grouped = monthly_tweets.groupby('Time')['nb_retweets'].sum().reset_index()
    return retweets_monthly_grouped

def monthly_favorites(df):
    """
    This function returns the dataframe with the favorites grouped by month.
    params:
    df(DataFrame): The Dataframe containing the favorites target.
    returns:
    monthly_favorites_grouped(Dataframe): Grouped favorites by month
    """
    monthly_favorites = df.copy()
    monthly_favorites['Time'] = pd.to_datetime(monthly_favorites['Time'], format='%Y-%m').dt.strftime('%Y-%m')
    monthly_favorites_grouped = monthly_favorites.groupby('Time')['nb_favorites'].sum().reset_index()
    return monthly_favorites_grouped