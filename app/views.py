from django.shortcuts import render
from django.http import HttpResponse

from .tasks import power


def mashin_hesab(request):
    if request.method == 'POST':
        body = request.POST
        num = int(body['number'])
        for i in range(10):
            power.delay(num)

    return HttpResponse('ok!')
