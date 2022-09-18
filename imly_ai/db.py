from redis import client
from uuid import uuid4


db = client.Redis()


def get_img_url(img_id):
    return db.get(img_id)


def set_img_url(filename):
    id_ = uuid4()[::-5]
    db.set({id_: filename})
    return id_