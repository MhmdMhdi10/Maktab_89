from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.mflix

movies = db.movies.aggregate([
    {
        '$match': {'$and': [{'$or': [
            {'year': {'$type': 'int'}},
            {'year': {'$type': "string"}},
        ]},
            {'$expr': {'$gt': [{'$toInt': {'$substr': [{'$ifNull': ["$year", "0"]}, 0, 4]}}, 1990]}}, ]}, },
    {'$project': {'_id': 0, 'title': 1, 'year': 1}}])

for i in movies:
    print(i)
