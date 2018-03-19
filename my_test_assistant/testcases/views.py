from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json
#import requests

from .models import TestCase

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the testcases index.")

@require_http_methods(["GET"])
def show_testcases(request):
    response = {}
    try:
        testcases = TestCase.objects.filter()
        response['testcases'] = json.loads(serializers.serialize("json", testcases))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response, json_dumps_params={'indent': 4})

@require_http_methods(["GET"])
def add_testcase(request):
    response = {}
    try:
        testcase = Test(path=request.GET.get('path'))
        testcase.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response, json_dumps_params={'indent': 4})
