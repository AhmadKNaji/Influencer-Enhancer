import sys

sys.path.insert(1, '../processing')

from twitter import Tweets

from data_clean import clean_tweet

import pandas as pd

tweets = Tweets('elonmusk')

data = tweets.get_tweets(1000)

datac = data.copy()

datac

pd.DataFrame.to_csv(datac, '../assets/csv files/raw_tweets.csv')

datac['Tweet'] = datac['Tweet'].apply(lambda tweet: clean_tweet(tweet))

pd.DataFrame.to_csv(datac, '../assets/csv files/unified_tweets.csv')