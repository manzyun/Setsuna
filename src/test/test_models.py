from importer import import_my_module
import_my_module('../setsuna')

from setsuna import conf, models
from unittest import TestCase, skip
from pymongo import MongoClient
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
        self.testresult = TestPost.collection.insert_one(testdata)

    def tearDown(self):
        TestPost.collection.delete_many({})

    def test_make_model(self):
        """ モデルが読み込まれてインスタンスが生成されるか """
        model = models.Post(self.testresult.inserted_id)

        d = {"content": model.content,
             "limit": model.limit,
             "delkey": model.delkey}

        del testdata['_id']

        self.assertDictEqual(d, testdata)

    @skip('エラー定義してない')
    def test_delete_model(self):
        """ 狙ったレコードがパスワードが合致した場合に削除されるか """
        model = models.Post(self.testresult.inserted_id)
        model.delete(testdata["delkey"])

        self.assertRaises(NoneRecordException,
                self.collection.find_one({"unique_id": testdata["unique_id"]}))

    @skip('エラー定義してない')
    def test_dead_model(self):
        """ リミットオーバーした場合投稿が削除されるか """
        model = models.Post(self.testresult.inserted_id)
        model.apoptosis()

        self.assertRaises(NoneRecordException,
            self.collection.find_one({"unique_id": testdata["unique_id"]}))