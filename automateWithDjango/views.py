from django.shortcuts import render
from django.http import HttpResponse
from dataentry.tasks import celery_test_task


def home(request):
    return render(request, 'home.html')


def celery_test(request):
    # I want to execute a time-consuming task
    celery_test_task.delay()
    return HttpResponse('<h3>Celery Test</h3>')
