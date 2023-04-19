from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("app1的首页")
# Create your views here.
