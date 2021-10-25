import tweepy
from dotenv import load_dotenv
from os import getenv
from scripts.stream import Watcher

if __name__ == "__main__":

    # Access a .env file
    load_dotenv()

    # Build the DB connection string
    conn_str = f"mongodb+srv://{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@{getenv('DB_CLUSTER')}.kpqzc.mongodb.net"
    conn_str += f"/{getenv('DB_NAME')}?retryWrites=true&w=majority"

    # Create the streaming object
    watcher = Watcher(getenv("C_KEY"),
                      getenv("C_SECRET"),
                      getenv("A_TOKEN"),
                      getenv("A_SECRET"),
                      conn_str,
                      getenv('DB_NAME'),
                      getenv("DB_COLLECTION"))

    print("App running...")

    watcher.filter(track=getenv("SEARCH_TERMS").split(","),
                   threaded=True,
                   languages=getenv("LANGUAGES").split(","))