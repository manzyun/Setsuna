from nose import eq_, ok_, raises, with_setup
from setsuna import conf, models
from PyMongo import MongoClient
import json
import datatime

class TestPost(clazz):
    # TODO:  unique_idのインクリメント処理やりたい
    testdata = {"unique_id": 1,
                "content": "美味しい美味しいスープカレー",
                "limit": datatime.datatime.utcnow(),
                "delkey": "hogefuga"
                }

    @classmethod
    def setup_class(clazz):
        client = MongoClient(conf._conf["address"],conf._conf["ip"])
        db = client[conf._conf["db"]]
        collection = db[conf._conf["collection"]]

    def setup(self):
        # とりあえず書く
        self.testindex = collection.insert_one(testdata)

    def teardown(self):
        collection.remove({"_id": testindex})

    @nottest
    def test_make_model(self):
        """ モデルが読み込まれてインスタンスが生成されるか """
        pass

    @nottest
    def test_insert_model(self):
        """ 生成したインスタンスが、インスタンスの情報を維持したまま挿入されるか """
        pass

    @nottest
    def test_delete_model(self):
        """ 狙ったレコードがパスワードが合致した場合に削除されるか """
        pass

    @nottest
    def test_dead_model(self):
        """ リミットオーバーした場合投稿が削除されるか """

