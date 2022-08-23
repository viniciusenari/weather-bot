from project import WeatherAPI, Twitter

if __name__ == "__main__":
    twitter = Twitter()
    twitter.authenticate()
    weather = WeatherAPI()
    weather.get_data()
    tweet = weather.create_tweet()
    twitter.post_tweet(tweet)