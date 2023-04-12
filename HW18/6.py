from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.mflix
movies = db.movies.find_one({'title': 'The Taking of Pelham 1 2 3'})
result = db.comments.aggregate([{
    '$match': {'movie_id': movies['_id']}},
    {'$group': {'_id': '$name'}},
    {'$project': {'_id': 1}}])

for r in result:
    print(r)
