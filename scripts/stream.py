"""This file contains the definition of the Watcher class; this class listens for new tweets and records them.
"""

from tweepy import Stream
from pymongo import MongoClient

import json

class Watcher(Stream):

    def __init__(self, c_key, c_secret, a_token, a_secret,
                 db_uri, db_name, db_collection):
        self.db_connection = MongoClient(db_uri)
        self.db_name = db_name
        self.db_collection = db_collection
        self.write_to_db({"message": "Hello, World!"})
        super().__init__(c_key, c_secret, a_token, a_secret)

    def write_to_db(self, doc):
        """Adds a document to the database."""
        self.db_connection[self.db_name][self.db_collection].insert_one(doc)

    def on_status(self, status):
        """Receives a status from the stream."""

        status = status._json

        # Only worry about original tweets
        if not status["is_quote_status"] and "retweeted_status" not in status \
            and not status["in_reply_to_status_id"]:

            # Take only a subset of fields
            doc = {
                "text": status["full_text"] if "full_text" in status else status["text"],
                "screen_name": status["user"]["screen_name"],
                "verified": status["user"]["verified"],
                "created_at": status["created_at"]
            }

            self.write_to_db(doc)