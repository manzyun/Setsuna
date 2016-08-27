import threading
import logging
from . import conf, models
import time
from datetime import datetime, timedelta
from bson import objectid


def killing():
    logging.info('-> Start Killing.')

    while True:
        try:
            logging.info('-!> Killing.')

            # Killing Target Search
            b_targets = [post['_id'] for post in conf.posts.find()]
            posts = [models.Post(str(a)) for a in b_targets]

            targets = []
            for target in posts:
                if target.limit < datetime.now() - timedelta(minutes=60):
                    targets.append(target.unique_id)

            # Killing
            count = 0
            for kill, target in enumerate(targets):
                conf.posts.delete_one({'_id': objectid.ObjectId(target)})
                count = kill

            logging.info('-!< %s killed.'.format(count))
        except KeyboardInterrupt:
            break

    logging.info('-<- Stop killing')


killer = threading.Thread(target=killing, name='killer')
killer.run()
