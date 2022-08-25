from project import WeatherAPI, Twitter

if __name__ == "__main__":
    twitter = Twitter()
    twitter.authenticate()
    weather = WeatherAPI()
    weather.get_data(lat = "-23.55", lon = "-46.64", units="metric")
    tweet = weather.create_tweet()
    twitter.post_tweet(tweet)