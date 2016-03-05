import unittest

from setsuna import conf, models
from unittest import TestCase, expectedFailure
from pymongo import MongoClient
import json
import datetime
import calendar


testdata = {"content": "美味しい美味しいスープカレー",
            "limit": calendar.timegm(
                datetime.datetime.utcnow().timetuple()),
            "delkey": "hogefuga"}

class TestPost(TestCase):
    client = MongoClient(conf._conf["address"], conf._conf["port"])
    db = client[conf._conf["database"]]
    collection = db[conf._conf["collection"]]

    def setUp(self):
        # とりあえず書く
        self.testindex = TestPost.collection.insert_one(testdata)

    def tearDown(self):
        TestPost.collection.delete_one(self.testindex)

    def test_make_model(self):
        """ モデルが読み込まれてインスタンスが生成されるか """
        model = models.Post()
        model.read(self.testindex)

        d = {"content": model.content,
                "limit": model.limit,
                "delkey": model.delkey}

        del testdata['_id']

        self.assertDictEqual(d, testdata)

    def test_insert_model(self):
        """ 生成したインスタンスが、インスタンスの情報を維持したまま挿入されるか """
        model = models.Post()
        model.content = "にくまん、あんまん、カレーまん"
        model.delkey = "nununeno"
        sample_id = model.post()

        model_sample = models.Post.read(sample_id)

        self.assertDictEqual(model, model_sample)


    def test_delete_model(self):
        """ 狙ったレコードがパスワードが合致した場合に削除されるか """
        model = models.Post(self.testindex)
        model.delete(testdata["delkey"])

        self.assertRaises(NoneRecordException,
                self.collection.find_one({"unique_id": testdata["unique_id"]}))

    def test_dead_model(self):
        """ リミットオーバーした場合投稿が削除されるか """
        model = models.Post(self.testindex)
        model.apoptosis()

        self.assertRaises(NoneRecordException,
            self.collection.find_one({"unique_id": testdata["unique_id"]}))

if __name__ == "__main__":
    unittest.main()

