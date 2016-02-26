import pymongo
import conf

client = pymongo.MongoClient(conf._conf["address"], conf._conf["port"])
db = client[conf._conf["database"]]
collection = db[conf._conf["collection"]]


savescript = {
                "_id": "getNextSequence",
                "value": 
                """function(name) {{
                    var ret = {}.{}.findAndModify(
                         {{
                              query: {{_id: name}},
                              update: {{$inc: {{seq: 1}}}},
                              new: true
                         }}
                    );

                    return req.seq;
                }}
                """.format(conf._conf["database"], conf._conf["collection"])
             }

def init_db():
    result = collection.create_index([("unique_id", pymongo.ASCENDING)],
            unique=True)
    print(result)
    result = db.counters.insert_one({"_id": "unique_id", "seq": 0})
    print(result)
    result = db.system.js.save({"_id": "getNextSequence", "value": savescript})
    print(result)

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
