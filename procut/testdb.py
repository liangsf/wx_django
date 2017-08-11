# _*_ coding: utf-8 _*_

from django.http import HttpResponse

#引入自定义的模型
from wx_app.models import Test



#数据库操作
def testdb(request):
    test1 = Test(name='liangsf')
    test1.save()
    return HttpResponse("<p>数据添加成功!</p>")
