from datetime import datetime
import tweepy


class Watcher(tweepy.StreamListener):
    """
    Collects tweets from a Twitter stream and writes them to a file.
    """
    def __init__(self, api, filter_list):

        # Assign authentication object
        self.api = api

        # Raise an error if credentials are invalid
        if not self.api.verify_credentials():
            self.on_error("Invalid credentials.")

        # The list of hashtags/searches to watch for
        self.filter = filter_list

    def on_status(self, status):
        """
        When a tweet comes down the stream, write it to file.
        """
        with open("tweets.csv", "a") as file:
            file.write(status.text)

    def on_error(self, error):
        """
        If Twitter returns an error, log it.
        """
        print(datetime.now(), "Error:", error)
