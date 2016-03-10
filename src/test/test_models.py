from importer import import_my_module
import_my_module('../setsuna')

from setsuna import conf, models
from unittest import TestCase, skip
from pymongo import MongoClient


testdata = {"content": "美味しい美味しいスープカレー",
            "limit": '2016/01/01 00:00:00',
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

        d = {"_id": model.unique_id,
             "content": model.content,
             "limit": model.limit,
             "delkey": model.delkey}

        self.assertDictEqual(d, testdata)

    def test_delete_model(self):
        """ 狙ったレコードがパスワードが合致した場合に削除されるか """
        model = models.Post(self.testresult.inserted_id)
        model.delete(testdata["delkey"])

        self.assertEqual(None, self.collection.find_one({'_id': model.unique_id}))