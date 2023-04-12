from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.mflix

result = db.movies.aggregate([{'$unwind': '$cast'},
                              {'$group': {'_id': '$cast', 'count': {'$sum': 1}}},
                              {'$sort': {'count': -1}}])
for i in result:
    print(i)
