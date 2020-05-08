from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('TOP')

# def index(request):
#     return render(request, name='index')