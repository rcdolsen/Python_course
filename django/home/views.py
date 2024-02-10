# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    print('I`m home')
    # return HttpResponse('<b>home</b> do app')

    context = {
        'context': 'At home'
    }

    return render(
        request,
        'home/index.html',
        # 'global/base.html',
        # context={
        #     'context': 'At home'
        # }
        context,
    )
