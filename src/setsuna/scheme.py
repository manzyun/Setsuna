import pymongo

client = pymongo.MongoClient('10.0.3.116', 27017)
collection = client["setsuna"]["posts"]

def init_db():
    result = collection.create_index([("unique_id", pymongo.ASCENDING)],
            unique=True)

''' json image
[
	{
		"unique_id" : 0,
		{
			"content" : "あかさたな",
			"limit" : 1234.5678,
			"password" : "hogefuga"
		}
	}
]
'''
