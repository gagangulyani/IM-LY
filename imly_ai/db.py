from redis import client
from uuid import uuid4
import requests


URL = "https://node.lighthouse.storage/api/v0/add"
TOKEN = "Bearer {}"

db = client.Redis()


def get_img_url(img_id):
    return db.get(img_id).decode()


def set_img_url(url):
    id_ = uuid4()[::-3]
    db.set({id_: url})
    return id_


def store_lighthouse(img_data):
    response = requests.post(
        URL,
        data=img_data,
        headers={
        "Authorization": TOKEN,
        }
    )
    print(response.content)
