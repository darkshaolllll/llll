from django.utils.deprecation import MiddlewareMixin
import re
from django.http.response import HttpResponse
class mymw(MiddlewareMixin):#限制固定ip访问次数
    visit_times = {}
    def process_request(self,request):
        ip_adress=request.META['REMOTE_ADDR']
        path_url=request.path_info
        if not re.match('^/test',path_url):
            return
        times=self.visit_times.get(ip_adress,0)
        print('ip',ip_adress,'已经访问了',times)
        self.visit_times[ip_adress]=times+1
        if times<5:
            return
        return HttpResponse('你已经访问过'+str(times)+'fsdfsfds')

