from django.shortcuts import render
from django.http import HttpResponse
from . import models
def index(request):
    return HttpResponse("app1的首页")
def publisher_list(request):
    publisher=models.publisher.objects.all()
    return render(request,'pub_list.html',{'pub_list':publisher})
def add_publisher(request):
    if request.method =='POST':
        new_author_name = request.POST.get('name')
        new_author_sex = request.POST.get('sex')
        new_author_age = request.POST.get('age')
        new_author_tel = request.POST.get('tel')
    return render(request,'add.html')
# Create your views here.
