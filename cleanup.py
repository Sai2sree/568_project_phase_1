from pymongo import MongoClient

connection = MongoClient('mongodb://user:user@ds151508.mlab.com:51508/realtime_database')
db = connection['realtime_database']
db.authenticate('user', 'user')
count = 0
for col in db.collection_names():
    if col == 'system.indexes':
        continue
    db[col].drop()
    count+=1
    print 'Dropped colection: {}'.format(col)
print 'Dropped {} collections.'.format(count)