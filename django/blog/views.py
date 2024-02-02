from django.http import HttpResponse

# from django.shortcuts import render


def blog(request):
    print('posso fazer outras coisas')
    return HttpResponse('Marrom Theo do app blog')


def exemple(request):
    print('exemple')
    return HttpResponse('exemple do app blog')