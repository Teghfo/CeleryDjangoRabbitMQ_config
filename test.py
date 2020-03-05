from test_celery import hello_celery, my_sum


hello_celery.delay()

my_sum.delay(2,8)

print('Done')