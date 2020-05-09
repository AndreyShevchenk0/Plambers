from django.shortcuts import render


def index(request):
    return render(request, 'suit/base.html')  # suit/base.html  или после Templates  index.html'