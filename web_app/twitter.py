
import csv
def get_stopwords():
    """
    This function returns a list of stopwords from our csv file.
    """
    with open('assets/csv files/twitterStopWords.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        twitter_stopwords = []
        for d in data:
            twitter_stopwords.append(d[0].replace(' ', ''))
    return twitter_stopwords
class Tweets:
    import configparser
    import tweepy
    import pandas as pd
    def __init__(self, username):
        self.username = username
    def who(self):
        """
        This returns the username.
        """
        return self.username
    def get_tweets(self, rows_of_data):
        """
        This function returns a dataframe containing a specified number of tweets.
        params:
        rows_of_data(int): Number of rows to fetch
        returns:
        df(DataFrame): Dataframe with tweets
        """
        # use config to address ini file
        config = self.configparser.ConfigParser()
        config.read('twitter_keys.ini')
        # Read the values
        api_key = config['TWITTER']['api_key']
        api_key_secret = config['TWITTER']['api_key_secret']
        access_token = config['TWITTER']['access_token']
        access_token_secret = config['TWITTER']['access_token_secret']
        # Twitter Authentication
        auth = self.tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = self.tweepy.API(auth)
        # using get_user with id
        # We use pagination since we can only pull a maximum of 200 tweets
        user_name = self.username
        paginated_tweets = self.tweepy.Cursor(api.user_timeline, screen_name = user_name, exclude_replies=True).items(rows_of_data)
        # create DataFrame
        columns = ['TweetId', 'User', 'Tweet', 'Time', 'nb_retweets', 'nb_favorites']
        data = []
        for status in paginated_tweets:
            data.append([status.id, status.user.screen_name, status.text, status.created_at, status.retweet_count, status.favorite_count])
        df = self.pd.DataFrame(data, columns=columns)
        return df