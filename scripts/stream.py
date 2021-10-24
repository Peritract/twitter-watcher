"""This file contains the definition of the Watcher class; this class listens for new tweets and records them.
"""

from tweepy import Stream

class Watcher(Stream):

    def on_status(self, status):
        print(status.text)