# Twitter Watcher

This program collects tweets for a provided search term and writes them to a .csv file or to an IBM DB2 database.

## Requirements

See [requirements.txt](./requirements.txt), but basically `Tweepy` and `PyMongo`.

## Set up

You need a .env file containing the several variables; sensible defaults are left where possible.

```python
C_KEY=XXXXXXXXXX
C_SECRET=XXXXXXXXXX
A_TOKEN=XXXXXXXXXX
A_SECRET=XXXXXXXXXX
DB_USER=XXXXXXXXXX
DB_PASSWORD=XXXXXXXXXX
DB_CLUSTER=XXXXXXXXXX
DB_NAME=tweets
DB_COLLECTION=XXXXXXXXXX
SEARCH_TERMS=XXXXXXXXXX
LANGUAGES=en
```

The first four should be filled with the values from a Twitter developer account. The remainder should be filled with the details for a MongoDB instance, and with the details of tweets that you're interested in.

## Customisation

To search for different tweets, or different languages, edit the environment variables. Both `SEARCH_TERMS` and `LANGUAGES` accept a single value or a comma-separated list.

## Run

`python app.py`

## Deployment

This should deploy relatively easily to Heroku, so that it can be run independently of any specific machine.

Set the `.env` values as config vars in Heroku.
