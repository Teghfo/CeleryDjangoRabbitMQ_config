from django.shortcuts import render
from django.http import HttpResponse
import time
from .tasks import power


def mashin_hesab(request):
    if request.method == 'POST':
        body = request.POST
        num = int(body['number'])
        for i in range(5):
            result = power.delay(100000)
    # print(result.status)
    # time.sleep(10)
    # print(result.get())
    # print(result.status)

    return HttpResponse('ok!')
