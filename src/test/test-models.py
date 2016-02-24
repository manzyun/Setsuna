from unittest import TestCase
from nose.tools import eq_, ok_, raises, with_setup
from setsuna import conf, models
from PyMongo import MongoClient
import json
import datatime
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
        eq_(json.dumps(model), testdata)

    def test_insert_model(self):
        """ 生成したインスタンスが、インスタンスの情報を維持したまま挿入されるか """
        model = models.Post(0)
        model.content = "にくまん、あんまん、カレーまん"
        model.delkey = "nununeno"
        model.post()

        model_sample = models.Post(model.unique_id)

        eq_(model, model_sample)


    @raises(NotRecordError)
    def test_delete_model(self):
        """ 狙ったレコードがパスワードが合致した場合に削除されるか """
        model = models.Post(testdata["unique_id"])
        model.delete(testdata["delkey"])

        collection.find_one({"unique_id": testdata["unique_id"]})

    @raises(NotRecordError)
    def test_dead_model(self):
        """ リミットオーバーした場合投稿が削除されるか """
        model = models.Post(testdata["unique_id"])
        model.apoptosis()

        collection.find_one({"unique_id": testdata["unique_id"]})

