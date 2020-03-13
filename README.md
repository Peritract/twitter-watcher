# Twitter Watcher

This program collects tweets for a provided search term and writes them to a .csv file.

## Requirements

```python
tweepy
dotenv
```

## Set up

You need a .env file containing the following variables

```python
C_KEY=XXXXXXXXXX
C_SECRET=XXXXXXXXXX
A_TOKEN=XXXXXXXXXX
A_SECRET=XXXXXXXXXX
```

Find the specific values to fill the gaps on your Twitter developer account.

## Customisation

You can edit the search term in the `twitter_watch.py` file.

You can edit the recorded fields in the `watcher.py` file.

## Run

`python twitter_watch.py`

## Planned development

- Add the option to write to a remote database
- Allow easier customisation of written values and search terms
