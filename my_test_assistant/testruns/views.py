from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
#import requests

from .models import TestRun, Task

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the testruns index.")

@require_http_methods(["GET"])
def show_testruns(request):
    response = {}
    try:
        testruns = TestRun.objects.filter()
        response['testruns'] = json.loads(serializers.serialize("json", testruns))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response, json_dumps_params={'indent': 4})
