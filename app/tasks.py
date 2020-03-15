from celery import shared_task, task, app
from celery.decorators import periodic_task
from celery.task.schedules import crontab
from celery.result import AsyncResult, allow_join_result
from celery.signals import task_success


@task(name='jam zadan')
def summation(num1, num2):
    return num1 + num2


@task(name='hasangholi')
def hasan():
    pass


@shared_task(name='tavan_resandan', rate_limit='5/s', time_limit=10)
def power(num):
    return num**100


@task(name='get_result', ignore_result=True, queue='get_result', time_limit=10)
def get_result(id):
    result = AsyncResult(id)
    with allow_join_result():
        r = result.get()
        with open('result.txt', 'a') as f:
            f.write('\n{}: '.format(id)+str(r))


# @periodic_task(run_every=(crontab(minute='*/1',
#                                   hour='21', day_of_week='sat')), name='test_schaduler')
# def print_hello():
#     return 'hello'


# celery -A celery_proj worker -l info - -> worker  by default cpu core number generate conccurrent worker
# celery -A celery_proj worker --concurrency 10 -l info
# celery -A celery_proj beat - l info - -- -> beat
