from . import conf
from datetime import datetime, timedelta
from bson import objectid

timeformat = '%Y-%m-%d %H:%M:%S'


class Post:
    def __init__(self, unique_id=None):
        if unique_id is None:
            self.unique_id = ''
            self.content = ''
            self.limit = datetime
            self.delkey = ''
        else:
            # Read DB
            self.unique_id = unique_id
            post = conf.posts.find_one({'_id': objectid.ObjectId(self.unique_id)})
            self.content = post['content']
            self.limit = datetime.strptime(post['limit'], timeformat)
            self.delkey = post['delkey']

    def post(self):
        self.limit = datetime.utcnow() + timedelta(seconds=86400)

        # Writing DB
        result = conf.posts.insert_one({'content': self.content,
                                        'limit': self.limit.strftime(timeformat),
                                        'delkey': self.delkey})
        self.unique_id = str(result.inserted_id)
        return result.inserted_id

    def tell(self):
        self.limit = self.limit + timedelta(seconds=3600)

        # Update DB
        conf.posts.update_one({'_id': objectid.ObjectId(self.unique_id)},
                              {'$set': {'limit': self.limit.strftime(timeformat)}})
        return True

    def delete(self,  delkey=''):
        if self.delkey == delkey:
            # Remove post in DB
            conf.posts.delete_one({'_id': objectid.ObjectId(self.unique_id)})
            return True
        else:
            return False

