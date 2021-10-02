import tweepy
from dotenv import dotenv_values
from watcher import Watcher

if __name__ == "__main__":

    # Access a .env file
    ENV = dotenv_values()

    # Authorise with the Twitter API
    auth = tweepy.OAuthHandler(ENV['C_KEY'], ENV['C_SECRET'])
    auth.set_access_token(ENV['A_TOKEN'], ENV['A_SECRET'])

    API = tweepy.API(auth)

    # Instantiate the Tweet handler
    watcher = Watcher(API, ENV["SEARCH_STRING"], connection=ENV['DB_CONNECTION'], out=ENV["OUT_FILE"], out_type=ENV['OUT_TYPE'])

    stream = tweepy.Stream(auth=API.auth, listener=watcher,
                           tweet_mode='extended')  # Start watching the stream

    # Set the filters and run asynchronously
    stream.filter(track=watcher.filter, languages=["en"],
                  is_async=True)
