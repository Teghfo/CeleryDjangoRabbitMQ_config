from celery import shared_task, task
from celery.decorators import periodic_task
from celery.task.schedules import crontab


@shared_task(name='tavan_resandan')
def power(num):
    return num**100000


@task(name='jam zadan')
def summation(num1, num2):
    return num1 + num2


@task(name='hasangholi')
def hasan():
    pass


# @periodic_task(run_every=(crontab(minute='*/1',
#                                   hour='21', day_of_week='sat')), name='test_schaduler')
# def print_hello():
#     return 'hello'


# celery -A celery_proj worker -l info - -> worker  by default cpu core number generate conccurrent worker
# celery -A celery_proj worker --concurrency 10 -l info
# celery -A celery_proj beat - l info - -- -> beat
