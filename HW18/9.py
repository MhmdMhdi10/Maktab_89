from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.mflix

result = db.movies.aggregate([{'$unwind': '$cast'},
                         {'$unwind': '$genres'},
                         {'$group': {'_id': '$cast', 'genres': {'$addToSet': '$genres'}}}])

for i in result:
    print(i)
