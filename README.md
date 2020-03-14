# Twitter Watcher

This program collects tweets for a provided search term and writes them to a .csv file or to an IBM DB2 database.

## Requirements

```python
tweepy
dotenv
ibm_db
```

## Set up

You need a .env file containing the following variables

```python
C_KEY=XXXXXXXXXX
C_SECRET=XXXXXXXXXX
A_TOKEN=XXXXXXXXXX
A_SECRET=XXXXXXXXXX
DB_CONNECT=XXXXXXXXXX
```

Find the specific values to fill the first four gaps on your Twitter developer account. Get the `DB_CONNECT`value from an IBM Cloud DB2 instance's service credentials (the `ssldsn` parameter).

## Customisation

You can edit the search term in the `twitter_watch.py` file.

You can edit the recorded fields in the `watcher.py` file.

## Run

`python twitter_watch.py`

As written, the code only writes to a file. Change the `out_type` parameter of the watcher object to "db" or "both" to start sending data to a database. This can be seen in the `heroku` branch of  the repository.

## Deploy

This should deploy relatively easily to Heroku, so that it can be run independently of any specific machine.

Heroku plays poorly with `dotenv`, so replace

```python
import dotenv
```

and

```python
# Access a .env file
load_dotenv()
```

in the `twitter_watch.py` file with nothing at all, removing `dotenv` from the `requirements.txt` file as well.

Set the `.env` values as config vars in Heroku.

The above changes can all be seen in the `heroku` branch of this repository.

## Planned development

- Allow easier customisation of written values and search terms
