# _*_ coding:utf-8 _*_

from django.shortcuts import render
from django.views.decorators import csrf

#接收请求POST数据
def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)

