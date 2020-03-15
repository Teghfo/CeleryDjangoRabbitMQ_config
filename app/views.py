from django.shortcuts import render
from django.http import HttpResponse
import time
from .tasks import power, get_result


def mashin_hesab(request):
    if request.method == 'POST':
        body = request.POST
        num = int(body['number'])
        for i in range(10):
            switch(body['sahm']):
                case 'khesapa':
                    khesapa.delay(500)

            result = power.delay(10000000000)
            get_result.delay(result.id)
    # print(result.status)
    # time.sleep(10)
    # print(result.get())
    # print(result.status)

    return HttpResponse('ok!')
