# encoding: utf-8
import logging

import db
import tasks


logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] (%(pathname)s:%(lineno)s) [%(levelname)s] %(name)s: %(message)s',
    datefmt='%m-%d %H:%M'
)
db.init('var/data/graveyard.db')


class TestTask(tasks.LikeTask):
    """
    测试任务
    """

    def run(self):
        if self._image_local_cache:
            while self.fetch_attachment():
                pass


#task = tasks.FollowingFollowerTask(db.Account.get_by_id(1))
#task = tasks.BroadcastCommentTask(db.Account.get_by_id(1))
#task = tasks.PhotoAlbumTask(db.Account.get_by_id(1))
#task = tasks.NoteTask(db.Account.get_by_id(1))
#task = tasks.LikeTask(db.Account.get_by_id(1))
#task = tasks.ReviewTask(db.Account.get_by_id(1))
task = TestTask(db.Account.get_by_id(1))

result = task(
    requests_per_minute=30,
    local_object_duration=60*60*24*300,
    broadcast_active_duration=60*60*24*10,
    broadcast_incremental_backup=True,
    image_local_cache=True
)
print(result)
