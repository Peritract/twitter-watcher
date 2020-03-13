from datetime import datetime
import tweepy
import csv


class Watcher(tweepy.StreamListener):
    """
    Collects tweets from a Twitter stream and writes them to a file.
    """
    def __init__(self, api, filter_list, out_file="tweets.csv"):

        # Assign authentication object
        self.api = api

        # Assign outfile
        self.out_file = out_file

        # Raise an error if credentials are invalid
        if not self.api.verify_credentials():
            self.on_error("Invalid credentials.")

        # The list of hashtags/searches to watch for
        self.filter = filter_list

        # Set headings for the file
        with open(self.out_file, "a") as file:
            writer = csv.writer(file, )
            writer.writerow(["text", "author",
                             "created_at",
                             "retweet_count",
                             "favorite_count",
                             "verified",
                             "source"])

    def write_to_file(self, status):
        """
        Writes a status to a .csv.
        """
        text = status.extended_tweet["full_text"] \
        if hasattr(status, "extended_tweet") else status.text

        text.encode("utf-8")

        with open(self.out_file, "a", encoding="utf8") as file:
            writer = csv.writer(file, delimiter="\t")
            row = [text,
                   status.author.screen_name,
                   status.created_at,
                   status.retweet_count,
                   status.favorite_count,
                   status.author.verified,
                   status.source
                   ]
            writer.writerow(row)

    def on_status(self, status):
        """
        When a tweet comes down the stream, sends it in the right direction.
        """
        self.write_to_file(status)

    def on_error(self, error):
        """
        If Twitter returns an error, log it.
        """
        print(datetime.now(), "Error:", error)
