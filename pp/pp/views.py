from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    html="<h1>我的第一个网页</h1>"
    return HttpResponse(html)
def hello2(request):
    return render(request,'test_html.html')
def mm_view(request):
    dic={
        "a":"asdasdadadadad",
        "b":"sadafasfafsaf"
    }
    return render(request,'test_html2.html',dic)
def image(request):
    return render(request,'imagination.html')
def test(request):
    html="<h1>我的第一个网页</h1>"
    return HttpResponse(html)
