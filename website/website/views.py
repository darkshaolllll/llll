from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.cache import cache_page
# Create your views here.
# 视图函数必须接收一个形参(request)
@cache_page(60 * 15)
def ab_render(request):
    user_dict = {'username': 'junjie', 'age': 18}
    # 在myifrst.html中使用data获取到user_dict，键自定义。
    # 将user_dict传给myifrst页面，页面通过data拿到字典值
    return render(request, 'myifrst.html', {'data': user_dict})
