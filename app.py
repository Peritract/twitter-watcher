import tweepy
from dotenv import dotenv_values
from scripts.stream import Watcher

if __name__ == "__main__":

    # Access a .env file
    ENV = dotenv_values()

    # Create the streaming object
    watcher = Watcher(ENV["C_KEY"],
                      ENV["C_SECRET"],
                      ENV["A_TOKEN"],
                      ENV["A_SECRET"])

    watcher.filter(track=ENV["SEARCH_TERMS"].split(","),
                   threaded=True,
                   languages=ENV["LANGUAGES"].split(","))