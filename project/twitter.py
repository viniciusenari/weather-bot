from config import twitter_api_key, twitter_api_key_secret, twitter_access_token, twitter_access_token_secret
import tweepy

class Twitter:
    def __init__(self):
        self.api = None

    def authenticate(self):
        auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_key_secret)
        auth.set_access_token(twitter_access_token, twitter_access_token_secret)
        self.api = tweepy.API(auth)
    
    def post_tweet(self, text):
        self.api.update_status(status = text)