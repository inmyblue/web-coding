from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

q1 = db.movies.find_one({'title':'매트릭스'})
print(q1['point'])

q2 = list(db.movies.find({'point':q1['point']}, {'_id' : False}))

for q2_list in q2:
    print(q2_list['title'])

#db.movies.update_one({'title':'매트릭스'},{'$set':{'point':'9.40'}})