import pymongo
from scrapy.conf import settings

host = settings['MONGODB_HOST']
port = settings['MONGODB_PORT']
dbName = settings['MONGODB_DBNAME']
col = settings['MONGODB_TEST']
client = pymongo.MongoClient(host=host,port=port)
tdb = client[dbName]        
post = tdb[col]

document = {'tkey':'000','tvalue':'May'}
# post.insert(document)

# post.update({key},{})
tname = 'killer'
post.update({"tkey":'000'}, {'$set':{"tvalue":tname}})
