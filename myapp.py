from __future__ import absolute_import, unicode_literals
from celery import Celery

# from . import settings

mycelery = Celery('mycelery', include=['mycelery.tasks'])

mycelery.config_from_object("mycelery.settings")
# app.config_from_object(settings)

if __name__ == "__main__":
    # app.worker_main()
    # print(app.main)
    mycelery.start()