from celery import Celery

from mycelery.settings import BROKER_URL

app = Celery('example', broker=BROKER_URL)

@app.task
def add(x, y):
    return x + y