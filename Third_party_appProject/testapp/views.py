from django.shortcuts import render
import requests
from django.http import HttpResponse
# Create your views here.
def Get_info(request):
    ip= request.META.get('HTTP_X_FORWARDED_FOR',None) or  request.META.get('REMOTE_ADDR')
    url='http://api.ipstack.com/'+'36.255.86.138'+'?access_key=0631543247927cb8f777f40edabaa544'
    resp=requests.get(url)
    data=resp.json()
    return render(request,'testapp/info.html',{'Data':data})
