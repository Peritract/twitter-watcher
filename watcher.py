from datetime import datetime
import csv


class Watcher(tweepy.StreamListener):
    """
    Collects tweets from a Twitter stream and records them.

    API - an authorised Tweepy API object
    filter_list - a list of search strings
    connection - a credentials string for an IBM DB2 database
    out - a name for the outfile/table
    out_type - a string describing where the results should be sent: 'file', 'db', or 'both'
    """
    def __init__(self, api, filter_list, connection=None, out_file="tweets", out_type="file"):

        self.api = api
        self.connection = connection
        self.out_file = out_file + '.csv'
        self.out_type = out_type
        self.filter = filter_list if type(filter_list) == list else [filter_list]

        # Set up the outfile and/or database
        if self.out_type == "file" or self.out_type == "both":
            self.set_up_file()

        # Raise an error if credentials are invalid
        if not self.api.verify_credentials():
            self.on_error("Invalid credentials.")        

    def prepare_status(self, status):
        """
        Extracts the desired data from a status.
        """
        text = status.extended_tweet["full_text"] \
        if hasattr(status, "extended_tweet") else status.text

        text.encode("utf-8")

        data = [text,
                status.author.screen_name,
                status.created_at,
                status.author.verified,
                status.source
                ]

        return data

    def set_up_file(self):
        """
        Create and format the outfile.
        """
        with open(self.out_file, "w") as file:
            writer = csv.writer(file)
            writer.writerow(["text", "author",
                             "created_at",
                             "verified",
                             "source"])

    def write_to_file(self, data):
        """
        Writes a prepared status to a .csv.
        """
        with open(self.out_file, "a", encoding="utf8") as file:
            writer = csv.writer(file, delimiter="\t")
            writer.writerow(data)

    def on_status(self, status):
        """
        When a tweet comes down the stream, send it in the right direction.
        """
        data = self.prepare_status(status)
        if self.out_type == "file" or self.out_type == "both":
            self.write_to_file(data)

    def on_error(self, error):
        """
        If Twitter returns an error, log it.
        """
        print(datetime.now(), "Error:", error)
