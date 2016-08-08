from pymongo import MongoClient
import configparser

# Import config
config = configparser.ConfigParser()
config.read('setsuna.cfg')
conf = config['laptop']
port_number = int(conf['port'])

# DB Connection
connect = MongoClient(conf['address'], port_number)
posts = connect[conf['database']][conf['collection']]

# Setsuna configp
life = int(conf['life'])
