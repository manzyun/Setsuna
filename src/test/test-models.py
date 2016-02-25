from unittest import TestCase, expectedFailure
from setsuna import conf, models
from pymongo import MongoClient
import json
import datetime
import calendar

class TestPost(TestCase):

    @classmethod
    def setup_class(self):
        client = MongoClient(conf._conf["address"], conf._conf["ip"])
        db = client[conf._conf["db"]]
        collection = db[conf._conf["collection"]]

        testdata = {"unique_id":
                     collection.find_one({}, {unique_id: 1, _id: 0}) + 1,
                    "content": "美味しい美味しいスープカレー",
                    "limit": calendar(
                        timegm(datetime.datetime.utcnow().timetuple())),
                    "delkey": "hogefuga"
                   }
    def setup(self):
        # とりあえず書く
        self.testindex = collection.insert_one(testdata)

    def teardown(self):
        collection.remove({"_id": self.testindex})

    def test_make_model(self):
        """ モデルが読み込まれてインスタンスが生成されるか """
        model = models.Post(testdata["unique_id"])
        self.assertEqual(json.dumps(model), testdata)

    def test_insert_model(self):
        """ 生成したインスタンスが、インスタンスの情報を維持したまま挿入されるか """
        model = models.Post(0)
        model.content = "にくまん、あんまん、カレーまん"
        model.delkey = "nununeno"
        model.post()

        model_sample = models.Post(model.unique_id)

        self.assertEqual(model, model_sample)


    @expectedFailure
    def test_delete_model(self):
        """ 狙ったレコードがパスワードが合致した場合に削除されるか """
        model = models.Post(testdata["unique_id"])
        model.delete(testdata["delkey"])

        collection.find_one({"unique_id": testdata["unique_id"]})

    @expectedFailure
    def test_dead_model(self):
        """ リミットオーバーした場合投稿が削除されるか """
        model = models.Post(testdata["unique_id"])
        model.apoptosis()

        collection.find_one({"unique_id": testdata["unique_id"]})

if __name__ == "__main__":
    unittest.main()
