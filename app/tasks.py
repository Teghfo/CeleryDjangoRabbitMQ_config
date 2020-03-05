from celery import shared_task


@shared_task(name='tavan_resandan')
def power(num):
    return num**100000


@shared_task(name='jam zadan')
def summation(num1, num2):
    return num1 + num2
