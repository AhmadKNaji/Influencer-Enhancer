import pandas as pd

tweets = pd.read_csv('../assets/csv files/unified_tweets.csv')

data_retweets = tweets[['Tweet', 'Time', 'nb_retweets']]

data_favorites = tweets[['Tweet', 'Time', 'nb_favorites']]

train_data_retweets = data_retweets.iloc[100:,:]

test_data_retweets = data_retweets.iloc[:100,:]

train_data_favorites = data_favorites.iloc[100:,:]

test_data_favorites = data_favorites.iloc[:100,:]

pd.DataFrame.to_csv(train_data_retweets, '../assets/csv files/train/retweets.csv')

pd.DataFrame.to_csv(test_data_retweets, '../assets/csv files/test/retweets.csv')

pd.DataFrame.to_csv(train_data_favorites, '../assets/csv files/train/favorites.csv')

pd.DataFrame.to_csv(test_data_favorites, '../assets/csv files/test/favorites.csv')

