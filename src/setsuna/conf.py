from pymongo import MongoClient

# DB Connection
connect = MongoClient(_conf['address'], _conf['port'])
posts = connect[_conf['database']][_conf['collection']]
