from __future__ import absolute_import
from celery import Celery
import time

app = Celery('celery_test', broker='amqp://localhost//')



@app.task
def hello_celery():
    return 'hello'


@app.task
def my_sum(arg1, arg2):
    time.sleep(15)
    return arg1 + arg2