class Tweets:

    import configparser

    import tweepy

    import pandas as pd

    def __init__(self, username):

        self.username = username

    def who(self):

        return self.username

    def get_tweets(self):

        config = self.configparser.ConfigParser()

        config.read('./config/Twitter Keys.ini')

        # Read the values

        api_key = config['twitter']['api_key']

        api_key_secret = config['twitter']['api_key_secret']

        access_token = config['twitter']['access_token']

        access_token_secret = config['twitter']['access_token_secret']

        # Twitter Authentication

        auth = self.tweepy.OAuthHandler(api_key, api_key_secret)

        auth.set_access_token(access_token, access_token_secret)

        api = self.tweepy.API(auth)

        # using get_user with id

        user_name = self.username

        tweets = api.user_timeline(screen_name=user_name, count = 200,tweet_mode='extended')

        # create DataFrame

        columns = ['TweetId', 'User', 'Tweet', 'Time', 'nb_retweets', 'nb_favorites']

        data = []

        for tweet in tweets:

            data.append([tweet.id, tweet.user.screen_name, tweet.full_text, tweet.created_at, tweet.retweet_count, tweet.favorite_count])

        df = self.pd.DataFrame(data, columns=columns)

        return df