import tweepy
import ibm_db as db
from dotenv import load_dotenv
from os import getenv
from watcher import Watcher

if __name__ == "__main__":

    # Access a .env file
    load_dotenv()

    # Load in environment variables
    C_KEY = getenv('C_KEY')
    C_SECRET = getenv('C_SECRET')
    A_TOKEN = getenv('A_TOKEN')
    A_SECRET = getenv('A_SECRET')
    DB_CONNECTION = getenv("DB_CONNECTION")

    # Authorise with the Twitter API
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_SECRET)

    API = tweepy.API(auth)

    # Instantiate the Tweet handler
    watcher = Watcher(API, ["#maga"], connection=DB_CONNECTION, out="tweets", out_type="file")

    stream = tweepy.Stream(auth=API.auth, listener=watcher,
                           tweet_mode='extended')  # Start watching the stream

    # Set the filters and run asynchronously
    stream.filter(track=watcher.filter, languages=["en"],
                  is_async=True)
