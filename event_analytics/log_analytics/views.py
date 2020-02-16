from django.shortcuts import render


def index(request):
    return render(request, 'log_analytics/index.html')