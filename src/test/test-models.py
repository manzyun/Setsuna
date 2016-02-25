from unittest import TestCase, expectedFailure
from setsuna import conf, models
from pymongo import MongoClient
import json
import datetime
import calendar

testdata = {"unique_id": 1,
            "content": "美味しい美味しいスープカレー",
            "limit": calendar.timegm(
                datetime.datetime.utcnow().timetuple()),
            "delkey": "hogefuga"
            }

class TestPost(TestCase):
    client = MongoClient(conf._conf["address"], conf._conf["port"])
    db = client[conf._conf["database"]]
    collection = db[conf._conf["collection"]]

    def setup(self):
        # とりあえず書く
        self.testindex = self.collection.insert_one(testdata)

    def teardown(self):
        self.collection.remove({"_id": self.testindex})

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


    def test_delete_model(self):
        """ 狙ったレコードがパスワードが合致した場合に削除されるか """
        model = models.Post(testdata["unique_id"])
        model.delete(testdata["delkey"])

        self.assertRaises(NoneRecordException,
                self.collection.find_one({"unique_id": testdata["unique_id"]}))

    def test_dead_model(self):
        """ リミットオーバーした場合投稿が削除されるか """
        model = models.Post(testdata["unique_id"])
        model.apoptosis()

        self.assertRaises(NoneRecordException,
            self.collection.find_one({"unique_id": testdata["unique_id"]}))

