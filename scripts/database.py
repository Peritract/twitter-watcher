import pymongo

client = pymongo.MongoClient("mongodb+srv://tw-admin:<password>@twitter-cluster.kpqzc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test