from twitter import Tweets
from data_clean import clean_tweet
import pandas as pd
def update_tweets(nb):
    """
    This function creates two csv files (retweets and favorites) after stemming takes place
    params:
    nb(int): number of rows to fetch
    """
    tweets = Tweets('elonmusk')
    data = tweets.get_tweets(nb)
    datac = data.copy()
    pd.DataFrame.to_csv(datac, 'assets/csv files/raw_tweets.csv')
    datac['Tweet'] = datac['Tweet'].apply(lambda tweet: clean_tweet(tweet))
    pd.DataFrame.to_csv(datac, 'assets/csv files/unified_tweets.csv')
    data_retweets = datac[['Tweet', 'Time', 'nb_retweets']]
    data_favorites = datac[['Tweet', 'Time', 'nb_favorites']]
    pd.DataFrame.to_csv(data_retweets, 'assets/csv files/data/retweets.csv')
    pd.DataFrame.to_csv(data_favorites, 'assets/csv files/data/favorites.csv')