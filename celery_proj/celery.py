from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from kombu import Queue, Exchange

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_proj.settings')
app = Celery('celery_proj')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.task_queues = (
    Queue('celery', routing_key='celery'),
    Queue('get_result', routing_key='get_result'),
)

app.conf.task_routes = {'get_*': {'queue': 'get_result'}}

# app.conf.beat_schedule = {
#     'hello_hasan': {
#         'task': 'jam zadan',
#         'schedule': 10.0,
#         'args': (15, 16)
#     },
# }


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
