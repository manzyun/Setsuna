from pymongo import MongoClient
import configparser

# Import config
config = configparser.ConfigParser()
config.read('setsuna.cfg')
conf = config['DBInfo']['desktop']

# DB Connection
connect = MongoClient(conf['address'], conf['port'])
posts = connect[conf['database']][conf['collection']]
