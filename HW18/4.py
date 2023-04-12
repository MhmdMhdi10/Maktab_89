from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.mflix

results = db.movies.aggregate([{'$unwind': "$languages"},
                              {'$group': {'_id': "$languages", 'count': {'$sum': 1}}}])
for result in results:
    print(result)
