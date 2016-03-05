import pymongo
import conf

client = pymongo.MongoClient(conf._conf["address"], conf._conf["port"])
db = client[conf._conf["database"]]
collection = db[conf._conf["collection"]]

''' json image
[
	{
		{
                        "unique_id" : 0,
			"content" : "あかさたな",
			"limit" : 1234.5678,
			"password" : "hogefuga"
		}
	}
]
'''
